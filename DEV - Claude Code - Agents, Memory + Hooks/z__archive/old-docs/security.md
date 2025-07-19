# /security - API Key & Secret Scanner

## Purpose
Detect and prevent API keys, tokens, and secrets from being stored in `.claude` folders.

## Usage
- `/security` or `/sec` - Interactive security menu
- `/security scan` - Deep scan all .claude files
- `/security fix` - Auto-redact found keys
- `/security patterns` - Show detection patterns

## Detection Patterns
### High Risk (Auto-Block)
- OpenAI: `sk-[A-Za-z0-9]{48}`
- Google: `AIza[A-Za-z0-9]{35}`
- AWS: `AKIA[0-9A-Z]{16}`
- GitHub: `ghp_[A-Za-z0-9]{36}`
- Stripe: `(sk|pk)_(test|live)_[A-Za-z0-9]{24}`

### Medium Risk (Warning)
- Generic: `[A-Za-z0-9]{32,}` (32+ chars)
- Bearer: `Bearer [A-Za-z0-9\-._~+/]+=*`
- Base64: `[A-Za-z0-9+/]{40,}={0,2}`
- UUID: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

### Keywords (Context Check)
- `api_key`, `apikey`, `api-key`
- `secret`, `token`, `password`
- `private_key`, `access_token`
- `client_secret`, `auth_token`

## Scan Behavior
1. **Pre-Write Protection**: Blocks file writes containing keys
2. **Session Scanning**: Checks all markdown in `.claude/project/sessions/`
3. **Knowledge Scanning**: Validates JSON in `.claude/project/knowledge/`
4. **Memory Scanning**: Reviews captures in `.claude/logic/memory/`

## Security Actions
### On Detection
```
🚨 SECURITY ALERT: API Key Detected!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: [OpenAI/Google/AWS/etc]
File: [path/to/file]
Line: [line number]
Pattern: [matched pattern]

Action Required:
1. Move to .env file
2. Use environment variable
3. Reference by name only
```

### Auto-Fixes
- Replace with `[REDACTED_API_KEY]`
- Add to `.env.example` template
- Update code to use `process.env.KEY_NAME`

## Integration
- Runs automatically with `/test security`
- Pre-commit hook via git
- Memory capture validation
- Response filtering

## Safe Storage Guide
```bash
# Good: .env file (gitignored)
OPENAI_API_KEY=sk-xxxxx
GOOGLE_API_KEY=AIzaxxxxx

# Bad: In code or docs
const key = "sk-xxxxx" # BLOCKED
```

## Command Flow
1. User runs `/security scan`
2. Scan all .claude directories
3. Generate security report
4. Offer fix options
5. Log to audit trail