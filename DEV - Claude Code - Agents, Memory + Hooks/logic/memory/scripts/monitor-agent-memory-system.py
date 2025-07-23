#!/usr/bin/env python3
"""
Agent Memory System Monitoring Dashboard
Real-time monitoring of memory filter performance, agent routing, and cost optimization
"""

import json
import time
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
import threading
from collections import deque

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the systems we're monitoring
from agents.integrations.memory_filter_integration import AgentMemoryIntegration
from agents.core.orchestrator import Orchestrator
from agents.core.routing_engine import SmartRoutingEngine
from memory.crawl4ai_memory_filter_optimized import OptimizedCrawl4AIMemoryFilter

class AgentMemoryMonitor:
    """Monitor and display real-time metrics for agent memory system"""
    
    def __init__(self):
        self.running = True
        self.metrics_history = {
            'memory_filter': deque(maxlen=100),
            'routing': deque(maxlen=100),
            'orchestration': deque(maxlen=100),
            'cost': deque(maxlen=100)
        }
        
        # Initialize components
        self.memory_integration = AgentMemoryIntegration()
        self.routing_engine = SmartRoutingEngine()
        
        # Initialize orchestrator with config
        orchestrator_config = {
            'routing_rules': {},
            'cost_limits': {'daily': 100, 'monthly': 5000},
            'model_configs': {
                'qwen3_coder': {'context_limit': 50000, 'cost_per_token': 0.0000075},
                'gemini_flash': {'context_limit': 100000, 'cost_per_token': 0.00000026},
                'opus': {'context_limit': 20000, 'cost_per_token': 0.00003}
            }
        }
        self.orchestrator = Orchestrator(orchestrator_config)
        
        # Metrics update thread
        self.update_thread = threading.Thread(target=self._update_metrics_loop, daemon=True)
        self.update_thread.start()
    
    def _update_metrics_loop(self):
        """Background thread to update metrics"""
        while self.running:
            timestamp = datetime.now().isoformat()
            
            # Collect memory filter stats
            memory_stats = self.memory_integration.memory_filter.get_stats()
            self.metrics_history['memory_filter'].append({
                'timestamp': timestamp,
                'stats': memory_stats
            })
            
            # Collect routing stats
            routing_stats = self.routing_engine.get_routing_stats()
            self.metrics_history['routing'].append({
                'timestamp': timestamp,
                'stats': routing_stats
            })
            
            # Collect orchestration stats
            orchestration_stats = self.orchestrator.get_orchestration_metrics()
            self.metrics_history['orchestration'].append({
                'timestamp': timestamp,
                'stats': orchestration_stats
            })
            
            # Calculate cost metrics
            cost_metrics = self._calculate_cost_metrics()
            self.metrics_history['cost'].append({
                'timestamp': timestamp,
                'stats': cost_metrics
            })
            
            time.sleep(5)  # Update every 5 seconds
    
    def _calculate_cost_metrics(self) -> Dict[str, Any]:
        """Calculate cost optimization metrics"""
        orchestration = self.orchestrator.orchestration_metrics
        
        total_decisions = len(orchestration['routing_decisions'])
        if total_decisions == 0:
            return {'no_data': True}
        
        # Calculate average savings
        total_savings = sum(d['savings_percent'] for d in orchestration['routing_decisions'])
        avg_savings = total_savings / total_decisions if total_decisions > 0 else 0
        
        # Model distribution
        model_counts = {}
        for decision in orchestration['routing_decisions']:
            model = decision['model']
            model_counts[model] = model_counts.get(model, 0) + 1
        
        return {
            'total_decisions': total_decisions,
            'average_savings_percent': avg_savings,
            'total_cost_saved': orchestration['cost_savings'],
            'model_distribution': model_counts
        }
    
    def display_dashboard(self):
        """Display real-time monitoring dashboard"""
        print("\033[2J\033[H")  # Clear screen
        print("=" * 80)
        print("🎯 AGENT MEMORY SYSTEM MONITORING DASHBOARD")
        print("=" * 80)
        print(f"Last Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Memory Filter Performance
        if self.metrics_history['memory_filter']:
            latest_memory = self.metrics_history['memory_filter'][-1]['stats']
            print("📊 MEMORY FILTER PERFORMANCE")
            print("-" * 40)
            
            if 'avg_processing_time_ms' in latest_memory:
                print(f"Avg Processing Time: {latest_memory['avg_processing_time_ms']:.2f}ms")
                print(f"Throughput: {latest_memory.get('throughput_per_second', 0):.2f} items/sec")
                
                if 'storage_distribution' in latest_memory:
                    dist = latest_memory['storage_distribution']
                    total = sum(dist.values()) or 1
                    print(f"Storage Distribution:")
                    print(f"  - Neo4j: {dist.get('both', 0) + dist.get('neo4j', 0)} ({(dist.get('both', 0) + dist.get('neo4j', 0))/total*100:.1f}%)")
                    print(f"  - Supabase: {dist.get('supabase', 0)} ({dist.get('supabase', 0)/total*100:.1f}%)")
                    print(f"  - Rejected: {dist.get('none', 0)} ({dist.get('none', 0)/total*100:.1f}%)")
                
                if 'cache' in latest_memory:
                    cache = latest_memory['cache']
                    print(f"Cache Hit Rate: {cache.get('hit_rate', 0)*100:.1f}%")
                
                print(f"Entity Extractions Skipped: {latest_memory.get('entity_extractions_skipped', 0)}")
        
        print()
        
        # Routing Engine Performance
        if self.metrics_history['routing']:
            latest_routing = self.metrics_history['routing'][-1]['stats']
            print("🚦 ROUTING ENGINE PERFORMANCE")
            print("-" * 40)
            print(f"Cache Hit Rate: {latest_routing.get('cache_hit_rate', 0)*100:.1f}%")
            print(f"Patterns Learned: {latest_routing.get('patterns_learned', 0)}")
            print(f"Daily Budget Remaining: ${latest_routing['cost_tracker']['daily_remaining']:.2f}")
            print(f"Monthly Budget Remaining: ${latest_routing['cost_tracker']['monthly_remaining']:.2f}")
        
        print()
        
        # Cost Optimization
        if self.metrics_history['cost']:
            latest_cost = self.metrics_history['cost'][-1]['stats']
            if not latest_cost.get('no_data'):
                print("💰 COST OPTIMIZATION")
                print("-" * 40)
                print(f"Total Routing Decisions: {latest_cost['total_decisions']}")
                print(f"Average Savings: {latest_cost['average_savings_percent']:.1f}%")
                print(f"Total Cost Saved: ${latest_cost['total_cost_saved']:.2f}")
                
                if 'model_distribution' in latest_cost:
                    print("Model Distribution:")
                    for model, count in latest_cost['model_distribution'].items():
                        percent = (count / latest_cost['total_decisions']) * 100
                        print(f"  - {model}: {count} ({percent:.1f}%)")
        
        print()
        
        # Queue Status
        if self.metrics_history['memory_filter']:
            latest_memory = self.metrics_history['memory_filter'][-1]['stats']
            if 'queue' in latest_memory:
                queue_info = latest_memory['queue']
                print("📥 QUEUE STATUS")
                print("-" * 40)
                print(f"Current Depth: {queue_info.get('current_depth', 0)}/{queue_info.get('max_size', 1000)}")
                print(f"Avg Queue Depth: {latest_memory.get('avg_queue_depth', 0):.1f}")
        
        print()
        
        # Circuit Breaker Status
        if self.metrics_history['memory_filter']:
            latest_memory = self.metrics_history['memory_filter'][-1]['stats']
            if 'circuit_breaker' in latest_memory:
                cb = latest_memory['circuit_breaker']
                status = "🔴 OPEN" if cb['is_open'] else "🟢 CLOSED"
                print(f"⚡ CIRCUIT BREAKER: {status}")
                if cb['failure_count'] > 0:
                    print(f"   Failure Count: {cb['failure_count']}")
        
        print()
        print("=" * 80)
        print("Press Ctrl+C to exit")
    
    def run_interactive(self):
        """Run interactive monitoring dashboard"""
        try:
            while True:
                self.display_dashboard()
                time.sleep(2)  # Refresh every 2 seconds
        except KeyboardInterrupt:
            print("\n\nShutting down monitor...")
            self.running = False
            self.save_metrics_history()
    
    def save_metrics_history(self):
        """Save metrics history to file"""
        history_file = Path(__file__).parent.parent.parent / 'logs' / 'agent_memory_metrics.json'
        history_file.parent.mkdir(exist_ok=True)
        
        # Convert deques to lists for JSON serialization
        history_data = {
            key: list(values) for key, values in self.metrics_history.items()
        }
        
        with open(history_file, 'w') as f:
            json.dump(history_data, f, indent=2)
        
        print(f"Metrics saved to: {history_file}")
    
    def generate_report(self) -> str:
        """Generate a summary report of system performance"""
        report = []
        report.append("AGENT MEMORY SYSTEM PERFORMANCE REPORT")
        report.append("=" * 50)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Memory Filter Summary
        if self.metrics_history['memory_filter']:
            memory_metrics = [m['stats'] for m in self.metrics_history['memory_filter']]
            avg_processing = sum(m.get('avg_processing_time_ms', 0) for m in memory_metrics) / len(memory_metrics)
            report.append("MEMORY FILTER PERFORMANCE:")
            report.append(f"- Average Processing Time: {avg_processing:.2f}ms")
            report.append(f"- Total Processed: {memory_metrics[-1].get('total_processed', 0)}")
        
        # Cost Optimization Summary
        if self.metrics_history['cost']:
            cost_metrics = [m['stats'] for m in self.metrics_history['cost'] if not m['stats'].get('no_data')]
            if cost_metrics:
                total_saved = cost_metrics[-1].get('total_cost_saved', 0)
                avg_savings = sum(m.get('average_savings_percent', 0) for m in cost_metrics) / len(cost_metrics)
                report.append("")
                report.append("COST OPTIMIZATION:")
                report.append(f"- Total Saved: ${total_saved:.2f}")
                report.append(f"- Average Savings: {avg_savings:.1f}%")
        
        return "\n".join(report)


def main():
    """Run the monitoring dashboard"""
    monitor = AgentMemoryMonitor()
    
    print("Starting Agent Memory System Monitor...")
    print("Loading initial metrics...")
    time.sleep(3)  # Allow time for initial metrics collection
    
    # Run interactive dashboard
    monitor.run_interactive()
    
    # Generate final report
    print("\n" + monitor.generate_report())


if __name__ == '__main__':
    main()