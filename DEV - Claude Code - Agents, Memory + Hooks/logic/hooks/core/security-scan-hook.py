#!/usr/bin/env python3
"""
Security Scan Hook for Claude Code
Automatically detects and blocks operations with API keys, secrets, and sensitive data
Replaces manual /security command
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase, ToolHook, MessageFormatter, SettingsManager


class SecurityScanHook(ToolHook):
    """Automatically scans for security issues and blocks sensitive operations"""
    
    def __init__(self):
        super().__init__()
        
        # Settings
        self.settings_path = self.claude_path / "logic" / "security" / "security-settings.json"
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        
        # Security patterns
        self.security_patterns = {
            "api_keys": {
                "patterns": [
                    # Generic API key patterns
                    r'(?i)(?:api[_-]?key|apikey)\s*[:=]\s*["\']?[\w\-]{20,}["\']?',
                    r'(?i)(?:secret[_-]?key|secretkey)\s*[:=]\s*["\']?[\w\-]{20,}["\']?',
                    r'(?i)(?:access[_-]?key|accesskey)\s*[:=]\s*["\']?[\w\-]{20,}["\']?',
                    r'(?i)(?:private[_-]?key|privatekey)\s*[:=]\s*["\']?[\w\-]{20,}["\']?',
                    
                    # Service-specific patterns
                    r'sk-[A-Za-z0-9]{48}',  # OpenAI
                    r'AIza[A-Za-z0-9\-_]{35}',  # Google
                    r'ghp_[A-Za-z0-9]{36}',  # GitHub personal access token
                    r'gho_[A-Za-z0-9]{36}',  # GitHub OAuth token
                    r'github_pat_[A-Za-z0-9]{22}_[A-Za-z0-9]{59}',  # New GitHub PAT
                    r'AKIA[A-Z0-9]{16}',  # AWS Access Key
                    r'[0-9a-zA-Z/+]{40}',  # AWS Secret Key (when near AKIA)
                ],
                "severity": "critical",
                "message": "API key or secret detected"
            },
            "tokens": {
                "patterns": [
                    r'(?i)(?:auth[_-]?token|authtoken)\s*[:=]\s*["\']?[\w\-\.]{20,}["\']?',
                    r'(?i)(?:bearer[_-]?token|bearer)\s*[:=]\s*["\']?[\w\-\.]{20,}["\']?',
                    r'(?i)(?:oauth[_-]?token|oauth)\s*[:=]\s*["\']?[\w\-\.]{20,}["\']?',
                    r'(?i)jwt\s*[:=]\s*["\']?eyJ[\w\-\.]+["\']?',  # JWT tokens
                    r'Bearer\s+[\w\-\.]{20,}',  # Bearer tokens in headers
                ],
                "severity": "critical",
                "message": "Authentication token detected"
            },
            "passwords": {
                "patterns": [
                    r'(?i)password\s*[:=]\s*["\'][^"\']{8,}["\']',
                    r'(?i)passwd\s*[:=]\s*["\'][^"\']{8,}["\']',
                    r'(?i)pwd\s*[:=]\s*["\'][^"\']{8,}["\']',
                    r'(?i)pass\s*[:=]\s*["\'][^"\']{8,}["\']',
                ],
                "severity": "critical",
                "message": "Hardcoded password detected"
            },
            "connection_strings": {
                "patterns": [
                    r'(?i)(?:mongodb|postgres|mysql|redis|amqp|rabbitmq)://[^:]+:[^@]+@[^/\s]+',
                    r'(?i)data\s*source\s*=.*password\s*=',
                    r'(?i)server\s*=.*uid\s*=.*pwd\s*=',
                ],
                "severity": "critical",
                "message": "Database connection string with credentials detected"
            },
            "private_keys": {
                "patterns": [
                    r'-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----',
                    r'-----BEGIN ENCRYPTED PRIVATE KEY-----',
                    r'-----BEGIN PGP PRIVATE KEY BLOCK-----',
                ],
                "severity": "critical",
                "message": "Private key content detected"
            },
            "sensitive_files": {
                "patterns": [
                    r'\.env(?:\.local|\.production|\.development)?$',
                    r'\.pem$',
                    r'\.key$',
                    r'\.pfx$',
                    r'\.p12$',
                    r'id_rsa$',
                    r'id_dsa$',
                    r'id_ecdsa$',
                    r'\.ssh/config$',
                ],
                "severity": "high",
                "message": "Sensitive file type detected"
            }
        }
        
        # Whitelisted patterns (false positives)
        self.whitelist_patterns = [
            r'(?i)example[_-]?api[_-]?key',
            r'(?i)your[_-]?api[_-]?key[_-]?here',
            r'(?i)placeholder',
            r'(?i)xxx+',
            r'(?i)dummy',
            r'(?i)sample',
            r'(?i)test[_-]?key',
            r'\$\{[^}]+\}',  # Template variables
            r'%\([^)]+\)s',  # Python format strings
            r'\{\{[^}]+\}\}',  # Jinja/Handlebars templates
        ]
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings"""
        return {
            "enabled": True,
            "block_on_detection": True,
            "scan_file_writes": True,
            "scan_commits": True,
            "scan_api_calls": True,
            "show_suggestions": True,
            "allowed_in_env_files": True,
            "verbose_logging": False
        }
    
    def process_tool_use(self, tool_name: str, tool_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process tool use and scan for security issues"""
        if not self.settings.get("enabled"):
            return 0, None
        
        # Determine what to scan based on tool
        scan_results = []
        
        if tool_name in ["Edit", "MultiEdit", "Write", "NotebookEdit"]:
            if self.settings.get("scan_file_writes"):
                scan_results.extend(self._scan_file_operation(tool_name, tool_input))
        
        elif tool_name == "Bash":
            command = tool_input.get("command", "")
            if self.settings.get("scan_commits") and "git" in command:
                scan_results.extend(self._scan_git_operation(command))
            if self.settings.get("scan_api_calls") and any(cmd in command for cmd in ["curl", "wget", "http"]):
                scan_results.extend(self._scan_api_operation(command))
        
        # If no issues found, return success
        if not scan_results:
            return 0, None
        
        # Generate output
        return self._generate_security_output(scan_results)
    
    def _scan_file_operation(self, tool_name: str, tool_input: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Scan file operations for security issues"""
        results = []
        
        # Extract content to scan
        content_to_scan = ""
        file_path = ""
        
        if tool_name == "Edit":
            content_to_scan = tool_input.get("new_string", "")
            file_path = tool_input.get("file_path", "")
        elif tool_name == "MultiEdit":
            file_path = tool_input.get("file_path", "")
            for edit in tool_input.get("edits", []):
                content_to_scan += edit.get("new_string", "") + "\n"
        elif tool_name == "Write":
            content_to_scan = tool_input.get("content", "")
            file_path = tool_input.get("file_path", "")
        
        # Check if this is an allowed file type
        if self.settings.get("allowed_in_env_files") and ".env" in file_path.lower():
            return []  # Skip scanning .env files
        
        # Check for .claude directory writes
        if ".claude" in file_path and any(sensitive in content_to_scan.lower() 
                                         for sensitive in ["api", "key", "secret", "token", "password"]):
            results.append({
                "type": "claude_directory",
                "severity": "critical",
                "message": f"Attempting to write sensitive data to .claude directory",
                "file": file_path,
                "suggestion": "Never store API keys or secrets in .claude directory files"
            })
        
        # Scan content
        for category, config in self.security_patterns.items():
            if category == "sensitive_files":
                # Check file path instead of content
                for pattern in config["patterns"]:
                    if re.search(pattern, file_path):
                        results.append({
                            "type": category,
                            "severity": config["severity"],
                            "message": config["message"],
                            "file": file_path,
                            "pattern": pattern
                        })
            else:
                # Scan content for patterns
                for pattern in config["patterns"]:
                    matches = re.finditer(pattern, content_to_scan)
                    for match in matches:
                        # Check whitelist
                        if not self._is_whitelisted(match.group(0)):
                            results.append({
                                "type": category,
                                "severity": config["severity"],
                                "message": config["message"],
                                "file": file_path,
                                "match": match.group(0)[:50] + "..." if len(match.group(0)) > 50 else match.group(0),
                                "line": content_to_scan[:match.start()].count('\n') + 1
                            })
        
        return results
    
    def _scan_git_operation(self, command: str) -> List[Dict[str, Any]]:
        """Scan git operations"""
        results = []
        
        # Check for sensitive patterns in git commands
        if "commit" in command or "add" in command:
            for category, config in self.security_patterns.items():
                if category != "sensitive_files":
                    for pattern in config["patterns"]:
                        if re.search(pattern, command):
                            results.append({
                                "type": "git_operation",
                                "severity": "critical",
                                "message": f"Git operation contains {config['message']}",
                                "command": command[:100] + "..." if len(command) > 100 else command
                            })
        
        return results
    
    def _scan_api_operation(self, command: str) -> List[Dict[str, Any]]:
        """Scan API operations"""
        results = []
        
        # Check for exposed credentials in API calls
        for category, config in self.security_patterns.items():
            if category in ["api_keys", "tokens", "passwords"]:
                for pattern in config["patterns"]:
                    if re.search(pattern, command):
                        results.append({
                            "type": "api_operation",
                            "severity": "critical",
                            "message": f"API call contains {config['message']}",
                            "command": command[:100] + "..." if len(command) > 100 else command,
                            "suggestion": "Use environment variables or secure credential storage"
                        })
        
        return results
    
    def _is_whitelisted(self, match: str) -> bool:
        """Check if a match is whitelisted"""
        for whitelist_pattern in self.whitelist_patterns:
            if re.search(whitelist_pattern, match, re.IGNORECASE):
                return True
        return False
    
    def _generate_security_output(self, scan_results: List[Dict[str, Any]]) -> Tuple[int, Optional[str]]:
        """Generate security scan output"""
        # Separate by severity
        critical = [r for r in scan_results if r["severity"] == "critical"]
        high = [r for r in scan_results if r["severity"] == "high"]
        
        # Determine if we should block
        should_block = self.settings.get("block_on_detection") and critical
        
        # Build output
        output = MessageFormatter.header("Security Scan Alert", "security")
        
        if critical:
            items = []
            for result in critical[:5]:  # Limit to 5
                items.append(f"🚨 {result['message']}")
                if "file" in result:
                    items.append(f"   File: {result['file']}")
                if "line" in result:
                    items.append(f"   Line: {result['line']}")
                if "match" in result:
                    items.append(f"   Found: {result['match']}")
                if "suggestion" in result:
                    items.append(f"   → {result['suggestion']}")
                items.append("")
            
            output += MessageFormatter.section("CRITICAL SECURITY ISSUES", items, "error")
        
        if high and self.settings.get("show_suggestions"):
            items = []
            for result in high[:3]:
                items.append(f"⚠️ {result['message']}")
                if "file" in result:
                    items.append(f"   File: {result['file']}")
                items.append("")
            
            output += MessageFormatter.section("Security Warnings", items, "warning")
        
        # Add remediation steps
        remediation = [
            "🔐 **Required Actions**:",
            "1. Never commit API keys, tokens, or passwords",
            "2. Use environment variables (.env files)",
            "3. Add .env to .gitignore",
            "4. Use secure credential management",
            "",
            "📖 See CLAUDE.md: Security & API Key Protection"
        ]
        output += MessageFormatter.section("Remediation", remediation, "security")
        
        # Quick actions
        if should_block:
            actions = [
                "❌ **Operation Blocked** - Remove sensitive data before proceeding",
                "💡 To store secrets: Create .env file (gitignored)",
                "🔍 To review: `/security scan` for manual scan"
            ]
        else:
            actions = [
                "⚠️ Security issues detected but not blocking",
                "💡 Review and address security concerns",
                "⚙️ To enable blocking: `/logic hooks security block on`"
            ]
        
        output += MessageFormatter.section("Actions", actions, "info")
        output += MessageFormatter.footer()
        
        # Return exit code (2 = block, 0 = warn)
        return (2 if should_block else 0), output
    
    def scan_codebase(self) -> Dict[str, Any]:
        """Scan entire codebase for security issues (for manual /security command)"""
        results = {
            "total_files": 0,
            "files_with_issues": 0,
            "critical_issues": 0,
            "high_issues": 0,
            "issues_by_type": {}
        }
        
        # This would be called by the /security command replacement
        # Implementation would use ripgrep for fast scanning
        
        return results


if __name__ == "__main__":
    hook = SecurityScanHook()
    hook.run()