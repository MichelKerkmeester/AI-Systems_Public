#!/usr/bin/env python3
"""
Implementation Agent wrapper for Unified Agent Architecture v3
Handles QWEN3 Simple/Coder and fallback to Opus
"""

import os
import sys
import json
import asyncio
import logging
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from pathlib import Path

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import qwen-hyperbolic using importlib due to hyphen in filename
import importlib.util
qwen_spec = importlib.util.spec_from_file_location(
    "qwen_hyperbolic",
    str(Path(__file__).parent.parent.parent / "scripts" / "qwen-hyperbolic.py")
)
qwen_module = importlib.util.module_from_spec(qwen_spec)
qwen_spec.loader.exec_module(qwen_module)
HyperbolicQWEN = qwen_module.HyperbolicQWEN

logger = logging.getLogger(__name__)

@dataclass
class ImplementationResult:
    """Result from implementation agent"""
    success: bool
    output: str
    model_used: str
    tokens_used: int
    cost: float
    execution_time: float
    error: Optional[str] = None
    fallback_used: bool = False

class ImplementationAgent:
    """Wrapper for implementation models (QWEN3, Opus fallback)"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.qwen_client = None
        self.opus_client = None  # Placeholder for Opus integration
        self._initialize_clients()
        
    def _initialize_clients(self):
        """Initialize model clients"""
        # Initialize QWEN3 if API key available
        if os.getenv('HYPERBOLIC_API_KEY'):
            try:
                self.qwen_client = HyperbolicQWEN()
                logger.info("QWEN3 client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize QWEN3: {e}")
        
        # TODO: Initialize Opus client when needed
        
    async def execute(self, task: str, model: str = "qwen3_coder", 
                     context: Dict[str, Any] = None) -> ImplementationResult:
        """
        Execute implementation task with specified model
        """
        start_time = asyncio.get_event_loop().time()
        
        try:
            # Prepare prompt with context
            prompt = self._prepare_prompt(task, context)
            
            # Route to appropriate model
            if model in ["qwen3_simple", "qwen3_coder"]:
                result = await self._execute_qwen(prompt, model, context)
            elif model == "opus":
                result = await self._execute_opus(prompt, context)
            else:
                raise ValueError(f"Unknown model: {model}")
            
            # Add execution time
            result.execution_time = asyncio.get_event_loop().time() - start_time
            
            return result
            
        except Exception as e:
            logger.error(f"Implementation execution failed: {e}")
            
            # Try fallback
            if model != "opus" and self.config.get('enable_fallback', True):
                logger.info("Attempting fallback to Opus")
                return await self._execute_fallback(task, context, str(e))
            
            return ImplementationResult(
                success=False,
                output="",
                model_used=model,
                tokens_used=0,
                cost=0.0,
                execution_time=asyncio.get_event_loop().time() - start_time,
                error=str(e)
            )
    
    async def _execute_qwen(self, prompt: str, model: str, 
                           context: Dict[str, Any] = None) -> ImplementationResult:
        """Execute task using QWEN3"""
        if not self.qwen_client:
            raise RuntimeError("QWEN3 client not initialized")
        
        # Configure based on model type
        if model == "qwen3_simple":
            max_tokens = 4000
            temperature = 0.1
            system_prompt = (
                "You are QWEN3 Simple, optimized for quick, straightforward code changes. "
                "Focus on simple, direct solutions without over-engineering."
            )
        else:  # qwen3_coder
            max_tokens = 8000
            temperature = 0.3
            system_prompt = (
                "You are QWEN3 Coder, an expert programming assistant. "
                "You excel at complex implementations, refactoring, and algorithm design. "
                "Always search for existing patterns and code to reuse before creating new solutions."
            )
        
        # Add system prompt to the beginning
        full_prompt = f"{system_prompt}\n\n{prompt}"
        
        # Execute in thread pool (since it's sync)
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            self.qwen_client.complete,
            full_prompt,
            temperature,
            max_tokens
        )
        
        # Estimate tokens and cost
        input_tokens = len(full_prompt) // 4
        output_tokens = len(response) // 4
        total_tokens = input_tokens + output_tokens
        
        # Cost calculation
        cost_per_million = 3.00 if model == "qwen3_simple" else 7.50
        cost = (total_tokens / 1_000_000) * cost_per_million
        
        return ImplementationResult(
            success=True,
            output=response,
            model_used=model,
            tokens_used=total_tokens,
            cost=cost,
            execution_time=0.0  # Will be set by caller
        )
    
    async def _execute_opus(self, prompt: str, context: Dict[str, Any] = None) -> ImplementationResult:
        """Execute task using Claude Opus"""
        # TODO: Implement Opus execution via MCP or direct API
        # For now, return a placeholder
        logger.warning("Opus execution not yet implemented")
        
        return ImplementationResult(
            success=False,
            output="Opus integration pending",
            model_used="opus",
            tokens_used=0,
            cost=0.0,
            execution_time=0.0,
            error="Opus not yet integrated"
        )
    
    async def _execute_fallback(self, task: str, context: Dict[str, Any], 
                               original_error: str) -> ImplementationResult:
        """Execute fallback to Opus after failure"""
        fallback_prompt = (
            f"The following task failed with QWEN3: {original_error}\n\n"
            f"Please complete this task:\n{task}"
        )
        
        result = await self._execute_opus(fallback_prompt, context)
        result.fallback_used = True
        return result
    
    def _prepare_prompt(self, task: str, context: Dict[str, Any] = None) -> str:
        """Prepare prompt with context"""
        prompt_parts = [task]
        
        if context:
            # Add code reuse context
            if 'existing_code' in context:
                prompt_parts.insert(0, "EXISTING CODE TO REUSE:")
                prompt_parts.insert(1, context['existing_code'])
                prompt_parts.insert(2, "\nTASK:")
            
            # Add file context
            if 'current_file' in context:
                prompt_parts.append(f"\nCURRENT FILE: {context['current_file']}")
            
            # Add constraints
            if 'constraints' in context:
                prompt_parts.append(f"\nCONSTRAINTS: {json.dumps(context['constraints'])}")
        
        return "\n".join(prompt_parts)
    
    def validate_output(self, output: str, task: str) -> Tuple[bool, List[str]]:
        """Validate implementation output"""
        issues = []
        
        # Check for common problems
        if not output or len(output) < 10:
            issues.append("Output too short")
        
        if "error" in output.lower() or "exception" in output.lower():
            issues.append("Output contains error indicators")
        
        # Task-specific validation
        if "implement" in task.lower() and "def " not in output and "class " not in output:
            issues.append("Implementation task but no function/class definitions found")
        
        if "test" in task.lower() and "test_" not in output:
            issues.append("Test task but no test functions found")
        
        return len(issues) == 0, issues