# Intelligence & Enhancement Modules

This directory contains intelligent modules that enhance Claude Code's capabilities through hooks and automated processing.

## 📁 Directory Structure

```
agents/
├── intelligence/          # Enhancement and integration modules
│   ├── prompt_enhancer.py      # Claude-Organizer prompt enhancement
│   ├── pattern_library.py      # Pattern matching for prompts
│   ├── graphiti_memory_integration.py  # Memory system integration
│   ├── sequential_thinking_integration.py  # Thinking tool integration
│   └── conflict_resolution.py  # Conflict handling utilities
└── clients/              # (Empty - previously contained API clients)
```

## 🧠 Intelligence Modules

### prompt_enhancer.py
The Claude-Organizer integration that enhances every prompt with:
- Two-pass enhancement (best practices + project rules)
- CLAUDE.md rule injection
- Context-aware improvements
- Pattern matching capabilities

### pattern_library.py
Pattern matching and learning system for common request types:
- Bug fix patterns
- Feature request patterns
- Documentation patterns
- Performance optimization patterns
- Success tracking and adaptation

### graphiti_memory_integration.py
Integration with the Graphiti memory system for:
- Long-term memory storage
- Context retrieval
- Knowledge graph operations
- Memory search capabilities

### sequential_thinking_integration.py
Integration with Sequential Thinking MCP for:
- Complex reasoning tasks
- Step-by-step problem solving
- Thought tracking
- Synthesis generation

### conflict_resolution.py
Utilities for handling conflicts in:
- Code merges
- Pattern matching
- Memory updates
- Enhancement suggestions

## 🚀 Usage

These modules work automatically through the hook system. They are invoked by:
- The prompt enhancement hook (`/logic/hooks/core/prompt-enhancement-hook.py`)
- Memory context hooks
- Other system hooks as needed

No direct commands are needed - the modules enhance Claude Code's capabilities behind the scenes.

## 🔧 Configuration

Module behavior is controlled through:
- `.claude/settings.json` - Hook configuration
- `.claude/logic/hooks/core/prompt-enhancement-settings.json` - Enhancement settings
- Individual module configuration files

## 📝 History

This directory previously contained a multi-agent orchestration system with external LLM clients (Kimi, Gemini, OpenRouter). That system has been removed in favor of:
- The Task tool in Claude Code for parallel execution
- MCP servers for specialized capabilities
- Hook-based automation for background processing

The focus is now on intelligence and enhancement rather than multi-agent coordination.