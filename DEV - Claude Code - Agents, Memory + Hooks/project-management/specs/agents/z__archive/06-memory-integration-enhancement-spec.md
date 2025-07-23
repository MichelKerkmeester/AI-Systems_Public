# Memory Integration Enhancement Specification

## Executive Summary
This specification enhances the existing memory system to support multi-agent collaboration, implementing real Graphiti integration to replace the current simulated MCPBridge, while maintaining full backward compatibility.

## Current Memory System Analysis

### Existing Architecture
```python
# Current Implementation (Simulated)
class MCPBridge:
    def call_mcp_tool(self, tool_name: str, args: dict):
        # Currently simulated - needs real implementation
        return {"status": "simulated", "data": {}}

# Memory Capture Queue (Already Implemented)
class MemoryCaptureQueue:
    - Background thread processing
    - Priority-based queue (CRITICAL, HIGH, MEDIUM, LOW)
    - 16 capture patterns
    - Thread-safe batch processing
```

### Enhancement Goals
1. Replace simulated MCPBridge with real Graphiti integration
2. Add agent-specific memory contexts
3. Implement cross-agent memory sharing
4. Enhance memory search with agent awareness
5. Maintain all existing functionality

## Enhanced Memory Architecture

### 1. Real MCPBridge Implementation
```python
class RealMCPBridge:
    """Production MCPBridge with actual Graphiti integration"""
    
    def __init__(self):
        self.graphiti_client = GraphitiMCPClient()
        self.connection_pool = ConnectionPool()
        self.retry_policy = ExponentialBackoff()
        
    async def call_mcp_tool(self, tool_name: str, args: dict) -> dict:
        """Execute real MCP tool calls with retry logic"""
        
        # Map tool names to Graphiti operations
        tool_mapping = {
            'mcp__graphiti-gemini__add_episode': self.graphiti_client.add_episode,
            'mcp__graphiti-gemini__search': self.graphiti_client.search,
            'mcp__graphiti-gemini__retrieve_episodes': self.graphiti_client.retrieve_episodes
        }
        
        # Execute with retry
        for attempt in range(self.retry_policy.max_attempts):
            try:
                result = await tool_mapping[tool_name](args)
                return {
                    'status': 'success',
                    'data': result,
                    'latency': self.measure_latency()
                }
            except Exception as e:
                if attempt == self.retry_policy.max_attempts - 1:
                    return {
                        'status': 'error',
                        'error': str(e),
                        'fallback': self.get_fallback_result(tool_name, args)
                    }
                await asyncio.sleep(self.retry_policy.get_delay(attempt))
```

### 2. Agent-Aware Memory System
```python
class AgentMemorySystem:
    """Enhanced memory system with agent contexts"""
    
    def __init__(self):
        self.bridge = RealMCPBridge()
        self.agent_contexts = {}
        self.shared_memory = SharedMemorySpace()
        self.access_control = MemoryAccessControl()
        
    async def create_agent_context(self, agent_id: str, capabilities: list):
        """Create isolated memory context for agent"""
        
        self.agent_contexts[agent_id] = {
            'id': agent_id,
            'capabilities': capabilities,
            'private_memories': [],
            'shared_access': self.determine_shared_access(capabilities),
            'memory_limit': self.calculate_memory_limit(agent_id),
            'created_at': datetime.now()
        }
        
    async def capture_agent_memory(self, agent_id: str, memory: dict):
        """Capture memory with agent attribution"""
        
        # Enhance memory with agent metadata
        enhanced_memory = {
            **memory,
            'agent_id': agent_id,
            'agent_context': self.agent_contexts.get(agent_id, {}),
            'visibility': self.determine_visibility(memory),
            'timestamp': datetime.now().isoformat()
        }
        
        # Determine storage strategy
        if enhanced_memory['visibility'] == 'private':
            self.agent_contexts[agent_id]['private_memories'].append(enhanced_memory)
        else:
            await self.bridge.call_mcp_tool(
                'mcp__graphiti-gemini__add_episode',
                {'data': enhanced_memory}
            )
            
        # Update shared memory if applicable
        if enhanced_memory['visibility'] in ['shared', 'public']:
            await self.shared_memory.update(agent_id, enhanced_memory)
```

### 3. Cross-Agent Memory Sharing
```python
class SharedMemorySpace:
    """Facilitate memory sharing between agents"""
    
    def __init__(self):
        self.shared_pool = {}
        self.access_log = []
        self.conflict_resolver = ConflictResolver()
        
    async def share_memory(self, source_agent: str, memory: dict, target_agents: list):
        """Share memory between specific agents"""
        
        # Validate permissions
        if not self.can_share(source_agent, target_agents):
            raise PermissionError(f"{source_agent} cannot share with {target_agents}")
            
        # Create shared memory entry
        shared_entry = {
            'id': self.generate_id(),
            'source': source_agent,
            'targets': target_agents,
            'memory': memory,
            'access_count': 0,
            'created_at': datetime.now()
        }
        
        self.shared_pool[shared_entry['id']] = shared_entry
        
        # Notify target agents
        for agent in target_agents:
            await self.notify_agent(agent, shared_entry)
            
    async def query_shared_memories(self, agent_id: str, query: str) -> list:
        """Query memories accessible to an agent"""
        
        accessible_memories = []
        
        # Check direct shares
        for memory_id, entry in self.shared_pool.items():
            if agent_id in entry['targets'] or entry['source'] == agent_id:
                if self.matches_query(entry['memory'], query):
                    accessible_memories.append(entry)
                    entry['access_count'] += 1
                    
        # Check public memories
        public_memories = await self.bridge.call_mcp_tool(
            'mcp__graphiti-gemini__search',
            {
                'query': query,
                'filter': {'visibility': 'public'}
            }
        )
        
        accessible_memories.extend(public_memories.get('data', []))
        
        # Log access
        self.access_log.append({
            'agent': agent_id,
            'query': query,
            'results_count': len(accessible_memories),
            'timestamp': datetime.now()
        })
        
        return accessible_memories
```

### 4. Memory Conflict Resolution
```python
class ConflictResolver:
    """Resolve conflicts in shared memories"""
    
    async def resolve_conflict(self, memories: list) -> dict:
        """Resolve conflicting memories from different agents"""
        
        # Sort by trust score and timestamp
        sorted_memories = sorted(
            memories,
            key=lambda m: (
                self.get_agent_trust_score(m['agent_id']),
                m['timestamp']
            ),
            reverse=True
        )
        
        # Merge strategies
        if self.can_merge(sorted_memories):
            return self.merge_memories(sorted_memories)
        else:
            # Return most trusted/recent with conflict note
            return {
                **sorted_memories[0],
                'conflicts': sorted_memories[1:],
                'resolution_method': 'trust_and_recency'
            }
```

## Enhanced Memory Patterns

### 1. Agent Collaboration Patterns
```python
AGENT_MEMORY_PATTERNS = {
    'agent_handoff': {
        'priority': 'CRITICAL',
        'pattern': r'handing off .* to .* agent',
        'capture': lambda m: {
            'source_agent': m.group(1),
            'target_agent': m.group(2),
            'context': m.group(3)
        }
    },
    'agent_learning': {
        'priority': 'HIGH',
        'pattern': r'learned new pattern|discovered approach',
        'capture': lambda m: {
            'learning_type': 'pattern_discovery',
            'details': m.group(1)
        }
    },
    'agent_collaboration': {
        'priority': 'HIGH',
        'pattern': r'agents? .* collaborat|working together',
        'capture': lambda m: {
            'collaboration_type': 'multi_agent',
            'agents_involved': extract_agent_names(m.group(0))
        }
    }
}
```

### 2. Memory Search Enhancement
```python
class EnhancedMemorySearch:
    """Advanced memory search with agent awareness"""
    
    async def search(self, query: str, context: dict = None) -> list:
        """Multi-dimensional memory search"""
        
        # 1. Semantic search
        semantic_results = await self.semantic_search(query)
        
        # 2. Agent-filtered search
        if context and 'agent_id' in context:
            agent_results = await self.agent_specific_search(
                query, 
                context['agent_id']
            )
        else:
            agent_results = []
            
        # 3. Temporal search
        if context and 'time_range' in context:
            temporal_results = await self.temporal_search(
                query,
                context['time_range']
            )
        else:
            temporal_results = []
            
        # 4. Pattern-based search
        pattern_results = await self.pattern_search(query)
        
        # 5. Merge and rank results
        all_results = self.merge_results([
            semantic_results,
            agent_results,
            temporal_results,
            pattern_results
        ])
        
        return self.rank_by_relevance(all_results, query, context)
```

## Integration with Existing Hooks

### 1. Enhanced Memory Context Hook
```python
class EnhancedMemoryContextHook(MemoryContextHook):
    """Upgraded hook with agent support"""
    
    def __init__(self):
        super().__init__()
        self.agent_memory = AgentMemorySystem()
        
    async def pre_user_prompt(self, prompt: str, context: dict = None):
        """Enhanced pre-prompt processing"""
        
        # Determine active agent
        active_agent = context.get('agent_id', 'orchestrator')
        
        # Search with agent context
        memories = await self.agent_memory.search_memories(
            prompt,
            agent_id=active_agent,
            include_shared=True
        )
        
        # Original functionality
        await super().pre_user_prompt(prompt)
        
        # Add agent-specific context
        return {
            'memories': memories,
            'agent_context': self.agent_memory.get_agent_context(active_agent),
            'shared_insights': await self.get_shared_insights(active_agent)
        }
```

### 2. Memory Capture Enhancement
```python
class EnhancedMemoryCaptureQueue(MemoryCaptureQueue):
    """Enhanced queue with agent attribution"""
    
    async def process_item(self, item: dict):
        """Process with agent awareness"""
        
        # Detect agent from context
        agent_id = self.detect_agent(item)
        
        # Enhance item with agent metadata
        enhanced_item = {
            **item,
            'agent_id': agent_id,
            'agent_capabilities': self.get_agent_capabilities(agent_id),
            'cross_agent_relevance': self.calculate_relevance(item)
        }
        
        # Process through original queue
        await super().process_item(enhanced_item)
        
        # Additional agent-specific processing
        if enhanced_item['cross_agent_relevance'] > 0.7:
            await self.share_with_relevant_agents(enhanced_item)
```

## Memory Analytics and Insights

### 1. Agent Performance Tracking
```python
class MemoryAnalytics:
    """Track agent memory usage and effectiveness"""
    
    async def generate_analytics(self) -> dict:
        """Generate comprehensive memory analytics"""
        
        return {
            'agent_metrics': {
                agent_id: {
                    'memories_created': len(context['private_memories']),
                    'memories_shared': self.count_shared(agent_id),
                    'memory_quality': self.assess_quality(agent_id),
                    'reuse_rate': self.calculate_reuse_rate(agent_id)
                }
                for agent_id, context in self.agent_contexts.items()
            },
            'system_metrics': {
                'total_memories': await self.count_total_memories(),
                'shared_memory_usage': len(self.shared_pool),
                'conflict_rate': self.calculate_conflict_rate(),
                'search_performance': await self.measure_search_performance()
            },
            'insights': await self.generate_insights()
        }
```

### 2. Memory Optimization
```python
class MemoryOptimizer:
    """Optimize memory storage and retrieval"""
    
    async def optimize(self):
        """Run memory optimization routines"""
        
        # 1. Deduplicate similar memories
        duplicates = await self.find_duplicates()
        await self.merge_duplicates(duplicates)
        
        # 2. Archive old memories
        old_memories = await self.find_old_memories()
        await self.archive_memories(old_memories)
        
        # 3. Update memory indices
        await self.rebuild_indices()
        
        # 4. Optimize agent contexts
        for agent_id in self.agent_contexts:
            await self.optimize_agent_context(agent_id)
```

## Migration Strategy

### Phase 1: Infrastructure (Week 1)
1. Implement RealMCPBridge
2. Test Graphiti connection
3. Set up fallback mechanisms

### Phase 2: Agent Contexts (Week 2)
1. Create agent memory contexts
2. Implement isolation boundaries
3. Test memory attribution

### Phase 3: Sharing System (Week 3)
1. Build shared memory space
2. Implement access control
3. Create conflict resolution

### Phase 4: Integration (Week 4)
1. Update existing hooks
2. Migrate current memories
3. Enable agent features

## Success Metrics
- Memory capture rate: >50/day (maintained)
- Search latency: <100ms (maintained)
- Agent attribution accuracy: >95%
- Memory sharing efficiency: >80%
- Zero data loss during migration

## Backward Compatibility
- All existing memory patterns continue to work
- Existing hooks function without modification
- Gradual migration with feature flags
- Fallback to simulated mode if needed
- No breaking changes to memory API