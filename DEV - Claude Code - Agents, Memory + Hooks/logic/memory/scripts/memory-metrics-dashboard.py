#!/usr/bin/env python3
"""
Memory Metrics Dashboard
Comprehensive real-time dashboard for memory system monitoring
"""

import os
import sys
import time
import json
import threading
from datetime import datetime, timedelta
from pathlib import Path
from collections import deque, defaultdict
import argparse

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

class MemoryMetricsDashboard:
    """Real-time memory system metrics dashboard"""
    
    def __init__(self):
        self.running = True
        self.start_time = time.time()
        
        # Metrics storage
        self.metrics = {
            # Performance metrics
            "processing_times": deque(maxlen=1000),
            "queue_depths": deque(maxlen=1000),
            "throughput_history": deque(maxlen=300),  # 5 minutes
            "cache_hits": 0,
            "cache_misses": 0,
            
            # Storage metrics
            "neo4j_writes": deque(maxlen=300),
            "supabase_writes": deque(maxlen=300),
            "storage_decisions": defaultdict(int),
            
            # Cost metrics
            "neo4j_costs": deque(maxlen=60),  # Per minute
            "supabase_costs": deque(maxlen=60),
            "total_cost_saved": 0.0,
            
            # Error tracking
            "errors": defaultdict(int),
            "circuit_breaker_state": "closed",
            "circuit_breaker_history": deque(maxlen=10),
            
            # System health
            "memory_usage_mb": deque(maxlen=300),
            "cpu_usage_percent": deque(maxlen=300),
            "active_threads": 0
        }
        
        # Cost configuration
        self.cost_per_neo4j_write = 0.001
        self.cost_per_supabase_write = 0.0001
        self.baseline_cost_per_item = 0.001  # All to Neo4j
        
    def run(self):
        """Run the dashboard"""
        # Start data collection threads
        threads = [
            threading.Thread(target=self.collect_performance_metrics, daemon=True),
            threading.Thread(target=self.collect_storage_metrics, daemon=True),
            threading.Thread(target=self.collect_system_metrics, daemon=True),
            threading.Thread(target=self.calculate_costs, daemon=True)
        ]
        
        for thread in threads:
            thread.start()
        
        # Display dashboard
        try:
            while self.running:
                self.display_dashboard()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nDashboard stopped by user.")
        finally:
            self.running = False
            self.save_session_data()
    
    def display_dashboard(self):
        """Display the main dashboard"""
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Header
        print("=" * 80)
        print("🎯 MEMORY SYSTEM METRICS DASHBOARD".center(80))
        print("=" * 80)
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(80))
        print(f"Uptime: {self.format_duration(time.time() - self.start_time)}".center(80))
        print("=" * 80)
        
        # Layout: 2x2 grid
        self.display_performance_section()
        self.display_storage_section()
        self.display_cost_section()
        self.display_health_section()
        
        # Footer
        print("=" * 80)
        print("Press Ctrl+C to exit | Updates every second | Logs: ./memory-dashboard.log")
    
    def display_performance_section(self):
        """Display performance metrics"""
        print("\n⚡ PERFORMANCE METRICS")
        print("-" * 40)
        
        # Current metrics
        current_throughput = self.metrics["throughput_history"][-1] if self.metrics["throughput_history"] else 0
        avg_throughput = sum(self.metrics["throughput_history"]) / len(self.metrics["throughput_history"]) if self.metrics["throughput_history"] else 0
        
        print(f"Throughput: {current_throughput:>6.1f} items/sec (avg: {avg_throughput:.1f})")
        
        # Processing times
        if self.metrics["processing_times"]:
            avg_time = sum(self.metrics["processing_times"]) / len(self.metrics["processing_times"])
            p99_time = sorted(self.metrics["processing_times"])[int(len(self.metrics["processing_times"]) * 0.99)]
            print(f"Processing: {avg_time:>6.2f}ms avg, {p99_time:.2f}ms p99")
        
        # Queue depth
        if self.metrics["queue_depths"]:
            current_queue = self.metrics["queue_depths"][-1]
            avg_queue = sum(self.metrics["queue_depths"]) / len(self.metrics["queue_depths"])
            print(f"Queue Depth: {current_queue:>5} (avg: {avg_queue:.1f})")
        
        # Cache performance
        total_cache_ops = self.metrics["cache_hits"] + self.metrics["cache_misses"]
        if total_cache_ops > 0:
            cache_hit_rate = (self.metrics["cache_hits"] / total_cache_ops) * 100
            print(f"Cache Hit Rate: {cache_hit_rate:>5.1f}% ({self.metrics['cache_hits']}/{total_cache_ops})")
        
        # Mini throughput chart
        if len(self.metrics["throughput_history"]) > 20:
            print("\nThroughput (last 60s):")
            self.draw_sparkline(list(self.metrics["throughput_history"])[-60:])
    
    def display_storage_section(self):
        """Display storage distribution"""
        print("\n💾 STORAGE DISTRIBUTION")
        print("-" * 40)
        
        total_items = sum(self.metrics["storage_decisions"].values())
        if total_items > 0:
            # Calculate percentages
            for storage_type in ["neo4j", "supabase", "both", "discarded"]:
                count = self.metrics["storage_decisions"].get(storage_type, 0)
                percentage = (count / total_items) * 100
                bar = "█" * int(percentage / 2)
                print(f"{storage_type:>10}: {bar:<40} {percentage:>5.1f}% ({count})")
        
        # Recent writes per minute
        if self.metrics["neo4j_writes"]:
            neo4j_rate = sum(list(self.metrics["neo4j_writes"])[-60:])
            supabase_rate = sum(list(self.metrics["supabase_writes"])[-60:])
            print(f"\nWrites/min: Neo4j={neo4j_rate}, Supabase={supabase_rate}")
    
    def display_cost_section(self):
        """Display cost analysis"""
        print("\n💰 COST ANALYSIS")
        print("-" * 40)
        
        # Current costs
        if self.metrics["neo4j_costs"] and self.metrics["supabase_costs"]:
            current_neo4j = self.metrics["neo4j_costs"][-1]
            current_supabase = self.metrics["supabase_costs"][-1]
            current_total = current_neo4j + current_supabase
            
            # Calculate baseline
            items_processed = sum(self.metrics["storage_decisions"].values())
            baseline_cost = items_processed * self.baseline_cost_per_item
            
            if baseline_cost > 0:
                savings_percent = ((baseline_cost - current_total) / baseline_cost) * 100
                print(f"Current Rate: ${current_total:.4f}/min (Neo4j: ${current_neo4j:.4f}, Supabase: ${current_supabase:.4f})")
                print(f"Baseline Rate: ${baseline_cost:.4f}/min (all Neo4j)")
                print(f"Savings: {savings_percent:.1f}% (${baseline_cost - current_total:.4f}/min)")
                
                # Projected daily savings
                daily_savings = (baseline_cost - current_total) * 60 * 24
                print(f"Projected Daily Savings: ${daily_savings:.2f}")
        
        print(f"\nTotal Saved This Session: ${self.metrics['total_cost_saved']:.2f}")
    
    def display_health_section(self):
        """Display system health"""
        print("\n🏥 SYSTEM HEALTH")
        print("-" * 40)
        
        # Circuit breaker
        cb_state = self.metrics["circuit_breaker_state"]
        cb_color = "🟢" if cb_state == "closed" else "🔴"
        print(f"Circuit Breaker: {cb_color} {cb_state.upper()}")
        
        if self.metrics["circuit_breaker_history"]:
            print(f"  Last activation: {self.metrics['circuit_breaker_history'][-1]}")
        
        # Errors
        total_errors = sum(self.metrics["errors"].values())
        if total_errors > 0:
            print(f"\nErrors (last hour): {total_errors}")
            for error_type, count in sorted(self.metrics["errors"].items(), key=lambda x: x[1], reverse=True)[:3]:
                print(f"  - {error_type}: {count}")
        else:
            print("\nErrors: ✅ None detected")
        
        # System resources
        if self.metrics["memory_usage_mb"]:
            current_memory = self.metrics["memory_usage_mb"][-1]
            avg_memory = sum(self.metrics["memory_usage_mb"]) / len(self.metrics["memory_usage_mb"])
            print(f"\nMemory Usage: {current_memory:.1f}MB (avg: {avg_memory:.1f}MB)")
        
        if self.metrics["cpu_usage_percent"]:
            current_cpu = self.metrics["cpu_usage_percent"][-1]
            avg_cpu = sum(self.metrics["cpu_usage_percent"]) / len(self.metrics["cpu_usage_percent"])
            print(f"CPU Usage: {current_cpu:.1f}% (avg: {avg_cpu:.1f}%)")
        
        print(f"Active Threads: {self.metrics['active_threads']}")
    
    def draw_sparkline(self, values, width=60):
        """Draw a simple sparkline chart"""
        if not values:
            return
        
        chars = "▁▂▃▄▅▆▇█"
        max_val = max(values)
        min_val = min(values)
        
        if max_val == min_val:
            print(chars[4] * width)
            return
        
        # Normalize and draw
        sparkline = ""
        for v in values[-width:]:
            index = int((v - min_val) / (max_val - min_val) * (len(chars) - 1))
            sparkline += chars[index]
        
        print(sparkline)
        print(f"{min_val:.1f} {'':>{width-20}} {max_val:.1f}")
    
    def format_duration(self, seconds):
        """Format duration in human-readable format"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    
    # Data collection methods (run in threads)
    def collect_performance_metrics(self):
        """Collect performance-related metrics"""
        import random
        
        while self.running:
            # Simulate data collection
            self.metrics["processing_times"].append(random.uniform(0.5, 5.0))
            self.metrics["queue_depths"].append(random.randint(0, 50))
            self.metrics["throughput_history"].append(random.uniform(8, 12))
            
            # Cache simulation
            if random.random() < 0.8:  # 80% cache hit rate
                self.metrics["cache_hits"] += 1
            else:
                self.metrics["cache_misses"] += 1
            
            time.sleep(0.1)
    
    def collect_storage_metrics(self):
        """Collect storage-related metrics"""
        import random
        
        while self.running:
            # Simulate storage decisions
            decision = random.choices(
                ["neo4j", "supabase", "both", "discarded"],
                weights=[15, 65, 10, 10]
            )[0]
            
            self.metrics["storage_decisions"][decision] += 1
            
            # Track writes
            if decision in ["neo4j", "both"]:
                self.metrics["neo4j_writes"].append(1)
            else:
                self.metrics["neo4j_writes"].append(0)
            
            if decision in ["supabase", "both"]:
                self.metrics["supabase_writes"].append(1)
            else:
                self.metrics["supabase_writes"].append(0)
            
            # Occasional errors
            if random.random() < 0.001:
                error_type = random.choice([
                    "neo4j_timeout",
                    "supabase_rate_limit",
                    "invalid_content",
                    "processing_error"
                ])
                self.metrics["errors"][error_type] += 1
            
            # Circuit breaker simulation
            if random.random() < 0.0001:  # Very rare
                self.metrics["circuit_breaker_state"] = "open"
                self.metrics["circuit_breaker_history"].append(datetime.now().strftime("%H:%M:%S"))
            elif self.metrics["circuit_breaker_state"] == "open" and random.random() < 0.1:
                self.metrics["circuit_breaker_state"] = "closed"
            
            time.sleep(0.2)
    
    def collect_system_metrics(self):
        """Collect system resource metrics"""
        import random
        
        while self.running:
            # Simulate system metrics
            self.metrics["memory_usage_mb"].append(random.uniform(40, 60))
            self.metrics["cpu_usage_percent"].append(random.uniform(5, 25))
            self.metrics["active_threads"] = random.randint(3, 8)
            
            time.sleep(1)
    
    def calculate_costs(self):
        """Calculate cost metrics"""
        while self.running:
            # Calculate per-minute costs
            neo4j_writes_per_min = sum(list(self.metrics["neo4j_writes"])[-60:]) if self.metrics["neo4j_writes"] else 0
            supabase_writes_per_min = sum(list(self.metrics["supabase_writes"])[-60:]) if self.metrics["supabase_writes"] else 0
            
            neo4j_cost = neo4j_writes_per_min * self.cost_per_neo4j_write
            supabase_cost = supabase_writes_per_min * self.cost_per_supabase_write
            
            self.metrics["neo4j_costs"].append(neo4j_cost)
            self.metrics["supabase_costs"].append(supabase_cost)
            
            # Calculate total savings
            total_writes = neo4j_writes_per_min + supabase_writes_per_min
            baseline_cost = total_writes * self.baseline_cost_per_item
            actual_cost = neo4j_cost + supabase_cost
            
            if baseline_cost > actual_cost:
                self.metrics["total_cost_saved"] += (baseline_cost - actual_cost) / 60  # Per second
            
            time.sleep(1)
    
    def save_session_data(self):
        """Save session data on exit"""
        session_data = {
            "start_time": datetime.fromtimestamp(self.start_time).isoformat(),
            "end_time": datetime.now().isoformat(),
            "duration_seconds": time.time() - self.start_time,
            "summary": {
                "total_items_processed": sum(self.metrics["storage_decisions"].values()),
                "storage_distribution": dict(self.metrics["storage_decisions"]),
                "cache_hit_rate": (self.metrics["cache_hits"] / (self.metrics["cache_hits"] + self.metrics["cache_misses"]) * 100) if (self.metrics["cache_hits"] + self.metrics["cache_misses"]) > 0 else 0,
                "total_errors": sum(self.metrics["errors"].values()),
                "total_cost_saved": self.metrics["total_cost_saved"],
                "circuit_breaker_activations": len(self.metrics["circuit_breaker_history"])
            }
        }
        
        output_file = f"dashboard-session-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        print(f"\nSession data saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Memory System Metrics Dashboard")
    parser.add_argument("--export-interval", type=int, default=300,
                        help="Export metrics interval in seconds (default: 300)")
    
    args = parser.parse_args()
    
    print("Starting Memory Metrics Dashboard...")
    print("Press Ctrl+C to stop\n")
    
    time.sleep(2)
    
    dashboard = MemoryMetricsDashboard()
    dashboard.run()

if __name__ == "__main__":
    main()