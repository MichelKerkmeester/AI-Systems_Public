"""
Google Gemini API Client

Provides integration with Gemini API for the multi-agent system.
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


class GeminiClient:
    """Client for Google Gemini API"""
    
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        # Use the model from env or default to gemini-2.0-flash
        self.model = os.getenv("GEMINI_SMALL_MODEL", "gemini-2.0-flash")
        
        # Token costs (per 1k tokens) - Gemini Flash pricing
        self.cost_per_1k_input = 0.005
        self.cost_per_1k_output = 0.015
    
    async def complete(self, messages: List[Dict[str, str]], 
                      temperature: float = 0.7,
                      max_tokens: int = 8192) -> Dict[str, Any]:
        """Send completion request to Gemini API"""
        
        endpoint = f"{self.base_url}/models/{self.model}:generateContent"
        
        # Convert messages to Gemini format
        contents = []
        for msg in messages:
            if msg["role"] == "system":
                # Gemini doesn't have system role, prepend to first user message
                contents.append({
                    "role": "user",
                    "parts": [{"text": f"System: {msg['content']}"}]
                })
            else:
                contents.append({
                    "role": "user" if msg["role"] == "user" else "model",
                    "parts": [{"text": msg["content"]}]
                })
        
        payload = {
            "contents": contents,
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens,
                "topK": 40,
                "topP": 0.95
            }
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        url = f"{endpoint}?key={self.api_key}"
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, 
                                      headers=headers,
                                      json=payload) as response:
                    
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(f"Gemini API error {response.status}: {error_text}")
                    
                    result = await response.json()
                    
                    # Debug print
                    if not result.get("candidates"):
                        print(f"Gemini API response: {json.dumps(result, indent=2)}")
                    
                    # Extract content and token usage
                    candidate = result.get("candidates", [{}])[0]
                    content_parts = candidate.get("content", {}).get("parts", [])
                    content = content_parts[0].get("text", "") if content_parts else ""
                    
                    # Gemini provides token counts in usageMetadata
                    usage_metadata = result.get("usageMetadata", {})
                    
                    usage = {
                        "input_tokens": usage_metadata.get("promptTokenCount", 0),
                        "output_tokens": usage_metadata.get("candidatesTokenCount", 0),
                        "total_tokens": usage_metadata.get("totalTokenCount", 0)
                    }
                    
                    return {
                        "content": content,
                        "usage": usage,
                        "cost": self._calculate_cost(usage),
                        "model": self.model
                    }
                    
            except aiohttp.ClientError as e:
                raise Exception(f"Network error calling Gemini API: {str(e)}")
    
    def _calculate_cost(self, usage: Dict[str, int]) -> float:
        """Calculate cost based on token usage"""
        input_cost = (usage.get("input_tokens", 0) / 1000) * self.cost_per_1k_input
        output_cost = (usage.get("output_tokens", 0) / 1000) * self.cost_per_1k_output
        return round(input_cost + output_cost, 4)
    
    async def test_connection(self) -> bool:
        """Test API connection"""
        try:
            result = await self.complete([
                {"role": "user", "content": "Say 'Hello' in one word"}
            ], max_tokens=10)
            
            content = result.get("content", "").lower()
            print(f"Gemini response: {content}")
            return "hello" in content
        except Exception as e:
            print(f"Gemini API test failed: {e}")
            import traceback
            traceback.print_exc()
            return False


# Singleton instance
_gemini_client = None

def get_gemini_client() -> GeminiClient:
    """Get or create Gemini client instance"""
    global _gemini_client
    if _gemini_client is None:
        _gemini_client = GeminiClient()
    return _gemini_client


async def route_to_gemini(task_description: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Route a task to Gemini API
    
    This is called by agents when they need deep analysis with large context.
    """
    client = get_gemini_client()
    
    # Build messages
    messages = [
        {
            "role": "system",
            "content": "You are an expert analyst. Provide thorough and insightful analysis."
        }
    ]
    
    # Add context if provided (Gemini can handle large contexts)
    if context and context.get("files"):
        context_msg = "Context files:\n"
        for file_path, content in context["files"].items():
            context_msg += f"\n--- {file_path} ---\n{content}\n"
        messages.append({"role": "user", "content": context_msg})
    
    # Add main task
    messages.append({"role": "user", "content": task_description})
    
    # Send to Gemini
    result = await client.complete(messages)
    
    return {
        "status": "completed",
        "model": "gemini",
        "response": result["content"],
        "usage": result["usage"],
        "cost": result["cost"],
        "cost_saved": 0.75  # 75% savings vs Claude
    }


if __name__ == "__main__":
    # Test the client
    async def test():
        print("Testing Gemini API connection...")
        client = get_gemini_client()
        
        if await client.test_connection():
            print("✅ Gemini API connection successful!")
            
            # Test an analysis task
            result = await route_to_gemini("Analyze the benefits of using async/await in Python")
            print(f"\nTest result:")
            print(f"Response: {result['response'][:100]}...")
            print(f"Tokens used: {result['usage']['total_tokens']}")
            print(f"Cost: ${result['cost']}")
        else:
            print("❌ Gemini API connection failed!")
    
    asyncio.run(test())