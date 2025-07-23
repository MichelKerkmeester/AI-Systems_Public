# Agent System Architecture Specification

## Executive Summary
This specification defines a comprehensive multi-agent system that builds upon the existing `.claude` infrastructure to improve quality, speed, and reduce Claude Opus token usage by 85% through intelligent model routing and task delegation.

## Core Architecture Principles

### 1. Hierarchical Agent Structure
```
┌─────────────────────────────────────────────────┐
│              Orchestrator Agent                  │
│            (Claude Opus - Minimal)               │
└─────────────────┬───────────────────────────────┘
                  │
    ┌─────────────┴─────────────┬──────────────┬────────────┬──────────┐
    │                           │              │            │          │
┌───▼────────┐         ┌───────▼──────┐  ┌───▼────┐  ┌────▼─────┐  ┌▼─────┐
│ Analysis   │         │ Implementation│  │ QA     │  │ Doc      │  │Debug │
│ Agent      │         │ Agents       │  │ Agent  │  │ Agent    │  │Agent │
│ (Gemini)   │         │ (Kimi/Opus)  │  │ (Opus) │  │ (Gemini) │  │(Gem) │
└────────────┘         └──────────────┘  └────────┘  └──────────┘  └──────┘
```

### 2. Agent Communication Protocol
- **Message Queue**: Async communication via priority queue
- **Context Sharing**: Shared memory through enhanced MCPBridge
- **Result Aggregation**: Parallel results merged by orchestrator

### 3. Integration Points

#### Memory System Enhancement
```python
class AgentMemoryBridge(MCPBridge):
    """Enhanced memory bridge with agent-specific features"""
    
    def __init__(self):
        super().__init__()
        self.agent_contexts = {}  # Per-agent isolated contexts
        self.shared_memory = {}   # Cross-agent shared data
        
    def delegate_to_agent(self, agent_id: str, task: dict):
        """Delegate task with isolated context"""
        context = self.agent_contexts.get(agent_id, {})
        return self.call_mcp_tool(f"agent_{agent_id}_execute", {
            "task": task,
            "context": context,
            "shared_memory": self.shared_memory
        })
```

#### Hook System Integration
- Extend existing hooks to support agent triggers
- New hook types: `pre-agent-dispatch`, `post-agent-result`
- Agent-aware memory capture patterns

## Agent Types and Responsibilities

### 1. Orchestrator Agent (Claude Opus - Minimal Token Usage)
**Purpose**: Route tasks, aggregate results, make high-level decisions
**Token Optimization**: Only processes summaries and routing logic (~200-500 tokens per decision)
**Triggers**: All user requests first go through orchestrator
**New Features**:
- Session monitoring and tracking
- Git worktree coordination
- Progress visualization

### 2. Analysis Agent (Gemini Pro 2.5)
**Purpose**: Code analysis, pattern detection, dependency mapping, visual analysis
**Strengths**: Multimodal capabilities, fast processing, large context
**Tasks**:
- Analyze existing code for reuse opportunities
- Map dependencies and relationships
- Visual UI/UX analysis
- Performance profiling
- LSP integration for semantic understanding

### 3. Implementation Agents (Kimi + Opus)
**3a. Simple/Medium Implementation (Kimi)**
- Direct implementation of features
- Basic refactoring tasks
- Standard pattern application
- Test implementation

**3b. Complex Implementation (Kimi → Opus)**
- Kimi creates initial draft
- Opus reviews and enhances
- Security-critical refinements
- Architecture decisions

### 4. QA Agent (Claude Opus)
**Purpose**: Final quality checks, validation, security
**Strengths**: Thorough validation, catches edge cases
**Tasks**:
- Review Kimi-generated code
- Knowledge file compliance
- Security vulnerability scanning
- Generate comprehensive test suites

### 5. Documentation Agent (Gemini Pro 2.5)
**Purpose**: Automated documentation generation
**Strengths**: Fast, consistent, template-based
**Tasks**:
- Auto-generate docs from code
- Maintain /logic folder documentation
- API documentation
- Prompt factory for consistent messaging

### 6. Debug Agent (Gemini Pro 2.5 + Browser Automation)
**Purpose**: Live debugging with visual capabilities
**Strengths**: Multimodal analysis, browser interaction
**Tasks**:
- Visual regression testing
- Cross-browser compatibility
- Performance profiling
- Interactive debugging sessions

## Technical Implementation

### Agent Registry
```python
AGENT_REGISTRY = {
    "orchestrator": {
        "model": "claude-opus",
        "mcp": "sequential-thinking",
        "max_tokens": 500,  # Minimal for routing
        "capabilities": ["routing", "aggregation", "session_monitoring"]
    },
    "analysis": {
        "model": "gemini-pro-2.5",
        "mcp": "gemini",
        "capabilities": ["code_analysis", "pattern_detection", "visual_analysis", "lsp_integration"]
    },
    "implementation_simple": {
        "model": "kimi",
        "mcp": "kimi",
        "capabilities": ["code_generation", "refactoring", "test_writing"]
    },
    "implementation_complex": {
        "model": "kimi",  # First pass
        "review_model": "claude-opus",  # Review and enhance
        "mcp": "kimi",
        "capabilities": ["complex_features", "architecture", "security"]
    },
    "qa": {
        "model": "claude-opus",
        "mcp": None,
        "capabilities": ["validation", "security_scan", "compliance_check"]
    },
    "documentation": {
        "model": "gemini-pro-2.5",
        "mcp": "gemini",
        "capabilities": ["doc_generation", "prompt_factory", "template_based"]
    },
    "debug": {
        "model": "gemini-pro-2.5",
        "mcp": ["puppeteer", "playwright", "chrome-debug"],
        "capabilities": ["browser_automation", "visual_testing", "performance_profiling"]
    }
}
```

### Task Routing Logic
```python
class TaskRouter:
    """Enhanced task routing with complexity assessment"""
    
    def route_task(self, task: dict) -> dict:
        """Route task to appropriate agent(s)"""
        
        description = task['description'].lower()
        complexity = self.assess_complexity(task)
        
        # Documentation → Gemini Pro 2.5
        if any(kw in description for kw in ['document', 'readme', 'api doc', 'comment']):
            return {'agent': 'documentation', 'model': 'gemini-pro-2.5'}
        
        # Analysis → Gemini Pro 2.5 (multimodal capabilities)
        if any(kw in description for kw in ['analyze', 'find', 'search', 'pattern', 'visual']):
            return {'agent': 'analysis', 'model': 'gemini-pro-2.5'}
        
        # Debug → Gemini Pro 2.5 + Browser
        if any(kw in description for kw in ['debug', 'test browser', 'visual', 'performance']):
            return {'agent': 'debug', 'model': 'gemini-pro-2.5'}
        
        # Implementation routing based on complexity
        if 'implement' in description or 'create' in description or 'build' in description:
            if complexity < 0.3:
                return {'agent': 'implementation_simple', 'model': 'kimi'}
            elif complexity < 0.7:
                return {'agent': 'implementation_simple', 'model': 'kimi'}
            else:
                # Complex: Kimi draft → Opus review
                return {
                    'agent': 'implementation_complex',
                    'pipeline': [
                        {'stage': 'draft', 'model': 'kimi'},
                        {'stage': 'review', 'model': 'opus'}
                    ]
                }
        
        # QA tasks → Opus
        if any(kw in description for kw in ['review', 'validate', 'check', 'test']):
            return {'agent': 'qa', 'model': 'opus'}
        
        # Default to orchestrator
        return {'agent': 'orchestrator', 'model': 'opus'}
    
    def assess_complexity(self, task: dict) -> float:
        """Assess task complexity (0.0 - 1.0)"""
        factors = {
            'lines_of_code': task.get('estimated_loc', 0) / 500,
            'dependencies': len(task.get('dependencies', [])) / 10,
            'security_critical': 1.0 if task.get('security', False) else 0.0,
            'architectural': 1.0 if 'architecture' in task.get('description', '') else 0.0,
            'cross_cutting': len(task.get('affected_files', [])) / 10
        }
        
        # Weighted average
        weights = {'lines_of_code': 0.2, 'dependencies': 0.2, 'security_critical': 0.3,
                  'architectural': 0.2, 'cross_cutting': 0.1}
        
        complexity = sum(factors[k] * weights[k] for k in factors)
        return min(complexity, 1.0)
```

## Compatibility Requirements

### Must Maintain
1. All existing hook functionality
2. Current memory system behavior
3. Command structure and syntax
4. Knowledge file references
5. Task management flow

### Enhancement Points
1. MCPBridge becomes real (not simulated)
2. Memory capture includes agent metadata
3. Hooks gain agent-awareness
4. Commands can specify preferred agent

## Success Metrics
- 85% reduction in Opus token usage (from 100% to 15%)
- 2x faster documentation generation with Gemini
- 3x faster implementation for simple tasks with Kimi
- Parallel task execution across all agents
- Zero breaking changes to existing system
- <2s average response time for routing decisions
- 95% task success rate without retry

## New Features from Repository Analysis

### 1. Session Monitoring (from Agent-MCP)
- Real-time agent activity tracking
- Session registry with automatic cleanup
- TUI for progress visualization

### 2. Git Worktree Support (from Agent-MCP)
- Agent-specific worktrees for isolated development
- Parallel feature development
- Automatic cleanup on completion

### 3. Prompt Factory Pattern (from Serena)
- Centralized prompt generation
- Task-specific prompt templates
- Consistent messaging across agents

### 4. Task Completion Signaling (from Make-It-Heavy)
- Explicit TaskDoneTool pattern
- Clean handoffs between agents
- Summary generation on completion

### 5. Tool Architecture (from Make-It-Heavy)
- BaseTool abstract class
- Schema generation for discovery
- Parameter validation

### 6. LSP Integration (from Serena)
- Deep semantic code understanding
- Multi-language support
- IDE-like capabilities

## Security Considerations
- Agent isolation prevents cross-contamination
- Sensitive operations stay with Opus
- Audit trail for all agent decisions
- Graceful fallback to single-agent mode

## Next Steps
See implementation roadmap (08-implementation-roadmap-spec.md) for phased rollout plan.