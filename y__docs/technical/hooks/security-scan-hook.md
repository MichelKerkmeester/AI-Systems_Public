# Security Scan Hook

## Overview

**Hook Name**: Security Scan Hook  
**Purpose**: Blocks operations containing sensitive information like API keys  
**Location**: `/hooks/core/security-scan-hook.py`  
**Triggers**: PostToolUse (Edit/Write/Bash operations)  
**Priority**: 1 (Critical - highest priority)  
**Performance**: ~10ms typical execution time

## Description

The Security Scan Hook is a critical safety mechanism that prevents accidental exposure of sensitive information. It scans all file operations and bash commands for API keys, passwords, tokens, and other secrets, blocking operations that could compromise security.

## Configuration

Settings file: `/hooks/core/security-settings.json`

```json
{
  "enabled": true,
  "block_on_detection": true,
  "scan_patterns": {
    "api_keys": true,
    "passwords": true,
    "tokens": true,
    "private_keys": true,
    "connection_strings": true
  },
  "whitelist_patterns": [],
  "custom_patterns": [],
  "severity_threshold": "medium"
}
```

## How It Works

1. **Intercepts Operations**:
   - Monitors all Write/Edit/MultiEdit operations
   - Scans Bash commands before execution
   - Checks file paths for sensitive names

2. **Pattern Detection**:
   - Regex patterns for common secret formats
   - Entropy analysis for random strings
   - Keyword detection for secret names

3. **Blocking Mechanism**:
   - Prevents operation execution
   - Shows clear security warning
   - Provides remediation guidance

4. **Logging**:
   - Records blocked operations
   - Maintains security audit trail
   - No actual secrets logged

## Security Patterns

### API Key Formats
```python
patterns = {
    "aws": r"AKIA[0-9A-Z]{16}",
    "github": r"ghp_[a-zA-Z0-9]{36}",
    "openai": r"sk-[a-zA-Z0-9]{48}",
    "stripe": r"sk_(?:test_|live_)[a-zA-Z0-9]{24}",
    "google": r"AIza[0-9A-Za-z\-_]{35}"
}
```

### Generic Patterns
- High entropy strings (>4.5)
- `password=`, `api_key=`, `secret=`
- Private key headers
- Connection strings with credentials

## Example Usage

### Blocked Operation
```bash
User attempts: git commit -m "Add config" 

File contains: api_key = "sk-1234567890abcdef..."

🛡️ SECURITY ALERT: Operation Blocked

Detected: OpenAI API Key
File: config.py
Line: 42

This operation would expose sensitive credentials.

Recommended Actions:
1. Use environment variables: os.getenv('OPENAI_API_KEY')
2. Add to .gitignore: echo "config.py" >> .gitignore
3. Use secret management: Consider using a .env file

To proceed safely:
- Remove the sensitive data
- Use secure configuration methods
- Re-run your command
```

## Integration Points

- **Quality Hook**: Coordinates for security in code quality
- **Git Operations**: Special handling for commits
- **Memory System**: Never stores detected secrets
- **Task Management**: Security violations tracked

## Performance Considerations

- Optimized regex compilation (~10ms scan time)
- Streaming scan for large files
- Early exit on first detection
- Minimal memory footprint

## Advanced Features

### Custom Pattern Addition
```json
{
  "custom_patterns": [
    {
      "name": "internal_api",
      "pattern": "INT_API_[A-Z0-9]{32}",
      "severity": "high",
      "message": "Internal API key detected"
    }
  ]
}
```

### Whitelist Configuration
```json
{
  "whitelist_patterns": [
    "test_api_key_example",
    "documentation/examples/*"
  ]
}
```

### Severity Levels
- **Critical**: Blocks immediately (private keys, passwords)
- **High**: Blocks with override option (API keys)
- **Medium**: Warning only (potential secrets)
- **Low**: Logged only (informational)

## Troubleshooting

### False Positives
- Add to whitelist patterns
- Adjust entropy threshold
- Use inline comments: `# safe-to-commit`

### Missed Secrets
- Add custom patterns
- Lower entropy threshold
- Enable deep scan mode

### Performance Impact
- Exclude large binary files
- Limit scan depth
- Use async scanning

## Security Best Practices

### Recommended Approach
```python
# Bad - Hardcoded secret
api_key = "sk-abc123..."

# Good - Environment variable
api_key = os.getenv('API_KEY')

# Better - Secret management
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')
```

### Git Safety
```bash
# Add sensitive files to .gitignore
echo "*.env" >> .gitignore
echo "config/secrets.py" >> .gitignore

# Remove from history if committed
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch config.py" \
  --prune-empty --tag-name-filter cat -- --all
```

## Emergency Procedures

### If Secret Is Exposed
1. **Revoke immediately** - Generate new credentials
2. **Scan history** - Check all commits
3. **Update systems** - Deploy new credentials
4. **Document incident** - For security audit

### Override (Use Carefully)
```bash
# Temporary disable for specific operation
CLAUDE_SECURITY_OVERRIDE=true <command>

# Must re-enable immediately after
```

## Audit Trail

Security events logged to:
- `.claude/logs/security-scan.log`
- Includes timestamp, operation, detection type
- No actual secrets logged
- Useful for compliance

## Related Documentation

- [Security Best Practices](../../security/best-practices.md)
- [Git Safety Guide](../../git/security.md)
- [Environment Configuration](../../setup/environment.md)