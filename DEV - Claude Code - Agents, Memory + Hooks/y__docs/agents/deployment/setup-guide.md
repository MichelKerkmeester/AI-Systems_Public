# Setup Guide

Complete installation and configuration guide for the Multi-Agent System.

## Prerequisites

- Python 3.8+
- Git (for worktree management)
- API keys for AI models
- 4GB+ RAM recommended

## Step 1: Environment Setup

### 1.1 Clone or Navigate to Project
```bash
cd /path/to/anobel.nl
```

### 1.2 Create Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 1.3 Install Dependencies
```bash
pip install -r .claude/agents/requirements.txt
```

Or install manually:
```bash
pip install aiohttp pytest pytest-cov python-dotenv
```

## Step 2: API Configuration

### 2.1 Create .env File
Create `.env` in the project root:
```bash
touch .env
```

### 2.2 Add API Keys
```env
# Google Gemini API (Required for cost savings)
GOOGLE_API_KEY=your_gemini_api_key_here

# Kimi Moonshot API (Currently has auth issues)
KIMI_API_KEY=your_kimi_api_key_here

# Optional: Gemini model selection
GEMINI_SMALL_MODEL=gemini-2.0-flash
```

### 2.3 Verify .gitignore
Ensure `.env` is in `.gitignore`:
```bash
grep "^\.env$" .gitignore || echo ".env" >> .gitignore
```

## Step 3: MCP Configuration

### 3.1 Install claude-code-router MCP
Edit `~/.claude.json`:
```json
{
  "mcpServers": {
    "claude-code-router": {
      "command": "npx",
      "args": ["-y", "claude-code-router"],
      "env": {
        "KIMI_API_KEY": "your_kimi_api_key_here"
      }
    }
  }
}
```

### 3.2 Verify MCP Installation
```bash
npx claude-code-router --version
```

## Step 4: System Configuration

### 4.1 Router Configuration
Edit `.claude/agents/configs/router-config.json`:
```json
{
  "complexity_thresholds": {
    "trivial_max": 2,
    "simple_max": 6,
    "medium_max": 12,
    "complex_max": 17
  },
  "model_assignments": {
    "trivial": "kimi-pro",
    "simple": "kimi-pro",
    "medium": "claude-opus-4",
    "complex": "claude-opus-4",
    "critical": "claude-opus-4"
  },
  "agent_model_overrides": {
    "analyst": {
      "primary": "gemini-mcp",
      "fallback": "claude-opus-4"
    },
    "synthesis": {
      "primary": "claude-opus-4",
      "fallback": null
    }
  }
}
```

### 4.2 Orchestrator Configuration
Edit `.claude/agents/configs/orchestrator-config.json`:
```json
{
  "max_agents": 5,
  "synthesis_threshold": 3,
  "auto_synthesis": true,
  "worktree_cleanup": true,
  "worktree_base": "~/.claude/agents/worktrees",
  "message_queue_size": 1000,
  "agent_timeout_seconds": 300
}
```

## Step 5: Verify Installation

### 5.1 Run Test Suite
```bash
cd .claude/agents/tests
./run_tests.py --type unit
```

Expected output:
```
🧪 Running Unit Tests...
============================================================
test_task_analyzer.py::TestTaskComplexityAnalyzer::test_trivial_task_scoring PASSED
test_task_analyzer.py::TestTaskComplexityAnalyzer::test_simple_task_scoring PASSED
...
=================== 25 passed in 2.34s ===================
```

### 5.2 Test API Connections
```bash
python .claude/agents/test_api_integration.py
```

Expected output:
```
🔷 Testing Gemini API...
✅ Gemini API: Connected
   Model: gemini-2.0-flash
   Cost: $0.005/1k input, $0.015/1k output

🟨 Testing Kimi API...
❌ Kimi API Error: 401 Invalid Authentication
```

### 5.3 Test Basic Orchestration
```python
import asyncio
from orchestration import orchestrator_command

async def test():
    result = await orchestrator_command.handle_analyze("Fix typo")
    print(f"Complexity: {result['complexity_level']}")
    print(f"Recommended model: {result['recommended_model']}")

asyncio.run(test())
```

## Step 6: Integration with Claude Code

### 6.1 Command Integration
The system integrates with `/logic agents` commands:
```
/logic agents analyze "task description"
/logic agents orchestrate "task description"
/logic agents status
/logic agents models
```

### 6.2 Direct Python Usage
```python
from orchestration import ParallelOrchestrator
from pathlib import Path

async def run_orchestration():
    orchestrator = ParallelOrchestrator(
        project_root=Path.cwd(),
        max_agents=5
    )
    
    await orchestrator.initialize()
    
    # Add work
    wp_id = await orchestrator.add_work_package(
        "Implement user authentication",
        work_type="feature"
    )
    
    # Execute
    await orchestrator.execute()
    
    # Get results
    report = await orchestrator.get_report()
    print(report)
```

## Step 7: Production Deployment

### 7.1 Performance Tuning
```bash
# Increase Python recursion limit if needed
export PYTHONRECURSIONLIMIT=3000

# Set memory limits
export PYTHON_MEMORY_LIMIT=4G
```

### 7.2 Logging Configuration
```python
# In your code
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('.claude/agents/logs/system.log'),
        logging.StreamHandler()
    ]
)
```

### 7.3 Monitoring Setup
```bash
# Create monitoring script
cat > monitor_agents.sh << 'EOF'
#!/bin/bash
watch -n 1 'ps aux | grep -E "(agent|orchestrat)" | grep -v grep'
EOF

chmod +x monitor_agents.sh
```

## Troubleshooting

### Issue: Kimi API Authentication Error
**Current Status**: Known issue, system falls back to Claude
**Impact**: Reduced cost savings (30-40% instead of 40-50%)
**Workaround**: System remains functional with Gemini savings

### Issue: Import Errors
```bash
# Add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/anobel.nl/.claude/agents"
```

### Issue: Git Worktree Errors
```bash
# Clean up worktrees
git worktree prune
git worktree list
```

### Issue: Memory Errors
Increase agent timeout or reduce max agents in orchestrator config.

## Next Steps

1. Run example orchestrations
2. Monitor cost savings
3. Adjust configurations based on workload
4. Set up continuous monitoring
5. Plan for Kimi API fix

## Support

- Check logs in `.claude/agents/logs/`
- Run diagnostics: `python -m agents.diagnostics`
- Review [troubleshooting guide](troubleshooting.md)