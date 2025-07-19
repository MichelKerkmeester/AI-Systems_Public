#!/usr/bin/env python3
"""
Message Queue System for Inter-Agent Communication

Provides asynchronous message passing between Claude agents without direct coupling.
Uses file-based messaging with directory watching for real-time notifications.
"""

import os
import json
import time
import uuid
import asyncio
import threading
from typing import Dict, List, Any, Callable, Optional
from datetime import datetime
from pathlib import Path
from collections import defaultdict

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileCreatedEvent
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False
    Observer = None
    FileSystemEventHandler = object
    FileCreatedEvent = None


class Message:
    """Represents a message in the queue"""
    
    def __init__(self, 
                 from_agent: str,
                 to_agent: str,
                 message_type: str,
                 payload: Any,
                 priority: int = 5):
        self.id = f"{time.time()}-{uuid.uuid4().hex[:8]}"
        self.from_agent = from_agent
        self.to_agent = to_agent  # Can be agent_id or "broadcast"
        self.message_type = message_type
        self.payload = payload
        self.priority = priority
        self.timestamp = time.time()
        self.status = "pending"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "from": self.from_agent,
            "to": self.to_agent,
            "type": self.message_type,
            "payload": self.payload,
            "priority": self.priority,
            "timestamp": self.timestamp,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Create from dictionary"""
        msg = cls(
            from_agent=data["from"],
            to_agent=data["to"],
            message_type=data["type"],
            payload=data["payload"],
            priority=data.get("priority", 5)
        )
        msg.id = data["id"]
        msg.timestamp = data["timestamp"]
        msg.status = data.get("status", "pending")
        return msg


class MessageHandler(FileSystemEventHandler):
    """Handles file system events for message notifications"""
    
    def __init__(self, callback: Callable[[str], None]):
        self.callback = callback
    
    def on_created(self, event):
        """Called when a new message file is created"""
        if not event.is_directory and event.src_path.endswith('.json'):
            self.callback(event.src_path)


class MessageQueue:
    """File-based message queue for inter-agent communication"""
    
    def __init__(self, agent_id: str, queue_dir: str = None):
        self.agent_id = agent_id
        self.queue_dir = queue_dir or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "messages"
        )
        self.broadcast_dir = os.path.join(self.queue_dir, "broadcast")
        self.agent_dir = os.path.join(self.queue_dir, self.agent_id)
        self.orchestrator_dir = os.path.join(self.queue_dir, "orchestrator")
        
        # Message handlers
        self.handlers: Dict[str, List[Callable]] = defaultdict(list)
        self.observer = None
        self._running = False
        
        # Ensure directories exist
        for directory in [self.broadcast_dir, self.agent_dir, self.orchestrator_dir]:
            os.makedirs(directory, exist_ok=True)
    
    def publish(self, message: Message) -> bool:
        """
        Publish a message to the queue
        
        Args:
            message: Message to publish
            
        Returns:
            True if published successfully
        """
        # Determine target directory
        if message.to_agent == "broadcast":
            target_dir = self.broadcast_dir
        elif message.to_agent == "orchestrator":
            target_dir = self.orchestrator_dir
        else:
            target_dir = os.path.join(self.queue_dir, message.to_agent)
            os.makedirs(target_dir, exist_ok=True)
        
        # Write message file
        message_file = os.path.join(target_dir, f"{message.id}.json")
        try:
            with open(message_file, 'w') as f:
                json.dump(message.to_dict(), f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to publish message: {e}")
            return False
    
    def subscribe(self, message_type: str, handler: Callable[[Message], None]):
        """
        Subscribe to messages of a specific type
        
        Args:
            message_type: Type of messages to subscribe to (or "*" for all)
            handler: Function to call when message received
        """
        self.handlers[message_type].append(handler)
    
    def unsubscribe(self, message_type: str, handler: Callable[[Message], None]):
        """Unsubscribe from messages"""
        if message_type in self.handlers and handler in self.handlers[message_type]:
            self.handlers[message_type].remove(handler)
    
    def start(self):
        """Start listening for messages"""
        if self._running:
            return
        
        self._running = True
        
        # Process existing messages
        self._process_existing_messages()
        
        # Start watching for new messages
        if WATCHDOG_AVAILABLE:
            self._start_file_watcher()
        else:
            # Fallback to polling
            self._start_polling()
    
    def stop(self):
        """Stop listening for messages"""
        self._running = False
        
        if self.observer:
            self.observer.stop()
            self.observer.join()
    
    def _process_existing_messages(self):
        """Process any existing messages in the queue"""
        # Check agent-specific directory
        self._process_directory(self.agent_dir)
        
        # Check broadcast directory
        self._process_directory(self.broadcast_dir)
    
    def _process_directory(self, directory: str):
        """Process all messages in a directory"""
        if not os.path.exists(directory):
            return
        
        for filename in sorted(os.listdir(directory)):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                self._process_message_file(file_path)
    
    def _process_message_file(self, file_path: str):
        """Process a single message file"""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            message = Message.from_dict(data)
            
            # Dispatch to handlers
            self._dispatch_message(message)
            
            # Mark as processed by moving to processed directory
            processed_dir = os.path.join(os.path.dirname(file_path), "processed")
            os.makedirs(processed_dir, exist_ok=True)
            
            processed_path = os.path.join(processed_dir, os.path.basename(file_path))
            os.rename(file_path, processed_path)
            
        except Exception as e:
            print(f"Error processing message file {file_path}: {e}")
    
    def _dispatch_message(self, message: Message):
        """Dispatch message to appropriate handlers"""
        # Call specific type handlers
        if message.message_type in self.handlers:
            for handler in self.handlers[message.message_type]:
                try:
                    handler(message)
                except Exception as e:
                    print(f"Handler error for message {message.id}: {e}")
        
        # Call wildcard handlers
        if "*" in self.handlers:
            for handler in self.handlers["*"]:
                try:
                    handler(message)
                except Exception as e:
                    print(f"Wildcard handler error for message {message.id}: {e}")
    
    def _start_file_watcher(self):
        """Start watching directories for new messages"""
        self.observer = Observer()
        
        # Watch agent-specific directory
        handler = MessageHandler(self._process_message_file)
        self.observer.schedule(handler, self.agent_dir, recursive=False)
        
        # Watch broadcast directory
        self.observer.schedule(handler, self.broadcast_dir, recursive=False)
        
        self.observer.start()
    
    def _start_polling(self):
        """Fallback polling mechanism if watchdog not available"""
        def poll_loop():
            while self._running:
                self._process_existing_messages()
                time.sleep(1)  # Poll every second
        
        thread = threading.Thread(target=poll_loop, daemon=True)
        thread.start()
    
    # Common message types
    def send_status_update(self, status: str, details: Dict[str, Any] = None):
        """Send a status update to the orchestrator"""
        message = Message(
            from_agent=self.agent_id,
            to_agent="orchestrator",
            message_type="status_update",
            payload={
                "status": status,
                "details": details or {}
            }
        )
        self.publish(message)
    
    def send_task_complete(self, task_id: str, results: Dict[str, Any] = None):
        """Notify task completion"""
        message = Message(
            from_agent=self.agent_id,
            to_agent="orchestrator",
            message_type="task_complete",
            payload={
                "task_id": task_id,
                "results": results or {}
            },
            priority=3  # High priority
        )
        self.publish(message)
    
    def request_resource(self, resource_name: str, exclusive: bool = False):
        """Request access to a resource"""
        message = Message(
            from_agent=self.agent_id,
            to_agent="orchestrator",
            message_type="resource_request",
            payload={
                "resource": resource_name,
                "exclusive": exclusive
            },
            priority=4
        )
        self.publish(message)
    
    def broadcast_discovery(self, capabilities: List[str]):
        """Broadcast agent capabilities for discovery"""
        message = Message(
            from_agent=self.agent_id,
            to_agent="broadcast",
            message_type="agent_discovery",
            payload={
                "capabilities": capabilities,
                "agent_type": "development"
            }
        )
        self.publish(message)


class AsyncMessageQueue(MessageQueue):
    """Async version of MessageQueue for use with asyncio"""
    
    def __init__(self, agent_id: str, queue_dir: str = None):
        super().__init__(agent_id, queue_dir)
        self._queue = asyncio.Queue()
        self._tasks = []
    
    async def async_start(self):
        """Start async message processing"""
        self._running = True
        
        # Start file watcher in thread
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.start)
        
        # Start async message processor
        task = asyncio.create_task(self._async_processor())
        self._tasks.append(task)
    
    async def async_stop(self):
        """Stop async message processing"""
        self._running = False
        self.stop()
        
        # Cancel all tasks
        for task in self._tasks:
            task.cancel()
        
        await asyncio.gather(*self._tasks, return_exceptions=True)
    
    async def _async_processor(self):
        """Process messages asynchronously"""
        while self._running:
            try:
                # Get message from queue
                message = await asyncio.wait_for(self._queue.get(), timeout=1.0)
                
                # Dispatch to async handlers
                await self._async_dispatch(message)
                
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                print(f"Async processor error: {e}")
    
    async def _async_dispatch(self, message: Message):
        """Dispatch message to async handlers"""
        # This would call async handlers
        pass
    
    def _dispatch_message(self, message: Message):
        """Override to add message to async queue"""
        super()._dispatch_message(message)
        
        # Also add to async queue
        try:
            self._queue.put_nowait(message)
        except asyncio.QueueFull:
            print(f"Async queue full, dropping message {message.id}")


if __name__ == "__main__":
    # Example usage
    print("Testing Message Queue...")
    
    # Create two test agents
    agent1_id = "test-agent-1"
    agent2_id = "test-agent-2"
    
    queue1 = MessageQueue(agent1_id)
    queue2 = MessageQueue(agent2_id)
    
    # Set up message handlers
    def on_message(message: Message):
        print(f"\nReceived message:")
        print(f"  From: {message.from_agent}")
        print(f"  Type: {message.message_type}")
        print(f"  Payload: {message.payload}")
    
    queue2.subscribe("*", on_message)
    
    # Start listening
    print(f"\n1. Starting message queue for {agent2_id}...")
    queue2.start()
    
    # Send test messages
    print(f"\n2. Sending messages from {agent1_id}...")
    
    # Direct message
    msg1 = Message(
        from_agent=agent1_id,
        to_agent=agent2_id,
        message_type="test_message",
        payload={"content": "Hello from agent 1!"}
    )
    queue1.publish(msg1)
    print(f"✓ Sent direct message: {msg1.id}")
    
    # Broadcast message
    msg2 = Message(
        from_agent=agent1_id,
        to_agent="broadcast",
        message_type="status_update",
        payload={"status": "active", "cpu": 45}
    )
    queue1.publish(msg2)
    print(f"✓ Sent broadcast message: {msg2.id}")
    
    # Give time for messages to be processed
    time.sleep(2)
    
    # Stop listening
    print("\n3. Stopping message queue...")
    queue2.stop()
    print("✓ Message queue test complete")