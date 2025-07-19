# /mode - Operation Mode Management

## Purpose
Adaptive behavior switching based on work context and requirements with intelligent suggestions.

## Usage
- `/mode` - Show current mode status and statistics
- `/mode [mode]` - Switch to specific mode (strict/auto/hybrid)
- `/mode suggest [query]` - Analyze query for mode recommendation
- `/mode auto on|off` - Toggle automatic mode suggestions
- `/mode manual` - Disable mode enforcement (suggestions only)
- `/mode status` - Detailed mode report with history
- `/m` - Short alias

## Available Modes
### 🔒 Strict Mode
- **Validation**: Maximum, aborts on warnings
- **Checkpoints**: After every action
- **Context refresh**: Every 50 points
- **Commands**: Focus on /test, /security, /context
- **Use for**: Production, critical fixes, security

### 🚀 Auto Mode (Default)
- **Validation**: Standard with auto-fixes
- **Checkpoints**: Smart triggers
- **Context refresh**: Every 120 points
- **Commands**: All commands available
- **Use for**: Regular development, features

### ⚖️ Hybrid Mode
- **Validation**: Balanced approach
- **Checkpoints**: At milestones only
- **Context refresh**: Every 80 points
- **Commands**: Balance safety and features
- **Use for**: Large refactors, complex work

## Quick Access
- `/mode-strict` or `/ms`
- `/mode-auto` or `/ma`
- `/mode-hybrid` or `/mh`

## Auto-Detection & Suggestions
The system analyzes every query for:
- Main/master branch → Suggests strict mode
- 10+ files modified → Suggests hybrid mode
- Keywords "production", "deploy", "security" → Suggests strict mode
- Testing/validation queries → Suggests strict mode
- Feature branches → Suggests auto mode

## Mode-Aware Commands
Commands adapt behavior based on current mode:
- **/test**: Stricter validation in strict mode
- **/workflow**: Limited phases in strict mode
- **/context**: Lower staleness thresholds in strict mode
- **/memory**: More aggressive capture in strict mode
- **/security**: Always runs at strict level

## Visual Indicators
Every response includes mode status:
```
[🚀 Mode: Auto | Suggested: 🔒 Strict (production branch)]
[Available: /test /workflow /security /memory /context]
```

## Behavior
1. Analyze query and context automatically
2. Suggest appropriate mode with reason
3. Wait for approval before switching (unless manual mode)
4. Adapt all commands to current mode
5. Show mode status in all responses