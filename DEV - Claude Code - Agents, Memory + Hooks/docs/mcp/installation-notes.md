# MCP Installation Notes

## Installed MCPs

### 1. claude-code-kimi-groq
- **Location**: `~/mcp-servers/claude-code-kimi-groq/`
- **Purpose**: Use Kimi K2 model through Groq API
- **Status**: Added to ~/.claude.json

**Setup Required**:
```bash
cd ~/mcp-servers/claude-code-kimi-groq
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

**Environment Variables Needed**:
- `GROQ_API_KEY`: Get from https://console.groq.com/

### 2. claude-gemini-mcp-slim
- **Location**: `~/mcp-servers/claude-gemini-mcp-slim/`
- **Purpose**: Lightweight Gemini AI integration
- **Status**: Added to ~/.claude.json

**Setup Required**:
```bash
cd ~/mcp-servers/claude-gemini-mcp-slim
pip install -r requirements.txt
```

**Environment Variables Needed**:
- `GOOGLE_API_KEY`: Get from https://makersuite.google.com/app/apikey

## Configuration Added

Both MCPs have been added to `~/.claude.json`:

```json
"claude-code-kimi-groq": {
  "command": "/Users/michel_kerkmeester/mcp-servers/claude-code-kimi-groq/.venv/bin/python",
  "args": ["/Users/michel_kerkmeester/mcp-servers/claude-code-kimi-groq/proxy.py"],
  "env": {
    "GROQ_API_KEY": "YOUR_GROQ_API_KEY"
  }
},
"claude-gemini-mcp-slim": {
  "command": "python3",
  "args": ["/Users/michel_kerkmeester/mcp-servers/claude-gemini-mcp-slim/gemini_helper.py"],
  "env": {
    "GOOGLE_API_KEY": "YOUR_GOOGLE_API_KEY",
    "GEMINI_PRO_MODEL": "gemini-2.5-pro",
    "GEMINI_FLASH_MODEL": "gemini-2.5-flash"
  }
}
```

## Model Configuration

- **Kimi**: Already uses the best model - `moonshotai/kimi-k2-instruct` (hardcoded in proxy.py)
- **Gemini**: Configured to ONLY use Gemini 2.5 Pro for ALL queries (Flash model disabled)
  - Both `GEMINI_PRO_MODEL` and `GEMINI_FLASH_MODEL` set to `gemini-2.5-pro`
  - `FORCE_PRO_MODEL=true` ensures Pro model is always used
  - Created `force_pro_model.py` wrapper to override any task-based model selection

## Next Steps

1. **Get API Keys**:
   - Groq API: https://console.groq.com/
   - Google API: https://makersuite.google.com/app/apikey

2. **Install Dependencies**:
   ```bash
   # For kimi-groq
   cd ~/mcp-servers/claude-code-kimi-groq
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .

   # For gemini-slim
   cd ~/mcp-servers/claude-gemini-mcp-slim
   pip install -r requirements.txt
   ```

3. **Update API Keys**:
   Edit `~/.claude.json` and replace:
   - `YOUR_GROQ_API_KEY` with actual Groq API key
   - `YOUR_GOOGLE_API_KEY` with actual Google API key

4. **Restart Claude Code** to load the new MCPs

## Notes
- Both MCPs require their dependencies to be installed before use
- API keys must be valid for the MCPs to function
- The kimi-groq MCP runs as a proxy server
- The gemini-slim MCP provides direct Gemini integration