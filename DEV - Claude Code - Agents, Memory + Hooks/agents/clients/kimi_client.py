"""
Kimi Moonshot API Client

Provides integration with Kimi API for the multi-agent system.
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


class KimiClient:
    """Client for Kimi Moonshot API"""
    
    def __init__(self):
        self.api_key = os.getenv("KIMI_API_KEY")
        if not self.api_key:
            raise ValueError("KIMI_API_KEY not found in environment variables")
        
        # OpenRouter API endpoint  
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = "moonshotai/kimi-k2"  # Available Kimi model on OpenRouter
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "HTTP-Referer": "https://github.com/yourusername/yourproject",  # Required by OpenRouter
            "X-Title": "Multi-Agent System"  # Optional but recommended
        }
        
        # Token costs (per 1k tokens)
        self.cost_per_1k_input = 0.003
        self.cost_per_1k_output = 0.012
    
    async def complete(self, messages: List[Dict[str, str]], 
                      temperature: float = 0.7,
                      max_tokens: int = 4096) -> Dict[str, Any]:
        """Send completion request to Kimi API"""
        
        endpoint = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(endpoint, 
                                      headers=self.headers,
                                      json=payload) as response:
                    
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(f"Kimi API error {response.status}: {error_text}")
                    
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
                        "cost": self._calculate_cost(usage),
                        "model": self.model
                    }
                    
            except aiohttp.ClientError as e:
                raise Exception(f"Network error calling Kimi API: {str(e)}")
    
    def _calculate_cost(self, usage: Dict[str, int]) -> float:
        """Calculate cost based on token usage"""
        input_cost = (usage.get("prompt_tokens", 0) / 1000) * self.cost_per_1k_input
        output_cost = (usage.get("completion_tokens", 0) / 1000) * self.cost_per_1k_output
        return round(input_cost + output_cost, 4)
    
    async def test_connection(self) -> bool:
        """Test API connection"""
        try:
            result = await self.complete([
                {"role": "user", "content": "Say 'Hello' in one word"}
            ], max_tokens=10)
            
            return result.get("content", "").strip().lower() in ["hello", "你好"]
        except Exception as e:
            print(f"Kimi API test failed: {e}")
            return False


# Singleton instance
_kimi_client = None

def get_kimi_client() -> KimiClient:
    """Get or create Kimi client instance"""
    global _kimi_client
    if _kimi_client is None:
        _kimi_client = KimiClient()
    return _kimi_client


async def route_to_kimi(task_description: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Route a task to Kimi API
    
    This is called by agents when they determine a task is simple enough for Kimi.
    """
    client = get_kimi_client()
    
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
    
    # Send to Kimi
    result = await client.complete(messages)
    
    return {
        "status": "completed",
        "model": "kimi-pro",
        "response": result["content"],
        "usage": result["usage"],
        "cost": result["cost"],
        "cost_saved": 0.6  # 60% savings vs Claude
    }


if __name__ == "__main__":
    # Test the client
    async def test():
        print("Testing Kimi API connection...")
        client = get_kimi_client()
        
        if await client.test_connection():
            print("✅ Kimi API connection successful!")
            
            # Test a simple task
            result = await route_to_kimi("Write a Python function to reverse a string")
            print(f"\nTest result:")
            print(f"Response: {result['response'][:100]}...")
            print(f"Tokens used: {result['usage']['total_tokens']}")
            print(f"Cost: ${result['cost']}")
        else:
            print("❌ Kimi API connection failed!")
    
    asyncio.run(test())