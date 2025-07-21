#!/usr/bin/env python3
"""
Post Tool Use Memory Hook V2
Enhanced version that uses MCPBridge for direct memory capture
Captures memories after significant tool operations with better context extraction
"""

import sys
import json
import re
import threading
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List
from datetime import datetime
import hashlib

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase
from logic.memory.mcp_bridge import MCPBridge, MCPBridgeError
from logic.memory.memory_capture_queue import MemoryCaptureQueue


class PostToolUseMemoryV2Hook(HookBase):
    """Enhanced memory capture after significant tool uses with direct MCPBridge execution"""
    
    def __init__(self):
        super().__init__()
        
        # Initialize MCP Bridge and Memory Queue
        self.mcp_bridge = MCPBridge(timeout=10)
        self.memory_queue = MemoryCaptureQueue()
        
        # Tools that trigger memory capture with enhanced metadata
        self.significant_tools = {
            # File operations
            "Edit": {
                "type": "code_change",
                "priority": "high",
                "patterns": ["ERROR_RESOLVED", "PATTERN", "BREAKING_CHANGE"]
            },
            "MultiEdit": {
                "type": "code_change_batch", 
                "priority": "high",
                "patterns": ["ERROR_RESOLVED", "PATTERN", "BREAKING_CHANGE", "REFACTOR"]
            },
            "Write": {
                "type": "file_creation",
                "priority": "medium",
                "patterns": ["PATTERN", "NEW_COMPONENT", "API_ENDPOINT"]
            },
            "NotebookEdit": {
                "type": "notebook_change",
                "priority": "medium",
                "patterns": ["EXPERIMENT", "ANALYSIS", "DATA_PROCESSING"]
            },
            
            # Git operations
            "mcp__github-mcp-server__create_pull_request": {
                "type": "pr_created",
                "priority": "critical",
                "patterns": ["FEATURE_COMPLETE", "BUG_FIX", "BREAKING_CHANGE"]
            },
            "mcp__github-mcp-server__merge_pull_request": {
                "type": "pr_merged",
                "priority": "critical",
                "patterns": ["DEPLOYED", "MERGED", "RELEASED"]
            },
            "mcp__github-mcp-server__create_issue": {
                "type": "issue_created",
                "priority": "medium",
                "patterns": ["BUG_REPORT", "FEATURE_REQUEST", "TASK"]
            },
            
            # System operations
            "Bash": {
                "type": "command_execution",
                "priority": "low",
                "patterns": ["ERROR_RESOLVED", "SYSTEM_CHANGE", "DEPENDENCY_UPDATE"]
            }
        }
        
        # Enhanced patterns with context extraction
        self.result_patterns = {
            "ERROR_RESOLVED": {
                "regex": r"(error|bug|issue|problem|crash|failure).*?(fixed|resolved|solved|debugged|corrected|patched)",
                "extract": r"(error[^.!?]*(?:fixed|resolved|solved)[^.!?]*)",
                "priority": "critical"
            },
            "PATTERN": {
                "regex": r"(pattern|convention|standard|best practice|approach|method).*?(discovered|identified|established|using|following)",
                "extract": r"((?:pattern|convention|standard)[^.!?]*)",
                "priority": "high"
            },
            "BREAKING_CHANGE": {
                "regex": r"(breaking change|migration|deprecated|incompatible|major change|api change)",
                "extract": r"(breaking change[^.!?]*|migration[^.!?]*)",
                "priority": "critical"
            },
            "PERFORMANCE": {
                "regex": r"(optimized|faster|performance|speed|efficiency).*?(improved|increased|reduced|enhanced)",
                "extract": r"((?:optimized|performance)[^.!?]*)",
                "priority": "high"
            },
            "SECURITY_FIX": {
                "regex": r"(vulnerability|security|exploit|injection|xss|csrf).*?(fixed|patched|secured|protected)",
                "extract": r"((?:vulnerability|security)[^.!?]*(?:fixed|patched)[^.!?]*)",
                "priority": "critical"
            },
            "API_ENDPOINT": {
                "regex": r"(endpoint|api|route|controller).*?(created|added|implemented|defined)",
                "extract": r"((?:endpoint|api|route)[^.!?]*)",
                "priority": "medium"
            },
            "REFACTOR": {
                "regex": r"(refactor|restructure|reorganize|clean.*?up|simplif)",
                "extract": r"(refactor[^.!?]*)",
                "priority": "medium"
            },
            "NEW_COMPONENT": {
                "regex": r"(component|module|service|class|function).*?(created|added|implemented|new)",
                "extract": r"((?:component|module|service)[^.!?]*)",
                "priority": "medium"
            }
        }
        
        # Load memory settings
        settings_path = Path(__file__).parent.parent.parent / "memory" / "settings.json"
        try:
            with open(settings_path) as f:
                self.memory_settings = json.load(f)
        except:
            self.memory_settings = {"automation_level": "semi"}
            
        # Context accumulator for better understanding
        self.context_accumulator = []
        self.last_operation_hash = None
        
        # Background thread for processing queue
        self.start_background_processor()
        
    def start_background_processor(self):
        """Start background thread to process memory queue"""
        def process_queue():
            while True:
                try:
                    # Get batch of memories
                    batch = self.memory_queue.get_batch(size=3)
                    
                    if batch:
                        for memory in batch:
                            try:
                                # Capture via MCPBridge
                                result = self.mcp_bridge.add_memory(
                                    name=memory['name'],
                                    episode_body=memory['body'],
                                    source=memory['source'],
                                    group_id=memory.get('group_id'),
                                    valid_at=memory.get('timestamp')
                                )
                                # Mark as processed
                                self.memory_queue.mark_processed(memory['id'])
                                self.logger.info(f"Successfully captured memory: {memory['name']}")
                            except MCPBridgeError as e:
                                # Mark as failed for retry
                                self.memory_queue.mark_failed(memory['id'], str(e))
                                self.logger.error(f"Failed to capture memory {memory['id']}: {e}")
                    
                    # Sleep before next batch
                    threading.Event().wait(5)
                    
                except Exception as e:
                    self.logger.error(f"Background processor error: {e}")
                    threading.Event().wait(10)
        
        # Start daemon thread
        processor_thread = threading.Thread(target=process_queue, daemon=True)
        processor_thread.start()
        
    def should_capture(self, tool_name: str, tool_args: Dict, result: Any) -> bool:
        """Enhanced capture decision with pattern detection"""
        # Check automation level
        level = self.memory_settings.get("automation_level", "semi")
        if level == "off":
            return False
            
        # Check if it's a significant tool
        if tool_name not in self.significant_tools:
            return False
            
        # For manual mode, only capture critical operations
        if level == "manual":
            tool_config = self.significant_tools.get(tool_name, {})
            return tool_config.get("priority") == "critical"
            
        # For semi/full mode, check additional criteria
        # Skip small edits (less than 3 lines)
        if tool_name in ["Edit", "MultiEdit"]:
            content = tool_args.get("new_string", "")
            if content.count('\n') < 3:
                return False
                
        # Check for pattern matches in result
        result_str = str(result) if result else ""
        tool_config = self.significant_tools.get(tool_name, {})
        expected_patterns = tool_config.get("patterns", [])
        
        for pattern_name in expected_patterns:
            pattern_config = self.result_patterns.get(pattern_name, {})
            if re.search(pattern_config.get("regex", ""), result_str, re.IGNORECASE):
                return True
                
        # In full mode, capture all significant operations
        if level == "full":
            return True
            
        return False
        
    def extract_operation_context(self, tool_name: str, tool_args: Dict, result: Any) -> Dict[str, Any]:
        """Enhanced context extraction with better understanding"""
        context = {
            "tool": tool_name,
            "type": self.significant_tools.get(tool_name, {}).get("type", "unknown"),
            "priority": self.significant_tools.get(tool_name, {}).get("priority", "low"),
            "timestamp": datetime.now().isoformat(),
            "success": True  # Assume success if we got here
        }
        
        # Extract file paths with better normalization
        if "file_path" in tool_args:
            file_path = Path(tool_args["file_path"])
            context["file"] = str(file_path)
            context["file_name"] = file_path.name
            context["file_type"] = file_path.suffix
        elif "path" in tool_args:
            file_path = Path(tool_args["path"])
            context["file"] = str(file_path)
            context["file_name"] = file_path.name
            context["file_type"] = file_path.suffix
            
        # Enhanced operation details extraction
        if tool_name == "Edit":
            old_content = tool_args.get("old_string", "")
            new_content = tool_args.get("new_string", "")
            context["changes"] = {
                "lines_removed": old_content.count('\n') + 1 if old_content else 0,
                "lines_added": new_content.count('\n') + 1 if new_content else 0,
                "change_summary": self._summarize_change(old_content, new_content)
            }
        elif tool_name == "MultiEdit":
            edits = tool_args.get("edits", [])
            context["changes"] = {
                "edit_count": len(edits),
                "total_lines_changed": sum(e.get("new_string", "").count('\n') + 1 for e in edits),
                "files_affected": 1
            }
        elif tool_name == "Write":
            content = tool_args.get("content", "")
            context["file_stats"] = {
                "lines": content.count('\n') + 1,
                "size": len(content),
                "has_tests": "test" in content.lower() or "describe(" in content,
                "has_docs": "/**" in content or '"""' in content
            }
        elif tool_name == "Bash":
            context["command"] = tool_args.get("command", "")
            context["command_type"] = self._classify_command(tool_args.get("command", ""))
            if isinstance(result, dict):
                context["output_summary"] = result.get("output", "")[:500]
        elif "github" in tool_name:
            context["repo"] = f"{tool_args.get('owner', '')}/{tool_args.get('repo', '')}"
            context["github_action"] = tool_name.split("__")[-1]
            
        # Enhanced pattern detection with context extraction
        result_str = str(result) if result else ""
        content_str = str(tool_args) + " " + result_str
        
        detected_patterns = []
        for pattern_name, pattern_config in self.result_patterns.items():
            match = re.search(pattern_config["regex"], content_str, re.IGNORECASE)
            if match:
                detected_patterns.append({
                    "type": pattern_name,
                    "priority": pattern_config["priority"],
                    "context": match.group(0)[:200]
                })
                
        if detected_patterns:
            # Sort by priority and take the most important
            detected_patterns.sort(key=lambda x: {"critical": 0, "high": 1, "medium": 2, "low": 3}[x["priority"]])
            context["patterns_detected"] = detected_patterns
            context["primary_pattern"] = detected_patterns[0]["type"]
            
        # Add to context accumulator for relationship detection
        self.context_accumulator.append(context)
        if len(self.context_accumulator) > 10:
            self.context_accumulator.pop(0)
            
        return context
        
    def _summarize_change(self, old_content: str, new_content: str) -> str:
        """Create a brief summary of what changed"""
        if not old_content:
            return "New content added"
        if not new_content:
            return "Content removed"
            
        # Check for common patterns
        if "function" in new_content and "function" not in old_content:
            return "Function added"
        if "class" in new_content and "class" not in old_content:
            return "Class added"
        if "import" in new_content and "import" not in old_content:
            return "Imports modified"
        if "test" in new_content.lower() and "test" not in old_content.lower():
            return "Tests added"
            
        # Default to line count change
        old_lines = old_content.count('\n') + 1
        new_lines = new_content.count('\n') + 1
        diff = new_lines - old_lines
        
        if diff > 0:
            return f"{diff} lines added"
        elif diff < 0:
            return f"{abs(diff)} lines removed"
        else:
            return "Content modified"
            
    def _classify_command(self, command: str) -> str:
        """Classify the type of bash command"""
        if "npm" in command or "yarn" in command:
            return "package_management"
        elif "git" in command:
            return "version_control"
        elif "test" in command or "jest" in command:
            return "testing"
        elif "build" in command or "webpack" in command:
            return "build"
        elif "docker" in command:
            return "containerization"
        else:
            return "system"
            
    def format_memory_episode(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Enhanced memory episode formatting with better context"""
        # Create a descriptive name with pattern awareness
        name_parts = []
        
        if context.get("primary_pattern"):
            pattern_name = context["primary_pattern"].replace("_", " ").title()
            name_parts.append(f"[{pattern_name}]")
            
        name_parts.append(context["type"].replace("_", " ").title())
        
        if context.get("file_name"):
            name_parts.append(f"in {context['file_name']}")
        elif context.get("repo"):
            name_parts.append(f"in {context['repo']}")
            
        name = " ".join(name_parts)
        
        # Build comprehensive episode body
        body_parts = []
        body_parts.append(f"Operation: {context['tool']}")
        body_parts.append(f"Type: {context['type']}")
        body_parts.append(f"Priority: {context['priority']}")
        body_parts.append(f"Timestamp: {context['timestamp']}")
        
        if context.get("file"):
            body_parts.append(f"\nFile: {context['file']}")
            body_parts.append(f"File Type: {context.get('file_type', 'unknown')}")
            
        # Add change details
        if context.get("changes"):
            body_parts.append("\nChanges:")
            for key, value in context["changes"].items():
                body_parts.append(f"  {key}: {value}")
                
        # Add file statistics
        if context.get("file_stats"):
            body_parts.append("\nFile Statistics:")
            for key, value in context["file_stats"].items():
                body_parts.append(f"  {key}: {value}")
                
        # Add command details
        if context.get("command"):
            body_parts.append(f"\nCommand: {context['command']}")
            body_parts.append(f"Command Type: {context.get('command_type', 'unknown')}")
            if context.get("output_summary"):
                body_parts.append(f"Output Preview: {context['output_summary']}")
                
        # Add GitHub details
        if context.get("repo"):
            body_parts.append(f"\nRepository: {context['repo']}")
            body_parts.append(f"Action: {context.get('github_action', 'unknown')}")
            
        # Add detected patterns
        if context.get("patterns_detected"):
            body_parts.append("\nPatterns Detected:")
            for pattern in context["patterns_detected"]:
                body_parts.append(f"  - {pattern['type']} (Priority: {pattern['priority']})")
                body_parts.append(f"    Context: {pattern['context']}")
                
        # Add relationship context if available
        if len(self.context_accumulator) > 1:
            body_parts.append("\nRecent Context:")
            for recent in self.context_accumulator[-3:]:
                if recent != context:
                    body_parts.append(f"  - {recent['type']} on {recent.get('file_name', 'unknown')}")
        
        episode_body = "\n".join(body_parts)
        
        # Generate a unique hash to prevent duplicates
        content_hash = hashlib.md5(episode_body.encode()).hexdigest()[:8]
        
        return {
            "name": f"{name} [{content_hash}]",
            "episode_body": episode_body,
            "source": "post_tool_use_v2",
            "source_description": f"Auto-captured from {context['tool']} operation with enhanced context",
            "group_id": self._determine_group_id(context),
            "valid_at": context["timestamp"]
        }
        
    def _determine_group_id(self, context: Dict[str, Any]) -> str:
        """Determine appropriate group ID based on context"""
        # Priority-based grouping
        if context.get("primary_pattern") == "ERROR_RESOLVED":
            return "error-fixes"
        elif context.get("primary_pattern") == "SECURITY_FIX":
            return "security"
        elif context.get("primary_pattern") == "BREAKING_CHANGE":
            return "breaking-changes"
        elif context.get("primary_pattern") == "PATTERN":
            return "patterns-conventions"
        elif context["type"] in ["pr_created", "pr_merged"]:
            return "pull-requests"
        elif context["type"] == "issue_created":
            return "issues"
        elif context.get("file_type") in [".test.js", ".spec.js", ".test.ts", ".spec.ts"]:
            return "testing"
        elif context.get("command_type") == "package_management":
            return "dependencies"
        else:
            return "development"
    
    def capture_memory_async(self, episode: Dict[str, Any]) -> str:
        """Queue memory for async capture and return tracking ID"""
        memory_id = self.memory_queue.add_memory(
            name=episode["name"],
            body=episode["episode_body"],
            source=episode["source"],
            group_id=episode.get("group_id")
        )
        
        self.logger.info(f"Queued memory for capture: {episode['name']} (ID: {memory_id})")
        return memory_id
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process post tool use events with enhanced async capture"""
        tool_name = hook_input.get('tool_name', '')
        tool_args = hook_input.get('tool_args', {})
        result = hook_input.get('result', {})
        
        try:
            # Check if we should capture this operation
            if not self.should_capture(tool_name, tool_args, result):
                return 0, None
                
            # Extract enhanced operation context
            context = self.extract_operation_context(tool_name, tool_args, result)
            
            # Check for duplicate operations (same content hash)
            operation_hash = hashlib.md5(
                f"{tool_name}{str(tool_args)}{str(result)}".encode()
            ).hexdigest()
            
            if operation_hash == self.last_operation_hash:
                self.logger.debug("Skipping duplicate operation")
                return 0, None
                
            self.last_operation_hash = operation_hash
            
            # Format as enhanced memory episode
            episode = self.format_memory_episode(context)
            
            # Queue for async capture
            memory_id = self.capture_memory_async(episode)
            
            # Get current queue stats
            stats = self.memory_queue.get_stats()
            
            # In verbose mode or when patterns detected, provide feedback
            if context.get("primary_pattern") or self.memory_settings.get("verbose", False):
                feedback = f"📝 Memory queued: {episode['name'][:50]}... (Queue: {stats['pending']} pending)"
                
                # Add pattern-specific feedback
                if context.get("primary_pattern") == "ERROR_RESOLVED":
                    feedback += "\n✅ Error fix captured for future reference"
                elif context.get("primary_pattern") == "BREAKING_CHANGE":
                    feedback += "\n⚠️ Breaking change documented for migration tracking"
                elif context.get("primary_pattern") == "PATTERN":
                    feedback += "\n🎯 Code pattern captured for consistency"
                    
                return 0, feedback
                
        except Exception as e:
            self.logger.error(f"PostToolUseMemoryV2 error: {e}", exc_info=True)
            
        return 0, None


# Main entry point
if __name__ == "__main__":
    hook = PostToolUseMemoryV2Hook()
    hook.run()