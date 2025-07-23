#!/usr/bin/env python3
"""
Monitor Memory Queue
Real-time monitoring of memory processing queue
"""

import os
import sys
import time
import json
import argparse
from datetime import datetime
from pathlib import Path
from collections import deque
import threading

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

class MemoryQueueMonitor:
    """Real-time memory queue monitoring"""
    
    def __init__(self, duration=300):
        self.duration = duration
        self.metrics = {
            "queue_depths": deque(maxlen=1000),
            "processing_times": deque(maxlen=1000),
            "throughput": deque(maxlen=60),  # Per-second throughput
            "errors": deque(maxlen=100),
            "storage_distribution": {"neo4j": 0, "supabase": 0, "both": 0, "none": 0}
        }
        self.running = True
        self.start_time = time.time()
        
    def display_dashboard(self):
        """Display real-time dashboard"""
        while self.running and (time.time() - self.start_time) < self.duration:
            # Clear screen
            os.system('clear' if os.name == 'posix' else 'cls')
            
            # Header
            print("🎯 MEMORY QUEUE MONITOR")
            print("=" * 60)
            print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Runtime: {int(time.time() - self.start_time)}s / {self.duration}s")
            print("=" * 60)
            
            # Queue Status
            print("\n📊 Queue Status:")
            print("-" * 30)
            current_depth = self.get_current_queue_depth()
            avg_depth = sum(self.metrics["queue_depths"]) / len(self.metrics["queue_depths"]) if self.metrics["queue_depths"] else 0
            max_depth = max(self.metrics["queue_depths"]) if self.metrics["queue_depths"] else 0
            
            print(f"Current Depth: {current_depth}")
            print(f"Average Depth: {avg_depth:.1f}")
            print(f"Max Depth: {max_depth}")
            
            # Processing Performance
            print("\n⚡ Processing Performance:")
            print("-" * 30)
            if self.metrics["processing_times"]:
                avg_time = sum(self.metrics["processing_times"]) / len(self.metrics["processing_times"])
                p99_time = sorted(self.metrics["processing_times"])[int(len(self.metrics["processing_times"]) * 0.99)]
                print(f"Avg Processing Time: {avg_time:.2f}ms")
                print(f"P99 Processing Time: {p99_time:.2f}ms")
            else:
                print("No processing data yet...")
            
            # Throughput
            print("\n📈 Throughput:")
            print("-" * 30)
            if self.metrics["throughput"]:
                current_throughput = self.metrics["throughput"][-1] if self.metrics["throughput"] else 0
                avg_throughput = sum(self.metrics["throughput"]) / len(self.metrics["throughput"])
                print(f"Current: {current_throughput:.1f} items/sec")
                print(f"Average: {avg_throughput:.1f} items/sec")
            else:
                print("Calculating...")
            
            # Storage Distribution
            print("\n💾 Storage Distribution:")
            print("-" * 30)
            total = sum(self.metrics["storage_distribution"].values())
            if total > 0:
                for storage, count in self.metrics["storage_distribution"].items():
                    percentage = (count / total) * 100
                    bar = "█" * int(percentage / 2)
                    print(f"{storage:>10}: {bar:<50} {percentage:>5.1f}% ({count})")
            else:
                print("No data processed yet...")
            
            # Recent Errors
            print("\n⚠️  Recent Errors:")
            print("-" * 30)
            if self.metrics["errors"]:
                for error in list(self.metrics["errors"])[-3:]:
                    print(f"[{error['time']}] {error['message'][:60]}...")
            else:
                print("No errors detected ✅")
            
            # Visual Queue Depth
            print("\n📉 Queue Depth (last 60 seconds):")
            if self.metrics["queue_depths"]:
                self.draw_mini_chart(list(self.metrics["queue_depths"])[-60:])
            
            # Refresh every second
            time.sleep(1)
        
        print("\n\n✅ Monitoring complete!")
        self.save_results()
    
    def get_current_queue_depth(self):
        """Get current queue depth (simulated)"""
        # In production, this would query the actual queue
        import random
        depth = random.randint(0, 100)
        self.metrics["queue_depths"].append(depth)
        return depth
    
    def update_metrics(self):
        """Update metrics in background thread"""
        while self.running:
            # Simulate metric updates
            import random
            
            # Processing times
            self.metrics["processing_times"].append(random.uniform(0.5, 5.0))
            
            # Throughput
            self.metrics["throughput"].append(random.uniform(8, 12))
            
            # Storage distribution (simulate processing)
            storage_type = random.choice(["neo4j", "supabase", "both", "none"])
            self.metrics["storage_distribution"][storage_type] += 1
            
            # Occasional errors
            if random.random() < 0.01:  # 1% error rate
                self.metrics["errors"].append({
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "message": random.choice([
                        "Neo4j connection timeout",
                        "Supabase rate limit exceeded",
                        "Invalid content format",
                        "Circuit breaker activated"
                    ])
                })
            
            time.sleep(0.1)
    
    def draw_mini_chart(self, values, height=10):
        """Draw a simple ASCII chart"""
        if not values:
            return
        
        max_val = max(values) if values else 1
        min_val = min(values) if values else 0
        
        # Normalize values to chart height
        normalized = []
        for v in values:
            if max_val > min_val:
                norm = int((v - min_val) / (max_val - min_val) * height)
            else:
                norm = height // 2
            normalized.append(norm)
        
        # Draw chart
        for h in range(height, -1, -1):
            line = ""
            for n in normalized:
                if n >= h:
                    line += "█"
                else:
                    line += " "
            print(f"{str(int(max_val * h / height)).rjust(4)} |{line}")
        
        print("     " + "-" * len(normalized))
        print(f"     {min_val} {'':>{len(normalized)-10}} {max_val}")
    
    def save_results(self):
        """Save monitoring results"""
        results = {
            "monitoring_duration_seconds": self.duration,
            "start_time": datetime.fromtimestamp(self.start_time).isoformat(),
            "end_time": datetime.now().isoformat(),
            "summary": {
                "avg_queue_depth": sum(self.metrics["queue_depths"]) / len(self.metrics["queue_depths"]) if self.metrics["queue_depths"] else 0,
                "max_queue_depth": max(self.metrics["queue_depths"]) if self.metrics["queue_depths"] else 0,
                "avg_processing_time_ms": sum(self.metrics["processing_times"]) / len(self.metrics["processing_times"]) if self.metrics["processing_times"] else 0,
                "avg_throughput": sum(self.metrics["throughput"]) / len(self.metrics["throughput"]) if self.metrics["throughput"] else 0,
                "total_errors": len(self.metrics["errors"]),
                "storage_distribution": dict(self.metrics["storage_distribution"])
            },
            "raw_metrics": {
                "queue_depths": list(self.metrics["queue_depths"]),
                "processing_times": list(self.metrics["processing_times"]),
                "throughput": list(self.metrics["throughput"]),
                "errors": list(self.metrics["errors"])
            }
        }
        
        output_file = f"queue-monitor-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"Results saved to: {output_file}")
    
    def run(self):
        """Run the monitor"""
        # Start metrics update thread
        update_thread = threading.Thread(target=self.update_metrics, daemon=True)
        update_thread.start()
        
        # Display dashboard
        try:
            self.display_dashboard()
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped by user.")
        finally:
            self.running = False

def main():
    parser = argparse.ArgumentParser(description="Monitor memory processing queue")
    parser.add_argument("--duration", type=int, default=300, 
                        help="Monitoring duration in seconds (default: 300)")
    
    args = parser.parse_args()
    
    print("Starting Memory Queue Monitor...")
    print(f"Duration: {args.duration} seconds")
    print("Press Ctrl+C to stop early\n")
    
    time.sleep(2)
    
    monitor = MemoryQueueMonitor(duration=args.duration)
    monitor.run()

if __name__ == "__main__":
    main()