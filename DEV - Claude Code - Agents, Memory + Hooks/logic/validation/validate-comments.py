#!/usr/bin/env python3
"""
Comment Pattern Validator
Checks JS and CSS files for comment pattern compliance
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
class CommentViolation:
    """Represents a comment pattern violation"""
    file_path: Path
    line_number: int
    severity: str  # 'error', 'warning', 'info'
    message: str
    original_line: str
    suggested_fix: Optional[str] = None
    pattern_type: str = ""  # 'header', 'section', 'inline', etc.


@dataclass
class ValidationResult:
    """Result of comment validation"""
    total_files: int = 0
    files_checked: int = 0
    violations: List[CommentViolation] = field(default_factory=list)
    fixed_count: int = 0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    @property
    def error_count(self) -> int:
        return len([v for v in self.violations if v.severity == 'error'])
    
    @property
    def warning_count(self) -> int:
        return len([v for v in self.violations if v.severity == 'warning'])
    
    @property
    def is_valid(self) -> bool:
        return self.error_count == 0


class CommentValidator:
    """Validates comment patterns in JS and CSS files"""
    
    def __init__(self, project_root: Path = None):
        """Initialize comment validator"""
        self.project_root = project_root or Path.cwd()
        self.formatter = MessageFormatter()
        
        # Define comment patterns for JS
        self.js_patterns = {
            'file_header': {
                'pattern': r'^// ─+\n// (.+)\n// (.+)?\n// ─+',
                'example': '// ───────────────────────────────────────────────────────────────\n// Component Name\n// Brief description\n// ───────────────────────────────────────────────────────────────',
                'severity': 'warning'
            },
            'section_header': {
                'pattern': r'^\s*/\* ─+\n\s+(.+)\n\s+─+\*/|^\s*/\* (.+) \*/',
                'example': '/* ─────────────────────────────────────────────────────────────\n   Section Name\n  ───────────────────────────────────────────────────────────── */',
                'severity': 'info'
            },
            'inline_comment': {
                'pattern': r'^\s*// (.+)$',
                'valid_starts': ['TODO:', 'NOTE:', 'FIXME:', 'WARNING:', 'DEPRECATED:', '#'],
                'severity': 'info'
            },
            'multi_line': {
                'pattern': r'/\*\*[\s\S]*?\*/',
                'severity': 'info'
            }
        }
        
        # Define comment patterns for CSS
        self.css_patterns = {
            'file_header': {
                'pattern': r'^/\* ─+\n\s+(.+)\n\s+─+ \*/',
                'example': '/* ───────────────────────────────────────────────────────────────\n   Component: Name\n   ─────────────────────────────────────────────────────────────── */',
                'severity': 'warning'
            },
            'section_header': {
                'pattern': r'^/\* (.+) \*/$',
                'valid_formats': [r'^[A-Z\s]+$', r'^[A-Z][a-z\s]+$'],  # ALL CAPS or Title Case
                'example': '/* SECTION NAME */ or /* Section Name */',
                'severity': 'info'
            },
            'inline_comment': {
                'pattern': r'/\*\s*(.+?)\s*\*/',
                'severity': 'info'
            }
        }
        
        # Forbidden patterns
        self.forbidden_patterns = {
            'console_log': {
                'pattern': r'console\.(log|info|warn|error|debug)',
                'message': 'Remove console statements in production code',
                'severity': 'error',
                'file_types': ['.js']
            },
            'pixel_units': {
                'pattern': r':\s*\d+px',
                'message': 'Use REM units instead of pixels (1rem = 16px)',
                'severity': 'error',
                'file_types': ['.css'],
                'exceptions': ['border', 'outline', 'box-shadow', '0px']
            },
            'global_variables': {
                'pattern': r'^\s*(var|let|const)\s+\w+\s*=(?!.*\bnamespace\b)',
                'message': 'Use namespace pattern for global variables',
                'severity': 'error',
                'file_types': ['.js'],
                'scope': 'global'  # Only check at file root level
            }
        }
    
    def validate_file(self, file_path: Path, auto_fix: bool = False) -> List[CommentViolation]:
        """Validate a single file"""
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.splitlines(keepends=True)
            
            # Determine file type
            if file_path.suffix == '.js':
                violations.extend(self._validate_js_comments(file_path, lines))
            elif file_path.suffix == '.css':
                violations.extend(self._validate_css_comments(file_path, lines))
            
            # Check forbidden patterns
            violations.extend(self._check_forbidden_patterns(file_path, lines))
            
            # Auto-fix if requested
            if auto_fix and violations:
                fixed_lines = self._auto_fix_comments(file_path, lines, violations)
                if fixed_lines != lines:
                    file_path.write_text(''.join(fixed_lines), encoding='utf-8')
                    return self.validate_file(file_path, auto_fix=False)  # Re-validate
            
        except Exception as e:
            violations.append(CommentViolation(
                file_path=file_path,
                line_number=0,
                severity='error',
                message=f"Error reading file: {e}",
                original_line="",
                pattern_type='file_error'
            ))
        
        return violations
    
    def _validate_js_comments(self, file_path: Path, lines: List[str]) -> List[CommentViolation]:
        """Validate JavaScript comment patterns"""
        violations = []
        
        # Check for file header (first non-empty lines)
        has_header = False
        for i, line in enumerate(lines[:10]):
            if line.strip() and not has_header:
                if re.match(self.js_patterns['file_header']['pattern'], ''.join(lines[i:i+4])):
                    has_header = True
                    break
        
        if not has_header and len(lines) > 10:
            violations.append(CommentViolation(
                file_path=file_path,
                line_number=1,
                severity=self.js_patterns['file_header']['severity'],
                message="Missing standard file header comment",
                original_line=lines[0] if lines else "",
                suggested_fix=self.js_patterns['file_header']['example'],
                pattern_type='file_header'
            ))
        
        # Check inline comments
        for i, line in enumerate(lines):
            if re.match(r'^\s*//\s*(.+)$', line):
                comment_match = re.match(r'^\s*//\s*(.+)$', line)
                if comment_match:
                    comment_text = comment_match.group(1)
                    # Check if it starts with valid prefix
                    valid_start = any(comment_text.startswith(prefix) 
                                    for prefix in self.js_patterns['inline_comment']['valid_starts'])
                    
                    if not valid_start and not comment_text.startswith(('─', '=', '-')):
                        # Check if it's a capitalized sentence
                        if not re.match(r'^[A-Z].*[.!?]?$', comment_text):
                            violations.append(CommentViolation(
                                file_path=file_path,
                                line_number=i + 1,
                                severity='info',
                                message="Inline comment should start with prefix (TODO:, NOTE:, etc.) or be a proper sentence",
                                original_line=line,
                                suggested_fix=f"// NOTE: {comment_text}",
                                pattern_type='inline_comment'
                            ))
        
        return violations
    
    def _validate_css_comments(self, file_path: Path, lines: List[str]) -> List[CommentViolation]:
        """Validate CSS comment patterns"""
        violations = []
        
        # Check for file header
        has_header = False
        for i, line in enumerate(lines[:10]):
            if line.strip() and not has_header:
                if re.match(self.css_patterns['file_header']['pattern'], ''.join(lines[i:i+3])):
                    has_header = True
                    break
        
        if not has_header and len(lines) > 10:
            violations.append(CommentViolation(
                file_path=file_path,
                line_number=1,
                severity=self.css_patterns['file_header']['severity'],
                message="Missing standard file header comment",
                original_line=lines[0] if lines else "",
                suggested_fix=self.css_patterns['file_header']['example'],
                pattern_type='file_header'
            ))
        
        # Check section headers
        for i, line in enumerate(lines):
            section_match = re.match(r'^/\*\s*([^*]+)\s*\*/$', line)
            if section_match:
                section_text = section_match.group(1).strip()
                # Check if it matches valid formats
                valid_format = any(re.match(fmt, section_text) 
                                 for fmt in self.css_patterns['section_header']['valid_formats'])
                
                if not valid_format and len(section_text) > 3:  # Ignore very short comments
                    violations.append(CommentViolation(
                        file_path=file_path,
                        line_number=i + 1,
                        severity='info',
                        message="Section headers should be in ALL CAPS or Title Case",
                        original_line=line,
                        suggested_fix=f"/* {section_text.upper()} */",
                        pattern_type='section_header'
                    ))
        
        return violations
    
    def _check_forbidden_patterns(self, file_path: Path, lines: List[str]) -> List[CommentViolation]:
        """Check for forbidden patterns"""
        violations = []
        file_ext = file_path.suffix
        
        for pattern_name, pattern_info in self.forbidden_patterns.items():
            # Check if pattern applies to this file type
            if 'file_types' in pattern_info and file_ext not in pattern_info['file_types']:
                continue
            
            pattern = pattern_info['pattern']
            
            for i, line in enumerate(lines):
                # Skip pattern if it has exceptions
                if 'exceptions' in pattern_info:
                    skip = False
                    for exception in pattern_info['exceptions']:
                        if exception in line:
                            skip = True
                            break
                    if skip:
                        continue
                
                # Check for pattern
                if re.search(pattern, line):
                    violations.append(CommentViolation(
                        file_path=file_path,
                        line_number=i + 1,
                        severity=pattern_info['severity'],
                        message=pattern_info['message'],
                        original_line=line,
                        pattern_type=pattern_name
                    ))
        
        return violations
    
    def _auto_fix_comments(self, file_path: Path, lines: List[str], 
                          violations: List[CommentViolation]) -> List[str]:
        """Auto-fix comment violations"""
        fixed_lines = lines.copy()
        
        # Sort violations by line number (descending) to avoid index issues
        sorted_violations = sorted(violations, key=lambda v: v.line_number, reverse=True)
        
        for violation in sorted_violations:
            if violation.suggested_fix and violation.line_number > 0:
                line_idx = violation.line_number - 1
                
                if violation.pattern_type == 'file_header' and line_idx == 0:
                    # Insert header at beginning
                    header_lines = violation.suggested_fix.split('\n')
                    fixed_lines = [line + '\n' for line in header_lines] + fixed_lines
                
                elif violation.pattern_type == 'inline_comment':
                    # Replace inline comment
                    if line_idx < len(fixed_lines):
                        indent = re.match(r'^(\s*)', fixed_lines[line_idx]).group(1)
                        fixed_lines[line_idx] = indent + violation.suggested_fix + '\n'
                
                elif violation.pattern_type == 'section_header':
                    # Replace section header
                    if line_idx < len(fixed_lines):
                        fixed_lines[line_idx] = violation.suggested_fix + '\n'
        
        return fixed_lines
    
    def validate_directory(self, directory: Path, pattern: str = "**/*", 
                         auto_fix: bool = False) -> ValidationResult:
        """Validate all matching files in a directory"""
        result = ValidationResult()
        
        # Find all JS and CSS files
        js_files = list(directory.glob(f"{pattern}.js"))
        css_files = list(directory.glob(f"{pattern}.css"))
        all_files = js_files + css_files
        
        result.total_files = len(all_files)
        
        for file_path in all_files:
            # Skip excluded paths
            if self._should_skip_file(file_path):
                continue
            
            violations = self.validate_file(file_path, auto_fix=auto_fix)
            result.violations.extend(violations)
            result.files_checked += 1
            
            if auto_fix and violations:
                # Count fixed violations
                re_violations = self.validate_file(file_path, auto_fix=False)
                result.fixed_count += len(violations) - len(re_violations)
        
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
            'spec'
        ]
        
        path_str = str(file_path)
        return any(pattern in path_str for pattern in skip_patterns)
    
    def print_report(self, result: ValidationResult):
        """Print validation report"""
        print("\n" + self.formatter.header("Comment Pattern Validation Report", emoji="quality"))
        print(f"\nFiles checked: {result.files_checked}/{result.total_files}")
        print(f"Violations found: {len(result.violations)}")
        print(f"  - Errors: {result.error_count}")
        print(f"  - Warnings: {result.warning_count}")
        print(f"  - Info: {len(result.violations) - result.error_count - result.warning_count}")
        
        if result.fixed_count > 0:
            print(f"\nAuto-fixed: {result.fixed_count} violations")
        
        if result.violations:
            print("\n" + self.formatter.header("Violations", separator=self.formatter.SEPARATOR_DASHED))
            
            # Group by file
            by_file = {}
            for violation in result.violations:
                file_key = str(violation.file_path)
                if file_key not in by_file:
                    by_file[file_key] = []
                by_file[file_key].append(violation)
            
            for file_path, file_violations in by_file.items():
                rel_path = Path(file_path).relative_to(self.project_root)
                print(f"\n📁 {rel_path}")
                print("-" * 40)
                
                for v in sorted(file_violations, key=lambda x: x.line_number):
                    severity_emoji = {
                        'error': '🚨',
                        'warning': '⚠️',
                        'info': 'ℹ️'
                    }.get(v.severity, '')
                    
                    print(f"  Line {v.line_number}: {severity_emoji} [{v.severity.upper()}] {v.message}")
                    
                    if v.original_line.strip():
                        print(f"    Found: {v.original_line.strip()}")
                    
                    if v.suggested_fix:
                        print(f"    Suggested: {v.suggested_fix.split(chr(10))[0]}...")
        
        print("\n" + self.formatter.footer())
        print("✅ All comment patterns valid!" if result.is_valid else "❌ Validation failed")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Validate comment patterns in JS and CSS files")
    parser.add_argument('path', nargs='?', default='src', 
                       help='Path to validate (default: src)')
    parser.add_argument('--fix', action='store_true', 
                       help='Auto-fix violations where possible')
    parser.add_argument('--pattern', default='**/*', 
                       help='Glob pattern for files (default: **/*)')
    
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
    
    # Create validator
    validator = CommentValidator(project_root)
    
    # Validate path
    validate_path = project_root / args.path
    if not validate_path.exists():
        print(f"❌ Path not found: {validate_path}")
        sys.exit(1)
    
    # Run validation
    if validate_path.is_file():
        violations = validator.validate_file(validate_path, auto_fix=args.fix)
        result = ValidationResult(
            total_files=1,
            files_checked=1,
            violations=violations
        )
    else:
        result = validator.validate_directory(validate_path, pattern=args.pattern, 
                                           auto_fix=args.fix)
    
    # Print report
    validator.print_report(result)
    
    # Exit with appropriate code
    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()