#!/usr/bin/env python3
"""
Fix import statements in all hooks to use correct paths
"""

import os
import re
from pathlib import Path

def fix_imports_in_file(file_path):
    """Fix imports in a single file"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace 'from shared import' with 'from hooks.shared import'
    modified = re.sub(
        r'^from shared import',
        'from hooks.shared import',
        content,
        flags=re.MULTILINE
    )
    
    # Also handle multiline imports
    modified = re.sub(
        r'^from shared import \(',
        'from hooks.shared import (',
        modified,
        flags=re.MULTILINE
    )
    
    if modified != content:
        with open(file_path, 'w') as f:
            f.write(modified)
        print(f"  ✓ Fixed imports in {file_path}")
        return True
    else:
        print(f"  - No changes needed in {file_path}")
        return False

def main():
    """Fix imports in all hook files"""
    hooks_dir = Path(__file__).resolve().parent.parent / "hooks"
    
    # Find all Python files
    python_files = list(hooks_dir.rglob("*.py"))
    
    fixed_count = 0
    for file_path in python_files:
        if fix_imports_in_file(file_path):
            fixed_count += 1
    
    print(f"\n✅ Fixed imports in {fixed_count} files")

if __name__ == "__main__":
    main()