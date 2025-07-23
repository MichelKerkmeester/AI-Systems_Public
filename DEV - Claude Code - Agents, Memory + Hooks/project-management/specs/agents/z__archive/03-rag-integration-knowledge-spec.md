# RAG Integration and Knowledge Base Specification

## Executive Summary
This specification defines the integration of crawl4ai-rag MCP server to build a comprehensive knowledge base that enhances agent capabilities through intelligent retrieval-augmented generation (RAG).

## Current State Analysis

### Existing crawl4ai-rag Installation
- **Location**: `/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/crawl4ai-rag`
- **Status**: Installed but not configured
- **Available Tools**:
  - `crawl_single_page`: Basic web crawling
  - `smart_crawl_url`: Intelligent multi-page crawling
  - `perform_rag_query`: Vector search (requires config)
  - `search_code_examples`: Code pattern search
  - `check_ai_script_hallucinations`: Validation using Neo4j
  - `query_knowledge_graph`: Neo4j graph exploration
  - `parse_github_repository`: Repository analysis

### Integration Requirements
1. Configure Supabase for vector storage
2. Set up Neo4j for knowledge graph
3. Integrate with existing memory system
4. Enhance agent decision-making with RAG

## Architecture Design

### Knowledge Base Structure
```
┌─────────────────────────────────────────────┐
│            Knowledge Base System             │
├─────────────────┬───────────────────────────┤
│  Vector Store   │      Graph Database       │
│   (Supabase)    │        (Neo4j)           │
├─────────────────┼───────────────────────────┤
│ • Code snippets │ • Code relationships      │
│ • Documentation │ • Dependency graphs       │
│ • Patterns      │ • Architecture maps       │
│ • Examples      │ • Hallucination detection │
└─────────────────┴───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────┐
│          RAG Query Engine                    │
│   (Semantic Search + Graph Traversal)       │
└─────────────────────────────────────────────┘
```

### Integration with Agent System
```python
class RAGEnhancedAgent:
    """Base agent class with RAG capabilities"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.rag_client = CrawlAIRAGClient()
        self.memory_bridge = AgentMemoryBridge()
        
    async def enhance_context_with_rag(self, task: dict) -> dict:
        """Enhance task context with relevant knowledge"""
        
        # 1. Search vector store for similar code/docs
        similar_content = await self.rag_client.perform_rag_query({
            "query": task['description'],
            "source": self.get_relevant_source(task),
            "match_count": 5
        })
        
        # 2. Query knowledge graph for relationships
        graph_insights = await self.rag_client.query_knowledge_graph({
            "command": f"explore {task.get('target_component', '')}"
        })
        
        # 3. Check for potential hallucinations
        if 'generated_code' in task:
            validation = await self.rag_client.check_hallucinations({
                "script_content": task['generated_code']
            })
            
        # 4. Merge with existing context
        return {
            **task,
            'rag_context': {
                'similar_examples': similar_content,
                'graph_insights': graph_insights,
                'validation_results': validation if 'generated_code' in task else None
            }
        }
```

## Knowledge Acquisition Strategy

### 1. Automated Crawling Pipeline
```python
class KnowledgeCrawler:
    """Automated knowledge acquisition system"""
    
    def __init__(self):
        self.sources = {
            'documentation': [
                'https://docs.anthropic.com/claude',
                'https://www.modelcontextprotocol.io/docs',
                'https://webflow.com/docs'
            ],
            'repositories': [
                'https://github.com/anthropics/claude-code',
                'https://github.com/modelcontextprotocol/servers',
                self.get_project_repo()
            ],
            'patterns': [
                'https://patterns.dev',
                'https://refactoring.guru/design-patterns'
            ]
        }
        
    async def crawl_and_index(self):
        """Crawl sources and build knowledge base"""
        
        for category, urls in self.sources.items():
            for url in urls:
                # Smart crawl with categorization
                result = await self.rag_client.smart_crawl_url({
                    "url": url,
                    "max_depth": 3,
                    "chunk_size": 2000,
                    "category": category
                })
                
                # Capture in memory system
                await self.memory_bridge.capture({
                    "name": f"Knowledge: {category} from {url}",
                    "content": result,
                    "type": "knowledge_acquisition"
                })
```

### 2. Code Pattern Extraction
```python
class PatternExtractor:
    """Extract reusable patterns from codebase"""
    
    async def extract_patterns(self, repo_path: str):
        """Analyze repository for patterns"""
        
        # Parse repository into knowledge graph
        result = await self.rag_client.parse_github_repository({
            "repo_url": repo_path
        })
        
        # Query for common patterns
        patterns = await self.rag_client.query_knowledge_graph({
            "command": "query MATCH (c:Class)-[:HAS_METHOD]->(m:Method) "
                      "WHERE m.name =~ '.*init.*' "
                      "RETURN c.name, m.params_list"
        })
        
        # Index patterns for reuse
        for pattern in patterns:
            await self.index_pattern(pattern)
```

### 3. Continuous Learning
```python
class ContinuousLearner:
    """Learn from agent interactions"""
    
    def __init__(self):
        self.success_threshold = 0.8
        self.pattern_detector = PatternDetector()
        
    async def learn_from_interaction(self, task: dict, result: dict):
        """Extract knowledge from successful completions"""
        
        if result.get('success_score', 0) > self.success_threshold:
            # Extract successful patterns
            patterns = self.pattern_detector.extract(task, result)
            
            # Store in knowledge base
            for pattern in patterns:
                await self.rag_client.index_pattern({
                    "pattern": pattern,
                    "context": task,
                    "success_metrics": result['metrics']
                })
```

## Query Enhancement Pipeline

### 1. Multi-Stage Query Processing
```python
class QueryEnhancer:
    """Enhance queries with RAG context"""
    
    async def enhance_query(self, original_query: str) -> dict:
        """Multi-stage query enhancement"""
        
        # Stage 1: Semantic expansion
        expanded = await self.semantic_expand(original_query)
        
        # Stage 2: Historical context
        history = await self.get_relevant_history(expanded)
        
        # Stage 3: Pattern matching
        patterns = await self.match_patterns(expanded)
        
        # Stage 4: Knowledge graph context
        graph_context = await self.get_graph_context(expanded)
        
        return {
            'original': original_query,
            'expanded': expanded,
            'context': {
                'history': history,
                'patterns': patterns,
                'graph': graph_context
            },
            'suggested_approach': self.suggest_approach(patterns, history)
        }
```

### 2. Hallucination Prevention
```python
class HallucinationPreventer:
    """Prevent AI hallucinations using knowledge base"""
    
    async def validate_generation(self, generated_code: str) -> dict:
        """Validate generated code against knowledge base"""
        
        # Parse generated code
        parsed = self.parse_code(generated_code)
        
        # Check imports
        import_validation = await self.validate_imports(parsed['imports'])
        
        # Check method calls
        method_validation = await self.validate_methods(parsed['method_calls'])
        
        # Check patterns
        pattern_validation = await self.validate_patterns(parsed['patterns'])
        
        return {
            'valid': all([
                import_validation['valid'],
                method_validation['valid'],
                pattern_validation['valid']
            ]),
            'issues': self.collect_issues([
                import_validation,
                method_validation,
                pattern_validation
            ]),
            'suggestions': self.generate_fixes(parsed, validation_results)
        }
```

## Integration Hooks

### 1. Pre-Task RAG Enhancement
```python
class PreTaskRAGHook(Hook):
    """Enhance task context before execution"""
    
    async def pre_agent_dispatch(self, task: dict) -> dict:
        # Get RAG context
        rag_context = await RAGEnhancedAgent().enhance_context_with_rag(task)
        
        # Add relevant examples
        examples = await self.get_similar_examples(task)
        
        # Add validation hints
        validation_hints = await self.get_validation_hints(task)
        
        return {
            **task,
            'enhanced_context': rag_context,
            'examples': examples,
            'validation_hints': validation_hints
        }
```

### 2. Post-Generation Validation
```python
class PostGenerationValidationHook(Hook):
    """Validate generated content against knowledge base"""
    
    async def post_agent_result(self, result: dict) -> dict:
        if 'generated_code' in result:
            validation = await HallucinationPreventer().validate_generation(
                result['generated_code']
            )
            
            if not validation['valid']:
                # Attempt auto-fix
                fixed_code = await self.auto_fix(
                    result['generated_code'],
                    validation['issues']
                )
                
                result['generated_code'] = fixed_code
                result['validation_fixes'] = validation['issues']
                
        return result
```

## Configuration Requirements

### 1. Environment Variables
```bash
# Supabase Configuration
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_service_key

# Neo4j Configuration  
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password

# OpenAI (for embeddings)
OPENAI_API_KEY=your_api_key

# Optional: Voyage AI (alternative embeddings)
VOYAGE_API_KEY=your_voyage_key
```

### 2. MCP Server Configuration
```json
{
  "crawl4ai-rag": {
    "command": "node",
    "args": ["path/to/crawl4ai-rag/index.js"],
    "env": {
      "SUPABASE_URL": "${SUPABASE_URL}",
      "SUPABASE_SERVICE_KEY": "${SUPABASE_SERVICE_KEY}",
      "NEO4J_URI": "${NEO4J_URI}",
      "NEO4J_USERNAME": "${NEO4J_USERNAME}",
      "NEO4J_PASSWORD": "${NEO4J_PASSWORD}",
      "OPENAI_API_KEY": "${OPENAI_API_KEY}"
    }
  }
}
```

## Knowledge Base Maintenance

### 1. Automated Updates
- Daily crawl of documentation sources
- Weekly repository analysis
- Real-time pattern extraction from successful tasks

### 2. Quality Assurance
- Deduplication of similar content
- Validation of outdated information
- Relevance scoring and pruning

### 3. Performance Optimization
- Vector index optimization
- Graph query optimization
- Cache frequently accessed knowledge

## Success Metrics
- 90% reduction in hallucinations
- 50% improvement in code reuse
- 75% faster pattern discovery
- 95% validation accuracy
- <100ms query latency

## Implementation Timeline
- Week 1: Configure Supabase and Neo4j
- Week 2: Implement knowledge crawler
- Week 3: Build query enhancement pipeline
- Week 4: Integrate with agent system
- Week 5: Implement validation hooks
- Week 6: Performance optimization