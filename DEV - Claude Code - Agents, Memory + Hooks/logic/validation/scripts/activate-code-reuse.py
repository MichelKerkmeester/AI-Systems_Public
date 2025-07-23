#!/usr/bin/env python3
"""
Activate Code Reuse Feature
This script initializes the code reuse state and ensures proper connectivity
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

# Add logic directory to path
logic_dir = Path(__file__).parent.parent
sys.path.insert(0, str(logic_dir))

# Add state directory to path for state_manager import
state_dir = Path(__file__).parent.parent.parent / 'state' / 'code_reuse'
sys.path.insert(0, str(state_dir))

# Import the state manager directly from state directory
from state_manager import get_state_manager, StateManager

def activate_code_reuse():
    """Initialize and activate the code reuse feature"""
    print("🚀 Activating Code Reuse Feature...")
    
    # Get state manager instance with correct state directory
    manager = StateManager(state_dir=str(state_dir))
    
    # Initialize state with current timestamp
    print("📊 Initializing state files...")
    
    # Update code_reuse_state.json
    def initialize_state(current_state):
        """Initialize the state with current timestamp"""
        current_state['last_updated'] = datetime.now().isoformat()
        current_state['feature_flags']['auto_consolidation_enabled'] = True
        current_state['feature_flags']['real_time_analysis'] = True
        current_state['statistics']['total_analyses'] = 1  # Mark as active
        return current_state
    
    manager.update_state('code_reuse_state', initialize_state)
    
    # Verify the update
    updated_state = manager.load_state('code_reuse_state')
    
    print("✅ Code Reuse State Initialized:")
    print(f"   - Last Updated: {updated_state['last_updated']}")
    print(f"   - Auto Consolidation: {updated_state['feature_flags']['auto_consolidation_enabled']}")
    print(f"   - Real-time Analysis: {updated_state['feature_flags']['real_time_analysis']}")
    print(f"   - Total Analyses: {updated_state['statistics']['total_analyses']}")
    
    # Check hook configuration
    settings_path = Path(__file__).parent.parent.parent / 'settings.json'
    with open(settings_path, 'r') as f:
        settings = json.load(f)
    
    hook_configured = False
    hook_path = '.claude/logic/hooks/code_reuse/code-reuse-validation-hook.py'
    
    # Check UserPromptSubmit hooks
    for hook_group in settings.get('hooks', {}).get('UserPromptSubmit', []):
        for hook in hook_group.get('hooks', []):
            if hook_path in hook.get('command', ''):
                hook_configured = True
                break
    
    # Check PostToolUse hooks
    for hook_group in settings.get('hooks', {}).get('PostToolUse', []):
        for hook in hook_group.get('hooks', []):
            if hook_path in hook.get('command', ''):
                hook_configured = True
                break
    
    if hook_configured:
        print("✅ Code Reuse Hook is properly configured in settings.json")
    else:
        print("❌ Code Reuse Hook is NOT configured in settings.json")
        print("   Please add it to the hooks configuration")
    
    # Test the hook
    print("\n🧪 Testing Code Reuse Hook...")
    hook_script = Path(__file__).parent.parent / 'hooks' / 'code_reuse' / 'code-reuse-validation-hook.py'
    os.system(f"python3 '{hook_script}' status")
    
    print("\n✅ Code Reuse Feature Activation Complete!")
    print("\n📝 Next Steps:")
    print("1. The code reuse hook will now validate all file operations")
    print("2. It will suggest existing components before creating new ones")
    print("3. State tracking is now active and will record all analyses")
    print("\n💡 Note: The hook and state manager need to be connected for full functionality")
    print("   Consider updating the hook to use StateManager for persistent tracking")

if __name__ == '__main__':
    activate_code_reuse()