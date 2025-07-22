# Superdesign Canvas Integration Rollback Plan (Simplified)

## Overview
Since we're using existing tools (Windsurf + Superdesign extension) with minimal custom code, rollback is extremely simple.

## What Needs Rollback?
1. **Windsurf**: Superdesign extension
2. **Claude Code**: design.py command script  
3. **File System**: .superdesign/ directory
4. **Shell**: Command aliases

## Rollback Steps (Total Time: ~5 minutes)

### 1. Uninstall Superdesign Extension
```bash
# In Windsurf IDE
1. Press Cmd+Shift+X (Extensions)
2. Find Superdesign
3. Click Uninstall
4. Restart Windsurf
```

### 2. Remove Claude Code Scripts
```bash
# Remove design generation commands
rm -f .claude/logic/commands/design.py
rm -f .claude/logic/commands/design-batch.sh
rm -f .claude/logic/commands/design-config.json
```

### 3. Clean Up Aliases
```bash
# Remove from shell config
sed -i '' '/cc-design/d' ~/.zshrc  # Mac
# OR
sed -i '/cc-design/d' ~/.bashrc    # Linux

# Reload shell
source ~/.zshrc
```

### 4. Archive/Remove Designs
```bash
# Option A: Archive (recommended)
mv .superdesign/ .superdesign-backup-$(date +%Y%m%d)/

# Option B: Delete
rm -rf .superdesign/
```

### 5. Archive Documentation
```bash
# Move specs to archive
mv .claude/project-management/specs/superdesign-canvas-integration/ \
   .claude/project-management/specs/z__archive/
```

## Verification
```bash
# Check removal
which cc-design                    # Should return nothing
ls .superdesign/                   # Should not exist  
ls .claude/logic/commands/design.py # Should not exist

# Test Windsurf
# Open Windsurf - should work normally without Superdesign
```

## Why This is Safe

### No Code Changes Required
- ❌ No viteflow components created
- ❌ No Vite config modified
- ❌ No package.json changes
- ❌ No build system touched

### What We Actually Did
- ✅ Installed an IDE extension
- ✅ Created one Python script
- ✅ Made a directory for designs
- ✅ Added a shell alias

## Data Backup
```bash
# Before removing, count designs
find .superdesign -name "*.html" -type f | wc -l

# Create backup if needed
tar -czf superdesign-backup-$(date +%Y%m%d).tar.gz .superdesign/
```

## Alternative Solutions

### If Superdesign Doesn't Work Well
1. **VS Code + Superdesign** - More stable/tested
2. **Figma Dev Mode** - Professional design tool
3. **Local HTML Server** - Simple Python/Node preview
4. **CodePen/JSFiddle** - Online preview
5. **Browser DevTools** - Direct HTML editing

### Minimal Preview Solution
```python
# Simple alternative: preview.py
import http.server
import webbrowser
import os

os.chdir('.superdesign/design_iterations')
webbrowser.open('http://localhost:8000')
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8000)
```

## Rollback Decision Matrix

| Issue | Impact | Rollback? | Alternative |
|-------|--------|-----------|-------------|
| Windsurf crashes | High | Yes | Use VS Code |
| Slow performance | Medium | Maybe | Reduce designs |
| Complex workflow | Low | No | Simplify process |
| Better tool found | Low | Yes | Migrate designs |

## Total Rollback Time
- Uninstall extension: 1 min
- Remove scripts: 1 min  
- Clean aliases: 1 min
- Archive files: 2 min
- **Total: 5 minutes**

## Summary
The beauty of this approach is that rollback is trivial. We're not modifying any existing code, just adding tools that work alongside your project. Removal is as simple as uninstalling an extension and deleting a folder.