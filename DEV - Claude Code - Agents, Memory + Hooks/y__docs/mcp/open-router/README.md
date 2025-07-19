# OpenRouter Integration Guide

## Overview

OpenRouter is a unified API gateway that provides access to multiple AI models through a single interface. It eliminates the need for separate MCP servers for each model provider, simplifying API management and improving reliability.

## Key Benefits

1. **Single API Key**: Manage one key instead of multiple provider keys
2. **Unified Interface**: Consistent API format across all models
3. **Model Flexibility**: Easy switching between models without code changes
4. **Cost Efficiency**: Pay-as-you-go pricing with transparent costs
5. **Automatic Failover**: Built-in redundancy across providers
6. **No MCP Overhead**: Direct API access without additional server processes

## Available Models

### Google Gemini Models
- `google/gemini-2.5-flash` - Fast, efficient model ($0.0000003/1k prompt tokens)
- `google/gemini-2.5-pro` - Advanced reasoning model ($0.00000125/1k prompt tokens)
- `google/gemini-2.0-flash` - Previous generation ($0.0000001/1k prompt tokens)

### Moonshot/Kimi Models
- `moonshotai/kimi-k2` - 1T parameter MoE model ($0.00000014/1k prompt tokens)
- `moonshotai/kimi-k2:free` - Free tier version

### Other Popular Models
- `anthropic/claude-3.5-sonnet` - Claude's flagship model
- `openai/gpt-4-turbo` - GPT-4 Turbo
- `mistralai/mistral-small` - Efficient small model
- `meta/llama-3.3-70b` - Open source powerhouse

## Setup Instructions

### 1. Get OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai)
2. Sign up for an account
3. Generate an API key from the dashboard
4. Add credits to your account

### 2. Configure Environment

Add your OpenRouter API key to `.env`:

```bash
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

### 3. Remove Redundant MCP Servers

Since OpenRouter provides access to Gemini models, you can remove the Gemini MCP server from `claude_desktop_config.json`:

```json
// Remove this entire section:
"gemini-mcp": {
  "command": "...",
  "args": [...],
  "env": {...}
}
```

## Usage Examples

### Basic API Call

```python
import aiohttp
import os

async def call_openrouter(model: str, messages: list):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/yourusername/yourproject",
        "X-Title": "Your Project Name"
    }
    
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": 1000
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        ) as response:
            return await response.json()
```

### Model Selection Strategy

```python
def select_model_for_task(task_complexity: int, task_type: str) -> str:
    """Select optimal model based on task requirements"""
    
    if task_complexity < 3:
        # Simple tasks - use fast, cheap models
        return "google/gemini-2.0-flash"
    
    elif task_complexity < 7:
        # Medium complexity - balance cost and capability
        if task_type == "code":
            return "moonshotai/kimi-k2"
        else:
            return "google/gemini-2.5-flash"
    
    else:
        # Complex tasks - use most capable models
        if task_type == "reasoning":
            return "google/gemini-2.5-pro"
        else:
            return "anthropic/claude-3.5-sonnet"
```

## Integration with Multi-Agent System

The multi-agent system can leverage OpenRouter for intelligent model routing:

1. **Task Analysis**: Determine complexity and requirements
2. **Model Selection**: Choose optimal model via OpenRouter
3. **Cost Optimization**: Use cheaper models for simple tasks
4. **Parallel Execution**: Different agents can use different models

### Example Integration

```python
class OpenRouterClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1"
    
    async def route_to_model(self, task: Task, model: str) -> dict:
        """Route task to specified model via OpenRouter"""
        
        messages = self._prepare_messages(task)
        
        response = await self._call_api(
            model=model,
            messages=messages,
            max_tokens=task.max_tokens
        )
        
        return {
            "model": model,
            "response": response["choices"][0]["message"]["content"],
            "usage": response["usage"],
            "cost": self._calculate_cost(response["usage"], model)
        }
```

## Cost Comparison

| Task Type | Direct API | OpenRouter | Savings |
|-----------|------------|------------|---------|
| Simple (Gemini Flash) | $0.0000003/1k | $0.0000003/1k | 0% |
| Complex (Gemini Pro) | $0.00000125/1k | $0.00000125/1k | 0% |
| Code (Kimi K2) | N/A (via Moonshot) | $0.00000014/1k | Unified access |

## Best Practices

1. **API Key Security**: Never commit API keys to version control
2. **Rate Limiting**: Implement exponential backoff for retries
3. **Error Handling**: Handle both API and network errors gracefully
4. **Cost Monitoring**: Track usage to optimize model selection
5. **Caching**: Cache responses for identical queries

## Migration Checklist

- [x] Remove Gemini MCP from claude_desktop_config.json
- [ ] Add OPENROUTER_API_KEY to .env
- [ ] Update model routing to use OpenRouter endpoints
- [ ] Test all model integrations
- [ ] Monitor costs and performance

## Troubleshooting

### Common Issues

1. **401 Unauthorized**: Check API key format and validity
2. **429 Rate Limited**: Implement backoff strategy
3. **Model Not Found**: Verify model ID format (provider/model-name)
4. **Insufficient Credits**: Add credits to OpenRouter account

### Debug Example

```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Test connection
async def test_openrouter():
    try:
        response = await call_openrouter(
            model="google/gemini-2.0-flash",
            messages=[{"role": "user", "content": "Hello"}]
        )
        print(f"Success: {response}")
    except Exception as e:
        print(f"Error: {e}")
        # Check headers, payload, and response
```

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Model Pricing](https://openrouter.ai/models)
- [API Reference](https://openrouter.ai/api/v1)
- [Status Page](https://status.openrouter.ai)