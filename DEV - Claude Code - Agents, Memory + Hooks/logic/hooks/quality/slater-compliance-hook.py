#!/usr/bin/env python3
"""
Slater Compliance Validation Hook

This hook validates that JavaScript code follows Slater-specific patterns:
1. No DOMContentLoaded usage (Slater provides its own initialization)
2. No jQuery $(document).ready() patterns
3. No other DOM ready patterns that conflict with Slater's lifecycle
4. Exception: /src/B__global/global.html is allowed to use these patterns

Slater provides its own initialization lifecycle that ensures scripts run at the
appropriate time, making traditional DOM ready patterns unnecessary and potentially
problematic.
"""

import sys
import re
from pathlib import Path
from typing import Dict, Any, Optional, Tuple, List
import json
import subprocess
from datetime import datetime

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[2]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase, ToolHook, MessageFormatter


class SlaterComplianceHook(ToolHook):
    """Validates JavaScript code for Slater compliance"""
    
    def __init__(self):
        super().__init__()
        self.name = "Slater Compliance Validation"
        self.priority = 85  # High priority but after code reuse
        
        # File paths that are exempt from Slater compliance
        self.exempt_paths = [
            'src/B__global/global.html',
            '/src/B__global/global.html'
        ]
        
        # Patterns to detect DOM ready implementations
        self.dom_ready_patterns = {
            'DOMContentLoaded': {
                'pattern': r'addEventListener\s*\(\s*[\'"]DOMContentLoaded[\'"]',
                'message': 'DOMContentLoaded listener detected',
                'suggestion': 'Remove DOMContentLoaded - Slater handles initialization timing'
            },
            'jQuery ready': {
                'pattern': r'\$\s*\(\s*document\s*\)\s*\.ready\s*\(',
                'message': 'jQuery $(document).ready() detected',
                'suggestion': 'Remove jQuery ready - Slater handles initialization timing'
            },
            'jQuery shorthand': {
                'pattern': r'\$\s*\(\s*function\s*\(\s*\)\s*{',
                'message': 'jQuery ready shorthand $() detected',
                'suggestion': 'Remove jQuery ready shorthand - Slater handles initialization timing'
            },
            'window load': {
                'pattern': r'window\s*\.\s*addEventListener\s*\(\s*[\'"]load[\'"]',
                'message': 'window.addEventListener("load") detected',
                'suggestion': 'Consider if window.load is necessary - Slater usually handles this'
            },
            'onload attribute': {
                'pattern': r'window\s*\.\s*onload\s*=',
                'message': 'window.onload assignment detected',
                'suggestion': 'Remove window.onload - use Slater\'s initialization'
            },
            'document ready state': {
                'pattern': r'document\s*\.\s*readyState\s*===?\s*[\'"]complete[\'"]',
                'message': 'document.readyState check detected',
                'suggestion': 'Remove readyState check - Slater ensures proper timing'
            }
        }
        
        # Track violations for memory capture
        self.violations_found = []
    
    def _is_exempt_file(self, file_path: str) -> bool:
        """Check if file is exempt from Slater compliance"""
        # Normalize path
        normalized_path = str(Path(file_path)).replace('\\', '/')
        
        # Check against exempt paths
        for exempt_path in self.exempt_paths:
            if normalized_path.endswith(exempt_path):
                return True
        
        return False
    
    def _check_content_violations(self, content: str, file_path: str) -> List[Dict[str, Any]]:
        """Check content for Slater compliance violations"""
        violations = []
        
        # Skip if file is exempt
        if self._is_exempt_file(file_path):
            return violations
        
        # Only check JavaScript files and HTML files (for inline scripts)
        file_ext = Path(file_path).suffix.lower()
        if file_ext not in ['.js', '.jsx', '.ts', '.tsx', '.html', '.htm']:
            return violations
        
        # For HTML files, extract script content
        if file_ext in ['.html', '.htm']:
            # Find all script tags
            script_pattern = r'<script[^>]*>(.*?)</script>'
            script_matches = re.finditer(script_pattern, content, re.DOTALL | re.IGNORECASE)
            
            for match in script_matches:
                script_content = match.group(1)
                line_offset = content[:match.start()].count('\n')
                
                # Check script content for violations
                for pattern_name, pattern_info in self.dom_ready_patterns.items():
                    if re.search(pattern_info['pattern'], script_content, re.IGNORECASE):
                        # Find the specific line within the script
                        script_lines = script_content.split('\n')
                        for i, line in enumerate(script_lines):
                            if re.search(pattern_info['pattern'], line, re.IGNORECASE):
                                violations.append({
                                    'type': pattern_name,
                                    'file': file_path,
                                    'line': line_offset + i + 1,
                                    'message': pattern_info['message'],
                                    'suggestion': pattern_info['suggestion'],
                                    'severity': 'warning',
                                    'context': 'inline script'
                                })
        else:
            # For JS files, check the entire content
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                for pattern_name, pattern_info in self.dom_ready_patterns.items():
                    if re.search(pattern_info['pattern'], line, re.IGNORECASE):
                        violations.append({
                            'type': pattern_name,
                            'file': file_path,
                            'line': i,
                            'message': pattern_info['message'],
                            'suggestion': pattern_info['suggestion'],
                            'severity': 'warning'
                        })
        
        return violations
    
    def _capture_violation_to_memory(self, violation: Dict[str, Any]):
        """Capture Slater violation pattern to memory"""
        # Create memory entry for the violation
        memory_entry = {
            'name': f'SLATER_VIOLATION: {violation["type"]} in {Path(violation["file"]).name}',
            'episode_body': (
                f'Found Slater compliance violation:\n'
                f'Type: {violation["type"]}\n'
                f'File: {violation["file"]} (line {violation["line"]})\n'
                f'Issue: {violation["message"]}\n'
                f'Fix: {violation["suggestion"]}\n'
                f'Context: Slater provides its own initialization lifecycle, '
                f'making DOM ready patterns unnecessary.'
            ),
            'source': 'slater_compliance',
            'group_id': 'code_quality',
            'valid_at': datetime.now().isoformat()
        }
        
        # Add to violations for batch capture
        self.violations_found.append(memory_entry)
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook input for Slater compliance"""
        # Only process tool usage events
        if "toolName" not in hook_input:
            return 0, None
        
        tool_name = hook_input.get("toolName", "")
        tool_input = hook_input.get("toolInput", {})
        
        # Only check file modification tools
        if tool_name not in ["Edit", "MultiEdit", "Write", "NotebookEdit"]:
            return 0, None
        
        violations = []
        files_checked = []
        
        # Process based on tool type
        if tool_name == "Write":
            file_path = tool_input.get("file_path", "")
            content = tool_input.get("content", "")
            
            if file_path and content:
                file_violations = self._check_content_violations(content, file_path)
                violations.extend(file_violations)
                files_checked.append(file_path)
                
        elif tool_name == "Edit":
            file_path = tool_input.get("file_path", "")
            new_string = tool_input.get("new_string", "")
            
            if file_path and new_string:
                file_violations = self._check_content_violations(new_string, file_path)
                violations.extend(file_violations)
                files_checked.append(file_path)
                
        elif tool_name == "MultiEdit":
            file_path = tool_input.get("file_path", "")
            edits = tool_input.get("edits", [])
            
            if file_path and edits:
                # Check each edit
                for edit in edits:
                    new_string = edit.get("new_string", "")
                    if new_string:
                        file_violations = self._check_content_violations(new_string, file_path)
                        violations.extend(file_violations)
                files_checked.append(file_path)
        
        # If no violations, return success
        if not violations:
            return 0, None
        
        # Capture violations to memory
        for violation in violations:
            self._capture_violation_to_memory(violation)
        
        # Generate output message
        output = self._generate_output(violations, files_checked)
        
        # Don't block, just warn
        return 0, output
    
    def _generate_output(self, violations: List[Dict[str, Any]], files: List[str]) -> str:
        """Generate formatted output for violations"""
        output_parts = []
        
        # Header
        output_parts.append(MessageFormatter.header("Slater Compliance Check", "slater"))
        
        # Group violations by file
        violations_by_file = {}
        for violation in violations:
            file_path = violation['file']
            if file_path not in violations_by_file:
                violations_by_file[file_path] = []
            violations_by_file[file_path].append(violation)
        
        # Display violations
        items = []
        for file_path, file_violations in violations_by_file.items():
            items.append(f"\n📄 **{file_path}**")
            
            for v in file_violations:
                items.append(f"  Line {v['line']}: {v['message']}")
                items.append(f"  → {v['suggestion']}")
                if v.get('context'):
                    items.append(f"  Context: {v['context']}")
        
        output_parts.append(MessageFormatter.section(
            "DOM Ready Pattern Violations", 
            items, 
            "warning"
        ))
        
        # Add explanation
        explanation = [
            "Slater provides its own script initialization lifecycle.",
            "Using DOMContentLoaded or jQuery ready can cause timing issues.",
            "Your code will run at the appropriate time without these patterns.",
            "",
            "**Exception**: /src/B__global/global.html can use these patterns."
        ]
        
        output_parts.append(MessageFormatter.section(
            "Why This Matters", 
            explanation, 
            "info"
        ))
        
        # Memory capture notice
        if self.violations_found:
            output_parts.append(MessageFormatter.section(
                "Memory Capture",
                [f"Captured {len(self.violations_found)} violation patterns for future reference"],
                "memory"
            ))
        
        output_parts.append(MessageFormatter.footer())
        
        return "\n".join(output_parts)
    
    def get_status(self) -> Dict[str, Any]:
        """Get hook status information"""
        return {
            'active': True,
            'name': self.name,
            'priority': self.priority,
            'exempt_paths': self.exempt_paths,
            'patterns_checked': list(self.dom_ready_patterns.keys()),
            'violations_captured': len(self.violations_found)
        }


def main():
    """CLI entry point for testing"""
    hook = SlaterComplianceHook()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'status':
            print(json.dumps(hook.get_status(), indent=2))
        elif sys.argv[1] == 'test':
            # Test with sample violations
            test_cases = [
                {
                    'name': 'DOMContentLoaded violation',
                    'tool': 'Write',
                    'file': 'src/components/test.js',
                    'content': '''
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page loaded');
});
'''
                },
                {
                    'name': 'jQuery ready violation',
                    'tool': 'Write',
                    'file': 'src/modules/slider.js',
                    'content': '''
$(document).ready(function() {
    initializeSlider();
});
'''
                },
                {
                    'name': 'Exempt file (should pass)',
                    'tool': 'Write',
                    'file': 'src/B__global/global.html',
                    'content': '''
<script>
document.addEventListener('DOMContentLoaded', function() {
    // This is allowed in global.html
});
</script>
'''
                }
            ]
            
            for test in test_cases:
                print(f"\n=== Testing: {test['name']} ===")
                
                hook_input = {
                    'toolName': test['tool'],
                    'toolInput': {
                        'file_path': test['file'],
                        'content': test['content']
                    }
                }
                
                exit_code, output = hook.process(hook_input)
                print(f"Exit code: {exit_code}")
                if output:
                    print(output)
                else:
                    print("✅ No violations found")
    else:
        # Run as hook
        hook.run()


if __name__ == '__main__':
    main()