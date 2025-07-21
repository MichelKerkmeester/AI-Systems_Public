# DesktopCommanderMCP Setup Instructions

**Note:** DesktopCommanderMCP is an optional enhancement for Claude Desktop app users. If you're using Claude Code CLI (which this project uses), this component is not required for full functionality.

## Installation Status
✅ **Completed**: Added to `.claude.json` configuration

## Next Steps (Only if using Claude Desktop App)

### 1. Verify Installation
After restarting Claude Desktop app, verify DesktopCommanderMCP is loaded:
- Check if Desktop Commander tools appear in available tools
- Look for tools like `start_process`, `edit_block`, `search_code`, etc.

### 2. Configure Security Settings
Run these configuration commands to secure DesktopCommanderMCP:

```javascript
// Restrict to project directory only
set_config_value({ 
  "key": "allowedDirectories", 
  "value": ["/Users/michel_kerkmeester/AI & Dev/Websites/• anobel.nl"] 
})

// Set default shell for macOS
set_config_value({ 
  "key": "defaultShell", 
  "value": "/bin/zsh" 
})

// Set file operation limits
set_config_value({ 
  "key": "fileWriteLineLimit", 
  "value": 100 
})

// Disable telemetry
set_config_value({ 
  "key": "telemetryEnabled", 
  "value": false 
})
```

### 3. Test Core Features
Test each major capability:

1. **Process Management**
   ```javascript
   // Start a simple process
   start_process({ "command": "echo 'Hello from Desktop Commander'" })
   
   // List processes
   list_processes()
   ```

2. **Code Search (Ripgrep)**
   ```javascript
   // Search for hook patterns
   search_code({ 
     "pattern": "HookBase",
     "directory": ".claude/logic",
     "include": "*.py"
   })
   ```

3. **File Operations**
   ```javascript
   // Test edit_block for precise edits
   edit_block({
     "file_path": "test.txt",
     "search_content": "old text",
     "new_content": "new text"
   })
   ```

4. **Audit Logging**
   ```javascript
   // Check usage statistics
   get_usage_stats()
   ```

### 4. Integration Points for WP1

DesktopCommanderMCP will enhance our hook infrastructure with:

1. **Process Monitoring**: 
   - `start_process` for hook execution with real-time output
   - `read_process_output` for streaming hook results
   - `get_usage_stats` for performance tracking

2. **Advanced Search**:
   - `search_code` with ripgrep for instant pattern matching
   - Faster than Grep tool for security scanning

3. **Surgical Edits**:
   - `edit_block` for precise code modifications
   - Better than Edit tool for auto-fixes

4. **In-Memory Execution**:
   - Run Python/Node.js code without creating files
   - Perfect for analysis and validation

## Benefits for Command Refactoring

- **Hook Performance**: Monitor execution times in real-time
- **Security Scanning**: Instant API key detection with ripgrep
- **Auto-Fixes**: Precise edits without full file rewrites
- **Parallel Execution**: Process management for concurrent hooks
- **Audit Trail**: Automatic logging of all operations

## WP1 Implementation Plan

With DesktopCommanderMCP installed, we can now:

1. Create enhanced hook infrastructure with process monitoring
2. Implement priority queue with real-time execution tracking
3. Add performance metrics to all hooks
4. Enable parallel hook execution
5. Implement auto-fix capabilities for violations

Ready to proceed with WP1 after restart and configuration!