"""
OpenRouter API Client

Provides unified access to multiple AI models through OpenRouter.
Replaces individual API clients with a single interface.
"""

import os
import asyncio
import aiohttp
import json
from typing import Dict, Any, List, Optional
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class OpenRouterClient:
    """Unified client for all models via OpenRouter"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            # Fallback to individual keys if OpenRouter not configured
            self.api_key = None
            
        self.base_url = "https://openrouter.ai/api/v1"
        
        # Model mapping for cost optimization
        self.model_costs = {
            # Google Gemini
            "google/gemini-2.0-flash": {"input": 0.0000001, "output": 0.0000004},
            "google/gemini-2.5-flash": {"input": 0.0000003, "output": 0.0000025},
            "google/gemini-2.5-pro": {"input": 0.00000125, "output": 0.00001},
            
            # Moonshot/Kimi
            "moonshotai/kimi-k2": {"input": 0.00000014, "output": 0.00000249},
            "moonshotai/kimi-k2:free": {"input": 0, "output": 0},
            
            # Others for comparison
            "anthropic/claude-3.5-sonnet": {"input": 0.000003, "output": 0.000015},
            "openai/gpt-4-turbo": {"input": 0.00001, "output": 0.00003}
        }
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/anobel/multi-agent-system",
            "X-Title": "Multi-Agent System"
        }
    
    def is_configured(self) -> bool:
        """Check if OpenRouter is configured"""
        return self.api_key is not None
    
    async def complete(self, 
                      model: str,
                      messages: List[Dict[str, str]], 
                      temperature: float = 0.7,
                      max_tokens: int = 4096,
                      **kwargs) -> Dict[str, Any]:
        """Send completion request via OpenRouter"""
        
        if not self.is_configured():
            raise ValueError("OPENROUTER_API_KEY not configured")
        
        endpoint = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs  # Pass through any additional parameters
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(endpoint, 
                                      headers=self.headers,
                                      json=payload) as response:
                    
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(f"OpenRouter API error {response.status}: {error_text}")
                    
                    result = await response.json()
                    
                    # Extract token usage
                    usage = result.get("usage", {})
                    
                    return {
                        "content": result["choices"][0]["message"]["content"],
                        "usage": {
                            "input_tokens": usage.get("prompt_tokens", 0),
                            "output_tokens": usage.get("completion_tokens", 0),
                            "total_tokens": usage.get("total_tokens", 0)
                        },
                        "cost": self._calculate_cost(usage, model),
                        "model": model,
                        "provider": "openrouter"
                    }
                    
            except aiohttp.ClientError as e:
                raise Exception(f"Network error calling OpenRouter API: {str(e)}")
    
    def _calculate_cost(self, usage: Dict[str, int], model: str) -> float:
        """Calculate cost based on token usage"""
        if model not in self.model_costs:
            # Unknown model - use average pricing
            input_cost = (usage.get("prompt_tokens", 0) / 1000) * 0.000001
            output_cost = (usage.get("completion_tokens", 0) / 1000) * 0.000002
        else:
            costs = self.model_costs[model]
            input_cost = (usage.get("prompt_tokens", 0) / 1000) * costs["input"]
            output_cost = (usage.get("completion_tokens", 0) / 1000) * costs["output"]
        
        return round(input_cost + output_cost, 6)
    
    async def list_models(self) -> List[Dict[str, Any]]:
        """List available models from OpenRouter"""
        
        if not self.is_configured():
            return []
        
        endpoint = f"{self.base_url}/models"
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(endpoint, headers=self.headers) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result.get("data", [])
                    return []
            except:
                return []
    
    def select_model_for_task(self, 
                             complexity: int, 
                             task_type: str = "general",
                             require_vision: bool = False) -> str:
        """Select optimal model based on task requirements"""
        
        if require_vision:
            # Vision-capable models
            if complexity < 5:
                return "google/gemini-2.0-flash"
            else:
                return "google/gemini-2.5-pro"
        
        if complexity < 3:
            # Simple tasks - use fastest/cheapest
            return "google/gemini-2.0-flash"
        
        elif complexity < 6:
            # Medium complexity
            if task_type == "code":
                return "moonshotai/kimi-k2"
            elif task_type == "analysis":
                return "google/gemini-2.5-flash"
            else:
                return "google/gemini-2.5-flash"
        
        elif complexity < 8:
            # Complex tasks
            if task_type == "reasoning":
                return "google/gemini-2.5-pro"
            else:
                return "google/gemini-2.5-flash"
        
        else:
            # Very complex - use most capable
            return "google/gemini-2.5-pro"
    
    async def test_connection(self) -> bool:
        """Test OpenRouter API connection"""
        try:
            result = await self.complete(
                model="google/gemini-2.0-flash",
                messages=[{"role": "user", "content": "Say 'Hello' in one word"}],
                max_tokens=10
            )
            
            return result.get("content", "").strip().lower() in ["hello", "hi"]
        except Exception as e:
            print(f"OpenRouter API test failed: {e}")
            return False


# Gemini-specific wrapper for compatibility
class GeminiClient(OpenRouterClient):
    """Gemini client via OpenRouter - drop-in replacement for direct API"""
    
    def __init__(self):
        super().__init__()
        # Default Gemini models
        self.flash_model = "google/gemini-2.5-flash"
        self.pro_model = "google/gemini-2.5-pro"
    
    async def complete_flash(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        """Use Gemini Flash model"""
        return await self.complete(self.flash_model, messages, **kwargs)
    
    async def complete_pro(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        """Use Gemini Pro model"""
        return await self.complete(self.pro_model, messages, **kwargs)


# Singleton instances
_openrouter_client = None
_gemini_client = None

def get_openrouter_client() -> OpenRouterClient:
    """Get or create OpenRouter client instance"""
    global _openrouter_client
    if _openrouter_client is None:
        _openrouter_client = OpenRouterClient()
    return _openrouter_client

def get_gemini_client() -> GeminiClient:
    """Get or create Gemini client instance"""
    global _gemini_client
    if _gemini_client is None:
        _gemini_client = GeminiClient()
    return _gemini_client


async def route_to_gemini(task_description: str, 
                         context: Dict[str, Any] = None,
                         complexity: int = 5) -> Dict[str, Any]:
    """
    Route a task to Gemini via OpenRouter
    
    This replaces direct Gemini API calls with OpenRouter routing.
    """
    client = get_gemini_client()
    
    # Select appropriate Gemini model
    if complexity < 6:
        model = client.flash_model
    else:
        model = client.pro_model
    
    # Build messages
    messages = [
        {
            "role": "system",
            "content": "You are a helpful coding assistant. Be concise and accurate."
        }
    ]
    
    # Add context if provided
    if context and context.get("files"):
        context_msg = "Context:\n"
        for file_path, content in context["files"].items():
            context_msg += f"\n--- {file_path} ---\n{content}\n"
        messages.append({"role": "user", "content": context_msg})
    
    # Add main task
    messages.append({"role": "user", "content": task_description})
    
    # Send to Gemini via OpenRouter
    result = await client.complete(model, messages)
    
    return {
        "status": "completed",
        "model": model,
        "response": result["content"],
        "usage": result["usage"],
        "cost": result["cost"],
        "provider": "openrouter"
    }


if __name__ == "__main__":
    # Test the clients
    async def test():
        print("Testing OpenRouter connection...")
        
        # Test OpenRouter client
        or_client = get_openrouter_client()
        if or_client.is_configured():
            if await or_client.test_connection():
                print("✅ OpenRouter connection successful!")
                
                # List available models
                models = await or_client.list_models()
                gemini_models = [m for m in models if "gemini" in m.get("id", "").lower()]
                print(f"\nAvailable Gemini models: {len(gemini_models)}")
                for model in gemini_models[:5]:
                    print(f"  - {model['id']}")
            else:
                print("❌ OpenRouter connection failed!")
        else:
            print("❌ OPENROUTER_API_KEY not configured")
        
        # Test Gemini client
        print("\nTesting Gemini client via OpenRouter...")
        gemini_client = get_gemini_client()
        if gemini_client.is_configured():
            result = await route_to_gemini(
                "Write a Python function to calculate fibonacci numbers",
                complexity=3
            )
            print(f"Response preview: {result['response'][:100]}...")
            print(f"Model used: {result['model']}")
            print(f"Cost: ${result['cost']}")
        
    asyncio.run(test())