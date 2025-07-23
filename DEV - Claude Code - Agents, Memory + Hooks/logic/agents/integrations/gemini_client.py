#!/usr/bin/env python3
"""
Gemini API Client for Unified Agent Architecture v3
Integrates with Google's Gemini Flash and Pro models
"""

import os
import asyncio
import logging
from typing import Dict, Optional, Any, List
import google.generativeai as genai

logger = logging.getLogger(__name__)

class GeminiClient:
    """Client for Gemini Flash and Pro models"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            logger.warning("GOOGLE_API_KEY not set")
            self.available = False
        else:
            try:
                genai.configure(api_key=self.api_key)
                self.flash_model = genai.GenerativeModel('gemini-2.5-flash')
                self.pro_model = genai.GenerativeModel('gemini-2.5-pro')
                self.available = True
                logger.info("Gemini clients initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Gemini: {e}")
                self.available = False
                
    def is_available(self) -> bool:
        """Check if Gemini is available"""
        return self.available
    
    async def analyze_with_flash(self, content: str, 
                                analysis_type: str = "general") -> Dict[str, Any]:
        """
        Fast analysis using Gemini Flash (1M context, 271 tokens/sec)
        """
        if not self.available:
            return {
                'success': False,
                'error': 'Gemini not available',
                'analysis': ''
            }
        
        try:
            # Prepare analysis prompt based on type
            prompts = {
                'general': "Analyze this code and provide insights on patterns, quality, and improvements:",
                'patterns': "Identify code patterns, anti-patterns, and architectural insights in:",
                'dependencies': "Analyze dependencies, imports, and module structure in:",
                'security': "Perform security analysis and identify vulnerabilities in:",
                'performance': "Analyze performance characteristics and optimization opportunities in:"
            }
            
            prompt = f"{prompts.get(analysis_type, prompts['general'])}\n\n{content}"
            
            # Generate response
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                self.flash_model.generate_content,
                prompt
            )
            
            return {
                'success': True,
                'analysis': response.text,
                'model': 'gemini_flash',
                'tokens': len(prompt) // 4 + len(response.text) // 4
            }
            
        except Exception as e:
            logger.error(f"Gemini Flash analysis failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'analysis': ''
            }
    
    async def analyze_with_pro(self, content: str, 
                              images: Optional[List[Any]] = None) -> Dict[str, Any]:
        """
        Advanced analysis using Gemini Pro with multimodal support
        """
        if not self.available:
            return {
                'success': False,
                'error': 'Gemini not available',
                'analysis': ''
            }
        
        try:
            # Prepare multimodal content if images provided
            if images:
                prompt_parts = [content] + images
            else:
                prompt_parts = [content]
            
            # Generate response
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                self.pro_model.generate_content,
                prompt_parts
            )
            
            return {
                'success': True,
                'analysis': response.text,
                'model': 'gemini_pro',
                'tokens': len(content) // 4 + len(response.text) // 4
            }
            
        except Exception as e:
            logger.error(f"Gemini Pro analysis failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'analysis': ''
            }
    
    async def generate_documentation(self, code: str) -> Dict[str, Any]:
        """
        Generate documentation using Gemini Flash
        """
        prompt = (
            "Generate comprehensive documentation for the following code. "
            "Include: purpose, parameters, return values, usage examples, "
            "and any important notes:\n\n"
            f"{code}"
        )
        
        return await self.analyze_with_flash(prompt, "documentation")
    
    async def visual_debug(self, screenshot: Any, error_context: str) -> Dict[str, Any]:
        """
        Debug using screenshot and error context (Gemini Pro multimodal)
        """
        prompt = (
            "Analyze this screenshot and error context to identify the issue "
            "and suggest fixes:\n\n"
            f"Error Context: {error_context}"
        )
        
        return await self.analyze_with_pro(prompt, images=[screenshot])
    
    def estimate_cost(self, tokens: int, model: str = "gemini_flash") -> float:
        """Estimate cost for token usage"""
        if model == "gemini_flash":
            cost_per_million = 0.26
        else:  # gemini_pro
            cost_per_million = 2.50
        
        return (tokens / 1_000_000) * cost_per_million