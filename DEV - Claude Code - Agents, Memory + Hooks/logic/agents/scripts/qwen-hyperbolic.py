#!/usr/bin/env python3
"""
QWEN via Hyperbolic API wrapper for Claude Code CLI
Usage: python3 qwen-hyperbolic.py "Your prompt here"
"""

import os
import sys
import json
import requests
from typing import Dict, List

class HyperbolicQWEN:
    """Simple wrapper for QWEN via Hyperbolic API"""
    
    def __init__(self):
        self.api_key = os.getenv('HYPERBOLIC_API_KEY')
        if not self.api_key:
            print("Error: HYPERBOLIC_API_KEY environment variable not set")
            print("Get your API key from: https://app.hyperbolic.ai")
            print("\nNote: The API key has been added to .env file")
            print("Run: source .env")
            sys.exit(1)
            
        self.base_url = "https://api.hyperbolic.xyz/v1/chat/completions"
        self.model = "Qwen/Qwen3-Coder-480B-A35B-Instruct"
        
    def complete(self, prompt: str, temperature: float = 0.7, max_tokens: int = 4096) -> str:
        """Get completion from QWEN"""
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        # Prepare messages
        messages = [
            {
                "role": "system",
                "content": (
                    "You are QWEN 3 Coder, an expert programming assistant. "
                    "You excel at code implementation, optimization, and problem-solving. "
                    "Always search for existing patterns and code to reuse before creating new solutions."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": 0.9,
            "stream": False
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=data, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
            
        except requests.exceptions.RequestException as e:
            return f"Error calling Hyperbolic API: {e}"
        except KeyError as e:
            return f"Unexpected response format: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 qwen-hyperbolic.py 'Your prompt here'")
        print("   or: python3 qwen-hyperbolic.py -f prompt_file.txt")
        sys.exit(1)
    
    # Check if reading from file
    if sys.argv[1] == '-f' and len(sys.argv) >= 3:
        with open(sys.argv[2], 'r') as f:
            prompt = f.read().strip()
    else:
        # Join all arguments as the prompt
        prompt = ' '.join(sys.argv[1:])
    
    # Initialize QWEN client
    qwen = HyperbolicQWEN()
    
    # Get completion
    print("🤖 QWEN 3 Coder via Hyperbolic")
    print("=" * 50)
    print(f"Prompt: {prompt[:100]}..." if len(prompt) > 100 else f"Prompt: {prompt}")
    print("=" * 50)
    print("\nGenerating response...\n")
    
    response = qwen.complete(prompt)
    print(response)

if __name__ == "__main__":
    main()