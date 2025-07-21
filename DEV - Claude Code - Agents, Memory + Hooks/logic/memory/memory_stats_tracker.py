#!/usr/bin/env python3
"""
Memory Statistics Tracker
Tracks memory capture metrics with enhanced performance and pattern analysis
"""

import json
import time
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, List, Optional, Tuple
from collections import defaultdict
import threading


class MemoryStatsTracker:
    """
    Singleton pattern memory stats tracker with enhanced functionality
    Tracks daily captures, automation rates, performance metrics, and pattern hit rates
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Ensure singleton pattern"""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize stats tracker with persistent storage"""
        # Skip if already initialized (singleton)
        if hasattr(self, '_initialized'):
            return
            
        self._initialized = True
        self.stats_file = Path(__file__).parent.parent.parent / "state" / "memory_stats.json"
        self.stats_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Performance tracking
        self._capture_start_times = {}  # Track capture latency
        self._queue_start_times = {}    # Track queue processing time
        
        # Load existing stats
        self.stats = self._load_stats()
        
        # Check and reset daily stats if needed
        self._check_daily_reset()
        
    def _load_stats(self) -> Dict[str, Any]:
        """Load existing statistics from persistent storage"""
        if self.stats_file.exists():
            try:
                with open(self.stats_file) as f:
                    data = json.load(f)
                    # Convert string keys back to proper types
                    for key in ['pattern_types', 'sources', 'automation_levels', 'sessions']:
                        if key in data and isinstance(data[key], dict):
                            data[key] = defaultdict(int, data[key])
                    return data
            except Exception as e:
                print(f"Error loading stats: {e}")
                
        # Default structure with enhanced fields
        return {
            "daily_captures": {},  # date -> {type -> count}
            "pattern_types": defaultdict(int),  # pattern_type -> count
            "sources": defaultdict(int),  # source -> count
            "automation_levels": defaultdict(int),  # level -> count
            "total_captures": 0,
            "first_capture": None,
            "last_capture": None,
            "sessions": defaultdict(int),  # session_id -> capture_count
            "performance_metrics": {
                "capture_latency": [],  # List of latencies in ms
                "queue_processing_time": [],  # List of queue times in ms
                "average_latency": 0,
                "average_queue_time": 0
            },
            "pattern_hit_rates": defaultdict(lambda: {"hits": 0, "misses": 0}),
            "daily_automation_rate": {},  # date -> {auto: count, manual: count}
            "hook_performance": {
                "memory_context_hook": {"triggered": 0, "captured": 0},
                "post_tool_use_hook": {"triggered": 0, "captured": 0},
                "pattern_extraction_hook": {"triggered": 0, "captured": 0},
                "todo_memory_hook": {"triggered": 0, "captured": 0}
            },
            "last_reset": datetime.now(timezone.utc).isoformat()
        }
        
    def _save_stats(self):
        """Save statistics to file with thread safety"""
        with self._lock:
            # Convert defaultdicts to regular dicts for JSON
            stats_to_save = {
                "daily_captures": self.stats["daily_captures"],
                "pattern_types": dict(self.stats["pattern_types"]),
                "sources": dict(self.stats["sources"]),
                "automation_levels": dict(self.stats["automation_levels"]),
                "total_captures": self.stats["total_captures"],
                "first_capture": self.stats["first_capture"],
                "last_capture": self.stats["last_capture"],
                "sessions": dict(self.stats["sessions"]),
                "performance_metrics": self.stats["performance_metrics"],
                "pattern_hit_rates": {k: dict(v) for k, v in self.stats["pattern_hit_rates"].items()},
                "daily_automation_rate": self.stats["daily_automation_rate"],
                "hook_performance": self.stats["hook_performance"],
                "last_reset": self.stats.get("last_reset")
            }
            
            with open(self.stats_file, 'w') as f:
                json.dump(stats_to_save, f, indent=2)
                
    def _check_daily_reset(self):
        """Check if daily stats need to be reset at midnight"""
        now = datetime.now(timezone.utc)
        if self.stats.get("last_reset"):
            last_reset = datetime.fromisoformat(self.stats["last_reset"])
            # Reset if it's a new day
            if now.date() > last_reset.date():
                self._reset_daily_stats()
        else:
            self.stats["last_reset"] = now.isoformat()
            self._save_stats()
            
    def _reset_daily_stats(self):
        """Reset daily statistics at midnight"""
        now = datetime.now(timezone.utc)
        
        # Archive performance metrics
        if self.stats["performance_metrics"]["capture_latency"]:
            self.stats["performance_metrics"]["average_latency"] = (
                sum(self.stats["performance_metrics"]["capture_latency"]) / 
                len(self.stats["performance_metrics"]["capture_latency"])
            )
            self.stats["performance_metrics"]["capture_latency"] = []
            
        if self.stats["performance_metrics"]["queue_processing_time"]:
            self.stats["performance_metrics"]["average_queue_time"] = (
                sum(self.stats["performance_metrics"]["queue_processing_time"]) / 
                len(self.stats["performance_metrics"]["queue_processing_time"])
            )
            self.stats["performance_metrics"]["queue_processing_time"] = []
            
        self.stats["last_reset"] = now.isoformat()
        self._save_stats()
        
    def start_capture_timing(self, capture_id: str):
        """Start timing a capture operation"""
        self._capture_start_times[capture_id] = time.time()
        
    def end_capture_timing(self, capture_id: str):
        """End timing a capture operation and record latency"""
        if capture_id in self._capture_start_times:
            latency = (time.time() - self._capture_start_times[capture_id]) * 1000  # ms
            self.stats["performance_metrics"]["capture_latency"].append(latency)
            del self._capture_start_times[capture_id]
            # Keep only last 1000 measurements
            if len(self.stats["performance_metrics"]["capture_latency"]) > 1000:
                self.stats["performance_metrics"]["capture_latency"] = (
                    self.stats["performance_metrics"]["capture_latency"][-1000:]
                )
            self._save_stats()
            
    def start_queue_timing(self, queue_id: str):
        """Start timing queue processing"""
        self._queue_start_times[queue_id] = time.time()
        
    def end_queue_timing(self, queue_id: str):
        """End timing queue processing and record time"""
        if queue_id in self._queue_start_times:
            queue_time = (time.time() - self._queue_start_times[queue_id]) * 1000  # ms
            self.stats["performance_metrics"]["queue_processing_time"].append(queue_time)
            del self._queue_start_times[queue_id]
            # Keep only last 1000 measurements
            if len(self.stats["performance_metrics"]["queue_processing_time"]) > 1000:
                self.stats["performance_metrics"]["queue_processing_time"] = (
                    self.stats["performance_metrics"]["queue_processing_time"][-1000:]
                )
            self._save_stats()
            
    def record_capture(self, pattern_type: str, source: str, automation_level: str, 
                      session_id: Optional[str] = None, is_auto: bool = True):
        """
        Record a memory capture event with enhanced tracking
        
        Args:
            pattern_type: Type of pattern captured (DECISION, SECURITY, etc.)
            source: Source of capture (hook name or tool)
            automation_level: Current automation level (off, manual, semi, full)
            session_id: Optional session identifier
            is_auto: Whether this was an automatic capture (True) or manual (False)
        """
        now = datetime.now(timezone.utc)
        today = now.date().isoformat()
        
        # Update daily count by type
        if today not in self.stats["daily_captures"]:
            self.stats["daily_captures"][today] = defaultdict(int)
        self.stats["daily_captures"][today][pattern_type] += 1
        
        # Update pattern type count
        self.stats["pattern_types"][pattern_type] += 1
        
        # Update source count
        self.stats["sources"][source] += 1
        
        # Update automation level count
        self.stats["automation_levels"][automation_level] += 1
        
        # Track automation rate
        if today not in self.stats["daily_automation_rate"]:
            self.stats["daily_automation_rate"][today] = {"auto": 0, "manual": 0}
        self.stats["daily_automation_rate"][today]["auto" if is_auto else "manual"] += 1
        
        # Update totals
        self.stats["total_captures"] += 1
        
        # Update timestamps
        if self.stats["first_capture"] is None:
            self.stats["first_capture"] = now.isoformat()
        self.stats["last_capture"] = now.isoformat()
        
        # Update session count
        if session_id:
            self.stats["sessions"][session_id] += 1
            
        # Save immediately
        self._save_stats()
        
    def record_pattern_hit(self, pattern_name: str, hit: bool = True):
        """Record pattern hit/miss for hit rate tracking"""
        if hit:
            self.stats["pattern_hit_rates"][pattern_name]["hits"] += 1
        else:
            self.stats["pattern_hit_rates"][pattern_name]["misses"] += 1
        self._save_stats()
        
    def record_hook_trigger(self, hook_name: str, captured: bool = False):
        """Record hook trigger event"""
        if hook_name in self.stats["hook_performance"]:
            self.stats["hook_performance"][hook_name]["triggered"] += 1
            if captured:
                self.stats["hook_performance"][hook_name]["captured"] += 1
        self._save_stats()
        
    def get_daily_stats(self, date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get statistics for a specific day
        
        Args:
            date: ISO format date string (YYYY-MM-DD), defaults to today
            
        Returns:
            Daily statistics including captures by type, automation rate, etc.
        """
        if date is None:
            date = datetime.now(timezone.utc).date().isoformat()
            
        daily_captures = self.stats["daily_captures"].get(date, {})
        daily_automation = self.stats["daily_automation_rate"].get(date, {"auto": 0, "manual": 0})
        
        total_daily = sum(daily_captures.values()) if isinstance(daily_captures, dict) else 0
        auto_rate = (
            (daily_automation["auto"] / (daily_automation["auto"] + daily_automation["manual"]) * 100)
            if (daily_automation["auto"] + daily_automation["manual"]) > 0 else 0
        )
        
        return {
            "date": date,
            "total_captures": total_daily,
            "captures_by_type": dict(daily_captures) if isinstance(daily_captures, dict) else {},
            "automation_rate": round(auto_rate, 1),
            "auto_captures": daily_automation["auto"],
            "manual_captures": daily_automation["manual"]
        }
        
    def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Get summary for a specific session"""
        capture_count = self.stats["sessions"].get(session_id, 0)
        
        # Calculate session-specific metrics if we tracked them
        session_patterns = defaultdict(int)
        session_sources = defaultdict(int)
        
        # Note: For more detailed session tracking, we'd need to store
        # session-specific data, but for now we return overall stats
        
        return {
            "session_id": session_id,
            "capture_count": capture_count,
            "status": "active" if capture_count > 0 else "no_captures"
        }
        
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics including latency and queue times"""
        latencies = self.stats["performance_metrics"]["capture_latency"]
        queue_times = self.stats["performance_metrics"]["queue_processing_time"]
        
        return {
            "capture_latency": {
                "current_average": sum(latencies) / len(latencies) if latencies else 0,
                "min": min(latencies) if latencies else 0,
                "max": max(latencies) if latencies else 0,
                "samples": len(latencies)
            },
            "queue_processing": {
                "current_average": sum(queue_times) / len(queue_times) if queue_times else 0,
                "min": min(queue_times) if queue_times else 0,
                "max": max(queue_times) if queue_times else 0,
                "samples": len(queue_times)
            },
            "historical_average_latency": self.stats["performance_metrics"].get("average_latency", 0),
            "historical_average_queue_time": self.stats["performance_metrics"].get("average_queue_time", 0)
        }
        
    def get_pattern_hit_rates(self) -> Dict[str, float]:
        """Calculate hit rates for each pattern"""
        hit_rates = {}
        
        for pattern, stats in self.stats["pattern_hit_rates"].items():
            total = stats["hits"] + stats["misses"]
            if total > 0:
                hit_rates[pattern] = round((stats["hits"] / total) * 100, 1)
            else:
                hit_rates[pattern] = 0.0
                
        return hit_rates
        
    def get_automation_rate(self, days: int = 7) -> float:
        """Calculate automation rate over specified days"""
        end_date = datetime.now(timezone.utc).date()
        start_date = end_date - timedelta(days=days-1)
        
        total_auto = 0
        total_manual = 0
        
        for i in range(days):
            date = (start_date + timedelta(days=i)).isoformat()
            if date in self.stats["daily_automation_rate"]:
                total_auto += self.stats["daily_automation_rate"][date]["auto"]
                total_manual += self.stats["daily_automation_rate"][date]["manual"]
                
        total = total_auto + total_manual
        return (total_auto / total * 100) if total > 0 else 0.0
        
    def export_formatted_report(self) -> str:
        """Export comprehensive statistics as formatted report"""
        now = datetime.now(timezone.utc)
        today = now.date().isoformat()
        
        # Get various metrics
        daily_stats = self.get_daily_stats(today)
        perf_metrics = self.get_performance_metrics()
        pattern_hit_rates = self.get_pattern_hit_rates()
        automation_rate_7d = self.get_automation_rate(7)
        automation_rate_30d = self.get_automation_rate(30)
        
        # Build report
        report = []
        report.append("=" * 80)
        report.append(f"📊 MEMORY CAPTURE STATISTICS REPORT")
        report.append(f"Generated: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        report.append("=" * 80)
        
        # Overview section
        report.append("\n📈 OVERVIEW")
        report.append("-" * 40)
        report.append(f"Total Memories Captured: {self.stats['total_captures']:,}")
        report.append(f"First Capture: {self.stats['first_capture'] or 'N/A'}")
        report.append(f"Last Capture: {self.stats['last_capture'] or 'N/A'}")
        report.append(f"Days Active: {len(self.stats['daily_captures'])}")
        
        # Today's stats
        report.append("\n📅 TODAY'S STATISTICS")
        report.append("-" * 40)
        report.append(f"Total Captures: {daily_stats['total_captures']}")
        report.append(f"Automatic: {daily_stats['auto_captures']} ({daily_stats['automation_rate']}%)")
        report.append(f"Manual: {daily_stats['manual_captures']}")
        if daily_stats['captures_by_type']:
            report.append("\nBy Type:")
            for ptype, count in sorted(daily_stats['captures_by_type'].items(), 
                                      key=lambda x: x[1], reverse=True):
                report.append(f"  {ptype}: {count}")
                
        # Automation rates
        report.append("\n🤖 AUTOMATION RATES")
        report.append("-" * 40)
        report.append(f"Last 7 Days: {automation_rate_7d:.1f}%")
        report.append(f"Last 30 Days: {automation_rate_30d:.1f}%")
        
        # Pattern distribution
        report.append("\n🎯 PATTERN DISTRIBUTION")
        report.append("-" * 40)
        total = self.stats['total_captures']
        for pattern, count in sorted(self.stats['pattern_types'].items(), 
                                   key=lambda x: x[1], reverse=True)[:10]:
            percentage = (count / total * 100) if total > 0 else 0
            report.append(f"{pattern:20} {count:6,} ({percentage:5.1f}%)")
            
        # Pattern hit rates
        if pattern_hit_rates:
            report.append("\n🎪 PATTERN HIT RATES")
            report.append("-" * 40)
            for pattern, rate in sorted(pattern_hit_rates.items(), 
                                       key=lambda x: x[1], reverse=True)[:10]:
                report.append(f"{pattern:20} {rate:5.1f}%")
                
        # Performance metrics
        report.append("\n⚡ PERFORMANCE METRICS")
        report.append("-" * 40)
        report.append("Capture Latency:")
        report.append(f"  Average: {perf_metrics['capture_latency']['current_average']:.1f}ms")
        report.append(f"  Min: {perf_metrics['capture_latency']['min']:.1f}ms")
        report.append(f"  Max: {perf_metrics['capture_latency']['max']:.1f}ms")
        report.append("\nQueue Processing:")
        report.append(f"  Average: {perf_metrics['queue_processing']['current_average']:.1f}ms")
        report.append(f"  Min: {perf_metrics['queue_processing']['min']:.1f}ms")
        report.append(f"  Max: {perf_metrics['queue_processing']['max']:.1f}ms")
        
        # Hook performance
        report.append("\n🪝 HOOK PERFORMANCE")
        report.append("-" * 40)
        for hook, stats in self.stats['hook_performance'].items():
            triggered = stats['triggered']
            captured = stats['captured']
            rate = (captured / triggered * 100) if triggered > 0 else 0
            report.append(f"{hook}:")
            report.append(f"  Triggered: {triggered:,} times")
            report.append(f"  Captured: {captured:,} memories")
            report.append(f"  Success Rate: {rate:.1f}%")
            
        # Top sources
        report.append("\n📍 TOP CAPTURE SOURCES")
        report.append("-" * 40)
        for source, count in sorted(self.stats['sources'].items(), 
                                   key=lambda x: x[1], reverse=True)[:5]:
            report.append(f"{source:30} {count:6,}")
            
        # Session summary (last 5 sessions)
        if self.stats['sessions']:
            report.append("\n🗂️ RECENT SESSIONS")
            report.append("-" * 40)
            for session, count in sorted(self.stats['sessions'].items(), 
                                        key=lambda x: x[1], reverse=True)[:5]:
                report.append(f"{session[:40]:40} {count:4} captures")
                
        report.append("\n" + "=" * 80)
        report.append("End of Report")
        
        return "\n".join(report)
        
    def reset_daily_stats(self):
        """Manually reset daily statistics (called at midnight)"""
        self._reset_daily_stats()


# Singleton instance getter
def get_stats_tracker() -> MemoryStatsTracker:
    """Get the singleton instance of MemoryStatsTracker"""
    return MemoryStatsTracker()


# Example usage and testing
if __name__ == "__main__":
    # Get tracker instance
    tracker = get_stats_tracker()
    
    # Simulate some captures with timing
    import random
    
    print("Testing Memory Stats Tracker...")
    
    # Test capture timing
    for i in range(5):
        capture_id = f"test_capture_{i}"
        tracker.start_capture_timing(capture_id)
        time.sleep(random.uniform(0.01, 0.05))  # Simulate capture time
        
        # Record capture
        pattern_types = ["DECISION", "SECURITY", "PATTERN", "BREAKING", "RESOLVED"]
        sources = ["memory_context_hook", "post_tool_use_hook", "manual", "pattern_extraction_hook"]
        automation_levels = ["full", "semi", "manual"]
        
        tracker.record_capture(
            pattern_type=random.choice(pattern_types),
            source=random.choice(sources),
            automation_level=random.choice(automation_levels),
            session_id="test_session_001",
            is_auto=random.choice([True, False])
        )
        
        tracker.end_capture_timing(capture_id)
    
    # Test pattern hit rates
    patterns = ["client_preference", "api_pattern", "security_rule"]
    for pattern in patterns:
        for _ in range(10):
            tracker.record_pattern_hit(pattern, random.choice([True, False]))
    
    # Test hook triggers
    hooks = ["memory_context_hook", "post_tool_use_hook"]
    for hook in hooks:
        for _ in range(5):
            tracker.record_hook_trigger(hook, random.choice([True, False]))
    
    # Test queue timing
    for i in range(3):
        queue_id = f"queue_{i}"
        tracker.start_queue_timing(queue_id)
        time.sleep(random.uniform(0.02, 0.08))
        tracker.end_queue_timing(queue_id)
    
    # Print formatted report
    print("\n" + tracker.export_formatted_report())
    
    # Test specific methods
    print("\n\nDaily Stats for Today:")
    print(json.dumps(tracker.get_daily_stats(), indent=2))
    
    print("\n\nSession Summary:")
    print(json.dumps(tracker.get_session_summary("test_session_001"), indent=2))
    
    print("\n\nPerformance Metrics:")
    print(json.dumps(tracker.get_performance_metrics(), indent=2))