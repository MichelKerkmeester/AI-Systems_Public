#!/usr/bin/env python3
"""
Memory Capture Queue - Thread-safe queue for batching memory operations
Implements singleton pattern with persistent storage and retry mechanism
"""

import json
import queue
import threading
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


class MemoryCaptureQueue:
    """Thread-safe queue for batching memory capture operations"""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Singleton pattern implementation"""
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance
    
    def __init__(self):
        """Initialize the queue with persistent storage"""
        if self._initialized:
            return
            
        self._initialized = True
        self._queue = queue.Queue()
        self._failed_memories = {}
        self._processed_count = 0
        self._lock = threading.RLock()
        
        # Set up persistent storage
        self._storage_path = Path("/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/state/memory_queue.json")
        self._storage_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing queue data
        self._load_from_storage()
    
    def add_memory(self, name: str, body: str, source: str, group_id: Optional[str] = None) -> str:
        """
        Add a memory to the capture queue
        
        Args:
            name: Memory name/title
            body: Memory content
            source: Source of the memory (e.g., 'task', 'conversation', 'error_fix')
            group_id: Optional group identifier
            
        Returns:
            Memory ID for tracking
        """
        with self._lock:
            memory_id = str(uuid.uuid4())
            memory_data = {
                'id': memory_id,
                'name': name,
                'body': body,
                'source': source,
                'group_id': group_id,
                'timestamp': datetime.now().isoformat(),
                'retry_count': 0,
                'status': 'pending'
            }
            
            self._queue.put(memory_data)
            self._save_to_storage()
            
            return memory_id
    
    def get_batch(self, size: int = 5) -> List[Dict[str, Any]]:
        """
        Get a batch of memories from the queue
        
        Args:
            size: Maximum number of memories to retrieve
            
        Returns:
            List of memory dictionaries
        """
        batch = []
        
        with self._lock:
            # Get up to 'size' items from the queue
            for _ in range(size):
                if not self._queue.empty():
                    try:
                        memory = self._queue.get_nowait()
                        batch.append(memory)
                    except queue.Empty:
                        break
            
            # Save state after removing items
            if batch:
                self._save_to_storage()
        
        return batch
    
    def mark_failed(self, memory_id: str, error_message: Optional[str] = None) -> None:
        """
        Mark a memory as failed and store for retry
        
        Args:
            memory_id: ID of the failed memory
            error_message: Optional error message
        """
        with self._lock:
            if memory_id not in self._failed_memories:
                # Find the memory in current batch or create placeholder
                self._failed_memories[memory_id] = {
                    'id': memory_id,
                    'retry_count': 0,
                    'last_error': error_message,
                    'last_attempt': datetime.now().isoformat(),
                    'status': 'failed'
                }
            else:
                # Increment retry count
                self._failed_memories[memory_id]['retry_count'] += 1
                self._failed_memories[memory_id]['last_error'] = error_message
                self._failed_memories[memory_id]['last_attempt'] = datetime.now().isoformat()
            
            self._save_to_storage()
    
    def retry_failed(self, max_retries: int = 3) -> List[Dict[str, Any]]:
        """
        Get failed memories that should be retried
        
        Args:
            max_retries: Maximum retry attempts before giving up
            
        Returns:
            List of memories to retry
        """
        retry_batch = []
        
        with self._lock:
            memories_to_remove = []
            
            for memory_id, failed_memory in self._failed_memories.items():
                if failed_memory['retry_count'] < max_retries:
                    # Update retry count and add to batch
                    failed_memory['retry_count'] += 1
                    failed_memory['status'] = 'retrying'
                    retry_batch.append(failed_memory)
                    memories_to_remove.append(memory_id)
            
            # Remove memories being retried from failed list
            for memory_id in memories_to_remove:
                del self._failed_memories[memory_id]
            
            if memories_to_remove:
                self._save_to_storage()
        
        return retry_batch
    
    def mark_processed(self, memory_id: str) -> None:
        """
        Mark a memory as successfully processed
        
        Args:
            memory_id: ID of the processed memory
        """
        with self._lock:
            self._processed_count += 1
            # Remove from failed memories if it was there
            if memory_id in self._failed_memories:
                del self._failed_memories[memory_id]
            self._save_to_storage()
    
    def get_stats(self) -> Dict[str, int]:
        """
        Get queue statistics
        
        Returns:
            Dictionary with pending, failed, and processed counts
        """
        with self._lock:
            return {
                'pending': self._queue.qsize(),
                'failed': len(self._failed_memories),
                'processed': self._processed_count,
                'total_attempted': self._queue.qsize() + len(self._failed_memories) + self._processed_count
            }
    
    def _save_to_storage(self) -> None:
        """Save queue state to persistent storage"""
        # Extract all items from queue temporarily
        queue_items = []
        temp_queue = queue.Queue()
        
        while not self._queue.empty():
            try:
                item = self._queue.get_nowait()
                queue_items.append(item)
                temp_queue.put(item)
            except queue.Empty:
                break
        
        # Restore queue
        self._queue = temp_queue
        
        # Create storage data
        storage_data = {
            'queue_items': queue_items,
            'failed_memories': self._failed_memories,
            'processed_count': self._processed_count,
            'last_saved': datetime.now().isoformat()
        }
        
        # Write to file
        try:
            with open(self._storage_path, 'w') as f:
                json.dump(storage_data, f, indent=2)
        except Exception as e:
            print(f"Error saving memory queue: {e}")
    
    def _load_from_storage(self) -> None:
        """Load queue state from persistent storage"""
        if not self._storage_path.exists():
            return
        
        try:
            with open(self._storage_path, 'r') as f:
                storage_data = json.load(f)
            
            # Restore queue items
            for item in storage_data.get('queue_items', []):
                self._queue.put(item)
            
            # Restore failed memories
            self._failed_memories = storage_data.get('failed_memories', {})
            
            # Restore processed count
            self._processed_count = storage_data.get('processed_count', 0)
            
        except Exception as e:
            print(f"Error loading memory queue: {e}")
    
    def clear_all(self) -> None:
        """Clear all queue data (use with caution)"""
        with self._lock:
            # Clear queue
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                except queue.Empty:
                    break
            
            # Clear failed memories
            self._failed_memories.clear()
            
            # Reset processed count
            self._processed_count = 0
            
            # Save empty state
            self._save_to_storage()
    
    def get_failed_memories(self) -> Dict[str, Dict[str, Any]]:
        """Get all failed memories for inspection"""
        with self._lock:
            return self._failed_memories.copy()


# Example usage and testing
if __name__ == "__main__":
    # Get singleton instance
    queue1 = MemoryCaptureQueue()
    queue2 = MemoryCaptureQueue()
    
    # Verify singleton
    assert queue1 is queue2, "Singleton pattern not working"
    
    # Add some test memories
    id1 = queue1.add_memory(
        name="Test Pattern Discovery",
        body="Discovered that all API calls should use the centralized error handler",
        source="pattern",
        group_id="api-patterns"
    )
    
    id2 = queue1.add_memory(
        name="Security Fix",
        body="Fixed XSS vulnerability in user input handling",
        source="error_fix",
        group_id="security"
    )
    
    # Get stats
    print("Queue stats:", queue1.get_stats())
    
    # Get a batch
    batch = queue1.get_batch(size=2)
    print(f"Retrieved batch of {len(batch)} memories")
    
    # Simulate processing
    if batch:
        # Mark first as processed
        queue1.mark_processed(batch[0]['id'])
        
        # Mark second as failed if exists
        if len(batch) > 1:
            queue1.mark_failed(batch[1]['id'], "API timeout")
    
    # Get updated stats
    print("Updated stats:", queue1.get_stats())
    
    # Retry failed
    retry_batch = queue1.retry_failed()
    print(f"Retrying {len(retry_batch)} failed memories")