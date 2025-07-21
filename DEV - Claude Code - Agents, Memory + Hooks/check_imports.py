#!/usr/bin/env python3
"""Check for broken imports after system restructuring."""

import ast
import os
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple

class ImportChecker:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.issues = []
        self.checked_files = 0
        
        # Patterns to check for
        self.problematic_patterns = {
            'project.': 'Old project prefix found',
            'from project import': 'Old project import found',
            'import project': 'Old project import found',
            'from .project import': 'Old relative project import found',
            'from ..project import': 'Old relative project import found',
            'test_': 'Possible test import (verify if deleted)',
            'hook_': 'Possible hook import (verify path)',
        }
        
        # Known deleted modules (based on git status)
        self.deleted_modules = {
            '.claude/hooks/core/claude-md-update-hook.py',
            '.claude/hooks/core/context-management-hook.py',
            '.claude/hooks/core/doc-update-hook.py',
            '.claude/hooks/core/folder-structure-hook.py',
            '.claude/hooks/core/mode-suggestion-hook.py',
            '.claude/hooks/core/parallel-agent-hook.py',
            '.claude/hooks/core/pattern-extraction-hook.py',
            '.claude/hooks/core/query-planning-hook.py',
            '.claude/hooks/core/security-scan-hook.py',
            '.claude/hooks/core/system-status-update-hook.py',
            '.claude/hooks/core/task-management-hook.py',
            '.claude/hooks/core/workflow-automation-hook.py',
            '.claude/hooks/memory/memory-context-hook-active.py',
            '.claude/hooks/memory/memory-context-hook.py',
            '.claude/hooks/quality/quality-hook.py',
            '.claude/hooks/session/session-hook.py',
            '.claude/hooks/shared/__init__.py',
            '.claude/hooks/shared/hook_base.py',
            '.claude/hooks/shared/hook_formatters.py',
            '.claude/hooks/shared/hook_manager.py',
            '.claude/hooks/shared/hook_priority.py',
            '.claude/hooks/shared/hook_registry.py',
            '.claude/hooks/shared/hook_settings.py',
            '.claude/hooks/shared/hook_state.py',
            '.claude/logic/session/commands/save',
            '.claude/logic/session/commands/save-command.py',
            '.claude/logic/session/utils/multi-agent-session-manager.py',
        }

    def check_file(self, file_path: Path) -> List[Dict]:
        """Check a single Python file for import issues."""
        issues = []
        self.checked_files += 1
        
        # Make file_path absolute if it's relative
        if not file_path.is_absolute():
            file_path = self.base_path / file_path
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Get relative path for display
            try:
                display_path = str(file_path.relative_to(self.base_path))
            except ValueError:
                display_path = str(file_path)
            
            # Check for problematic patterns in raw content
            for pattern, description in self.problematic_patterns.items():
                if pattern in content:
                    lines = content.split('\n')
                    for i, line in enumerate(lines, 1):
                        if pattern in line and not line.strip().startswith('#'):
                            issues.append({
                                'file': display_path,
                                'line': i,
                                'issue': description,
                                'code': line.strip()
                            })
            
            # Parse AST for detailed import analysis
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            if self._is_problematic_import(alias.name):
                                issues.append({
                                    'file': display_path,
                                    'line': node.lineno,
                                    'issue': f"Import of potentially deleted module: {alias.name}",
                                    'code': f"import {alias.name}"
                                })
                    
                    elif isinstance(node, ast.ImportFrom):
                        module = node.module or ''
                        if self._is_problematic_import(module):
                            import_stmt = f"from {module} import " + ", ".join(alias.name for alias in node.names)
                            issues.append({
                                'file': display_path,
                                'line': node.lineno,
                                'issue': f"Import from potentially deleted module: {module}",
                                'code': import_stmt
                            })
                        
                        # Check for relative imports that might be broken
                        if node.level > 0:  # Relative import
                            # Calculate the actual module path
                            parent_levels = node.level
                            current_dir = file_path.parent
                            for _ in range(parent_levels):
                                current_dir = current_dir.parent
                            
                            if module:
                                target_path = current_dir / module.replace('.', '/')
                                if not self._module_exists(target_path):
                                    import_stmt = "." * node.level + (module or '') + " import " + ", ".join(alias.name for alias in node.names)
                                    issues.append({
                                        'file': display_path,
                                        'line': node.lineno,
                                        'issue': f"Relative import might be broken",
                                        'code': f"from {import_stmt}"
                                    })
            
            except SyntaxError as e:
                issues.append({
                    'file': display_path,
                    'line': e.lineno or 0,
                    'issue': f"Syntax error: {e.msg}",
                    'code': ''
                })
                
        except Exception as e:
            issues.append({
                'file': display_path if 'display_path' in locals() else str(file_path),
                'line': 0,
                'issue': f"Error reading file: {str(e)}",
                'code': ''
            })
        
        return issues

    def _is_problematic_import(self, module_name: str) -> bool:
        """Check if an import might be problematic."""
        if not module_name:
            return False
            
        # Check for old project prefix
        if module_name.startswith('project.'):
            return True
            
        # Check against deleted modules
        for deleted in self.deleted_modules:
            deleted_module = deleted.replace('/', '.').replace('.py', '')
            if deleted_module.endswith(module_name) or module_name in deleted_module:
                return True
                
        return False

    def _module_exists(self, module_path: Path) -> bool:
        """Check if a module exists at the given path."""
        # Check for Python file
        if module_path.with_suffix('.py').exists():
            return True
        # Check for package directory
        if module_path.is_dir() and (module_path / '__init__.py').exists():
            return True
        return False

    def check_all_files(self, file_list: List[str]):
        """Check all Python files in the list."""
        for file_path in file_list:
            path = Path(file_path)
            if path.exists() and path.suffix == '.py':
                file_issues = self.check_file(path)
                self.issues.extend(file_issues)

    def generate_report(self) -> str:
        """Generate a detailed report of findings."""
        report = []
        report.append("=" * 80)
        report.append("IMPORT CHECK REPORT")
        report.append("=" * 80)
        report.append(f"\nTotal files checked: {self.checked_files}")
        report.append(f"Total issues found: {len(self.issues)}\n")
        
        if not self.issues:
            report.append("✅ No import issues found!")
        else:
            # Group issues by file
            issues_by_file = {}
            for issue in self.issues:
                file_path = issue['file']
                if file_path not in issues_by_file:
                    issues_by_file[file_path] = []
                issues_by_file[file_path].append(issue)
            
            # Report issues by file
            for file_path, file_issues in sorted(issues_by_file.items()):
                report.append(f"\n📄 {file_path}")
                report.append("-" * len(f"📄 {file_path}"))
                
                for issue in sorted(file_issues, key=lambda x: x['line']):
                    report.append(f"  Line {issue['line']:4d}: {issue['issue']}")
                    if issue['code']:
                        report.append(f"           > {issue['code']}")
        
        report.append("\n" + "=" * 80)
        return "\n".join(report)


def main():
    # Get all Python files from stdin or arguments
    if len(sys.argv) > 1:
        file_list = sys.argv[1:]
    else:
        file_list = [line.strip() for line in sys.stdin if line.strip()]
    
    base_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude"
    checker = ImportChecker(base_path)
    checker.check_all_files(file_list)
    
    print(checker.generate_report())
    
    # Exit with error code if issues found
    sys.exit(1 if checker.issues else 0)


if __name__ == "__main__":
    main()