#!/usr/bin/env python3
"""
Slater Compliance Checker
Validates initialization patterns and DOMContentLoaded usage
"""

import sys
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime
import argparse

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(claude_path))

from logic.shared import MessageFormatter


@dataclass
class SlaterViolation:
    """Represents a Slater compliance violation"""
    file_path: Path
    line_number: int
    severity: str  # 'error', 'warning', 'info'
    violation_type: str  # 'dom_ready', 'jquery_ready', 'init_pattern', etc.
    message: str
    code_snippet: str
    suggested_fix: Optional[str] = None


@dataclass
class ComplianceResult:
    """Result of Slater compliance check"""
    total_files: int = 0
    files_checked: int = 0
    violations: List[SlaterViolation] = field(default_factory=list)
    compliant_files: List[Path] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    @property
    def error_count(self) -> int:
        return len([v for v in self.violations if v.severity == 'error'])
    
    @property
    def warning_count(self) -> int:
        return len([v for v in self.violations if v.severity == 'warning'])
    
    @property
    def is_compliant(self) -> bool:
        return self.error_count == 0


class SlaterComplianceChecker:
    """Checks JavaScript files for Slater framework compliance"""
    
    def __init__(self, project_root: Path = None):
        """Initialize Slater compliance checker"""
        self.project_root = project_root or Path.cwd()
        self.formatter = MessageFormatter()
        
        # Slater loader file (excluded from checks)
        self.slater_loader = self.project_root / "src/B__global/global.html"
        
        # Define violation patterns
        self.violation_patterns = {
            'dom_content_loaded': {
                'pattern': r'document\.addEventListener\s*\(\s*["\']DOMContentLoaded["\']\s*,',
                'message': 'DOMContentLoaded not needed - Slater autoloads scripts',
                'severity': 'error',
                'suggested_fix': 'Remove DOMContentLoaded wrapper and initialize directly'
            },
            'jquery_ready': {
                'pattern': r'\$\s*\(\s*document\s*\)\.ready|jQuery\s*\(\s*document\s*\)\.ready|\$\s*\(\s*function\s*\(\s*\)\s*{',
                'message': 'jQuery ready pattern not needed - Slater autoloads scripts',
                'severity': 'error',
                'suggested_fix': 'Remove jQuery ready wrapper and initialize directly'
            },
            'window_onload': {
                'pattern': r'window\.(onload|addEventListener\s*\(\s*["\']load["\']\s*,)',
                'message': 'Window onload not recommended - Slater handles initialization',
                'severity': 'warning',
                'suggested_fix': 'Use direct initialization or element checks if needed'
            },
            'global_function': {
                'pattern': r'^function\s+\w+\s*\(|^const\s+\w+\s*=\s*function|^let\s+\w+\s*=\s*function|^var\s+\w+\s*=\s*function',
                'message': 'Global functions should be wrapped in namespace or IIFE',
                'severity': 'warning',
                'suggested_fix': 'Use IIFE pattern: (() => { /* your code */ })()'
            }
        }
        
        # Define proper initialization patterns
        self.proper_patterns = {
            'iife': {
                'pattern': r'^\s*\(\s*\(\s*\)\s*=>\s*{|\(\s*function\s*\(\s*\)\s*{',
                'description': 'IIFE (Immediately Invoked Function Expression)'
            },
            'namespace': {
                'pattern': r'window\.\w+\s*=\s*window\.\w+\s*\|\|\s*{',
                'description': 'Namespace pattern for global access'
            },
            'direct_init': {
                'pattern': r'// Initialize immediately \(Slater auto-loads\)|// Slater autoloads',
                'description': 'Direct initialization with comment'
            }
        }
        
        # Elements that might need ready state checks
        self.ready_check_elements = {
            'form': 'Forms might need DOM ready check',
            'input': 'Input elements might need DOM ready check',
            'select': 'Select elements might need DOM ready check',
            'video': 'Video elements might need ready state check',
            'audio': 'Audio elements might need ready state check'
        }
    
    def check_file(self, file_path: Path) -> List[SlaterViolation]:
        """Check a single file for Slater compliance"""
        violations = []
        
        # Skip if it's the Slater loader itself
        if file_path.samefile(self.slater_loader):
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.splitlines()
            
            # Check for violation patterns
            for pattern_name, pattern_info in self.violation_patterns.items():
                pattern = pattern_info['pattern']
                
                for i, line in enumerate(lines):
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append(SlaterViolation(
                            file_path=file_path,
                            line_number=i + 1,
                            severity=pattern_info['severity'],
                            violation_type=pattern_name,
                            message=pattern_info['message'],
                            code_snippet=line.strip(),
                            suggested_fix=pattern_info.get('suggested_fix')
                        ))
            
            # Check initialization patterns
            has_proper_init = self._check_proper_initialization(content)
            uses_dom_elements = self._check_dom_element_usage(content)
            
            # Warn if using DOM elements without proper checks
            if uses_dom_elements and not has_proper_init:
                violations.append(SlaterViolation(
                    file_path=file_path,
                    line_number=0,
                    severity='warning',
                    violation_type='init_pattern',
                    message='File accesses DOM elements but lacks proper initialization pattern',
                    code_snippet='',
                    suggested_fix='Wrap code in IIFE or add element existence checks'
                ))
            
            # Check for console.log statements
            console_pattern = r'console\.(log|info|warn|error|debug)'
            for i, line in enumerate(lines):
                if re.search(console_pattern, line):
                    violations.append(SlaterViolation(
                        file_path=file_path,
                        line_number=i + 1,
                        severity='error',
                        violation_type='console_log',
                        message='Remove console statements in production code',
                        code_snippet=line.strip(),
                        suggested_fix='Remove or comment out console statement'
                    ))
            
        except Exception as e:
            violations.append(SlaterViolation(
                file_path=file_path,
                line_number=0,
                severity='error',
                violation_type='file_error',
                message=f"Error reading file: {e}",
                code_snippet=''
            ))
        
        return violations
    
    def _check_proper_initialization(self, content: str) -> bool:
        """Check if file uses proper initialization patterns"""
        for pattern_name, pattern_info in self.proper_patterns.items():
            if re.search(pattern_info['pattern'], content, re.MULTILINE):
                return True
        return False
    
    def _check_dom_element_usage(self, content: str) -> bool:
        """Check if file accesses DOM elements"""
        dom_patterns = [
            r'document\.(getElementById|querySelector|querySelectorAll)',
            r'document\.(getElementsByClassName|getElementsByTagName)',
            r'\$\s*\(["\'][\w\-#.]+["\']\)',  # jQuery selectors
            r'\.classList\.',
            r'\.addEventListener\s*\(',
            r'\.style\.',
            r'\.innerHTML',
            r'\.textContent'
        ]
        
        for pattern in dom_patterns:
            if re.search(pattern, content):
                return True
        return False
    
    def check_directory(self, directory: Path, pattern: str = "**/*.js") -> ComplianceResult:
        """Check all JavaScript files in a directory"""
        result = ComplianceResult()
        
        # Find all JS files
        js_files = list(directory.glob(pattern))
        result.total_files = len(js_files)
        
        for file_path in js_files:
            # Skip excluded paths
            if self._should_skip_file(file_path):
                continue
            
            violations = self.check_file(file_path)
            
            if violations:
                result.violations.extend(violations)
            else:
                result.compliant_files.append(file_path)
            
            result.files_checked += 1
        
        return result
    
    def _should_skip_file(self, file_path: Path) -> bool:
        """Check if file should be skipped"""
        skip_patterns = [
            'node_modules',
            'vendor',
            'dist',
            'build',
            '.min.',
            'test',
            'spec',
            'mock',
            'global.html'  # Skip Slater loader
        ]
        
        path_str = str(file_path)
        return any(pattern in path_str for pattern in skip_patterns)
    
    def generate_migration_guide(self, violations: List[SlaterViolation]) -> str:
        """Generate migration guide for fixing violations"""
        guide = []
        guide.append("# Slater Compliance Migration Guide\n")
        guide.append("## Overview")
        guide.append("Slater automatically loads scripts after DOM is ready.")
        guide.append("Remove unnecessary wrappers and initialize directly.\n")
        
        guide.append("## Common Patterns to Fix\n")
        
        # DOMContentLoaded
        guide.append("### 1. DOMContentLoaded Pattern")
        guide.append("```javascript")
        guide.append("// ❌ OLD PATTERN")
        guide.append("document.addEventListener('DOMContentLoaded', function() {")
        guide.append("  // your code")
        guide.append("});")
        guide.append("")
        guide.append("// ✅ NEW PATTERN")
        guide.append("(() => {")
        guide.append("  // your code - runs immediately")
        guide.append("})();")
        guide.append("```\n")
        
        # jQuery Ready
        guide.append("### 2. jQuery Ready Pattern")
        guide.append("```javascript")
        guide.append("// ❌ OLD PATTERN")
        guide.append("$(document).ready(function() {")
        guide.append("  // your code")
        guide.append("});")
        guide.append("")
        guide.append("// ✅ NEW PATTERN")
        guide.append("(() => {")
        guide.append("  // your code - runs immediately")
        guide.append("})();")
        guide.append("```\n")
        
        # Element checks
        guide.append("### 3. Element Existence Checks")
        guide.append("```javascript")
        guide.append("// ✅ SAFE PATTERN")
        guide.append("(() => {")
        guide.append("  const element = document.querySelector('.my-element');")
        guide.append("  if (!element) return;")
        guide.append("  ")
        guide.append("  // your code")
        guide.append("})();")
        guide.append("```\n")
        
        # Global namespace
        guide.append("### 4. Global Namespace Pattern")
        guide.append("```javascript")
        guide.append("// ✅ NAMESPACE PATTERN")
        guide.append("window.MyApp = window.MyApp || {};")
        guide.append("window.MyApp.myFunction = function() {")
        guide.append("  // your code")
        guide.append("};")
        guide.append("```\n")
        
        return '\n'.join(guide)
    
    def print_report(self, result: ComplianceResult):
        """Print compliance report"""
        print("\n" + self.formatter.header("Slater Compliance Check Report", emoji="check"))
        print(f"\nFiles checked: {result.files_checked}/{result.total_files}")
        print(f"Compliant files: {len(result.compliant_files)}")
        print(f"Violations found: {len(result.violations)}")
        print(f"  - Errors: {result.error_count}")
        print(f"  - Warnings: {result.warning_count}")
        
        if result.violations:
            print("\n" + self.formatter.header("Violations by Type", separator=self.formatter.SEPARATOR_DASHED))
            
            # Count by type
            by_type = {}
            for v in result.violations:
                if v.violation_type not in by_type:
                    by_type[v.violation_type] = 0
                by_type[v.violation_type] += 1
            
            for vtype, count in sorted(by_type.items(), key=lambda x: x[1], reverse=True):
                print(f"  - {vtype}: {count}")
            
            print("\n" + self.formatter.header("Detailed Violations", separator=self.formatter.SEPARATOR_DASHED))
            
            # Group by file
            by_file = {}
            for violation in result.violations:
                file_key = str(violation.file_path)
                if file_key not in by_file:
                    by_file[file_key] = []
                by_file[file_key].append(violation)
            
            for file_path, file_violations in by_file.items():
                try:
                    rel_path = Path(file_path).relative_to(self.project_root)
                except:
                    rel_path = Path(file_path)
                
                print(f"\n📁 {rel_path}")
                print("-" * 40)
                
                for v in sorted(file_violations, key=lambda x: x.line_number):
                    severity_emoji = {
                        'error': '🚨',
                        'warning': '⚠️',
                        'info': 'ℹ️'
                    }.get(v.severity, '')
                    
                    print(f"  Line {v.line_number}: {severity_emoji} [{v.severity.upper()}] {v.message}")
                    
                    if v.code_snippet:
                        print(f"    Code: {v.code_snippet}")
                    
                    if v.suggested_fix:
                        print(f"    Fix: {v.suggested_fix}")
        
        if result.compliant_files and len(result.violations) == 0:
            print("\n" + self.formatter.header("Compliant Files", separator=self.formatter.SEPARATOR_DASHED))
            for file_path in sorted(result.compliant_files)[:10]:
                try:
                    rel_path = file_path.relative_to(self.project_root)
                except:
                    rel_path = file_path
                print(f"  ✅ {rel_path}")
            
            if len(result.compliant_files) > 10:
                print(f"  ... and {len(result.compliant_files) - 10} more")
        
        print("\n" + self.formatter.footer())
        print("✅ All files are Slater compliant!" if result.is_compliant 
              else "❌ Slater compliance issues found")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Check JavaScript files for Slater compliance")
    parser.add_argument('path', nargs='?', default='src', 
                       help='Path to check (default: src)')
    parser.add_argument('--pattern', default='**/*.js', 
                       help='Glob pattern for JS files (default: **/*.js)')
    parser.add_argument('--guide', action='store_true',
                       help='Generate migration guide')
    parser.add_argument('--exclude', nargs='*', 
                       help='Additional paths to exclude')
    
    args = parser.parse_args()
    
    # Determine project root
    current_path = Path.cwd()
    if '.claude' in current_path.parts:
        # We're inside .claude, go up to project root
        project_root = current_path
        while project_root.name != '.claude' and project_root.parent != project_root:
            project_root = project_root.parent
        project_root = project_root.parent
    else:
        project_root = current_path
    
    # Create checker
    checker = SlaterComplianceChecker(project_root)
    
    # Note: Custom exclusions would need to be implemented in _should_skip_file method
    
    # Check path
    check_path = project_root / args.path
    if not check_path.exists():
        print(f"❌ Path not found: {check_path}")
        sys.exit(1)
    
    # Run compliance check
    if check_path.is_file() and check_path.suffix == '.js':
        violations = checker.check_file(check_path)
        result = ComplianceResult(
            total_files=1,
            files_checked=1,
            violations=violations,
            compliant_files=[] if violations else [check_path]
        )
    else:
        result = checker.check_directory(check_path, pattern=args.pattern)
    
    # Print report
    checker.print_report(result)
    
    # Generate migration guide if requested
    if args.guide and result.violations:
        guide_path = project_root / '.claude/logic/validation/slater-migration-guide.md'
        guide_content = checker.generate_migration_guide(result.violations)
        guide_path.write_text(guide_content, encoding='utf-8')
        print(f"\n📄 Migration guide saved to: {guide_path}")
    
    # Exit with appropriate code
    sys.exit(0 if result.is_compliant else 1)


if __name__ == "__main__":
    main()