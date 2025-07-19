# How Automation Works

## Table of Contents

- [Automation Levels](#automation-levels)
  - [🔴 Off](#-off)
  - [🔵 Manual](#-manual)
  - [🟡 Semi-Auto (Default)](#-semi-auto-default)
  - [🟢 Full Auto](#-full-auto)
- [Automation Flow](#automation-flow)
  - [1. Event Detection](#1-event-detection)
  - [2. Pattern Recognition](#2-pattern-recognition)
    - [Critical Patterns (Always Auto)](#critical-patterns-always-auto)
    - [Important Patterns (Semi/Full Auto)](#important-patterns-semifull-auto)
  - [3. Automated Actions](#3-automated-actions)
    - [Session Management](#session-management)
    - [Memory Capture](#memory-capture)
    - [Pattern Extraction](#pattern-extraction)
    - [Quality Enforcement](#quality-enforcement)
    - [Mode Suggestions](#mode-suggestions)
- [Smart Triggers](#smart-triggers)
  - [Context-Based Triggers](#context-based-triggers)
  - [Time-Based Triggers](#time-based-triggers)
  - [Threshold Triggers](#threshold-triggers)
- [Automation Benefits](#automation-benefits)
  - [1. Consistency](#1-consistency)
  - [2. Efficiency](#2-efficiency)
  - [3. Intelligence](#3-intelligence)
  - [4. Recovery](#4-recovery)
- [Customizing Automation](#customizing-automation)
  - [Global Settings](#global-settings)
  - [Per-Hook Settings](#per-hook-settings)
  - [Override Mechanisms](#override-mechanisms)
- [Monitoring Automation](#monitoring-automation)
  - [Status Commands](#status-commands)
  - [Activity Tracking](#activity-tracking)
  - [Performance Impact](#performance-impact)
- [Best Practices](#best-practices)
  - [1. Start with Semi-Auto](#1-start-with-semi-auto)
  - [2. Review Captures](#2-review-captures)
  - [3. Customize Gradually](#3-customize-gradually)
  - [4. Emergency Preparedness](#4-emergency-preparedness)
- [Future Automation](#future-automation)
## Automation Levels

### 🔴 Off
- No automatic capture or execution
- All features require manual commands
- Use when: Maximum control needed

### 🔵 Manual  
- Automation available but requires confirmation
- Prompts before taking actions
- Use when: Learning the system

### 🟡 Semi-Auto (Default)
- Critical patterns captured automatically
- Non-critical patterns prompt for confirmation
- Balanced automation and control
- Use when: Normal development

### 🟢 Full Auto
- All patterns captured automatically
- No confirmation prompts
- Maximum efficiency
- Use when: Trusted environment

Set level with: `/memory auto [level]`

## Automation Flow

### 1. Event Detection
```
User Action → Event Triggered → Hooks Activated
```

Examples:
- Submit prompt → UserPromptSubmit → Context loading
- Edit file → PostToolUse → Quality checks
- 4 hours pass → PreToolUse → New session

### 2. Pattern Recognition

#### Critical Patterns (Always Auto)
- `DECISION:` → Architecture decisions
- `SECURITY:` → Security updates  
- `BREAKING:` → Breaking changes
- API key detection → Security alert
- Production keywords → Strict mode

#### Important Patterns (Semi/Full Auto)
- `RESOLVED:` → Bug fixes
- `PATTERN:` → Code patterns
- `OPTIMIZATION:` → Performance improvements
- Client preferences → Requirements
- Technical limits → Constraints

### 3. Automated Actions

#### Session Management
- **Trigger**: 4-hour timeout or session limit
- **Action**: Create new session, archive old
- **Result**: Organized work history

#### Memory Capture
- **Trigger**: Pattern detection in conversation
- **Action**: Extract and store in Graphiti
- **Result**: Persistent knowledge

#### Pattern Extraction
- **Trigger**: Significant code changes
- **Action**: Update knowledge JSON files
- **Result**: Maintained conventions

#### Quality Enforcement
- **Trigger**: Multiple file edits
- **Action**: Suggest testing, scan for issues
- **Result**: Consistent code quality

#### Mode Suggestions
- **Trigger**: Task complexity analysis
- **Action**: Recommend optimal mode
- **Result**: Appropriate safeguards

## Smart Triggers

### Context-Based Triggers
```python
if branch == "main" and files_changed > 5:
    suggest_strict_mode()

if pattern_matches("security|production|api"):
    enable_enhanced_checks()

if task_complexity > threshold:
    activate_sequential_thinking()
```

### Time-Based Triggers
- Session timeout after 4 hours
- Pattern extraction every 100 lines
- Cleanup old sessions after 10 accumulated

### Threshold Triggers
- Test reminder after 3 files changed
- Full test suite after 5 files
- Memory context on 5+ keyword matches

## Automation Benefits

### 1. Consistency
- Same patterns always handled same way
- No missed security checks
- Uniform documentation

### 2. Efficiency  
- No manual command typing
- Parallel processing
- Automatic organization

### 3. Intelligence
- Learns from patterns
- Adapts to context
- Prevents mistakes

### 4. Recovery
- Automatic crash recovery
- State persistence
- Cleanup mechanisms

## Customizing Automation

### Global Settings
```json
{
  "hooks": {
    "enabled": true
  },
  "memory": {
    "auto_context": true,
    "automation_level": "semi"
  }
}
```

### Per-Hook Settings
Each hook can have individual configuration:
- Thresholds
- Patterns
- Exclusions
- Behavior

### Override Mechanisms
1. **Temporary disable**: `CLAUDE_HOOKS_DISABLED=1`
2. **Specific hook**: `/logic hooks disable [name]`
3. **Emergency**: `/logic emergency disable`
4. **Mode override**: Respond to mode suggestions

## Monitoring Automation

### Status Commands
```bash
/logic hooks status      # Active hooks
/memory                  # Automation level
/logic metrics          # Performance stats
/save stats            # Session statistics
```

### Activity Tracking
- Session files record all actions
- Memory stats show capture rates
- Hook logs available with `--debug`

### Performance Impact
- Hooks: < 100ms average
- Memory operations: < 200ms
- Pattern extraction: < 500ms
- Negligible overhead

## Best Practices

### 1. Start with Semi-Auto
- Good balance of automation and control
- Learn what gets automated
- Adjust based on comfort

### 2. Review Captures
- Check `/memory` periodically
- Verify pattern extraction
- Ensure quality matches expectations

### 3. Customize Gradually
- Use defaults initially
- Adjust thresholds based on experience
- Create custom patterns as needed

### 4. Emergency Preparedness
- Know emergency commands
- Understand override mechanisms
- Keep backups of important state

## Future Automation

Planned enhancements:
- AI-driven pattern learning
- Predictive command suggestions
- Cross-project knowledge sharing
- Team automation profiles