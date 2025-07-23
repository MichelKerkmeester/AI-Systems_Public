# Documentation Automation Agent Specification

## Executive Summary
This specification defines a Gemini Pro-powered documentation agent that automates the creation, maintenance, and organization of documentation within the `/logic` folder structure, significantly reducing Claude Opus token usage for documentation tasks.

## Current Documentation Analysis

### Existing Structure
```
.claude/
├── docs/              # Current documentation location
├── logic/             # New documentation will live here
│   ├── agents/
│   │   └── docs/      # Agent-specific documentation
│   ├── hooks/
│   │   └── docs/      # Hook documentation
│   ├── memory/
│   │   └── docs/      # Memory system docs
│   └── commands/
│       └── docs/      # Command documentation
```

### Migration Strategy
- Move documentation to relevant `/logic` subdirectories
- Maintain backward compatibility with symlinks
- Auto-generate documentation for new logic components

## Documentation Agent Architecture

### Core Components
```python
class DocumentationAgent:
    """Gemini-powered documentation automation"""
    
    def __init__(self):
        self.gemini_client = GeminiMCPClient()
        self.template_engine = DocTemplateEngine()
        self.ast_analyzer = ASTAnalyzer()
        
    async def generate_documentation(self, file_path: str) -> dict:
        """Generate documentation for a logic component"""
        
        # 1. Analyze code structure
        analysis = self.ast_analyzer.analyze(file_path)
        
        # 2. Determine documentation type
        doc_type = self.determine_doc_type(file_path)
        
        # 3. Generate documentation using Gemini
        doc_content = await self.gemini_client.generate({
            "prompt": self.create_doc_prompt(analysis, doc_type),
            "context": {
                "code_analysis": analysis,
                "existing_docs": self.get_related_docs(file_path),
                "conventions": self.get_doc_conventions()
            }
        })
        
        # 4. Format and save
        formatted_doc = self.template_engine.format(doc_content, doc_type)
        doc_path = self.get_doc_path(file_path)
        
        return {
            'doc_path': doc_path,
            'content': formatted_doc,
            'metadata': self.generate_metadata(analysis)
        }
```

### Documentation Types

#### 1. Hook Documentation
```python
class HookDocGenerator:
    """Generate hook-specific documentation"""
    
    TEMPLATE = """
# {hook_name} Hook

## Purpose
{purpose}

## Trigger Events
{triggers}

## Configuration
```yaml
{config}
```

## Usage Example
```python
{usage_example}
```

## Integration Points
{integration_points}

## Performance Impact
{performance_metrics}

## Related Hooks
{related_hooks}
"""
    
    async def generate_hook_doc(self, hook_path: str) -> str:
        """Generate comprehensive hook documentation"""
        
        analysis = self.analyze_hook(hook_path)
        
        doc_data = {
            'hook_name': analysis['name'],
            'purpose': await self.extract_purpose(analysis),
            'triggers': self.list_triggers(analysis),
            'config': self.extract_config(analysis),
            'usage_example': await self.generate_example(analysis),
            'integration_points': self.find_integrations(analysis),
            'performance_metrics': await self.measure_performance(hook_path),
            'related_hooks': self.find_related_hooks(analysis)
        }
        
        return self.TEMPLATE.format(**doc_data)
```

#### 2. Agent Documentation
```python
class AgentDocGenerator:
    """Generate agent-specific documentation"""
    
    TEMPLATE = """
# {agent_name} Agent

## Overview
{overview}

## Capabilities
{capabilities}

## Model Configuration
- **Primary Model**: {model}
- **Token Limit**: {token_limit}
- **Cost per 1M tokens**: ${cost}

## Task Types
{task_types}

## API Reference
{api_reference}

## Integration Example
```python
{integration_example}
```

## Performance Benchmarks
{benchmarks}

## Best Practices
{best_practices}
"""
```

#### 3. Command Documentation
```python
class CommandDocGenerator:
    """Generate command documentation"""
    
    async def generate_command_doc(self, command: dict) -> str:
        """Generate user-friendly command documentation"""
        
        return f"""
# {command['name']} Command

## Syntax
```bash
{command['syntax']}
```

## Description
{command['description']}

## Options
{self.format_options(command['options'])}

## Examples
{self.format_examples(command['examples'])}

## Related Commands
{self.find_related_commands(command)}

## Automation Notes
{command.get('automation_notes', 'This command may trigger automated workflows.')}
"""
```

## Automated Documentation Workflows

### 1. Real-time Documentation Updates
```python
class DocUpdateHook(Hook):
    """Auto-update documentation on code changes"""
    
    def __init__(self):
        self.doc_agent = DocumentationAgent()
        self.change_detector = ChangeDetector()
        
    async def post_tool_use(self, tool: str, result: dict):
        """Update docs after code modifications"""
        
        if tool in ['Edit', 'Write', 'MultiEdit']:
            file_path = result.get('file_path')
            
            # Check if it's a logic component
            if self.is_logic_component(file_path):
                # Detect significant changes
                changes = self.change_detector.analyze(file_path)
                
                if changes['significant']:
                    # Generate updated documentation
                    updated_doc = await self.doc_agent.generate_documentation(file_path)
                    
                    # Save to appropriate location
                    await self.save_documentation(updated_doc)
                    
                    # Update INDEX files
                    await self.update_index_files(updated_doc)
```

### 2. Batch Documentation Generation
```python
class BatchDocGenerator:
    """Generate documentation for multiple components"""
    
    async def generate_batch_docs(self, components: list) -> dict:
        """Parallel documentation generation"""
        
        # Group by type for efficiency
        grouped = self.group_by_type(components)
        
        # Generate prompts in batch
        batch_prompts = []
        for doc_type, items in grouped.items():
            template = self.get_batch_template(doc_type)
            prompt = self.create_batch_prompt(items, template)
            batch_prompts.append(prompt)
            
        # Send to Gemini in parallel
        tasks = [
            self.gemini_client.generate_batch(prompt)
            for prompt in batch_prompts
        ]
        
        results = await asyncio.gather(*tasks)
        
        # Process and save results
        return await self.process_batch_results(results)
```

### 3. Documentation Quality Assurance
```python
class DocQualityChecker:
    """Ensure documentation quality and consistency"""
    
    async def check_documentation(self, doc_path: str) -> dict:
        """Comprehensive documentation quality check"""
        
        doc_content = self.read_documentation(doc_path)
        
        checks = {
            'completeness': self.check_completeness(doc_content),
            'accuracy': await self.verify_accuracy(doc_content, doc_path),
            'consistency': self.check_consistency(doc_content),
            'examples_valid': await self.validate_examples(doc_content),
            'links_valid': self.check_links(doc_content),
            'formatting': self.check_formatting(doc_content)
        }
        
        # Generate improvement suggestions
        if any(not check['passed'] for check in checks.values()):
            improvements = await self.generate_improvements(checks, doc_content)
            
            # Auto-fix if possible
            if improvements['auto_fixable']:
                fixed_content = await self.apply_fixes(doc_content, improvements)
                await self.save_fixed_documentation(doc_path, fixed_content)
                
        return {
            'quality_score': self.calculate_score(checks),
            'checks': checks,
            'improvements': improvements
        }
```

## Integration with Existing System

### 1. Hook Integration
```python
# Extend existing doc-update-hook.py
class EnhancedDocUpdateHook(DocUpdateHook):
    """Enhanced documentation hook with agent support"""
    
    def __init__(self):
        super().__init__()
        self.doc_agent = DocumentationAgent()
        self.should_use_agent = True
        
    async def process_doc_update(self, file_path: str):
        """Route to appropriate documentation handler"""
        
        if self.should_use_agent and self.is_automatable(file_path):
            # Use Gemini agent for documentation
            return await self.doc_agent.generate_documentation(file_path)
        else:
            # Fall back to Opus for complex documentation
            return await self.fallback_to_opus(file_path)
```

### 2. Memory System Integration
```python
class DocMemoryIntegration:
    """Integrate documentation with memory system"""
    
    async def capture_doc_pattern(self, doc_result: dict):
        """Capture successful documentation patterns"""
        
        await self.memory_bridge.capture({
            'name': f"Doc Pattern: {doc_result['type']}",
            'content': {
                'template': doc_result['template_used'],
                'structure': doc_result['structure'],
                'success_metrics': doc_result['metrics']
            },
            'type': 'documentation_pattern'
        })
```

## Documentation Templates

### 1. Logic Component Template
```markdown
# {component_name}

## Overview
Brief description of what this component does.

## Location
`{file_path}`

## Dependencies
- List of dependencies
- Both internal and external

## Configuration
Any configuration options or environment variables.

## Usage
```python
# Example usage
{usage_example}
```

## API Reference
Detailed API documentation for public methods.

## Testing
How to test this component.

## Related Components
- Links to related logic components
- Integration points

## Changelog
- Latest changes and updates
```

### 2. Auto-generated INDEX Template
```python
class IndexGenerator:
    """Generate INDEX.md files automatically"""
    
    TEMPLATE = """
# {category} Documentation Index

> Auto-generated on {timestamp}

## Overview
{overview}

## Components

{component_list}

## Quick Links
{quick_links}

## Recent Updates
{recent_updates}

---
*This index is automatically maintained by the Documentation Agent.*
"""
    
    async def generate_index(self, directory: str) -> str:
        """Generate INDEX.md for a directory"""
        
        components = self.scan_directory(directory)
        
        return self.TEMPLATE.format(
            category=self.get_category_name(directory),
            timestamp=datetime.now().isoformat(),
            overview=await self.generate_overview(components),
            component_list=self.format_component_list(components),
            quick_links=self.generate_quick_links(components),
            recent_updates=self.get_recent_updates(components)
        )
```

## Performance Optimization

### 1. Caching Strategy
```python
class DocCache:
    """Cache documentation generation results"""
    
    def __init__(self):
        self.cache = {}
        self.embeddings = {}
        
    def should_regenerate(self, file_path: str) -> bool:
        """Determine if documentation needs regeneration"""
        
        # Check file modification time
        file_mtime = os.path.getmtime(file_path)
        cache_mtime = self.cache.get(file_path, {}).get('mtime', 0)
        
        # Check significant changes
        if file_mtime > cache_mtime:
            old_embedding = self.embeddings.get(file_path)
            new_embedding = self.generate_embedding(file_path)
            
            similarity = cosine_similarity(old_embedding, new_embedding)
            return similarity < 0.95  # Significant change threshold
            
        return False
```

### 2. Batch Processing
```python
async def process_documentation_queue():
    """Process documentation queue efficiently"""
    
    queue = DocQueue()
    batch_size = 10
    
    while True:
        # Collect batch
        batch = await queue.get_batch(batch_size, timeout=5)
        
        if batch:
            # Process in parallel with Gemini
            results = await DocumentationAgent().generate_batch_docs(batch)
            
            # Save results
            for result in results:
                await save_documentation(result)
                
        await asyncio.sleep(1)
```

## Success Metrics
- Documentation coverage: >95%
- Auto-generation accuracy: >90%
- Token usage reduction: 80% (vs Opus)
- Generation speed: <2 seconds per component
- Quality score: >85%

## Cost Analysis
- Opus 4: $15/$75 per 1M tokens (input/output) - via Claude MAX plan
- Gemini 2.5 Pro: $1.25-2.50/$10-15 per 1M tokens (varies by context size)
- Average doc: 500 tokens
- Daily docs: ~100
- Monthly savings: ~$93.75 (85% reduction with output-heavy workload)

## Implementation Timeline
- Week 1: Set up Gemini integration
- Week 2: Implement core doc generators
- Week 3: Create template system
- Week 4: Integrate with existing hooks
- Week 5: Implement quality checks
- Week 6: Performance optimization