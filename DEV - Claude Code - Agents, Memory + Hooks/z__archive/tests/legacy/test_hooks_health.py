#!/usr/bin/env python3
"""Test script to verify hook health after system restructuring."""

import os
import sys
import json
import importlib.util
import traceback
from pathlib import Path

# Add the logic directory to the Python path
base_dir = Path(__file__).parent.parent
sys.path.insert(0, str(base_dir / "logic"))

def test_hook_import(hook_path):
    """Test if a hook can be imported without errors."""
    try:
        # Convert path to module name
        spec = importlib.util.spec_from_file_location("test_hook", hook_path)
        if spec is None:
            return False, f"Could not create spec for {hook_path}"
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        return True, "Import successful"
    except Exception as e:
        return False, f"Import failed: {str(e)}\n{traceback.format_exc()}"

def check_file_references(hook_path):
    """Check for references to deleted files in hook code."""
    deleted_paths = [
        ".claude/hooks/",  # Old hooks directory
        ".claude/project/sessions/",  # Deleted sessions directory
        ".claude/logic/session/commands/save",  # Deleted save command
        ".claude/logic/shared/hook_",  # Old hook shared modules
        ".claude/project/tasks/active/",  # Check for hardcoded task paths
        ".claude/project/tasks/completed/",
        ".claude/project/tasks/to-do/"
    ]
    
    broken_refs = []
    
    try:
        with open(hook_path, 'r') as f:
            content = f.read()
            
        for deleted_path in deleted_paths:
            if deleted_path in content:
                # Find line numbers
                lines = content.split('\n')
                for i, line in enumerate(lines, 1):
                    if deleted_path in line:
                        broken_refs.append(f"Line {i}: References '{deleted_path}'")
    except Exception as e:
        broken_refs.append(f"Could not read file: {str(e)}")
    
    return broken_refs

def main():
    """Run hook health checks."""
    print("🔍 Hook System Health Check")
    print("=" * 50)
    
    # Load settings.json
    settings_path = base_dir / "settings.json"
    with open(settings_path, 'r') as f:
        settings = json.load(f)
    
    # Extract all hook paths from settings
    registered_hooks = set()
    
    for event_type in ['UserPromptSubmit', 'PreToolUse', 'PostToolUse']:
        if event_type in settings['hooks']:
            for config in settings['hooks'][event_type]:
                hooks = config.get('hooks', [])
                for hook in hooks:
                    if hook['type'] == 'command':
                        # Extract path from command
                        cmd_parts = hook['command'].split("'")
                        if len(cmd_parts) >= 2:
                            hook_path = cmd_parts[1]
                            registered_hooks.add(hook_path)
    
    # Find all hook files in the logic/hooks directory
    hooks_dir = base_dir / "logic" / "hooks"
    all_hook_files = list(hooks_dir.rglob("*.py"))
    all_hook_paths = [str(f) for f in all_hook_files if not f.name.startswith('__')]
    
    # Test results
    results = {
        'import_failures': [],
        'broken_references': [],
        'missing_from_settings': [],
        'not_found_on_disk': [],
        'successful': []
    }
    
    print("\n📋 Testing registered hooks...")
    print("-" * 50)
    
    for hook_path in registered_hooks:
        print(f"\nTesting: {os.path.basename(hook_path)}")
        
        # Check if file exists
        if not os.path.exists(hook_path):
            results['not_found_on_disk'].append(hook_path)
            print("  ❌ File not found on disk!")
            continue
        
        # Test import
        success, message = test_hook_import(hook_path)
        if not success:
            results['import_failures'].append({
                'path': hook_path,
                'error': message
            })
            print(f"  ❌ Import failed: {message.split(':')[0]}")
        else:
            print("  ✅ Import successful")
        
        # Check for broken references
        broken_refs = check_file_references(hook_path)
        if broken_refs:
            results['broken_references'].append({
                'path': hook_path,
                'references': broken_refs
            })
            print(f"  ⚠️  Found {len(broken_refs)} broken reference(s)")
        
        if success and not broken_refs:
            results['successful'].append(hook_path)
    
    # Check for hooks not in settings.json
    print("\n📋 Checking for unregistered hooks...")
    print("-" * 50)
    
    for hook_file in all_hook_paths:
        if hook_file not in registered_hooks and not hook_file.endswith('.backup.py'):
            # Skip helper files and backup files
            if any(skip in os.path.basename(hook_file) for skip in ['helper', 'buffer', 'stats', '__init__']):
                continue
            results['missing_from_settings'].append(hook_file)
            print(f"  ⚠️  Not registered: {os.path.basename(hook_file)}")
    
    # Summary report
    print("\n📊 Summary Report")
    print("=" * 50)
    print(f"✅ Healthy hooks: {len(results['successful'])}")
    print(f"❌ Import failures: {len(results['import_failures'])}")
    print(f"⚠️  Broken references: {len(results['broken_references'])}")
    print(f"📁 Missing files: {len(results['not_found_on_disk'])}")
    print(f"⚙️  Unregistered hooks: {len(results['missing_from_settings'])}")
    
    # Detailed report
    if results['import_failures']:
        print("\n❌ Import Failures:")
        for failure in results['import_failures']:
            print(f"\n  {os.path.basename(failure['path'])}:")
            print(f"    {failure['error'].split(chr(10))[0]}")
    
    if results['broken_references']:
        print("\n⚠️  Broken References:")
        for ref in results['broken_references']:
            print(f"\n  {os.path.basename(ref['path'])}:")
            for broken_ref in ref['references'][:3]:  # Show first 3
                print(f"    {broken_ref}")
    
    if results['not_found_on_disk']:
        print("\n📁 Missing Files:")
        for path in results['not_found_on_disk']:
            print(f"  - {path}")
    
    # Overall health status
    print("\n🏥 Overall Health Status:")
    total_registered = len(registered_hooks)
    healthy = len(results['successful'])
    health_percentage = (healthy / total_registered * 100) if total_registered > 0 else 0
    
    if health_percentage >= 90:
        print(f"  ✅ GOOD ({health_percentage:.0f}% healthy)")
    elif health_percentage >= 70:
        print(f"  ⚠️  FAIR ({health_percentage:.0f}% healthy)")
    else:
        print(f"  ❌ POOR ({health_percentage:.0f}% healthy)")
    
    return results

if __name__ == "__main__":
    results = main()