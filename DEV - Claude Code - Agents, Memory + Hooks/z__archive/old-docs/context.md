# /context - Context Management

## Purpose
Monitor and manage conversation context freshness for optimal performance.

## Usage
- `/context` - Check current status
- `/context [subcommand]` - Specific action
- `/c` - Short alias

## Subcommands
- **status** - Detailed context report
- **refresh** - Smart context refresh
- **checkpoint** - Force save current state
- **export** - Generate portable session

## Quick Access
- `/context-status` or `/cs`
- `/context-refresh` or `/cr`
- `/context-checkpoint` or `/cc`
- `/context-export` or `/ce`

## Staleness Scoring (0-120+ points)
- 🟢 **0-49**: Fresh context
- 🟡 **50-79**: Aging context
- 🟠 **80-119**: Stale, refresh recommended
- 🔴 **120+**: Critical, must refresh

## Point System
- File edit: +3 points
- New file: +5 points
- Error: +10 points
- Time: +2 points/hour
- Major refactor: +15 points

## Behavior
1. Calculate current staleness score
2. Show visual health indicator
3. Recommend action based on score
4. Perform smart refresh if needed
5. Update checkpoint after significant work