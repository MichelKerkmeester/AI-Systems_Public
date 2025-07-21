#!/usr/bin/env python3
"""
Code Reuse Validation Hook

This hook enforces code reuse principles by:
1. Validating code changes follow reuse principles
2. For new file creation: checks if exhaustive reuse analysis was done
3. For modifications: verifies existing patterns are followed
4. Detects duplicate code patterns
5. Suggests existing components that could be reused
6. Works as both UserPromptSubmit and PostToolUse hook
7. Integrates with memory system to capture REUSABLE_COMPONENT patterns
8. Outputs warnings when reuse opportunities are missed
"""

import sys
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import subprocess
from datetime import datetime


class CodeReuseValidationHook:
    """Validates code reuse principles and captures reusable patterns"""
    
    def __init__(self):
        self.name = "Code Reuse Validation"
        self.priority = 90  # High priority
        self.project_root = self._find_project_root()
        self.memory_patterns: Set[str] = set()
        self.existing_components: Dict[str, List[str]] = {}
        self.validation_results: List[Dict] = []
        
    def _find_project_root(self) -> Path:
        """Find project root by looking for .git directory"""
        current = Path.cwd()
        while current != current.parent:
            if (current / '.git').exists():
                return current
            current = current.parent
        return Path.cwd()
    
    def _load_existing_patterns(self) -> Dict[str, List[str]]:
        """Load existing code patterns from the codebase"""
        patterns = {
            'components': [],
            'utilities': [],
            'services': [],
            'styles': [],
            'animations': []
        }
        
        # Common component patterns
        component_dirs = [
            'src/C__components',
            'src/D__modules',
            'src/B__global'
        ]
        
        for dir_path in component_dirs:
            full_path = self.project_root / dir_path
            if full_path.exists():
                for file_path in full_path.rglob('*.js'):
                    rel_path = file_path.relative_to(self.project_root)
                    patterns['components'].append(str(rel_path))
                    
                for file_path in full_path.rglob('*.css'):
                    rel_path = file_path.relative_to(self.project_root)
                    patterns['styles'].append(str(rel_path))
        
        return patterns
    
    def _search_similar_code(self, code_snippet: str, file_type: str) -> List[Dict]:
        """Search for similar code patterns in the codebase"""
        similar = []
        
        # Extract key patterns from the code snippet
        patterns_to_search = []
        
        if file_type == 'js':
            # Look for function names
            func_matches = re.findall(r'function\s+(\w+)|const\s+(\w+)\s*=\s*(?:async\s*)?\(', code_snippet)
            for match in func_matches:
                func_name = match[0] or match[1]
                if func_name:
                    patterns_to_search.append(func_name)
            
            # Look for class names
            class_matches = re.findall(r'class\s+(\w+)', code_snippet)
            patterns_to_search.extend(class_matches)
            
            # Look for common patterns
            if 'addEventListener' in code_snippet:
                patterns_to_search.append('addEventListener')
            if 'querySelector' in code_snippet:
                patterns_to_search.append('querySelector')
            if 'IntersectionObserver' in code_snippet:
                patterns_to_search.append('IntersectionObserver')
                
        elif file_type == 'css':
            # Look for class names
            class_matches = re.findall(r'\.([a-zA-Z][\w-]*)', code_snippet)
            patterns_to_search.extend(class_matches[:5])  # Limit to avoid too many searches
            
            # Look for data attributes
            data_matches = re.findall(r'\[data-([\w-]+)\]', code_snippet)
            patterns_to_search.extend([f'data-{attr}' for attr in data_matches])
        
        # Search for each pattern
        for pattern in patterns_to_search:
            if len(pattern) > 3:  # Skip very short patterns
                try:
                    # Use grep to search for the pattern
                    result = subprocess.run(
                        ['grep', '-r', '-l', '--include=*.' + file_type, pattern, str(self.project_root / 'src')],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    
                    if result.returncode == 0 and result.stdout:
                        files = result.stdout.strip().split('\n')
                        for file_path in files[:5]:  # Limit results
                            if file_path:
                                similar.append({
                                    'pattern': pattern,
                                    'file': file_path.replace(str(self.project_root) + '/', ''),
                                    'type': 'similar_pattern'
                                })
                except Exception:
                    pass
        
        return similar
    
    def _check_duplicate_functionality(self, content: str, file_path: str) -> List[Dict]:
        """Check for duplicate functionality in the codebase"""
        duplicates = []
        file_type = Path(file_path).suffix[1:]  # Remove the dot
        
        if file_type not in ['js', 'css']:
            return duplicates
        
        # Search for similar code patterns
        similar_code = self._search_similar_code(content, file_type)
        
        # Group by file to avoid duplicate warnings
        seen_files = set()
        for item in similar_code:
            if item['file'] not in seen_files and item['file'] != file_path:
                seen_files.add(item['file'])
                duplicates.append({
                    'type': 'potential_duplicate',
                    'existing_file': item['file'],
                    'pattern': item['pattern'],
                    'suggestion': f"Consider reusing code from {item['file']} instead of duplicating"
                })
        
        return duplicates
    
    def _validate_new_file_creation(self, file_path: str, content: str) -> Dict:
        """Validate if new file creation is justified"""
        validation = {
            'valid': True,
            'warnings': [],
            'suggestions': [],
            'reuse_opportunities': []
        }
        
        # Check if this is an allowed file type
        allowed_patterns = [
            r'\.claude/project-management/specs/',
            r'\.claude/tests/',
            r'test-results.*\.json$',
            r'.*-results-\d{4}-\d{2}-\d{2}.*\.json$',
            r'\.md$'  # Documentation when explicitly requested
        ]
        
        is_allowed = any(re.search(pattern, file_path) for pattern in allowed_patterns)
        
        if not is_allowed:
            # Check for duplicate functionality
            duplicates = self._check_duplicate_functionality(content, file_path)
            
            if duplicates:
                validation['valid'] = False
                validation['warnings'].append(
                    f"🚨 NEW FILE VIOLATION: Creating {file_path} without exhaustive reuse analysis!"
                )
                validation['reuse_opportunities'] = duplicates
                
                for dup in duplicates:
                    validation['suggestions'].append(
                        f"• {dup['suggestion']}"
                    )
            
            # Check if similar components exist
            file_name = Path(file_path).stem
            similar_files = []
            
            try:
                # Search for files with similar names
                result = subprocess.run(
                    ['find', str(self.project_root / 'src'), '-name', f'*{file_name}*', '-type', 'f'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                if result.returncode == 0 and result.stdout:
                    files = result.stdout.strip().split('\n')
                    for found_file in files[:3]:
                        if found_file and found_file != file_path:
                            rel_path = found_file.replace(str(self.project_root) + '/', '')
                            similar_files.append(rel_path)
            except Exception:
                pass
            
            if similar_files:
                validation['warnings'].append(
                    f"⚠️  Found similar files that might be extended instead:"
                )
                for sim_file in similar_files:
                    validation['suggestions'].append(f"• {sim_file}")
        
        return validation
    
    def _validate_code_patterns(self, content: str, file_path: str) -> List[str]:
        """Validate code follows established patterns"""
        warnings = []
        
        if file_path.endswith('.js'):
            # Check for console.log
            if 'console.log' in content:
                warnings.append("❌ console.log found - use proper logging or remove")
            
            # Check for global variables
            if re.search(r'^\s*var\s+\w+\s*=', content, re.MULTILINE):
                warnings.append("❌ Global var declaration - use namespace pattern")
            
            # Check for proper error handling
            if 'addEventListener' in content and 'try' not in content:
                warnings.append("⚠️  Event listeners should have error handling")
                
        elif file_path.endswith('.css'):
            # Check for pixel units
            if re.search(r'\d+px', content):
                warnings.append("❌ Pixel units found - use REM units")
            
            # Check for hardcoded colors
            hardcoded_colors = re.findall(r'#[0-9a-fA-F]{3,6}', content)
            if len(hardcoded_colors) > 2:
                warnings.append("⚠️  Multiple hardcoded colors - consider using CSS variables")
        
        return warnings
    
    def _capture_reusable_pattern(self, file_path: str, pattern_type: str, description: str):
        """Capture a reusable component pattern to memory"""
        pattern = {
            'name': f"REUSABLE_COMPONENT: {Path(file_path).stem}",
            'episode_body': f"Found reusable {pattern_type} at {file_path}: {description}",
            'source': 'code_reuse_validation',
            'group_id': 'reusable_components'
        }
        self.memory_patterns.add(json.dumps(pattern))
    
    def process_user_prompt(self, prompt_data: Dict) -> Dict:
        """Validate user prompt for code reuse compliance"""
        prompt = prompt_data.get('prompt', '').lower()
        
        # Keywords that indicate code creation
        creation_keywords = ['create', 'implement', 'build', 'make', 'add new', 'write']
        reuse_keywords = ['refactor', 'consolidate', 'merge', 'combine', 'optimize']
        
        warnings = []
        suggestions = []
        
        # Check if user is asking to create something new
        is_creation_request = any(keyword in prompt for keyword in creation_keywords)
        is_reuse_request = any(keyword in prompt for keyword in reuse_keywords)
        
        if is_creation_request and not is_reuse_request:
            warnings.append(
                "📋 REMINDER: Follow the 5-step code reuse workflow before creating new files!"
            )
            suggestions.extend([
                "1. Search for existing implementations using Grep/Glob",
                "2. Check patterns.json for established conventions",
                "3. Look for reusable components in src/C__components",
                "4. Justify why existing code cannot be extended",
                "5. Reference specific files in your implementation"
            ])
        
        if warnings or suggestions:
            return {
                'success': True,
                'modified': False,
                'warnings': warnings,
                'suggestions': suggestions,
                'metadata': {
                    'hook': 'code_reuse_validation',
                    'stage': 'pre_prompt'
                }
            }
        
        return {'success': True, 'modified': False}
    
    def process_tool_use(self, tool_data: Dict) -> Dict:
        """Validate tool use for code reuse compliance"""
        tool_name = tool_data.get('tool', '')
        args = tool_data.get('args', {})
        
        warnings = []
        suggestions = []
        reuse_opportunities = []
        
        # Track file operations
        if tool_name == 'Write':
            file_path = args.get('file_path', '')
            content = args.get('content', '')
            
            # Validate new file creation
            if file_path and not Path(file_path).exists():
                validation = self._validate_new_file_creation(file_path, content)
                
                if not validation['valid']:
                    warnings.extend(validation['warnings'])
                    suggestions.extend(validation['suggestions'])
                    reuse_opportunities.extend(validation['reuse_opportunities'])
            
            # Validate code patterns
            pattern_warnings = self._validate_code_patterns(content, file_path)
            warnings.extend(pattern_warnings)
            
            # Check for reusable patterns
            if file_path.endswith('.js'):
                # Check for utility functions
                if re.search(r'function\s+\w+|const\s+\w+\s*=\s*(?:async\s*)?\(', content):
                    self._capture_reusable_pattern(
                        file_path, 
                        'utility',
                        'JavaScript functions that could be reused'
                    )
                
                # Check for event handlers
                if 'addEventListener' in content:
                    self._capture_reusable_pattern(
                        file_path,
                        'event_handler',
                        'Event handling pattern'
                    )
                    
            elif file_path.endswith('.css'):
                # Check for reusable styles
                if re.search(r'\[data-[\w-]+\]', content):
                    self._capture_reusable_pattern(
                        file_path,
                        'style_pattern',
                        'Data attribute styling pattern'
                    )
        
        elif tool_name in ['Edit', 'MultiEdit']:
            file_path = args.get('file_path', '')
            
            # For edits, check if they're following patterns
            if file_path:
                suggestions.append(
                    f"✅ Good: Editing existing file {file_path} instead of creating new"
                )
        
        # Track search operations for compliance
        elif tool_name in ['Grep', 'Glob', 'Read']:
            self.validation_results.append({
                'timestamp': datetime.now().isoformat(),
                'action': 'code_search',
                'tool': tool_name,
                'details': args
            })
        
        if warnings or suggestions or reuse_opportunities:
            return {
                'success': True,
                'modified': False,
                'warnings': warnings,
                'suggestions': suggestions,
                'reuse_opportunities': reuse_opportunities,
                'metadata': {
                    'hook': 'code_reuse_validation',
                    'stage': 'post_tool',
                    'memory_patterns': list(self.memory_patterns)
                }
            }
        
        return {'success': True, 'modified': False}
    
    def run(self):
        """Main entry point for hook execution"""
        try:
            # Read input from stdin
            input_data = json.loads(sys.stdin.read())
            
            event_type = input_data.get('event_type', '')
            
            if event_type == 'UserPromptSubmit':
                result = self.process_user_prompt(input_data)
            elif event_type == 'PostToolUse':
                result = self.process_tool_use(input_data)
            else:
                result = {'success': True, 'modified': False}
            
            # Output result
            print(json.dumps(result))
            sys.exit(0)
            
        except Exception as e:
            # On error, don't block operations
            error_result = {
                'success': True,
                'modified': False,
                'error': str(e)
            }
            print(json.dumps(error_result))
            sys.exit(0)
    
    def get_status(self) -> Dict:
        """Get hook status"""
        self.existing_components = self._load_existing_patterns()
        
        return {
            'active': True,
            'components_tracked': {
                'javascript': len(self.existing_components.get('components', [])),
                'styles': len(self.existing_components.get('styles', [])),
            },
            'validation_results': len(self.validation_results),
            'memory_patterns_captured': len(self.memory_patterns),
            'last_check': datetime.now().isoformat()
        }


def main():
    """CLI entry point"""
    hook = CodeReuseValidationHook()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'status':
            print(json.dumps(hook.get_status(), indent=2))
        elif sys.argv[1] == 'test':
            # Test with sample data
            test_prompt = {
                'prompt': 'Create a new animation component for the hero section'
            }
            result = hook.process_user_prompt(test_prompt)
            print("Prompt validation:", json.dumps(result, indent=2))
            
            # Test file creation
            test_tool = {
                'tool': 'Write',
                'args': {
                    'file_path': 'src/components/new-animation.js',
                    'content': 'function animateHero() { console.log("test"); }'
                }
            }
            result = hook.process_tool_use(test_tool)
            print("\nTool validation:", json.dumps(result, indent=2))
    else:
        # Run as hook
        hook.run()


if __name__ == '__main__':
    main()