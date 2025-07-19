# 🤖 Multi-Agent System with Intelligent Routing

> Achieve 40-50% cost reduction through intelligent model routing while maintaining quality

## 🚀 Quick Start

Get up and running in 2 minutes:

```bash
# 1. Install dependencies
pip install pytest pytest-cov aiohttp python-dotenv

# 2. Set up API keys in .env
KIMI_API_KEY=your_kimi_key
GOOGLE_API_KEY=your_gemini_key

# 3. Run your first orchestration
python -c "
from orchestration import orchestrator_command
import asyncio
asyncio.run(orchestrator_command.handle_orchestrate('Fix typo in README'))
"
```

## 📚 Table of Contents

- [Architecture Overview](architecture/system-design.md)
- [Installation Guide](deployment/setup-guide.md)
- [API Documentation](api/README.md)
- [Examples](examples/README.md)
- [Troubleshooting](deployment/troubleshooting.md)

## 🎯 Key Features

### 1. **Intelligent Model Routing**
- **Kimi Pro**: Simple tasks (60% cheaper)
- **Gemini**: Analysis tasks (75% cheaper)
- **Claude**: Complex tasks (baseline)

### 2. **Parallel Orchestration**
- Up to 5 agents working simultaneously
- Git worktree isolation prevents conflicts
- Automatic synthesis of results

### 3. **Agent Intelligence**
- Sequential thinking for reasoning
- Shared memory system
- Conflict detection and resolution
- Pattern learning

### 4. **Cost Optimization**
- 30-40% overall cost reduction
- 75% savings on analysis tasks
- Automatic fallback on API failures

## 🏗️ System Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Task Input     │────▶│ Complexity      │────▶│ Model Selector  │
└─────────────────┘     │ Analyzer        │     └─────────────────┘
                        └─────────────────┘              │
                                                         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Parallel        │◀────│ Agent Types     │◀────│ Model APIs      │
│ Orchestrator    │     │ (4 types)       │     │ (3 models)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                                               
         ▼                                               
┌─────────────────┐     ┌─────────────────┐     
│ Intelligence    │────▶│ Final Output    │     
│ Layer           │     │ & Synthesis     │     
└─────────────────┘     └─────────────────┘     
```

## 📊 Performance Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Task Analysis | <50ms | 15ms | ✅ |
| Model Selection | <10ms | 3ms | ✅ |
| Agent Spawn | <2s | 1.5s | ✅ |
| Cost Reduction | 40-50% | 30-40% | ⚠️ |

*Note: Full 40-50% reduction achievable when Kimi API is fixed*

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
./tests/run_tests.py

# Run specific test type
./tests/run_tests.py --type unit
./tests/run_tests.py --type integration
./tests/run_tests.py --type performance

# Run with coverage
./tests/run_tests.py --coverage
```

## 🔧 Configuration

### Model Routing Configuration
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
  }
}
```

### Orchestrator Configuration
Edit `.claude/agents/configs/orchestrator-config.json`:

```json
{
  "max_agents": 5,
  "synthesis_threshold": 3,
  "auto_synthesis": true,
  "worktree_cleanup": true
}
```

## 🛠️ Common Use Cases

### 1. Simple Task (Single Agent)
```python
# Automatically routes to Kimi Pro for 60% savings
/logic agents orchestrate "Update version number in package.json"
```

### 2. Complex Refactoring (Multi-Agent)
```python
# Spawns analyst, developers, reviewer, and synthesis agents
/logic agents orchestrate "Refactor authentication system to use OAuth2"
```

### 3. Deep Analysis (Gemini)
```python
# Routes to Gemini for 75% cost savings
/logic agents orchestrate "Analyze codebase architecture and suggest improvements"
```

## 🚨 Troubleshooting

### Kimi API Authentication Error
Currently experiencing 401 errors with Kimi API. System automatically falls back to Claude.

**Workaround**: System remains functional with 30-40% savings using Gemini for analysis.

### Performance Issues
1. Check agent count: `ps aux | grep agent`
2. Clear worktrees: `git worktree prune`
3. Check logs: `.claude/agents/logs/`

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📈 Roadmap

- [ ] Fix Kimi API authentication
- [ ] Add more model providers (Ollama, Claude Haiku)
- [ ] Implement ML-based pattern recognition
- [ ] Create web dashboard for monitoring
- [ ] Add cross-project memory sharing

## 📄 License

This project is part of the anobel.nl codebase.

---

**Need help?** Check the [troubleshooting guide](deployment/troubleshooting.md) or [open an issue](https://github.com/yourusername/repo/issues).