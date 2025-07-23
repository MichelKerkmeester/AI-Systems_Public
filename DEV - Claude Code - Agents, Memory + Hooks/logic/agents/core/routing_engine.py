#!/usr/bin/env python3
"""
Smart Routing Engine for Unified Agent Architecture
Three-tier routing: Static rules → ML patterns → LLM decisions
"""

import json
import time
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import logging
from pathlib import Path
import sys

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import memory integration
from integrations.memory_filter_integration import AgentMemoryIntegration

logger = logging.getLogger(__name__)

class RouteDecision(Enum):
    """Routing decision types"""
    STATIC = "static"      # Rule-based decision
    PATTERN = "pattern"    # ML pattern match
    DYNAMIC = "dynamic"    # LLM-based decision

@dataclass
class RouteResult:
    """Result of routing decision"""
    model: str
    agent_type: str
    decision_type: RouteDecision
    confidence: float
    reasoning: str
    estimated_cost: float
    context_limit: int

class SmartRoutingEngine:
    """Three-tier routing engine for optimal model selection"""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config = self._load_config(config_path)
        self.static_rules = self.config.get('static_rules', [])
        self.patterns = self.config.get('learned_patterns', {})
        self.cost_tracker = CostTracker()
        self.performance_history = []
        
        # Initialize memory integration for pattern learning
        self.memory_integration = AgentMemoryIntegration()
        
        # Cache for routing decisions
        self.routing_cache = {}
        self.cache_hits = 0
        self.cache_misses = 0
        
    def route(self, task: str, context: Dict[str, Any] = None) -> RouteResult:
        """
        Route task to optimal model using three-tier decision process
        """
        # Check cache first
        cache_key = self._generate_cache_key(task, context)
        if cache_key in self.routing_cache:
            self.cache_hits += 1
            cached_result = self.routing_cache[cache_key]
            logger.info(f"Cache hit for routing: {task[:50]}... → {cached_result.model}")
            return cached_result
        
        self.cache_misses += 1
        
        # Get memory context for better routing
        memory_context = self.memory_integration.get_routing_history(
            self._extract_task_pattern(task), 
            limit=5
        )
        
        # Tier 1: Static Rules
        static_result = self._check_static_rules(task, context)
        if static_result and static_result.confidence > 0.9:
            logger.info(f"Static routing: {task[:50]}... → {static_result.model}")
            self._cache_and_capture_result(cache_key, static_result, task, memory_context)
            return static_result
        
        # Tier 2: Learned Patterns (enhanced with memory)
        pattern_result = self._check_patterns(task, context, memory_context)
        if pattern_result and pattern_result.confidence > 0.8:
            logger.info(f"Pattern routing: {task[:50]}... → {pattern_result.model}")
            self._cache_and_capture_result(cache_key, pattern_result, task, memory_context)
            return pattern_result
        
        # Tier 3: Dynamic LLM Decision
        dynamic_result = self._dynamic_routing(task, context)
        logger.info(f"Dynamic routing: {task[:50]}... → {dynamic_result.model}")
        self._cache_and_capture_result(cache_key, dynamic_result, task, memory_context)
        return dynamic_result
    
    def _check_static_rules(self, task: str, context: Dict[str, Any] = None) -> Optional[RouteResult]:
        """Check static routing rules"""
        task_lower = task.lower()
        
        for rule in self.static_rules:
            if self._matches_static_rule(task_lower, rule, context):
                return RouteResult(
                    model=rule['model'],
                    agent_type=rule['agent_type'],
                    decision_type=RouteDecision.STATIC,
                    confidence=rule.get('confidence', 1.0),
                    reasoning=rule.get('reason', 'Static rule match'),
                    estimated_cost=self._estimate_cost(task, rule['model']),
                    context_limit=rule.get('context_limit', 10000)
                )
        
        return None
    
    def _check_patterns(self, task: str, context: Dict[str, Any] = None, memory_context: List[Dict] = None) -> Optional[RouteResult]:
        """Check learned patterns from historical data"""
        # Calculate similarity scores with learned patterns
        best_match = None
        best_score = 0.0
        
        for pattern_id, pattern in self.patterns.items():
            score = self._calculate_pattern_similarity(task, pattern, context)
            if score > best_score:
                best_score = score
                best_match = pattern
        
        if best_match and best_score > 0.7:
            return RouteResult(
                model=best_match['model'],
                agent_type=best_match['agent_type'],
                decision_type=RouteDecision.PATTERN,
                confidence=best_score,
                reasoning=f"Pattern match: {best_match['description']}",
                estimated_cost=self._estimate_cost(task, best_match['model']),
                context_limit=best_match.get('context_limit', 10000)
            )
        
        return None
    
    def _dynamic_routing(self, task: str, context: Dict[str, Any] = None) -> RouteResult:
        """Fall back to intelligent routing based on task analysis"""
        # Analyze task characteristics
        characteristics = self._analyze_task(task, context)
        
        # Budget check
        daily_budget_remaining = self.cost_tracker.get_daily_remaining()
        
        # Decision logic
        if characteristics['is_simple'] and characteristics['lines_changed'] < 100:
            # Simple tasks still use QWEN3 Coder but with lower token limit
            model = "qwen3_coder"
            agent_type = "implementation"
            reasoning = "Simple task with minimal changes - using QWEN3 Coder with optimized context"
            
        elif characteristics['is_analysis']:
            model = "gemini_flash"
            agent_type = "analysis"
            reasoning = "Analysis task suitable for fast multimodal processing"
            
        elif characteristics['is_security_critical'] or characteristics['is_production']:
            model = "opus"
            agent_type = "quality_assurance"
            reasoning = "Security-critical or production code requires highest quality"
            
        elif daily_budget_remaining < 10.0:  # Low budget mode
            model = "gemini_flash"
            agent_type = "implementation"
            reasoning = f"Budget conservation mode (${daily_budget_remaining:.2f} remaining) - using Gemini Flash"
            
        else:
            model = "qwen3_coder"
            agent_type = "implementation"
            reasoning = "Standard implementation task"
        
        return RouteResult(
            model=model,
            agent_type=agent_type,
            decision_type=RouteDecision.DYNAMIC,
            confidence=0.85,
            reasoning=reasoning,
            estimated_cost=self._estimate_cost(task, model),
            context_limit=self._get_context_limit(model)
        )
    
    def update_pattern(self, task: str, result: RouteResult, performance: Dict[str, Any]):
        """Update learned patterns based on task performance"""
        pattern_key = self._generate_pattern_key(task)
        
        if pattern_key not in self.patterns:
            self.patterns[pattern_key] = {
                'description': task[:100],
                'model': result.model,
                'agent_type': result.agent_type,
                'success_rate': 0.0,
                'avg_cost': 0.0,
                'avg_time': 0.0,
                'usage_count': 0
            }
        
        # Update pattern statistics
        pattern = self.patterns[pattern_key]
        pattern['usage_count'] += 1
        pattern['success_rate'] = self._update_average(
            pattern['success_rate'],
            1.0 if performance['success'] else 0.0,
            pattern['usage_count']
        )
        pattern['avg_cost'] = self._update_average(
            pattern['avg_cost'],
            performance['cost'],
            pattern['usage_count']
        )
        pattern['avg_time'] = self._update_average(
            pattern['avg_time'],
            performance['time'],
            pattern['usage_count']
        )
        
        # Save updated patterns
        self._save_patterns()
    
    def _matches_static_rule(self, task_lower: str, rule: Dict[str, Any], context: Dict[str, Any] = None) -> bool:
        """Check if task matches a static rule"""
        # Keyword matching
        if 'keywords' in rule:
            if not any(keyword in task_lower for keyword in rule['keywords']):
                return False
        
        # File pattern matching
        if 'file_patterns' in rule and context and 'files' in context:
            if not any(pattern in str(f) for f in context['files'] for pattern in rule['file_patterns']):
                return False
        
        # Size constraints
        if 'max_lines' in rule and context and 'lines_changed' in context:
            if context['lines_changed'] > rule['max_lines']:
                return False
        
        return True
    
    def _calculate_pattern_similarity(self, task: str, pattern: Dict[str, Any], context: Dict[str, Any] = None) -> float:
        """Calculate similarity between task and learned pattern"""
        score = 0.0
        weights = {'keywords': 0.4, 'context': 0.3, 'performance': 0.3}
        
        # Keyword similarity
        task_words = set(task.lower().split())
        pattern_words = set(pattern['description'].lower().split())
        keyword_overlap = len(task_words & pattern_words) / max(len(task_words), 1)
        score += keyword_overlap * weights['keywords']
        
        # Context similarity
        if context and 'context_features' in pattern:
            context_score = self._compare_contexts(context, pattern['context_features'])
            score += context_score * weights['context']
        
        # Performance weighting
        if pattern['usage_count'] > 5:
            performance_score = pattern['success_rate'] * 0.7 + (1 - pattern['avg_cost'] / 100) * 0.3
            score += performance_score * weights['performance']
        
        return score
    
    def _analyze_task(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Analyze task characteristics for routing decision"""
        task_lower = task.lower()
        
        return {
            'is_simple': any(kw in task_lower for kw in ['fix', 'typo', 'rename', 'comment', 'simple']),
            'is_analysis': any(kw in task_lower for kw in ['analyze', 'review', 'find', 'search', 'check']),
            'is_security_critical': any(kw in task_lower for kw in ['security', 'auth', 'password', 'token', 'key']),
            'is_production': any(kw in task_lower for kw in ['production', 'deploy', 'release', 'critical']),
            'lines_changed': context.get('lines_changed', 0) if context else 0,
            'file_count': context.get('file_count', 1) if context else 1,
            'has_tests': 'test' in task_lower or (context and context.get('includes_tests', False))
        }
    
    def _estimate_cost(self, task: str, model: str) -> float:
        """Estimate cost for task based on model"""
        # Token estimation
        base_tokens = len(task) // 4
        response_multiplier = 15  # Average response length multiplier
        total_tokens = base_tokens * response_multiplier
        
        # Model pricing (per million tokens)
        pricing = {
            'qwen3_coder': 7.50,
            'gemini_flash': 0.26,
            'gemini_pro': 2.50,
            'opus': 30.00
        }
        
        cost_per_token = pricing.get(model, 10.00) / 1_000_000
        return total_tokens * cost_per_token
    
    def _get_context_limit(self, model: str) -> int:
        """Get context limit for model"""
        limits = {
            'qwen3_coder': 50000,
            'gemini_flash': 100000,
            'gemini_pro': 100000,
            'opus': 20000
        }
        return limits.get(model, 10000)
    
    def _generate_pattern_key(self, task: str) -> str:
        """Generate a key for pattern storage"""
        # Simple hash of task keywords
        keywords = sorted(set(task.lower().split()))[:5]
        return "_".join(keywords)
    
    def _update_average(self, current_avg: float, new_value: float, count: int) -> float:
        """Update running average"""
        return ((current_avg * (count - 1)) + new_value) / count
    
    def _compare_contexts(self, context1: Dict[str, Any], context2: Dict[str, Any]) -> float:
        """Compare two contexts for similarity"""
        # Simple feature comparison
        score = 0.0
        features = ['file_count', 'lines_changed', 'includes_tests', 'language']
        
        for feature in features:
            if feature in context1 and feature in context2:
                if isinstance(context1[feature], (int, float)):
                    # Numeric comparison
                    diff = abs(context1[feature] - context2[feature])
                    score += 1.0 / (1.0 + diff)
                else:
                    # Exact match
                    score += 1.0 if context1[feature] == context2[feature] else 0.0
        
        return score / len(features)
    
    def _load_config(self, config_path: Optional[Path] = None) -> Dict[str, Any]:
        """Load routing configuration"""
        if not config_path:
            config_path = Path(__file__).parent.parent.parent.parent / "config" / "agents" / "routing_rules.json"
        
        default_config = {
            'static_rules': [
                {
                    'keywords': ['typo', 'comment', 'rename'],
                    'model': 'gemini_flash',
                    'agent_type': 'implementation',
                    'confidence': 0.95,
                    'max_lines': 100,
                    'reason': 'Simple tasks best handled by fast, efficient model'
                },
                {
                    'keywords': ['security', 'auth', 'crypto'],
                    'model': 'opus',
                    'agent_type': 'quality_assurance',
                    'confidence': 1.0
                },
                {
                    'keywords': ['analyze', 'review', 'pattern'],
                    'model': 'gemini_flash',
                    'agent_type': 'analysis',
                    'confidence': 0.9
                }
            ],
            'learned_patterns': {}
        }
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        
        return default_config
    
    def _save_patterns(self):
        """Save learned patterns to configuration"""
        # Save to patterns file
        patterns_path = Path(__file__).parent.parent.parent.parent / "config" / "agents" / "learned_patterns.json"
        patterns_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(patterns_path, 'w') as f:
            json.dump(self.patterns, f, indent=2)
    
    def _generate_cache_key(self, task: str, context: Dict[str, Any] = None) -> str:
        """Generate a cache key for routing decision"""
        # Use first 100 chars of task + context features
        task_key = task[:100].lower().replace(' ', '_')
        
        if context:
            context_key = f"_f{context.get('file_count', 0)}_l{context.get('lines_changed', 0)}"
        else:
            context_key = "_nocontext"
        
        return f"{task_key}{context_key}"
    
    def _extract_task_pattern(self, task: str) -> str:
        """Extract a pattern from task for memory lookup"""
        # Simple keyword extraction
        keywords = []
        task_lower = task.lower()
        
        # Extract action keywords
        for action in ['implement', 'fix', 'add', 'update', 'refactor', 'analyze', 'test']:
            if action in task_lower:
                keywords.append(action)
                break
        
        # Extract component keywords
        for component in ['component', 'service', 'function', 'class', 'module', 'api']:
            if component in task_lower:
                keywords.append(component)
                break
        
        return '_'.join(keywords) if keywords else 'general_task'
    
    def _cache_and_capture_result(self, cache_key: str, result: RouteResult, 
                                 task: str, memory_context: List[Dict]) -> None:
        """Cache result and capture to memory"""
        # Cache the result
        self.routing_cache[cache_key] = result
        
        # Limit cache size
        if len(self.routing_cache) > 1000:
            # Remove oldest entries (simple FIFO)
            oldest_key = next(iter(self.routing_cache))
            del self.routing_cache[oldest_key]
        
        # Capture routing decision
        routing_data = {
            'task': task,
            'model': result.model,
            'agent_type': result.agent_type,
            'decision_type': result.decision_type.value,
            'confidence': result.confidence,
            'reasoning': result.reasoning,
            'estimated_cost': result.estimated_cost,
            'memory_context_used': len(memory_context) > 0 if memory_context else False
        }
        
        self.memory_integration.capture_routing_decision(routing_data)
    
    def get_routing_stats(self) -> Dict[str, Any]:
        """Get routing engine statistics"""
        cache_hit_rate = self.cache_hits / max(1, self.cache_hits + self.cache_misses)
        
        return {
            'cache_hits': self.cache_hits,
            'cache_misses': self.cache_misses,
            'cache_hit_rate': cache_hit_rate,
            'cache_size': len(self.routing_cache),
            'patterns_learned': len(self.patterns),
            'cost_tracker': {
                'daily_remaining': self.cost_tracker.get_daily_remaining(),
                'monthly_remaining': self.cost_tracker.get_monthly_remaining()
            }
        }


class CostTracker:
    """Track and manage API costs"""
    
    def __init__(self):
        self.daily_limit = 100.0  # $100 daily limit
        self.monthly_limit = 5000.0  # $5000 monthly limit
        self.costs_today = 0.0
        self.costs_month = 0.0
        self.last_reset = time.time()
        
    def add_cost(self, amount: float):
        """Add cost to tracker"""
        self.costs_today += amount
        self.costs_month += amount
        
    def get_daily_remaining(self) -> float:
        """Get remaining daily budget"""
        return max(0, self.daily_limit - self.costs_today)
    
    def get_monthly_remaining(self) -> float:
        """Get remaining monthly budget"""
        return max(0, self.monthly_limit - self.costs_month)
    
    def check_budget_alert(self) -> Optional[str]:
        """Check if budget alerts needed"""
        daily_percent = (self.costs_today / self.daily_limit) * 100
        monthly_percent = (self.costs_month / self.monthly_limit) * 100
        
        if daily_percent >= 100:
            return "CRITICAL: Daily budget exceeded!"
        elif daily_percent >= 90:
            return "WARNING: 90% of daily budget used"
        elif daily_percent >= 80:
            return "INFO: 80% of daily budget used"
        elif monthly_percent >= 90:
            return "WARNING: 90% of monthly budget used"
        
        return None