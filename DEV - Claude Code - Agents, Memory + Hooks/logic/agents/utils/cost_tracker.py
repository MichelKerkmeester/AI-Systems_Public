#!/usr/bin/env python3
"""
Cost tracking and budget management for Unified Agent Architecture v3
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class CostTracker:
    """Track API costs and enforce budget limits"""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path.home() / '.claude' / 'agent_costs.json'
        self.daily_limit = 100.0  # $100 daily limit
        self.monthly_limit = 5000.0  # $5000 monthly limit
        self.alert_thresholds = [0.8, 0.9, 1.0]  # 80%, 90%, 100%
        
        # Load existing cost data
        self.cost_data = self._load_cost_data()
        
    def add_cost(self, amount: float, model: str, task_id: str, 
                 tokens: int, context: Dict = None) -> None:
        """Record a cost entry"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'amount': amount,
            'model': model,
            'task_id': task_id,
            'tokens': tokens,
            'context': context or {}
        }
        
        # Add to today's costs
        today = datetime.now().date().isoformat()
        if today not in self.cost_data['daily']:
            self.cost_data['daily'][today] = {
                'total': 0.0,
                'entries': []
            }
        
        self.cost_data['daily'][today]['total'] += amount
        self.cost_data['daily'][today]['entries'].append(entry)
        
        # Update monthly total
        month = datetime.now().strftime('%Y-%m')
        if month not in self.cost_data['monthly']:
            self.cost_data['monthly'][month] = 0.0
        self.cost_data['monthly'][month] += amount
        
        # Update model statistics
        if model not in self.cost_data['by_model']:
            self.cost_data['by_model'][model] = {
                'total': 0.0,
                'count': 0,
                'tokens': 0
            }
        
        self.cost_data['by_model'][model]['total'] += amount
        self.cost_data['by_model'][model]['count'] += 1
        self.cost_data['by_model'][model]['tokens'] += tokens
        
        # Save updated data
        self._save_cost_data()
        
        # Check for alerts
        self._check_budget_alerts()
        
    def get_daily_spent(self) -> float:
        """Get amount spent today"""
        today = datetime.now().date().isoformat()
        return self.cost_data['daily'].get(today, {}).get('total', 0.0)
    
    def get_daily_remaining(self) -> float:
        """Get remaining daily budget"""
        return max(0, self.daily_limit - self.get_daily_spent())
    
    def get_monthly_spent(self) -> float:
        """Get amount spent this month"""
        month = datetime.now().strftime('%Y-%m')
        return self.cost_data['monthly'].get(month, 0.0)
    
    def get_monthly_remaining(self) -> float:
        """Get remaining monthly budget"""
        return max(0, self.monthly_limit - self.get_monthly_spent())
    
    def can_afford(self, estimated_cost: float) -> Tuple[bool, Optional[str]]:
        """Check if we can afford an estimated cost"""
        daily_remaining = self.get_daily_remaining()
        monthly_remaining = self.get_monthly_remaining()
        
        if estimated_cost > daily_remaining:
            return False, f"Exceeds daily budget (${daily_remaining:.2f} remaining)"
        
        if estimated_cost > monthly_remaining:
            return False, f"Exceeds monthly budget (${monthly_remaining:.2f} remaining)"
        
        return True, None
    
    def get_cost_summary(self) -> Dict[str, Any]:
        """Get comprehensive cost summary"""
        return {
            'daily': {
                'spent': self.get_daily_spent(),
                'remaining': self.get_daily_remaining(),
                'limit': self.daily_limit,
                'percentage': (self.get_daily_spent() / self.daily_limit) * 100
            },
            'monthly': {
                'spent': self.get_monthly_spent(),
                'remaining': self.get_monthly_remaining(),
                'limit': self.monthly_limit,
                'percentage': (self.get_monthly_spent() / self.monthly_limit) * 100
            },
            'by_model': self.cost_data['by_model'],
            'last_7_days': self._get_last_n_days_costs(7),
            'top_tasks': self._get_top_cost_tasks(10)
        }
    
    def get_model_efficiency(self) -> Dict[str, Any]:
        """Analyze model cost efficiency"""
        efficiency = {}
        
        for model, stats in self.cost_data['by_model'].items():
            if stats['tokens'] > 0:
                efficiency[model] = {
                    'total_cost': stats['total'],
                    'total_tokens': stats['tokens'],
                    'cost_per_1k_tokens': (stats['total'] / stats['tokens']) * 1000,
                    'usage_count': stats['count'],
                    'avg_cost_per_task': stats['total'] / max(stats['count'], 1)
                }
        
        return efficiency
    
    def optimize_routing(self) -> Dict[str, Any]:
        """Suggest routing optimizations based on cost data"""
        suggestions = []
        
        # Analyze cost patterns
        daily_costs = self._get_last_n_days_costs(7)
        avg_daily = sum(daily_costs.values()) / max(len(daily_costs), 1)
        
        if avg_daily > self.daily_limit * 0.8:
            suggestions.append({
                'type': 'budget_warning',
                'message': f'Average daily spend ${avg_daily:.2f} is close to limit',
                'action': 'Increase usage of cheaper models (QWEN3, Gemini Flash)'
            })
        
        # Check model distribution
        model_costs = self.cost_data['by_model']
        if 'opus' in model_costs and model_costs['opus']['total'] > sum(m['total'] for m in model_costs.values()) * 0.5:
            suggestions.append({
                'type': 'model_imbalance',
                'message': 'Over 50% of costs from Opus model',
                'action': 'Route more tasks to QWEN3 or Gemini Flash'
            })
        
        return {
            'suggestions': suggestions,
            'potential_savings': self._calculate_potential_savings()
        }
    
    def _check_budget_alerts(self) -> None:
        """Check and log budget alerts"""
        daily_percent = (self.get_daily_spent() / self.daily_limit) * 100
        monthly_percent = (self.get_monthly_spent() / self.monthly_limit) * 100
        
        for threshold in self.alert_thresholds:
            if daily_percent >= threshold * 100:
                logger.warning(f"Daily budget at {daily_percent:.1f}% (${self.get_daily_spent():.2f})")
            
            if monthly_percent >= threshold * 100:
                logger.warning(f"Monthly budget at {monthly_percent:.1f}% (${self.get_monthly_spent():.2f})")
    
    def _get_last_n_days_costs(self, n: int) -> Dict[str, float]:
        """Get costs for last n days"""
        costs = {}
        today = datetime.now().date()
        
        for i in range(n):
            date = (today - timedelta(days=i)).isoformat()
            costs[date] = self.cost_data['daily'].get(date, {}).get('total', 0.0)
        
        return costs
    
    def _get_top_cost_tasks(self, n: int) -> List[Dict[str, Any]]:
        """Get top n most expensive tasks"""
        all_tasks = []
        
        for day_data in self.cost_data['daily'].values():
            all_tasks.extend(day_data.get('entries', []))
        
        # Sort by cost
        all_tasks.sort(key=lambda x: x['amount'], reverse=True)
        
        return all_tasks[:n]
    
    def _calculate_potential_savings(self) -> float:
        """Calculate potential savings by optimizing model usage"""
        potential_savings = 0.0
        
        # Calculate savings if Opus tasks were routed to QWEN3
        opus_costs = self.cost_data['by_model'].get('opus', {})
        if opus_costs:
            # Assume 70% of Opus tasks could use QWEN3 Coder
            opus_total = opus_costs['total']
            qwen_equivalent = opus_total * (7.50 / 30.00)  # QWEN3 is 4x cheaper
            potential_savings = opus_total - qwen_equivalent
        
        return potential_savings * 0.7  # Conservative estimate
    
    def _load_cost_data(self) -> Dict[str, Any]:
        """Load cost data from file"""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load cost data: {e}")
        
        # Return default structure
        return {
            'daily': {},
            'monthly': {},
            'by_model': {},
            'metadata': {
                'created': datetime.now().isoformat(),
                'version': '1.0'
            }
        }
    
    def _save_cost_data(self) -> None:
        """Save cost data to file"""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, 'w') as f:
                json.dump(self.cost_data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save cost data: {e}")