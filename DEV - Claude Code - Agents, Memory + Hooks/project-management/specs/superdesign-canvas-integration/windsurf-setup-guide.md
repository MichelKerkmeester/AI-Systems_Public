# Windsurf + Superdesign Setup Guide

## Prerequisites
- Windsurf IDE installed
- Claude Code CLI configured
- Project repository cloned

## Step 1: Install Superdesign in Windsurf

### Option A: Via Marketplace (Recommended)
1. Open Windsurf IDE
2. Press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux)
3. Search for "Superdesign"
4. Click "Install"
5. Reload Windsurf when prompted

### Option B: Via Command Palette
1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
2. Type: `Extensions: Install Extensions`
3. Search: "Superdesign"
4. Install and reload

## Step 2: Configure Superdesign

### Initial Setup
1. After installation, Superdesign icon appears in sidebar
2. Click the Superdesign icon
3. If prompted for API key:
   - Use your existing Claude API key
   - Or continue without (for viewing only)

### Project Configuration
1. Superdesign auto-creates `.superdesign/` folder
2. Verify structure:
   ```
   .superdesign/
   ├── design_iterations/    # Your designs go here
   ├── moodboard/           # Reference images
   └── design_system/       # Design tokens
   ```

## Step 3: Test Integration

### Generate Test Design
```bash
# In terminal (Claude Code)
echo '<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">Test Design</h1>
        <p class="text-gray-600">If you see this in Superdesign canvas, integration works!</p>
    </div>
</body>
</html>' > .superdesign/design_iterations/design_1.html
```

### Verify in Windsurf
1. Open Superdesign panel (sidebar icon)
2. Should see "Test Design" in canvas
3. Try zoom/pan controls
4. Test grid/hierarchy view toggle

## Step 4: Claude Code Commands Setup

### Create Design Command
```bash
# Create command file
mkdir -p .claude/logic/commands
cat > .claude/logic/commands/design.py << 'EOF'
#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime

def setup_design_directory():
    """Ensure .superdesign directory structure exists"""
    dirs = [
        ".superdesign",
        ".superdesign/design_iterations",
        ".superdesign/moodboard",
        ".superdesign/design_system"
    ]
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)

def get_next_design_number():
    """Get the next available design number"""
    iterations_dir = ".superdesign/design_iterations"
    if not os.path.exists(iterations_dir):
        return 1
    
    existing = [f for f in os.listdir(iterations_dir) 
                if f.startswith("design_") and f.endswith(".html")]
    
    if not existing:
        return 1
    
    numbers = []
    for f in existing:
        try:
            # Extract number from design_X.html or design_X_Y.html
            base = f.replace("design_", "").replace(".html", "")
            num = int(base.split("_")[0])
            numbers.append(num)
        except:
            continue
    
    return max(numbers) + 1 if numbers else 1

def generate_design(prompt, style="default"):
    """Generate a design and save it in Superdesign format"""
    setup_design_directory()
    next_num = get_next_design_number()
    
    # This is where Claude Code would generate the design
    # For now, we'll create a template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Design {next_num}: {prompt}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen p-8">
    <div class="max-w-6xl mx-auto">
        <!-- Generated: {datetime.now().isoformat()} -->
        <!-- Prompt: {prompt} -->
        <!-- Style: {style} -->
        <div class="bg-white rounded-lg shadow-lg p-8">
            <h1 class="text-3xl font-bold text-gray-900 mb-4">Design {next_num}</h1>
            <p class="text-gray-600 mb-6">Prompt: {prompt}</p>
            <div class="border-2 border-dashed border-gray-300 rounded-lg p-12 text-center">
                <p class="text-gray-500">AI-generated design will appear here</p>
                <p class="text-sm text-gray-400 mt-2">Style: {style}</p>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    filename = f".superdesign/design_iterations/design_{next_num}.html"
    with open(filename, 'w') as f:
        f.write(html_content)
    
    print(f"✅ Generated: {filename}")
    print(f"📋 Open Windsurf to see the design in Superdesign canvas")
    
    return filename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python design.py <prompt> [style]")
        sys.exit(1)
    
    prompt = sys.argv[1]
    style = sys.argv[2] if len(sys.argv) > 2 else "default"
    
    generate_design(prompt, style)
EOF

chmod +x .claude/logic/commands/design.py
```

### Add Alias for Easy Access
```bash
# Add to your shell profile (.zshrc or .bashrc)
echo 'alias cc-design="python .claude/logic/commands/design.py"' >> ~/.zshrc
source ~/.zshrc
```

## Step 5: Workflow Examples

### Basic Design Generation
```bash
# Generate a hero section
cc-design "hero section with gradient background"

# Generate with specific style
cc-design "pricing cards" "minimal"
```

### Batch Generation Script
```bash
# Create batch script
cat > .claude/logic/commands/design-batch.sh << 'EOF'
#!/bin/bash
PROMPT="$1"
STYLES=("minimal" "bold" "playful" "corporate" "modern")

for style in "${STYLES[@]}"; do
    python .claude/logic/commands/design.py "$PROMPT" "$style"
    sleep 1  # Give Windsurf time to update
done
EOF

chmod +x .claude/logic/commands/design-batch.sh
```

## Troubleshooting

### Superdesign Not Showing Designs
1. Check `.superdesign/` directory exists
2. Verify files are in `design_iterations/` subfolder
3. Restart Windsurf
4. Check Superdesign panel is open

### Canvas Not Updating
1. Click refresh button in Superdesign
2. Check file permissions
3. Ensure valid HTML structure
4. Try manual refresh: `Cmd+R` / `Ctrl+R`

### Performance Issues
1. Limit designs to ~50 per session
2. Archive old designs regularly
3. Use smaller viewport for many designs
4. Close unused design files

## Best Practices

### File Organization
```
.superdesign/
├── design_iterations/
│   ├── archive/              # Move old designs here
│   ├── design_1.html         # Active designs
│   └── design_1_1.html       # Iterations
├── moodboard/
│   └── inspiration_1.png     # Reference images
└── design_system/
    └── tokens.json           # Shared design tokens
```

### Naming Conventions
- Base designs: `design_[number].html`
- Iterations: `design_[number]_[iteration].html`
- Themes: `design_[number]_[theme].html`
- Components: `component_[name]_[variant].html`

### Git Integration
```gitignore
# Add to .gitignore
.superdesign/design_iterations/archive/
.superdesign/moodboard/
.superdesign/.cache/

# Keep these
# .superdesign/design_iterations/
# .superdesign/design_system/
```

## Next Steps
1. ✅ Installation complete
2. ✅ Test design generated
3. 🎯 Start creating with `cc-design "your prompt"`
4. 🎨 Iterate in Windsurf's Superdesign canvas
5. 🚀 Build your design system