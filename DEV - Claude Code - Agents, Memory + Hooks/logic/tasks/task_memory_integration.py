#!/usr/bin/env python3
"""
Task Memory Integration for Claude Code
Enforces mandatory memory operations for TodoWrite tool events:
- Before task start: Mandatory memory search
- After task completion: Capture task outcome
- During tasks: Track patterns and error resolutions
"""

import logging
import json
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path
import threading
import queue
import time

# Import MCPBridge for memory operations
import sys
sys.path.append(str(Path(__file__).parent.parent))
from memory.mcp_bridge import MCPBridge, MCPBridgeError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TaskMemoryIntegration:
    """
    Integrates TodoWrite events with memory operations via MCPBridge.
    Enforces mandatory memory search before tasks and captures outcomes.
    """
    
    def __init__(self, mcp_timeout: int = 5):
        """
        Initialize the Task Memory Integration.
        
        Args:
            mcp_timeout: Timeout for MCP operations in seconds
        """
        self.mcp_bridge = MCPBridge(timeout=mcp_timeout)
        self._task_contexts = {}  # Track task contexts by task ID
        self._pattern_buffer = []  # Buffer for discovered patterns
        self._error_resolutions = []  # Track error fixes
        self._memory_stats = {
            "searches_performed": 0,
            "memories_captured": 0,
            "patterns_discovered": 0,
            "errors_resolved": 0
        }
        
        # Non-blocking execution queue
        self._memory_queue = queue.Queue()
        self._worker_thread = threading.Thread(target=self._process_memory_queue, daemon=True)
        self._worker_thread.start()
        
        logger.info("Task Memory Integration initialized")
    
    def _process_memory_queue(self):
        """Background worker to process memory operations non-blocking"""
        while True:
            try:
                operation = self._memory_queue.get(timeout=1)
                if operation is None:  # Shutdown signal
                    break
                    
                operation_type = operation.get("type")
                
                if operation_type == "search":
                    self._perform_memory_search(operation)
                elif operation_type == "capture":
                    self._capture_memory(operation)
                    
            except queue.Empty:
                continue
            except Exception as e:
                logger.error(f"Error processing memory operation: {e}")
    
    def on_todo_write(self, todos: List[Dict[str, Any]], event_type: str = "update") -> Dict[str, Any]:
        """
        Handle TodoWrite tool events.
        
        Args:
            todos: List of todo items from TodoWrite
            event_type: Type of event (create, update, complete)
            
        Returns:
            Dict with memory operation results and recommendations
        """
        result = {
            "memory_search_performed": False,
            "memories_found": 0,
            "relevant_memories": [],
            "message": "",
            "capture_scheduled": False
        }
        
        # Identify task context
        task_id = self._extract_task_id(todos)
        
        if event_type == "create" or self._is_new_task(task_id):
            # MANDATORY: Search memories before task start
            search_keywords = self._extract_search_keywords(todos)
            
            if search_keywords:
                # Perform synchronous search for immediate feedback
                search_result = self._search_memories_sync(search_keywords)
                
                result["memory_search_performed"] = True
                result["memories_found"] = search_result.get("count", 0)
                result["relevant_memories"] = search_result.get("memories", [])
                result["message"] = f"Searched {result['memories_found']} memories, found {len(result['relevant_memories'])} relevant"
                
                # Store context for this task
                self._task_contexts[task_id] = {
                    "start_time": datetime.now(),
                    "initial_search": search_result,
                    "todos": todos,
                    "patterns_discovered": [],
                    "errors_resolved": []
                }
                
                self._memory_stats["searches_performed"] += 1
                
                # Log for enforcement tracking
                logger.info(f"MANDATORY SEARCH COMPLETED: Task {task_id} - {result['message']}")
            else:
                result["message"] = "WARNING: Could not extract search keywords from task. Memory search required!"
                logger.warning(f"Failed to extract search keywords for task {task_id}")
        
        elif event_type == "complete":
            # Capture task completion memory
            if task_id in self._task_contexts:
                context = self._task_contexts[task_id]
                
                # Schedule async memory capture
                self._memory_queue.put({
                    "type": "capture",
                    "task_id": task_id,
                    "context": context,
                    "todos": todos,
                    "completion_time": datetime.now()
                })
                
                result["capture_scheduled"] = True
                result["message"] = "Task completion memory capture scheduled"
                
                # Clean up context
                del self._task_contexts[task_id]
        
        # Always check for patterns and errors in todos
        self._detect_patterns_and_errors(todos, task_id)
        
        return result
    
    def _extract_task_id(self, todos: List[Dict[str, Any]]) -> str:
        """Extract or generate a task ID from todos"""
        # Look for high-priority or in-progress tasks
        for todo in todos:
            if todo.get("status") == "in_progress" or todo.get("priority") == "high":
                return todo.get("id", f"task_{hash(todo.get('content', ''))}")
        
        # Fall back to first todo
        if todos:
            return todos[0].get("id", f"task_{hash(todos[0].get('content', ''))}")
        
        return f"task_{int(time.time())}"
    
    def _is_new_task(self, task_id: str) -> bool:
        """Check if this is a new task"""
        return task_id not in self._task_contexts
    
    def _extract_search_keywords(self, todos: List[Dict[str, Any]]) -> List[str]:
        """Extract relevant search keywords from todos"""
        keywords = []
        
        for todo in todos:
            content = todo.get("content", "").lower()
            
            # Extract meaningful terms
            tech_terms = ["api", "component", "function", "module", "service", "hook", 
                         "memory", "database", "auth", "security", "pattern", "error"]
            
            for term in tech_terms:
                if term in content:
                    keywords.append(term)
            
            # Extract action verbs
            action_verbs = ["implement", "fix", "refactor", "integrate", "update", 
                           "create", "debug", "optimize", "test"]
            
            for verb in action_verbs:
                if verb in content:
                    keywords.append(verb)
            
            # Extract feature names (capitalized words)
            words = content.split()
            for word in words:
                if word and word[0].isupper() and len(word) > 3:
                    keywords.append(word.lower())
        
        # Deduplicate and limit
        return list(set(keywords))[:5]
    
    def _search_memories_sync(self, keywords: List[str]) -> Dict[str, Any]:
        """Perform synchronous memory search"""
        try:
            # Build search query
            query = " OR ".join(keywords)
            
            # Search memories
            result = self.mcp_bridge.search_memories(
                query=query,
                limit=20,
                group_ids=["anobel-project", "code-patterns", "error-fixes"]
            )
            
            # Process results
            memories = result.get("results", [])
            relevant_memories = []
            
            for memory in memories:
                relevance_score = self._calculate_relevance(memory, keywords)
                if relevance_score > 0.3:  # Relevance threshold
                    relevant_memories.append({
                        "content": memory.get("episode_body", ""),
                        "name": memory.get("name", ""),
                        "relevance": relevance_score,
                        "created": memory.get("valid_at", "")
                    })
            
            # Sort by relevance
            relevant_memories.sort(key=lambda x: x["relevance"], reverse=True)
            
            return {
                "count": len(memories),
                "memories": relevant_memories[:5],  # Top 5 most relevant
                "keywords_used": keywords
            }
            
        except MCPBridgeError as e:
            logger.error(f"Memory search failed: {e}")
            return {"count": 0, "memories": [], "error": str(e)}
    
    def _calculate_relevance(self, memory: Dict[str, Any], keywords: List[str]) -> float:
        """Calculate relevance score for a memory"""
        content = (memory.get("episode_body", "") + " " + memory.get("name", "")).lower()
        
        # Count keyword matches
        matches = sum(1 for keyword in keywords if keyword in content)
        
        # Normalize by number of keywords
        relevance = matches / len(keywords) if keywords else 0
        
        # Boost recent memories
        try:
            memory_date = datetime.fromisoformat(memory.get("valid_at", "").replace("Z", "+00:00"))
            days_old = (datetime.now(memory_date.tzinfo) - memory_date).days
            if days_old < 7:
                relevance *= 1.5
            elif days_old < 30:
                relevance *= 1.2
        except:
            pass
        
        return min(relevance, 1.0)
    
    def _detect_patterns_and_errors(self, todos: List[Dict[str, Any]], task_id: str):
        """Detect patterns and error resolutions in todos"""
        for todo in todos:
            content = todo.get("content", "").lower()
            status = todo.get("status", "")
            
            # Pattern detection
            pattern_indicators = ["always", "convention", "best practice", "pattern", 
                                "standard", "rule", "guideline"]
            
            if any(indicator in content for indicator in pattern_indicators) and status == "completed":
                self._pattern_buffer.append({
                    "content": todo.get("content"),
                    "task_id": task_id,
                    "timestamp": datetime.now()
                })
                
                # Capture pattern memory if buffer is significant
                if len(self._pattern_buffer) >= 3:
                    self._capture_pattern_memory()
            
            # Error resolution detection
            error_indicators = ["fixed", "resolved", "solution", "error", "bug", 
                              "issue", "problem solved"]
            
            if any(indicator in content for indicator in error_indicators) and status == "completed":
                self._error_resolutions.append({
                    "content": todo.get("content"),
                    "task_id": task_id,
                    "timestamp": datetime.now()
                })
                
                # Capture error resolution immediately
                self._capture_error_resolution(todo.get("content"))
    
    def _perform_memory_search(self, operation: Dict[str, Any]):
        """Perform async memory search"""
        try:
            keywords = operation.get("keywords", [])
            task_id = operation.get("task_id")
            
            result = self._search_memories_sync(keywords)
            
            # Store result in context if available
            if task_id and task_id in self._task_contexts:
                self._task_contexts[task_id]["search_results"] = result
                
            logger.info(f"Async memory search completed for task {task_id}")
            
        except Exception as e:
            logger.error(f"Async memory search failed: {e}")
    
    def _capture_memory(self, operation: Dict[str, Any]):
        """Capture memory asynchronously"""
        try:
            task_id = operation.get("task_id")
            context = operation.get("context", {})
            todos = operation.get("todos", [])
            completion_time = operation.get("completion_time")
            
            # Build memory content
            task_duration = (completion_time - context["start_time"]).total_seconds() / 60
            completed_todos = [t for t in todos if t.get("status") == "completed"]
            
            memory_name = f"TASK_COMPLETED: {todos[0].get('content', 'Unknown task')[:50]}"
            
            memory_body = f"""Task completed in {task_duration:.1f} minutes.

Initial Search: Found {context['initial_search'].get('count', 0)} relevant memories
Keywords Used: {', '.join(context['initial_search'].get('keywords_used', []))}

Completed Items ({len(completed_todos)}):
{chr(10).join(f"- {t.get('content')}" for t in completed_todos)}

Patterns Discovered: {len(context.get('patterns_discovered', []))}
Errors Resolved: {len(context.get('errors_resolved', []))}
"""
            
            # Add memory
            result = self.mcp_bridge.add_memory(
                name=memory_name,
                episode_body=memory_body,
                source="task_completion",
                source_description="Task Memory Integration",
                group_id="anobel-tasks"
            )
            
            self._memory_stats["memories_captured"] += 1
            logger.info(f"Task completion memory captured for {task_id}")
            
        except Exception as e:
            logger.error(f"Failed to capture task memory: {e}")
    
    def _capture_pattern_memory(self):
        """Capture discovered patterns as memory"""
        if not self._pattern_buffer:
            return
            
        try:
            patterns = self._pattern_buffer[-3:]  # Last 3 patterns
            
            memory_name = "PATTERN: Discovered coding patterns"
            memory_body = "Discovered patterns:\n\n" + "\n\n".join(
                f"- {p['content']}\n  Task: {p['task_id']}\n  Time: {p['timestamp'].strftime('%Y-%m-%d %H:%M')}"
                for p in patterns
            )
            
            self.mcp_bridge.add_memory(
                name=memory_name,
                episode_body=memory_body,
                source="pattern_discovery",
                source_description="Task Memory Integration",
                group_id="code-patterns"
            )
            
            self._memory_stats["patterns_discovered"] += len(patterns)
            self._pattern_buffer = []  # Clear buffer
            
            logger.info("Pattern memory captured")
            
        except Exception as e:
            logger.error(f"Failed to capture pattern memory: {e}")
    
    def _capture_error_resolution(self, resolution: str):
        """Capture error resolution as memory"""
        try:
            memory_name = f"ERROR_FIX: {resolution[:50]}"
            memory_body = f"""Error Resolution Captured:

{resolution}

Captured at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Context: Task execution with TodoWrite
"""
            
            self.mcp_bridge.add_memory(
                name=memory_name,
                episode_body=memory_body,
                source="error_resolution",
                source_description="Task Memory Integration",
                group_id="error-fixes"
            )
            
            self._memory_stats["errors_resolved"] += 1
            logger.info("Error resolution memory captured")
            
        except Exception as e:
            logger.error(f"Failed to capture error resolution: {e}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get memory operation statistics"""
        return {
            **self._memory_stats,
            "active_tasks": len(self._task_contexts),
            "pattern_buffer_size": len(self._pattern_buffer),
            "error_resolutions_pending": len(self._error_resolutions)
        }
    
    def display_search_message(self, result: Dict[str, Any]) -> str:
        """Format search result message for display"""
        if not result.get("memory_search_performed"):
            return "⚠️ MEMORY SEARCH REQUIRED - No search performed!"
        
        message = f"🔍 {result['message']}"
        
        if result.get("relevant_memories"):
            message += "\n\n📚 Relevant memories found:"
            for i, memory in enumerate(result["relevant_memories"][:3], 1):
                message += f"\n{i}. {memory['name']} (relevance: {memory['relevance']:.2f})"
        
        return message
    
    def shutdown(self):
        """Shutdown the integration gracefully"""
        logger.info("Shutting down Task Memory Integration")
        self._memory_queue.put(None)  # Signal shutdown
        self._worker_thread.join(timeout=5)
        
        # Capture any remaining patterns
        if self._pattern_buffer:
            self._capture_pattern_memory()
        
        logger.info(f"Final stats: {self.get_stats()}")


# Integration helper for task_manager.py
class TodoWriteMemoryHandler:
    """
    Handler to integrate with existing task_manager.py
    Intercepts TodoWrite operations and enforces memory operations
    """
    
    def __init__(self):
        self.memory_integration = TaskMemoryIntegration()
    
    def before_todo_write(self, todos: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Called before TodoWrite execution"""
        # Determine event type based on todo states
        event_type = "update"
        
        # Check if this is a new task (no in_progress items)
        has_in_progress = any(t.get("status") == "in_progress" for t in todos)
        if not has_in_progress and todos:
            event_type = "create"
        
        # Check if all todos are completed
        all_completed = all(t.get("status") == "completed" for t in todos)
        if all_completed and todos:
            event_type = "complete"
        
        # Process with memory integration
        result = self.memory_integration.on_todo_write(todos, event_type)
        
        # Display mandatory message
        if result.get("message"):
            print(f"\n{self.memory_integration.display_search_message(result)}\n")
        
        return result
    
    def after_todo_write(self, todos: List[Dict[str, Any]], success: bool):
        """Called after TodoWrite execution"""
        if success:
            # Check for task completion
            all_completed = all(t.get("status") == "completed" for t in todos)
            if all_completed:
                self.memory_integration.on_todo_write(todos, "complete")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get integration statistics"""
        return self.memory_integration.get_stats()
    
    def shutdown(self):
        """Shutdown the handler"""
        self.memory_integration.shutdown()


# Example usage
if __name__ == "__main__":
    # Test the integration
    handler = TodoWriteMemoryHandler()
    
    # Simulate new task
    test_todos = [
        {
            "id": "test-1",
            "content": "Implement new API authentication module",
            "status": "pending",
            "priority": "high"
        },
        {
            "id": "test-2", 
            "content": "Fix security vulnerability in user service",
            "status": "pending",
            "priority": "high"
        }
    ]
    
    # Before TodoWrite (new task)
    result = handler.before_todo_write(test_todos)
    print(f"Pre-execution result: {json.dumps(result, indent=2)}")
    
    # Simulate task progress
    test_todos[0]["status"] = "in_progress"
    result = handler.before_todo_write(test_todos)
    
    # Simulate task completion
    test_todos[0]["status"] = "completed"
    test_todos[1]["status"] = "completed"
    handler.after_todo_write(test_todos, True)
    
    # Get stats
    print(f"\nStats: {json.dumps(handler.get_stats(), indent=2)}")
    
    # Shutdown
    handler.shutdown()