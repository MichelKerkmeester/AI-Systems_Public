#!/bin/bash
# Create symlinks from logic/shared to hooks/shared for hook-related modules

cd "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/shared"

# Create symlinks to hook modules
ln -sf ../../hooks/shared/hook_base.py hook_base.py
ln -sf ../../hooks/shared/hook_settings.py hook_settings.py
ln -sf ../../hooks/shared/hook_formatters.py hook_formatters.py
ln -sf ../../hooks/shared/hook_state.py hook_state.py
ln -sf ../../hooks/shared/hook_priority.py hook_priority.py
ln -sf ../../hooks/shared/hook_manager.py hook_manager.py
ln -sf ../../hooks/shared/hook_registry.py hook_registry.py

echo "✅ Created symlinks for hook modules"