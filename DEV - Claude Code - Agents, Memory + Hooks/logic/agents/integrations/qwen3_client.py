#!/usr/bin/env python3
"""
QWEN3 API Client for Unified Agent Architecture
Integrates with Hyperbolic API for QWEN3-Coder-480B-A35B-Instruct model
"""

import os
import sys
from pathlib import Path
from typing import Dict, Optional, Any
import logging

# Import the existing QWEN wrapper
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

logger = logging.getLogger(__name__)

class QWEN3Client:
    """Unified client for QWEN3 Coder model via Hyperbolic"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('HYPERBOLIC_API_KEY')
        if not self.api_key:
            logger.warning("HYPERBOLIC_API_KEY not set")
        
        # Import dynamically to avoid import errors if not configured
        try:
            from qwen_hyperbolic import HyperbolicQWEN
            self.client = HyperbolicQWEN()
            self.available = True
        except Exception as e:
            logger.error(f"Failed to initialize QWEN3 client: {e}")
            self.client = None
            self.available = False
            
    def is_available(self) -> bool:
        """Check if QWEN3 is available"""
        return self.available and self.api_key is not None
    
    async def complete(self, prompt: str, max_tokens: int = 8000, temperature: float = 0.3) -> Dict[str, Any]:
        """
        Complete using QWEN3-Coder-480B-A35B-Instruct model
        """
        if not self.available:
            return {
                'success': False,
                'error': 'QWEN3 not available',
                'response': ''
            }
        
        try:
            # Add coder mode system prompt
            system_prompt = (
                "You are QWEN3-Coder-480B-A35B-Instruct, an expert programming assistant. "
                "You excel at complex implementations, algorithms, and system design. "
                "Always analyze existing code patterns before creating new solutions."
            )
            full_prompt = f"{system_prompt}\n\n{prompt}"
            
            # Use provided temperature or default
            response = self.client.complete(full_prompt, temperature=temperature, max_tokens=max_tokens)
            
            return {
                'success': True,
                'response': response,
                'model': 'qwen3_coder',
                'tokens': len(full_prompt) // 4 + len(response) // 4
            }
            
        except Exception as e:
            logger.error(f"QWEN3 Coder completion failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'response': ''
            }
    
    # Legacy method for backward compatibility
    async def complete_coder(self, prompt: str, max_tokens: int = 8000) -> Dict[str, Any]:
        """
        Legacy method - redirects to complete()
        """
        return await self.complete(prompt, max_tokens)
    
    def estimate_cost(self, tokens: int, model: str = "qwen3_coder") -> float:
        """Estimate cost for token usage"""
        # QWEN3-Coder-480B-A35B-Instruct pricing
        cost_per_million = 7.50
        
        return (tokens / 1_000_000) * cost_per_million