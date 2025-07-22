# Code Reuse State Management

This directory contains the state management and configuration files for the code reuse system.

## Files

### 1. `code_reuse_state.json`
Tracks operational metrics and system state:
- **Statistics**: Files analyzed, duplicates found, consolidations completed
- **Performance Metrics**: Analysis time, cache hit rates, memory usage
- **Historical Data**: Daily/weekly/monthly trends for reporting
- **Feature Flags**: Control system behavior and gradual feature rollout
- **Cache**: In-memory cache for performance optimization

### 2. `reuse_patterns.json`
Maintains discovered patterns and learning data:
- **Discovered Patterns**: Code patterns found during analysis
- **Pattern Usage**: Frequency and effectiveness tracking
- **Reuse Strategies**: Success rates for different approaches
- **Component Catalog**: Registry of reusable components
- **Learning Data**: Successful/failed consolidation attempts

### 3. `compliance_rules.json`
Defines enforcement rules and configurations:
- **Severity Levels**: Critical, High, Medium, Low with auto-fix policies
- **Threshold Configurations**: Duplication, complexity, performance limits
- **Allowed Exceptions**: File patterns and rules that can be bypassed
- **Custom Rules**: Webflow-specific, project-specific, and quality rules
- **Enforcement Modes**: Development, staging, production configurations

### 4. `state_manager.py`
Python module for managing state files:
- Atomic writes to prevent corruption
- Thread-safe operations with locks
- In-memory caching for performance
- Automatic backups and recovery
- State migration support

## Usage

```python
from .claude.logic.state.code_reuse import get_state_manager

# Get singleton instance
manager = get_state_manager()

# Read state
stats = manager.get_statistics()
flags = manager.get_feature_flags()
rules = manager.get_compliance_rules()

# Update state
manager.increment_counter('code_reuse_state', ['statistics', 'files_analyzed'])
manager.set_feature_flag('auto_consolidation_enabled', True)

# Update nested values
manager.update_nested('code_reuse_state', ['performance_metrics', 'cache_hit_rate'], 0.85)

# Append to lists with size limits
manager.append_to_list('code_reuse_state', ['historical_data', 'daily_metrics'], {
    'date': '2025-07-21',
    'files_analyzed': 150,
    'duplicates_found': 23
}, max_items=30)
```

## State File Versions

All state files include a `version` field for migration support:
- Current version: `1.0.0`
- Migrations are applied automatically when loading older versions
- Backups are created before migrations

## Feature Flags

Control system behavior through feature flags:
- `auto_consolidation_enabled`: Automatically consolidate duplicate code
- `pattern_learning_enabled`: Learn from successful consolidations
- `aggressive_deduplication`: Use stricter duplicate detection
- `real_time_analysis`: Analyze files as they're edited
- `cross_project_analysis`: Look for patterns across projects
- `ai_suggestions_enabled`: Provide AI-powered suggestions
- `webhook_notifications`: Send notifications to external services
- `performance_mode`: "balanced", "fast", or "thorough"

## Compliance Modes

Different enforcement levels for different environments:
- **Development**: Auto-fix enabled, non-blocking, learning mode
- **Staging**: Auto-fix enabled, blocks on critical, no learning
- **Production**: No auto-fix, blocks on critical, no suggestions

## Backup and Recovery

- Automatic backups on every save
- Last 10 backups kept per state file
- Automatic recovery from latest backup on corruption
- Manual export with `manager.export_state(output_dir)`

## Thread Safety

All operations are thread-safe:
- File-level locks prevent concurrent modifications
- Atomic writes using temporary files and rename
- In-memory cache with timestamps for consistency