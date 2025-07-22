# Shared Directory Configuration Guide

## Overview
Configure a shared `.superdesign/` directory that both Windsurf (with Superdesign) and Claude Code CLI can access seamlessly.

## Directory Structure

### Standard Layout
```
project-root/
├── .superdesign/                    # Shared directory
│   ├── design_iterations/          # All generated designs
│   │   ├── design_1.html          # From Claude Code
│   │   ├── design_1_1.html        # Iteration from Windsurf
│   │   ├── design_2.html          # From Claude Code
│   │   └── archive/               # Old designs (optional)
│   ├── moodboard/                 # Reference images
│   │   ├── hero-inspiration.png
│   │   └── color-palette.jpg
│   ├── design_system/             # Shared design tokens
│   │   ├── tokens.json
│   │   ├── components.json
│   │   └── typography.json
│   └── config.json                # Shared configuration
├── .claude/                       # Claude Code config
│   └── logic/
│       └── commands/
│           └── design.py          # Design generation
└── src/                          # Your project files
```

## Configuration Files

### 1. Shared Config (.superdesign/config.json)
```json
{
  "version": "1.0.0",
  "workspace": {
    "defaultViewport": "desktop",
    "gridColumns": 4,
    "autoRefresh": true,
    "refreshInterval": 500
  },
  "generation": {
    "defaultStyle": "modern",
    "includeTailwind": true,
    "tailwindConfig": "default",
    "outputFormat": "html"
  },
  "tools": {
    "windsurf": {
      "enabled": true,
      "canvasUpdateMode": "auto"
    },
    "claudeCode": {
      "enabled": true,
      "batchLimit": 10,
      "generationTimeout": 30000
    }
  },
  "paths": {
    "iterations": "./design_iterations",
    "moodboard": "./moodboard",
    "designSystem": "./design_system",
    "archive": "./design_iterations/archive"
  }
}
```

### 2. Design System Tokens (.superdesign/design_system/tokens.json)
```json
{
  "colors": {
    "primary": {
      "50": "#eff6ff",
      "500": "#3b82f6",
      "900": "#1e3a8a"
    },
    "secondary": {
      "50": "#f0fdf4",
      "500": "#10b981",
      "900": "#064e3b"
    }
  },
  "spacing": {
    "xs": "0.5rem",
    "sm": "1rem",
    "md": "1.5rem",
    "lg": "2rem",
    "xl": "3rem"
  },
  "typography": {
    "fontFamily": {
      "sans": ["Inter", "system-ui", "sans-serif"],
      "mono": ["JetBrains Mono", "monospace"]
    },
    "fontSize": {
      "sm": "0.875rem",
      "base": "1rem",
      "lg": "1.125rem",
      "xl": "1.25rem",
      "2xl": "1.5rem",
      "3xl": "1.875rem",
      "4xl": "2.25rem"
    }
  },
  "breakpoints": {
    "sm": "640px",
    "md": "768px",
    "lg": "1024px",
    "xl": "1280px",
    "2xl": "1536px"
  }
}
```

### 3. Claude Code Integration (.claude/logic/commands/design-config.json)
```json
{
  "superdesignPath": "./.superdesign",
  "templates": {
    "default": {
      "includes": ["tailwind", "responsive"],
      "viewport": "width=device-width, initial-scale=1.0"
    },
    "minimal": {
      "includes": ["tailwind"],
      "classes": "min-h-screen bg-white"
    },
    "bold": {
      "includes": ["tailwind", "animations"],
      "classes": "min-h-screen bg-gradient-to-br from-purple-600 to-blue-600"
    }
  },
  "fileNaming": {
    "pattern": "design_{number}.html",
    "iterationPattern": "design_{number}_{iteration}.html",
    "componentPattern": "component_{name}_{variant}.html"
  }
}
```

## Setup Instructions

### Step 1: Initialize Directory Structure
```bash
# Run this from your project root
mkdir -p .superdesign/design_iterations/archive
mkdir -p .superdesign/moodboard
mkdir -p .superdesign/design_system

# Create initial config files
cat > .superdesign/config.json << 'EOF'
{
  "version": "1.0.0",
  "workspace": {
    "defaultViewport": "desktop",
    "gridColumns": 4,
    "autoRefresh": true
  }
}
EOF
```

### Step 2: Set Permissions
```bash
# Ensure both tools can read/write
chmod -R 755 .superdesign/
```

### Step 3: Configure Git
```bash
# Add to .gitignore
cat >> .gitignore << 'EOF'
# Superdesign temp files
.superdesign/.cache/
.superdesign/design_iterations/archive/
.superdesign/moodboard/*.tmp

# Keep important files
!.superdesign/config.json
!.superdesign/design_system/
!.superdesign/design_iterations/design_*.html
EOF
```

## Access Patterns

### Windsurf/Superdesign Access
- **Read**: All files in `.superdesign/`
- **Write**: New iterations, modifications
- **Watch**: `design_iterations/` for changes
- **Display**: Canvas view of all designs

### Claude Code Access
- **Read**: Config files, existing designs
- **Write**: New designs in `design_iterations/`
- **Generate**: Based on templates and tokens
- **Analyze**: Learn from existing designs

## Synchronization

### File Watching
Both tools watch for changes:
```javascript
// Superdesign watches (automatic)
.superdesign/design_iterations/*.html

// Claude Code can watch (optional)
import { watch } from 'fs';
watch('.superdesign/design_iterations', (event, filename) => {
  console.log(`Design updated: ${filename}`);
});
```

### Conflict Resolution
- **Naming**: Automatic numbering prevents conflicts
- **Iterations**: `_1`, `_2` suffix for versions
- **Locking**: No file locking needed (append-only)

## Common Workflows

### 1. Generate → Review → Iterate
```bash
# Claude Code generates
cc-design "hero section"  # Creates design_1.html

# Open in Windsurf
# Superdesign shows design_1.html
# Make visual adjustments
# Saves as design_1_1.html

# Claude Code can analyze changes
cc-design analyze design_1 design_1_1
```

### 2. Batch Generation
```bash
# Generate multiple designs
for style in minimal bold playful; do
  cc-design "pricing card" $style
done

# All appear in Windsurf canvas
# Compare and iterate on best ones
```

### 3. Design System Integration
```javascript
// Both tools read tokens
const tokens = require('./.superdesign/design_system/tokens.json');

// Use in generation
const primaryColor = tokens.colors.primary[500];
```

## Troubleshooting

### Files Not Appearing
1. Check directory permissions
2. Verify correct path in both tools
3. Ensure valid HTML structure
4. Try manual refresh in Superdesign

### Sync Issues
1. Check file system events are enabled
2. Verify no antivirus blocking
3. Test with simple text file first
4. Check console for errors

### Performance
1. Archive old designs regularly
2. Limit active designs to ~100
3. Use smaller viewport for many designs
4. Enable lazy loading if available

## Best Practices

### 1. File Organization
- Keep active designs in root
- Archive completed projects
- Group related designs by prefix
- Use descriptive iteration notes

### 2. Version Control
- Commit significant designs
- Tag release versions
- Document design decisions
- Track iteration history

### 3. Collaboration
- Share `.superdesign/` in repo
- Document design conventions
- Use consistent naming
- Add comments in HTML

## Advanced Configuration

### Custom Watchers
```python
# .claude/logic/watchers/design-watcher.py
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DesignHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith('.html'):
            print(f"New design: {event.src_path}")
            # Trigger any automation

observer = Observer()
observer.schedule(DesignHandler(), '.superdesign/design_iterations')
observer.start()
```

### Integration Hooks
```bash
# Git hook example (.git/hooks/pre-commit)
#!/bin/bash
# Archive old designs before commit
find .superdesign/design_iterations -name "*.html" -mtime +30 \
  -exec mv {} .superdesign/design_iterations/archive/ \;
```

## Summary
The shared directory approach eliminates complex integration code while providing seamless collaboration between Windsurf's visual canvas and Claude Code's generation capabilities. Both tools work with the same files in real-time, creating an efficient design workflow.