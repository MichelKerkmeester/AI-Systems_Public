"""
Model Selector for Multi-Agent System

Manages model selection and routing based on:
1. Task complexity analysis
2. Agent type requirements
3. Cost optimization
4. Performance requirements
5. Fallback strategies
"""

import json
import os
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
import logging

from .task_complexity_analyzer import TaskAnalysis, ComplexityLevel, TaskType


class ModelProvider(Enum):
    """Available model providers"""
    CLAUDE = "claude"
    KIMI = "kimi"
    GEMINI = "gemini"
    OLLAMA = "ollama"


@dataclass
class ModelConfig:
    """Configuration for a specific model"""
    provider: ModelProvider
    model_name: str
    api_endpoint: Optional[str]
    cost_per_1k_tokens: float
    max_context_window: int
    supports_streaming: bool
    supports_tools: bool
    best_for: List[TaskType]
    avoid_for: List[TaskType]


@dataclass
class ModelSelection:
    """Result of model selection"""
    primary_model: str
    fallback_model: Optional[str]
    provider: ModelProvider
    reasoning: List[str]
    estimated_cost: float
    warnings: List[str]


class ModelSelector:
    """Selects optimal models for tasks based on multiple factors"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.logger = logging.getLogger(__name__)
        self.models = self._load_model_configs()
        self.usage_stats = {}
        self.cost_tracker = {}
        self._load_user_preferences(config_path)
    
    def _load_model_configs(self) -> Dict[str, ModelConfig]:
        """Load model configurations"""
        return {
            "claude-opus-4": ModelConfig(
                provider=ModelProvider.CLAUDE,
                model_name="claude-opus-4-20250514",
                api_endpoint=None,  # Uses native integration
                cost_per_1k_tokens=0.015,  # Input cost
                max_context_window=200000,
                supports_streaming=True,
                supports_tools=True,
                best_for=[
                    TaskType.ARCHITECTURE, TaskType.DESIGN,
                    TaskType.SYNTHESIS, TaskType.DEBUG,
                    TaskType.REFACTOR
                ],
                avoid_for=[]
            ),
            "kimi-pro": ModelConfig(
                provider=ModelProvider.KIMI,
                model_name="kimi-pro",
                api_endpoint="${KIMI_API_ENDPOINT}",
                cost_per_1k_tokens=0.003,  # Much cheaper
                max_context_window=128000,
                supports_streaming=True,
                supports_tools=False,
                best_for=[
                    TaskType.SEARCH, TaskType.READ,
                    TaskType.EDIT, TaskType.DOCUMENT
                ],
                avoid_for=[
                    TaskType.ARCHITECTURE, TaskType.SYNTHESIS,
                    TaskType.REVIEW  # Especially security reviews
                ]
            ),
            "gemini-mcp": ModelConfig(
                provider=ModelProvider.GEMINI,
                model_name="gemini-2.5-pro",
                api_endpoint="mcp://gemini",  # Via MCP
                cost_per_1k_tokens=0.005,
                max_context_window=1000000,  # 1M tokens!
                supports_streaming=True,
                supports_tools=True,
                best_for=[
                    TaskType.ANALYSIS, TaskType.REVIEW,
                    TaskType.TEST
                ],
                avoid_for=[
                    TaskType.SYNTHESIS  # Keep synthesis on Claude
                ]
            ),
            "qwen-coder": ModelConfig(
                provider=ModelProvider.OLLAMA,
                model_name="qwen2.5-coder:latest",
                api_endpoint="ollama://localhost",
                cost_per_1k_tokens=0.0,  # Local model
                max_context_window=32000,
                supports_streaming=True,
                supports_tools=False,
                best_for=[
                    TaskType.READ, TaskType.DOCUMENT
                ],
                avoid_for=[
                    TaskType.ARCHITECTURE, TaskType.DESIGN,
                    TaskType.DEBUG, TaskType.SYNTHESIS
                ]
            )
        }
    
    def _load_user_preferences(self, config_path: Optional[str]):
        """Load user preferences for model selection"""
        self.preferences = {
            "cost_weight": 0.3,  # How much to weight cost (0-1)
            "performance_weight": 0.7,  # How much to weight performance
            "always_use_claude_for": ["security", "architecture", "synthesis"],
            "enable_kimi": True,
            "enable_ollama": False,  # Local models
            "max_cost_per_task": 1.0,  # Dollar limit
            "prefer_fast_models": False,
            "fallback_enabled": True
        }
        
        # Override with user config if provided
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_prefs = json.load(f)
                self.preferences.update(user_prefs)
    
    def select_model(self, task_analysis: TaskAnalysis, 
                    agent_type: str,
                    force_model: Optional[str] = None) -> ModelSelection:
        """
        Select the optimal model for a task
        
        Args:
            task_analysis: Analysis of the task complexity
            agent_type: Type of agent (analyst, developer, etc.)
            force_model: Override model selection
            
        Returns:
            ModelSelection with primary and fallback models
        """
        reasoning = []
        warnings = []
        
        # Handle forced model selection
        if force_model:
            if force_model in self.models:
                reasoning.append(f"Using forced model: {force_model}")
                return ModelSelection(
                    primary_model=force_model,
                    fallback_model="claude-opus-4" if force_model != "claude-opus-4" else None,
                    provider=self.models[force_model].provider,
                    reasoning=reasoning,
                    estimated_cost=self._estimate_cost(task_analysis, force_model),
                    warnings=warnings
                )
            else:
                warnings.append(f"Forced model {force_model} not found, using default selection")
        
        # Special handling for synthesis agents
        if agent_type == "synthesis":
            reasoning.append("Synthesis agent always uses Claude for complex merging")
            return ModelSelection(
                primary_model="claude-opus-4",
                fallback_model=None,
                provider=ModelProvider.CLAUDE,
                reasoning=reasoning,
                estimated_cost=self._estimate_cost(task_analysis, "claude-opus-4"),
                warnings=warnings
            )
        
        # Check for security-related tasks
        if self._is_security_related(task_analysis):
            reasoning.append("Security-related task requires Claude")
            return ModelSelection(
                primary_model="claude-opus-4",
                fallback_model=None,
                provider=ModelProvider.CLAUDE,
                reasoning=reasoning,
                estimated_cost=self._estimate_cost(task_analysis, "claude-opus-4"),
                warnings=warnings
            )
        
        # Score each model
        model_scores = {}
        for model_name, config in self.models.items():
            if not self._is_model_enabled(config):
                continue
            
            score, model_reasoning = self._score_model(
                task_analysis, agent_type, config
            )
            model_scores[model_name] = (score, model_reasoning)
        
        # Select best model
        if not model_scores:
            warnings.append("No models available, defaulting to Claude")
            primary_model = "claude-opus-4"
        else:
            primary_model = max(model_scores.items(), key=lambda x: x[1][0])[0]
            reasoning.extend(model_scores[primary_model][1])
        
        # Select fallback model
        fallback_model = self._select_fallback(primary_model, task_analysis)
        
        # Check cost limits
        estimated_cost = self._estimate_cost(task_analysis, primary_model)
        if estimated_cost > self.preferences["max_cost_per_task"]:
            warnings.append(f"Estimated cost ${estimated_cost:.2f} exceeds limit")
            # Try cheaper model
            if primary_model != "kimi-pro" and self.preferences["enable_kimi"]:
                primary_model = "kimi-pro"
                reasoning.append("Switched to Kimi Pro due to cost limits")
        
        # Update usage stats
        self._update_usage_stats(primary_model, task_analysis)
        
        return ModelSelection(
            primary_model=primary_model,
            fallback_model=fallback_model,
            provider=self.models[primary_model].provider,
            reasoning=reasoning,
            estimated_cost=estimated_cost,
            warnings=warnings
        )
    
    def _score_model(self, task_analysis: TaskAnalysis, 
                    agent_type: str,
                    config: ModelConfig) -> Tuple[float, List[str]]:
        """Score a model for a specific task"""
        score = 0.0
        reasoning = []
        
        # Task type compatibility
        if task_analysis.task_type in config.best_for:
            score += 3.0
            reasoning.append(f"Model excels at {task_analysis.task_type.value}")
        elif task_analysis.task_type in config.avoid_for:
            score -= 5.0
            reasoning.append(f"Model not recommended for {task_analysis.task_type.value}")
        
        # Complexity matching
        complexity_scores = {
            ComplexityLevel.TRIVIAL: {"kimi-pro": 3, "qwen-coder": 2, "gemini-mcp": 1, "claude-opus-4": 0},
            ComplexityLevel.SIMPLE: {"kimi-pro": 3, "gemini-mcp": 2, "claude-opus-4": 1, "qwen-coder": 0},
            ComplexityLevel.MEDIUM: {"gemini-mcp": 3, "claude-opus-4": 2, "kimi-pro": 1, "qwen-coder": -1},
            ComplexityLevel.COMPLEX: {"claude-opus-4": 3, "gemini-mcp": 1, "kimi-pro": -1, "qwen-coder": -3},
            ComplexityLevel.CRITICAL: {"claude-opus-4": 5, "gemini-mcp": -1, "kimi-pro": -3, "qwen-coder": -5}
        }
        
        model_name = next(k for k, v in self.models.items() if v == config)
        complexity_score = complexity_scores.get(
            task_analysis.complexity_level, {}
        ).get(model_name, 0)
        score += complexity_score
        
        # Cost consideration
        cost_score = (1 - config.cost_per_1k_tokens / 0.015) * self.preferences["cost_weight"] * 5
        score += cost_score
        if cost_score > 1:
            reasoning.append(f"Cost-effective: ${config.cost_per_1k_tokens:.3f}/1k tokens")
        
        # Context window check
        if task_analysis.estimated_tokens > config.max_context_window:
            score -= 10
            reasoning.append("Insufficient context window")
        elif task_analysis.estimated_tokens < config.max_context_window * 0.1:
            score += 1
            reasoning.append("Efficient context usage")
        
        # Tool support requirements
        if task_analysis.requires_reasoning and not config.supports_tools:
            score -= 2
            reasoning.append("Limited tool support for complex reasoning")
        
        # Performance preference
        if self.preferences["prefer_fast_models"]:
            speed_scores = {"kimi-pro": 2, "qwen-coder": 3, "gemini-mcp": 1, "claude-opus-4": 0}
            score += speed_scores.get(model_name, 0) * self.preferences["performance_weight"]
        
        # Agent type compatibility
        agent_preferences = {
            "analyst": {"gemini-mcp": 2, "claude-opus-4": 1},
            "developer": {"claude-opus-4": 2, "kimi-pro": 1},
            "reviewer": {"claude-opus-4": 2, "gemini-mcp": 1},
            "synthesis": {"claude-opus-4": 5}  # Strong preference
        }
        
        agent_score = agent_preferences.get(agent_type, {}).get(model_name, 0)
        score += agent_score
        
        return score, reasoning
    
    def _is_model_enabled(self, config: ModelConfig) -> bool:
        """Check if a model provider is enabled"""
        if config.provider == ModelProvider.KIMI:
            return self.preferences["enable_kimi"]
        elif config.provider == ModelProvider.OLLAMA:
            return self.preferences["enable_ollama"]
        return True
    
    def _is_security_related(self, task_analysis: TaskAnalysis) -> bool:
        """Check if task involves security concerns"""
        security_keywords = [
            "security", "auth", "password", "token", "secret",
            "vulnerability", "exploit", "injection", "xss", "csrf"
        ]
        
        task_desc = str(task_analysis.task_type).lower()
        for keyword in security_keywords:
            if keyword in task_desc:
                return True
        
        for keyword in self.preferences["always_use_claude_for"]:
            if keyword in task_desc:
                return True
        
        return False
    
    def _select_fallback(self, primary_model: str, 
                        task_analysis: TaskAnalysis) -> Optional[str]:
        """Select a fallback model"""
        if not self.preferences["fallback_enabled"]:
            return None
        
        # Claude doesn't need fallback
        if primary_model == "claude-opus-4":
            return None
        
        # For simple tasks, fall back to Claude
        if task_analysis.complexity_level.value <= 1:
            return "claude-opus-4"
        
        # For complex tasks routed to other models, use Claude as fallback
        return "claude-opus-4"
    
    def _estimate_cost(self, task_analysis: TaskAnalysis, model_name: str) -> float:
        """Estimate cost for a task with a specific model"""
        config = self.models[model_name]
        
        # Rough estimate: input + output tokens
        estimated_total_tokens = task_analysis.estimated_tokens * 1.5
        
        # Cost per 1k tokens
        cost = (estimated_total_tokens / 1000) * config.cost_per_1k_tokens
        
        # Add small buffer for multiple interactions
        cost *= 1.2
        
        return round(cost, 3)
    
    def _update_usage_stats(self, model_name: str, task_analysis: TaskAnalysis):
        """Track model usage statistics"""
        if model_name not in self.usage_stats:
            self.usage_stats[model_name] = {
                "count": 0,
                "total_tokens": 0,
                "total_cost": 0,
                "task_types": {}
            }
        
        stats = self.usage_stats[model_name]
        stats["count"] += 1
        stats["total_tokens"] += task_analysis.estimated_tokens
        stats["total_cost"] += self._estimate_cost(task_analysis, model_name)
        
        task_type = task_analysis.task_type.value
        stats["task_types"][task_type] = stats["task_types"].get(task_type, 0) + 1
    
    def get_usage_report(self) -> Dict[str, Any]:
        """Get usage statistics report"""
        total_cost = sum(
            stats["total_cost"] for stats in self.usage_stats.values()
        )
        
        report = {
            "total_cost": total_cost,
            "total_tasks": sum(
                stats["count"] for stats in self.usage_stats.values()
            ),
            "by_model": self.usage_stats,
            "cost_savings": self._calculate_savings(),
            "recommendations": self._generate_recommendations()
        }
        
        return report
    
    def _calculate_savings(self) -> Dict[str, float]:
        """Calculate cost savings from routing"""
        # Assume all tasks would have used Claude
        claude_cost_per_token = self.models["claude-opus-4"].cost_per_1k_tokens
        
        actual_cost = sum(
            stats["total_cost"] for stats in self.usage_stats.values()
        )
        
        hypothetical_cost = sum(
            (stats["total_tokens"] / 1000) * claude_cost_per_token
            for stats in self.usage_stats.values()
        )
        
        return {
            "actual_cost": actual_cost,
            "without_routing": hypothetical_cost,
            "saved": hypothetical_cost - actual_cost,
            "percentage": ((hypothetical_cost - actual_cost) / hypothetical_cost * 100)
            if hypothetical_cost > 0 else 0
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate usage recommendations"""
        recommendations = []
        
        # Check if Kimi is underutilized
        kimi_usage = self.usage_stats.get("kimi-pro", {}).get("count", 0)
        total_usage = sum(stats["count"] for stats in self.usage_stats.values())
        
        if total_usage > 10 and kimi_usage / total_usage < 0.2:
            recommendations.append(
                "Consider routing more simple tasks to Kimi Pro for cost savings"
            )
        
        # Check if too many complex tasks going to cheap models
        for model_name, stats in self.usage_stats.items():
            if model_name != "claude-opus-4":
                complex_tasks = sum(
                    count for task_type, count in stats.get("task_types", {}).items()
                    if task_type in ["architecture", "design", "synthesis"]
                )
                if complex_tasks > 5:
                    recommendations.append(
                        f"Warning: {complex_tasks} complex tasks routed to {model_name}"
                    )
        
        return recommendations