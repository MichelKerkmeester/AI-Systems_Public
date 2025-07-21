#!/usr/bin/env python3
"""
Unified Quality Hook for Claude Code
Combines: reminder, enforcement, and actually-works functionality
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import (
    HookBase, ToolHook, UserPromptHook,
    SettingsManager, StateManager,
    MessageFormatter, TestTracker
)


class QualityHook(HookBase):
    """Unified quality hook handling reminders, enforcement, and testing"""
    
    def __init__(self):
        super().__init__()
        
        # Settings and state paths
        self.settings_path = self.claude_path / "logic" / "quality" / "quality-settings.json"
        self.state_path = self.claude_path / "state"
        
        # Initialize managers
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        self.test_tracker = TestTracker(self.state_path)
        
        # Load CLAUDE.md content
        self.claude_md_path = self.project_root / "CLAUDE.md"
        
        # Initialize patterns
        self._init_reminder_triggers()
        self._init_violation_patterns()
        self._init_test_suggestions()
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings"""
        return {
            "enforcement_level": "balanced",  # strict, balanced, minimal, off
            "auto_test_reminder": True,
            "auto_test_execution": True,  # Auto-run tests when threshold exceeded
            "show_suggestions": True,
            "show_reminders": True,
            "reminder_threshold": {
                "lines_changed": 20,
                "files_changed": 3,
                "critical_files": ["auth", "api", "payment", "security"]
            },
            "auto_test_threshold": {
                "files_changed": 5,  # Auto-run tests after 5 files
                "critical_violations": 3,  # Auto-run on 3+ critical issues
                "security_files": 1  # Auto-run on any security file change
            }
        }
    
    def _init_reminder_triggers(self):
        """Initialize keyword-based reminder triggers"""
        self.reminder_triggers = {
            "test": {
                "keywords": ["test", "testing", "verify", "check", "validate"],
                "section": "Actually Works Protocol",
                "reminder": [
                    "ALWAYS test code before claiming completion",
                    "Run appropriate /test commands",
                    "Verify functionality, don't assume",
                    "Testing is not optional - it's professional"
                ]
            },
            "security": {
                "keywords": ["api", "key", "secret", "token", "password", "auth"],
                "section": "Security & API Key Protection",
                "reminder": [
                    "NEVER store API keys in code or documentation",
                    "Use .env files for secrets (gitignored)",
                    "Reference keys by name only",
                    "Redact all sensitive data in outputs"
                ]
            },
            "css": {
                "keywords": ["css", "style", "styling", "design", "layout"],
                "section": "Technical Constraints - CSS",
                "reminder": [
                    "Use REM units, not pixels (16px = 1rem)",
                    "Use data attributes for components: [data-component=\"\"]",
                    "Keep CSS files under 20KB",
                    "Follow existing Webflow structure"
                ]
            },
            "javascript": {
                "keywords": ["javascript", "js", "script", "function", "code"],
                "section": "Technical Constraints - JavaScript",
                "reminder": [
                    "No console.log in production (use DEBUG wrapper)",
                    "Always check element existence before DOM manipulation",
                    "Use module pattern to avoid global scope pollution",
                    "Keep JS files under 50KB, max 500 lines per file"
                ]
            },
            "commit": {
                "keywords": ["commit", "git", "push", "merge"],
                "section": "Git & Commits",
                "reminder": [
                    "NEVER commit unless explicitly asked",
                    "Run tests before committing",
                    "Describe WHY not WHAT in commit messages",
                    "Check for sensitive data before committing"
                ]
            },
            "general": {
                "keywords": ["help", "start", "begin", "create", "build", "implement"],
                "section": "Core Philosophy",
                "reminder": [
                    "Fix root causes, not symptoms",
                    "Take full ownership of solutions",
                    "Deliver production-grade code",
                    "Work with existing Webflow structure",
                    "Apply DRY & KISS principles",
                    "Don't be helpful, be better"
                ]
            }
        }
    
    def _init_violation_patterns(self):
        """Initialize code violation patterns"""
        self.violation_patterns = {
            "console_log": {
                "pattern": r'\bconsole\.(log|error|warn|info)\s*\(',
                "message": "Found console.{method} in production code",
                "suggestion": "Use debug wrapper: if (DEBUG) console.{method}(...)",
                "severity": "warning",
                "section": "Technical Constraints"
            },
            "px_units": {
                "pattern": r':\s*\d+px(?:\s|;|$)',
                "message": "CSS uses px units",
                "suggestion": "Convert to REM: 16px = 1rem",
                "severity": "warning",
                "section": "Technical Constraints"
            },
            "api_keys": {
                "pattern": r'(?:api[_-]?key|secret|token|password)\s*[:=]\s*["\'][\w\-]{20,}["\']',
                "message": "Potential API key or secret detected",
                "suggestion": "Use environment variables (.env file)",
                "severity": "critical",
                "section": "Security & API Key Protection"
            },
            "global_pollution": {
                "pattern": r'^(?!(?:const|let|var|function|class)\s+)\w+\s*=\s*[^=]',
                "message": "Potential global scope pollution",
                "suggestion": "Use module pattern or namespace",
                "severity": "warning",
                "section": "Technical Constraints"
            },
            "missing_null_check": {
                "pattern": r'document\.(querySelector|getElementById|getElementsBy\w+)\([^)]+\)\.',
                "message": "Direct DOM access without null check",
                "suggestion": "Add existence check: const el = document.querySelector(...); if (el) { ... }",
                "severity": "warning",
                "section": "Technical Constraints"
            }
        }
    
    def _init_test_suggestions(self):
        """Initialize test command suggestions"""
        self.test_suggestions = {
            ".js": "/test quick",
            ".css": "/test quick",
            ".html": "/test full",
            "api": "/test security",
            "auth": "/test security",
            "payment": "/test security"
        }
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook based on event type"""
        # Detect event type from hook input structure
        if "userMessage" in hook_input:
            return self._handle_user_prompt(hook_input)
        elif "toolName" in hook_input:
            return self._handle_tool_use(hook_input)
        else:
            return 0, None
    
    def _handle_user_prompt(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Handle UserPromptSubmit event - show contextual reminders"""
        if not self.settings.get("show_reminders"):
            return 0, None
        
        prompt = hook_input.get("userMessage", "").lower()
        
        # Find triggered sections
        triggered = []
        for section, config in self.reminder_triggers.items():
            if any(keyword in prompt for keyword in config["keywords"]):
                triggered.append(section)
        
        # Default to general if no specific triggers
        if not triggered:
            triggered.append("general")
        
        # Build reminder message
        output = MessageFormatter.header("CLAUDE.md Context Reminders", "quality")
        
        for section in triggered:
            if section in self.reminder_triggers:
                config = self.reminder_triggers[section]
                output += MessageFormatter.section(
                    f"{config['section']}",
                    config["reminder"],
                    self._get_section_emoji(section)
                )
        
        # Add quick reference
        output += MessageFormatter.section(
            "Quick Reference",
            [
                "Commands: /workflow, /test, /memory, /mode, /pr, /security",
                "Status indicators: ⏳ Progress | ✅ Complete | ❌ Failed | ⚠️ Warning",
                "Task files: .claude/project-management/",
                "Knowledge: facts.json, patterns.json, constraints.json"
            ],
            "info"
        )
        
        output += "\n" + MessageFormatter.footer()
        
        return 0, output
    
    def _handle_tool_use(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Handle PostToolUse event - check violations and test reminders"""
        tool_name = hook_input.get("toolName", "")
        tool_input = hook_input.get("toolInput", {})
        
        # Track test commands
        if tool_name == "Bash":
            command = tool_input.get("command", "").lower()
            if any(test_cmd in command for test_cmd in ["npm test", "pytest", "/test", "npm run test"]):
                self.test_tracker.mark_test_run()
                return 0, None
        
        # Only process file modification tools
        if tool_name not in ["Edit", "MultiEdit", "Write", "NotebookEdit"]:
            return 0, None
        
        # Process file changes
        violations = []
        files_processed = []
        lines_changed = 0
        
        if tool_name == "Edit":
            file_path = tool_input.get("file_path", "")
            new_content = tool_input.get("new_string", "")
            if file_path and new_content:
                violations.extend(self._check_content(file_path, new_content))
                files_processed.append(file_path)
                lines_changed += len(new_content.split('\n'))
        
        elif tool_name == "MultiEdit":
            file_path = tool_input.get("file_path", "")
            edits = tool_input.get("edits", [])
            if file_path and edits:
                for edit in edits:
                    new_content = edit.get("new_string", "")
                    if new_content:
                        violations.extend(self._check_content(file_path, new_content))
                        lines_changed += len(new_content.split('\n'))
                files_processed.append(file_path)
        
        elif tool_name == "Write":
            file_path = tool_input.get("file_path", "")
            content = tool_input.get("content", "")
            if file_path and content:
                violations.extend(self._check_content(file_path, content))
                files_processed.append(file_path)
                lines_changed += len(content.split('\n'))
        
        # Update test tracker
        if files_processed:
            self.test_tracker.increment_changes(
                files=len(set(files_processed)),
                lines=lines_changed
            )
        
        # Generate output
        return self._generate_enforcement_output(violations, files_processed)
    
    def _check_content(self, file_path: str, content: str) -> List[Dict[str, Any]]:
        """Check content for violations"""
        if self.settings.get("enforcement_level") == "off":
            return []
        
        violations = []
        ext = Path(file_path).suffix.lower()
        is_js = ext in ['.js', '.jsx', '.ts', '.tsx']
        is_css = ext in ['.css', '.scss', '.sass']
        
        # Check each pattern
        for name, pattern_info in self.violation_patterns.items():
            # Skip irrelevant patterns
            if name == "px_units" and not is_css:
                continue
            if name in ["console_log", "global_pollution", "missing_null_check"] and not is_js:
                continue
            
            # Search for violations
            for i, line in enumerate(content.split('\n'), 1):
                if re.search(pattern_info["pattern"], line, re.IGNORECASE):
                    violations.append({
                        "type": name,
                        "line": i,
                        "file": file_path,
                        **pattern_info
                    })
        
        # Check file size
        line_count = len(content.split('\n'))
        if line_count > 500:
            violations.append({
                "type": "large_file",
                "file": file_path,
                "message": f"File has {line_count} lines (exceeds 500 line limit)",
                "suggestion": "Consider splitting into modules",
                "severity": "warning",
                "section": "Technical Constraints"
            })
        
        return violations
    
    def _generate_enforcement_output(self, violations: List[Dict], 
                                   files: List[str]) -> Tuple[int, Optional[str]]:
        """Generate enforcement output message"""
        # Check if we should show anything
        show_test = (self.settings.get("auto_test_reminder") and 
                    files and 
                    self.test_tracker.should_remind_test())
        
        show_violations = (self.settings.get("show_suggestions") and violations)
        
        # Check if we should auto-run tests
        should_auto_test = self._should_auto_run_tests(violations, files)
        
        if not show_test and not show_violations and not should_auto_test:
            return 0, None
        
        # Build output
        output_parts = []
        
        # Header
        output_parts.append(MessageFormatter.header("CLAUDE.md Compliance Check", "quality"))
        
        # Critical violations (blocking)
        critical = [v for v in violations if v["severity"] == "critical"]
        if critical:
            items = []
            for v in critical:
                items.append(f"{v['message']} (line {v.get('line', 'N/A')})")
                items.append(f"→ {v['suggestion']}")
                items.append(f"📖 See CLAUDE.md: {v['section']}")
            output_parts.append(MessageFormatter.section("CRITICAL ISSUES", items, "error"))
        
        # Warnings (non-blocking)
        warnings = [v for v in violations if v["severity"] == "warning"]
        if warnings and self.settings.get("show_suggestions"):
            items = []
            for v in warnings[:5]:  # Limit to 5
                items.append(f"{v['message']} (line {v.get('line', 'N/A')})")
                items.append(f"→ {v['suggestion']}")
            
            if len(warnings) > 5:
                items.append(f"... and {len(warnings) - 5} more warnings")
            
            output_parts.append(MessageFormatter.section("Code Quality Reminders", items, "warning"))
        
        # Auto-test execution notice
        if should_auto_test:
            test_cmd = self._get_test_suggestion(files[0] if files else "")
            items = [
                "🚀 **Auto-Running Tests** (threshold exceeded)",
                f"Executing: `{test_cmd}`",
                "Monitoring with subprocess for real-time results..."
            ]
            output_parts.append(MessageFormatter.section("Automated Testing", items, "test"))
            
            # Mark test as run
            self.test_tracker.mark_test_run()
            
        # Test reminder (if not auto-running)
        elif show_test:
            test_cmd = self._get_test_suggestion(files[0] if files else "")
            items = [
                f"Run `{test_cmd}` to validate changes",
                "Verify functionality before claiming completion",
                "📖 Testing is not optional - it's professional"
            ]
            
            # Add file-specific checks
            if files:
                file_checks = self._get_file_specific_checks(files[0])
                if file_checks:
                    items.extend(file_checks)
            
            output_parts.append(MessageFormatter.section("Actually Works Protocol", items, "test"))
        
        # Success message if clean
        if not violations and not show_test and not should_auto_test:
            output_parts.append(f"\n{MessageFormatter.EMOJIS['success']} Following CLAUDE.md best practices")
        
        # Stats
        tracker_summary = self.test_tracker.state
        if tracker_summary["files_since_test"] > 5 or tracker_summary["lines_since_test"] > 100:
            stats = f"Session Impact: {tracker_summary['files_since_test']} files, {tracker_summary['lines_since_test']} lines changed since last test"
            output_parts.append(MessageFormatter.section("Statistics", [stats], "stats"))
        
        output_parts.append(MessageFormatter.footer())
        
        # Determine exit code (block on critical violations)
        exit_code = 2 if critical else 0
        
        return exit_code, "\n".join(output_parts)
    
    def _should_auto_run_tests(self, violations: List[Dict], files: List[str]) -> bool:
        """Check if we should automatically run tests based on thresholds"""
        if not self.settings.get("auto_test_execution"):
            return False
        
        thresholds = self.settings.get("auto_test_threshold", {})
        tracker_state = self.test_tracker.state
        
        # Check file count threshold
        if tracker_state["files_since_test"] >= thresholds.get("files_changed", 5):
            return True
        
        # Check critical violations threshold
        critical_count = len([v for v in violations if v["severity"] == "critical"])
        if critical_count >= thresholds.get("critical_violations", 3):
            return True
        
        # Check security file changes
        if files and thresholds.get("security_files", 1) > 0:
            critical_files = self.settings.settings["reminder_threshold"]["critical_files"]
            for file_path in files:
                if any(critical in file_path.lower() for critical in critical_files):
                    return True
        
        return False
    
    def _get_test_suggestion(self, file_path: str) -> str:
        """Get appropriate test command suggestion"""
        if not file_path:
            return "/test quick"
        
        file_lower = file_path.lower()
        
        # Check for critical files
        for critical in self.settings.settings["reminder_threshold"]["critical_files"]:
            if critical in file_lower:
                return "/test security"
        
        # Check by extension
        ext = Path(file_path).suffix
        if ext in self.test_suggestions:
            return self.test_suggestions[ext]
        
        return "/test quick"
    
    def _get_file_specific_checks(self, file_path: str) -> List[str]:
        """Get file-specific testing checks"""
        if not file_path:
            return []
        
        ext = Path(file_path).suffix.lower()
        file_name = Path(file_path).name.lower()
        checks = []
        
        if ext in ['.js', '.ts', '.jsx', '.tsx']:
            checks.extend([
                "Check browser console for errors",
                "Verify all event handlers work",
                "Test with different data inputs"
            ])
        elif ext in ['.css', '.scss', '.sass']:
            checks.extend([
                "View in all major browsers",
                "Check mobile responsiveness",
                "Test hover/active states"
            ])
        elif 'api' in file_name or 'auth' in file_name:
            checks.extend([
                "Run security tests immediately",
                "Verify no exposed secrets",
                "Test authentication flows"
            ])
        
        return checks
    
    def _get_section_emoji(self, section: str) -> str:
        """Get emoji for section"""
        emoji_map = {
            "test": "test",
            "security": "security",
            "css": "css",
            "javascript": "code",
            "commit": "commit",
            "general": "info"
        }
        return emoji_map.get(section, "info")


if __name__ == "__main__":
    hook = QualityHook()
    hook.run()