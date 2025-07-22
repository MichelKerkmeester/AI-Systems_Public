#!/usr/bin/env python3
"""
Enhanced Memory Context Hook v2 with MCPBridge and MemoryCaptureQueue
Processes memories in background thread, non-blocking execution
"""

import sys
import json
import re
import threading
import queue
import time
import logging
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List, Set
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

# Add parent directories to path for imports
hooks_path = Path(__file__).resolve().parent
logic_path = hooks_path.parent
claude_path = logic_path.parent
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase, UserPromptHook


class MemoryPriority(Enum):
    """Priority levels for memory capture"""
    CRITICAL = 1  # Security, breaking changes
    HIGH = 2      # Decisions, patterns
    MEDIUM = 3    # Errors fixed, optimizations
    LOW = 4       # General learnings


@dataclass
class MemoryItem:
    """Memory item to be captured"""
    content: str
    memory_type: str
    context: str
    priority: MemoryPriority
    timestamp: datetime
    file_path: Optional[str] = None
    line_number: Optional[int] = None


class MCPBridge:
    """Bridge to interact with MCP tools"""
    
    def __init__(self, logger):
        self.logger = logger
        self._simulated_mode = True  # For testing without actual MCP
        
    def call_tool(self, tool_name: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Call an MCP tool with parameters"""
        try:
            if self._simulated_mode:
                self.logger.debug(f"[Simulated] MCP tool call: {tool_name}")
                self.logger.debug(f"[Simulated] Parameters: {json.dumps(params, indent=2)}")
                
                # Simulate successful response
                if tool_name == "mcp__graphiti-gemini__search":
                    return {
                        "results": [],
                        "status": "success"
                    }
                elif tool_name == "mcp__graphiti-gemini__add_episode":
                    return {
                        "id": f"memory_{int(time.time())}",
                        "status": "success"
                    }
            else:
                # Real MCP integration would go here
                # This would use subprocess or MCP client library
                pass
                
            return {"status": "success"}
            
        except Exception as e:
            self.logger.error(f"MCPBridge error calling {tool_name}: {e}")
            return None
            
    def search_memories(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search for memories using Graphiti"""
        result = self.call_tool(
            "mcp__graphiti-gemini__search",
            {
                "query": {
                    "query": query,
                    "limit": limit
                }
            }
        )
        
        if result and "results" in result:
            return result["results"]
        return []
        
    def add_memory(self, memory_item: MemoryItem) -> bool:
        """Add a memory to Graphiti"""
        episode_data = {
            "name": f"{memory_item.memory_type}: {memory_item.content[:50]}...",
            "episode_body": memory_item.content,
            "source": "memory_context_hook_v2",
            "source_description": f"Auto-captured from {memory_item.context}",
            "valid_at": memory_item.timestamp.isoformat()
        }
        
        # Add file context if available
        if memory_item.file_path:
            episode_data["source_description"] += f" in {memory_item.file_path}"
            if memory_item.line_number:
                episode_data["source_description"] += f":L{memory_item.line_number}"
        
        result = self.call_tool(
            "mcp__graphiti-gemini__add_episode",
            {"data": episode_data}
        )
        
        return result is not None and result.get("status") == "success"


class MemoryCaptureQueue:
    """Queue for processing memories in background"""
    
    def __init__(self, mcp_bridge: MCPBridge, logger):
        self.mcp_bridge = mcp_bridge
        self.logger = logger
        self.queue = queue.PriorityQueue()
        self.processing_thread = None
        self.shutdown = False
        self.processed_count = 0
        self.failed_count = 0
        
    def start(self):
        """Start the background processing thread"""
        if not self.processing_thread or not self.processing_thread.is_alive():
            self.shutdown = False
            self.processing_thread = threading.Thread(
                target=self._process_queue,
                daemon=True
            )
            self.processing_thread.start()
            self.logger.debug("Memory capture queue started")
            
    def stop(self):
        """Stop the background processing thread"""
        self.shutdown = True
        if self.processing_thread and self.processing_thread.is_alive():
            self.processing_thread.join(timeout=2)
            
    def add(self, memory_item: MemoryItem):
        """Add a memory item to the queue"""
        # Priority queue uses tuple (priority_value, item)
        # Lower values have higher priority
        self.queue.put((memory_item.priority.value, memory_item))
        self.logger.debug(f"Added {memory_item.memory_type} to queue with priority {memory_item.priority.name}")
        
    def _process_queue(self):
        """Background thread to process memory items"""
        while not self.shutdown:
            try:
                # Wait for items with timeout
                priority, memory_item = self.queue.get(timeout=1)
                
                # Process the memory
                if self.mcp_bridge.add_memory(memory_item):
                    self.processed_count += 1
                    self.logger.debug(f"Successfully captured {memory_item.memory_type} memory")
                else:
                    self.failed_count += 1
                    self.logger.error(f"Failed to capture {memory_item.memory_type} memory")
                    
                self.queue.task_done()
                
            except queue.Empty:
                continue
            except Exception as e:
                self.logger.error(f"Error processing memory queue: {e}")
                
    def get_stats(self) -> Dict[str, int]:
        """Get queue statistics"""
        return {
            "queued": self.queue.qsize(),
            "processed": self.processed_count,
            "failed": self.failed_count
        }


class EnhancedMemoryContextHook(UserPromptHook):
    """Enhanced memory context hook with background processing and extended patterns"""
    
    def __init__(self):
        super().__init__()
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
        
        # Initialize components
        self.mcp_bridge = MCPBridge(self.logger)
        self.capture_queue = MemoryCaptureQueue(self.mcp_bridge, self.logger)
        
        # State tracking
        self.memory_loaded = False
        self.session_memories = []
        self.processed_prompts = set()
        
        # Load settings
        self.settings = self._load_settings()
        
        # Enhanced capture patterns with priorities
        self.capture_patterns = {
            # Critical patterns (Priority 1)
            "SECURITY": (r"security|auth|token|credential|password|encryption|api[_\s]?key", MemoryPriority.CRITICAL),
            "BREAKING": (r"breaking change|migration|upgrade|deprecated|incompatible", MemoryPriority.CRITICAL),
            
            # High priority patterns (Priority 2)
            "DECISION": (r"decided to|will use|choosing|selected|going with|opted for", MemoryPriority.HIGH),
            "PATTERN": (r"pattern|convention|standard|always|never|best practice", MemoryPriority.HIGH),
            "REUSABLE_COMPONENT": (r"reusable|component|module|utility|helper|shared", MemoryPriority.HIGH),
            "EXISTING_SOLUTION": (r"already exists|found existing|can reuse|duplicate of", MemoryPriority.HIGH),
            
            # Medium priority patterns (Priority 3)
            "RESOLVED": (r"fixed|resolved|solution|workaround|solved|debugged", MemoryPriority.MEDIUM),
            "ERROR_FIX": (r"error.*fixed|resolved.*issue|bug.*solution|troubleshooted", MemoryPriority.MEDIUM),
            "OPTIMIZATION": (r"optimized|improved.*performance|faster|reduced|efficient", MemoryPriority.MEDIUM),
            "REFACTOR_OPPORTUNITY": (r"could refactor|should consolidate|duplicate code|cleanup", MemoryPriority.MEDIUM),
            
            # Low priority patterns (Priority 4)
            "USER_FEEDBACK": (r"user.*said|client.*wants|requirement|asked for|requested", MemoryPriority.LOW),
            "CONFIG_CHANGE": (r"configured|setting.*changed|updated.*config|modified", MemoryPriority.LOW),
            "LEARNING": (r"learned|discovered|found out|realized|understood|insight", MemoryPriority.LOW),
            "ARCHITECTURE": (r"architecture|design.*decision|structure|system design", MemoryPriority.LOW),
            "API_CHANGE": (r"api.*changed|endpoint|interface.*modified|contract", MemoryPriority.LOW),
            "DEPENDENCY": (r"installed|upgraded.*package|dependency|library|npm|pip", MemoryPriority.LOW)
        }
        
        # Start the capture queue
        self.capture_queue.start()
        
    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from settings.json"""
        try:
            settings_path = self.claude_path / "settings.json"
            if settings_path.exists():
                with open(settings_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load settings: {e}")
        
        # Default settings
        return {
            "memory": {
                "auto_context": True,
                "context_on_startup": True,
                "max_relevant_memories": 5,
                "show_suggestions": True
            }
        }
        
    def extract_keywords(self, text: str, max_keywords: int = 7) -> List[str]:
        """Extract meaningful keywords from user input"""
        # Enhanced stop words including technical terms
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
            'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
            'could', 'should', 'may', 'might', 'must', 'can', 'how', 'what',
            'when', 'where', 'why', 'which', 'who', 'whom', 'this', 'that',
            'these', 'those', 'i', 'you', 'we', 'they', 'it', 'me', 'my',
            'please', 'help', 'need', 'want', 'like', 'make', 'create',
            'update', 'change', 'modify', 'add', 'remove', 'delete', 'get', 'set'
        }
        
        # Extract words including compound terms
        words = re.findall(r'\b[a-zA-Z][a-zA-Z0-9_-]*\b', text.lower())
        
        # Prioritize longer, more specific terms
        keywords = []
        seen = set()
        
        # First pass: compound terms and technical words
        for i in range(len(words)):
            # Try to capture compound terms
            if i < len(words) - 1:
                compound = f"{words[i]}_{words[i+1]}"
                if compound not in seen and len(compound) > 5:
                    keywords.append(compound)
                    seen.add(compound)
                    
        # Second pass: individual meaningful words
        for word in words:
            if (word not in stop_words and 
                len(word) > 2 and 
                word not in seen and
                not word.isdigit()):
                keywords.append(word)
                seen.add(word)
                
        return keywords[:max_keywords]
        
    def extract_context(self, text: str, match_start: int, match_end: int, 
                       context_chars: int = 150) -> Tuple[str, Optional[str], Optional[int]]:
        """Extract context around a match, including file path and line number if available"""
        # Get surrounding context
        start = max(0, match_start - context_chars)
        end = min(len(text), match_end + context_chars)
        context = text[start:end].strip()
        
        # Try to extract file path from context
        file_path = None
        line_number = None
        
        # Look for file paths (common patterns)
        file_pattern = r'(?:file:|path:|in\s+)([/\w\-\.]+\.(?:js|py|jsx|tsx|ts|css|html|json))'
        file_match = re.search(file_pattern, context, re.IGNORECASE)
        if file_match:
            file_path = file_match.group(1)
            
            # Look for line numbers
            line_pattern = r'(?:line|L|:)(\d+)'
            line_match = re.search(line_pattern, context[file_match.end():], re.IGNORECASE)
            if line_match:
                line_number = int(line_match.group(1))
                
        return context, file_path, line_number
        
    def detect_patterns(self, text: str) -> List[Tuple[str, str, MemoryPriority, Optional[str], Optional[int]]]:
        """Detect capture patterns in text with enhanced context"""
        detected = []
        
        for pattern_type, (pattern, priority) in self.capture_patterns.items():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                context, file_path, line_number = self.extract_context(
                    text, match.start(), match.end()
                )
                detected.append((pattern_type, context, priority, file_path, line_number))
                
        return detected
        
    def format_memory_context(self, memories: List[Dict], keywords: List[str], 
                            captured_count: int = 0) -> str:
        """Format memories for display with enhanced information"""
        output = []
        output.append("\n" + "="*60)
        output.append("🧠 MEMORY CONTEXT v2 - Enhanced with Background Processing")
        output.append("="*60)
        
        # Show search status
        if keywords:
            output.append(f"\n🔍 Searched memories for: {', '.join(keywords[:3])}")
            
        if memories:
            output.append(f"\n📍 Found {len(memories)} relevant memories:")
            
            for i, memory in enumerate(memories[:self.settings['memory']['max_relevant_memories']], 1):
                name = memory.get('name', 'Untitled')
                content = memory.get('episode_body', '')
                source = memory.get('source', '')
                timestamp = memory.get('valid_at', '')
                
                # Format timestamp
                if timestamp:
                    try:
                        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                        time_str = dt.strftime('%Y-%m-%d %H:%M')
                    except:
                        time_str = timestamp
                else:
                    time_str = 'Unknown'
                
                # Truncate content if too long
                if len(content) > 200:
                    content = content[:200] + "..."
                    
                output.append(f"\n{i}. {name}")
                output.append(f"   📅 {time_str} | 📝 {source}")
                if content:
                    # Indent content for readability
                    content_lines = content.split('\n')
                    for line in content_lines[:3]:  # Max 3 lines
                        output.append(f"   {line.strip()}")
                        
        else:
            output.append("\n📭 No relevant memories found")
            
        # Show capture queue stats
        stats = self.capture_queue.get_stats()
        if captured_count > 0 or stats['queued'] > 0:
            output.append(f"\n💾 Memory Capture Status:")
            output.append(f"   • Captured this prompt: {captured_count}")
            output.append(f"   • In queue: {stats['queued']}")
            output.append(f"   • Processed total: {stats['processed']}")
            if stats['failed'] > 0:
                output.append(f"   • Failed: {stats['failed']} ⚠️")
                
        # Show session summary
        if self.session_memories:
            output.append(f"\n📊 Session Summary: {len(self.session_memories)} memories captured")
            # Group by type
            type_counts = {}
            for mem in self.session_memories:
                type_counts[mem['type']] = type_counts.get(mem['type'], 0) + 1
            
            for mem_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
                output.append(f"   • {mem_type}: {count}")
                
        output.append("\n" + "="*60 + "\n")
        return "\n".join(output)
        
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook input with enhanced pattern detection and background capture"""
        user_input = hook_input.get('user_input', '')
        
        # Skip for certain commands
        skip_patterns = ['/memory', '/test', '/workflow', '/mode', '/pr', '/security', '/save', '/logic']
        if any(user_input.strip().startswith(cmd) for cmd in skip_patterns):
            return 0, None
            
        try:
            # Avoid processing the same prompt multiple times
            prompt_hash = hash(user_input)
            if prompt_hash in self.processed_prompts:
                return 0, None
            self.processed_prompts.add(prompt_hash)
            
            # Extract keywords from user input
            keywords = self.extract_keywords(user_input)
            
            # Detect patterns for automatic capture
            detected_patterns = self.detect_patterns(user_input)
            
            # Queue detected patterns for background capture
            captured_count = 0
            for pattern_type, context, priority, file_path, line_number in detected_patterns:
                memory_item = MemoryItem(
                    content=context,
                    memory_type=pattern_type,
                    context="user_prompt",
                    priority=priority,
                    timestamp=datetime.now(),
                    file_path=file_path,
                    line_number=line_number
                )
                self.capture_queue.add(memory_item)
                captured_count += 1
                
                # Track in session memories
                self.session_memories.append({
                    "type": pattern_type,
                    "content": context[:100],  # Truncated for tracking
                    "priority": priority.name,
                    "timestamp": datetime.now().isoformat()
                })
                
            # Search and display memories
            output = None
            
            # Always search on first interaction or if keywords present
            if (not self.memory_loaded and keywords) or (keywords and self.settings['memory']['auto_context']):
                # Search for relevant memories
                query = " ".join(keywords[:5])  # Use more keywords for better search
                memories = self.mcp_bridge.search_memories(query, 
                    limit=self.settings['memory']['max_relevant_memories'] * 2)  # Get extra for filtering
                
                # Display context if memories found or patterns captured
                if memories or captured_count > 0:
                    self.memory_loaded = True
                    output = self.format_memory_context(memories, keywords, captured_count)
                    
            # If patterns were captured but no full context shown, show brief notification
            elif captured_count > 0 and self.settings['memory']['show_suggestions']:
                queue_stats = self.capture_queue.get_stats()
                output = (f"\n💾 Auto-captured {captured_count} memory patterns "
                         f"({queue_stats['queued']} in queue)\n")
                
            return 0, output
            
        except Exception as e:
            # Log error but don't disrupt user experience
            self.logger.error(f"Memory context hook v2 error: {e}")
            return 0, None
            
    def __del__(self):
        """Cleanup when hook is destroyed"""
        try:
            self.capture_queue.stop()
        except:
            pass


# Main entry point
if __name__ == "__main__":
    hook = EnhancedMemoryContextHook()
    hook.run()