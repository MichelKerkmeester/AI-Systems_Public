#!/usr/bin/env python3
"""
Memory Statistics Tracker
Tracks memory capture metrics and provides insights
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any, List
from collections import defaultdict


class MemoryStatsTracker:
    """Track and analyze memory capture statistics"""
    
    def __init__(self, stats_file: Path = None):
        """
        Initialize stats tracker
        
        Args:
            stats_file: Path to store statistics (creates if not exists)
        """
        if stats_file is None:
            stats_file = Path(__file__).parent.parent.parent / "project" / "state" / "memory_stats.json"
            
        self.stats_file = stats_file
        self.stats_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing stats
        self.stats = self._load_stats()
        
    def _load_stats(self) -> Dict[str, Any]:
        """Load existing statistics"""
        if self.stats_file.exists():
            try:
                with open(self.stats_file) as f:
                    return json.load(f)
            except:
                pass
                
        # Default structure
        return {
            "daily_captures": {},  # date -> count
            "pattern_types": defaultdict(int),  # pattern_type -> count
            "sources": defaultdict(int),  # source -> count
            "automation_levels": defaultdict(int),  # level -> count
            "total_captures": 0,
            "first_capture": None,
            "last_capture": None,
            "sessions": defaultdict(int),  # session_id -> capture_count
            "hook_performance": {
                "memory_context_hook": {"triggered": 0, "captured": 0},
                "post_tool_use_hook": {"triggered": 0, "captured": 0},
                "pattern_extraction_hook": {"triggered": 0, "captured": 0}
            }
        }
        
    def _save_stats(self):
        """Save statistics to file"""
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
            "hook_performance": self.stats["hook_performance"]
        }
        
        with open(self.stats_file, 'w') as f:
            json.dump(stats_to_save, f, indent=2)
            
    def record_capture(self, pattern_type: str, source: str, automation_level: str, 
                      session_id: str = None):
        """
        Record a memory capture event
        
        Args:
            pattern_type: Type of pattern captured (DECISION, SECURITY, etc.)
            source: Source of capture (hook name or tool)
            automation_level: Current automation level
            session_id: Optional session identifier
        """
        now = datetime.now()
        today = now.date().isoformat()
        
        # Update daily count
        if today not in self.stats["daily_captures"]:
            self.stats["daily_captures"][today] = 0
        self.stats["daily_captures"][today] += 1
        
        # Update pattern type count
        self.stats["pattern_types"][pattern_type] += 1
        
        # Update source count
        self.stats["sources"][source] += 1
        
        # Update automation level count
        self.stats["automation_levels"][automation_level] += 1
        
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
        
    def record_hook_trigger(self, hook_name: str, captured: bool = False):
        """
        Record hook trigger event
        
        Args:
            hook_name: Name of the hook
            captured: Whether memory was actually captured
        """
        if hook_name in self.stats["hook_performance"]:
            self.stats["hook_performance"][hook_name]["triggered"] += 1
            if captured:
                self.stats["hook_performance"][hook_name]["captured"] += 1
                
        self._save_stats()
        
    def get_daily_average(self, days: int = 7) -> float:
        """Get average daily captures over specified days"""
        if not self.stats["daily_captures"]:
            return 0.0
            
        # Get dates for the past N days
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days-1)
        
        total = 0
        days_with_data = 0
        
        for i in range(days):
            date = (start_date + timedelta(days=i)).isoformat()
            if date in self.stats["daily_captures"]:
                total += self.stats["daily_captures"][date]
                days_with_data += 1
                
        return total / days_with_data if days_with_data > 0 else 0.0
        
    def get_pattern_distribution(self) -> Dict[str, float]:
        """Get percentage distribution of pattern types"""
        total = self.stats["total_captures"]
        if total == 0:
            return {}
            
        distribution = {}
        for pattern_type, count in self.stats["pattern_types"].items():
            distribution[pattern_type] = (count / total) * 100
            
        return distribution
        
    def get_automation_effectiveness(self) -> Dict[str, float]:
        """Get effectiveness of each automation level"""
        effectiveness = {}
        
        for level, count in self.stats["automation_levels"].items():
            effectiveness[level] = count
            
        return effectiveness
        
    def get_hook_performance(self) -> Dict[str, Dict[str, Any]]:
        """Get performance metrics for each hook"""
        performance = {}
        
        for hook, metrics in self.stats["hook_performance"].items():
            triggered = metrics["triggered"]
            captured = metrics["captured"]
            
            performance[hook] = {
                "triggered": triggered,
                "captured": captured,
                "capture_rate": (captured / triggered * 100) if triggered > 0 else 0
            }
            
        return performance
        
    def get_summary(self) -> Dict[str, Any]:
        """Get comprehensive statistics summary"""
        return {
            "total_memories": self.stats["total_captures"],
            "daily_average_7d": round(self.get_daily_average(7), 1),
            "daily_average_30d": round(self.get_daily_average(30), 1),
            "today_count": self.stats["daily_captures"].get(datetime.now().date().isoformat(), 0),
            "pattern_distribution": self.get_pattern_distribution(),
            "top_patterns": sorted(
                self.stats["pattern_types"].items(), 
                key=lambda x: x[1], 
                reverse=True
            )[:5],
            "automation_effectiveness": self.get_automation_effectiveness(),
            "hook_performance": self.get_hook_performance(),
            "first_capture": self.stats["first_capture"],
            "last_capture": self.stats["last_capture"],
            "days_active": len(self.stats["daily_captures"])
        }
        
    def format_report(self) -> str:
        """Format a human-readable statistics report"""
        summary = self.get_summary()
        
        report = []
        report.append("="*60)
        report.append("📊 MEMORY CAPTURE STATISTICS")
        report.append("="*60)
        
        report.append(f"\n📈 Overview:")
        report.append(f"   Total Memories: {summary['total_memories']}")
        report.append(f"   Today's Captures: {summary['today_count']}")
        report.append(f"   7-Day Average: {summary['daily_average_7d']}/day")
        report.append(f"   30-Day Average: {summary['daily_average_30d']}/day")
        
        if summary['top_patterns']:
            report.append(f"\n🎯 Top Pattern Types:")
            for pattern, count in summary['top_patterns']:
                percentage = (count / summary['total_memories'] * 100) if summary['total_memories'] > 0 else 0
                report.append(f"   {pattern}: {count} ({percentage:.1f}%)")
                
        report.append(f"\n⚡ Hook Performance:")
        for hook, perf in summary['hook_performance'].items():
            report.append(f"   {hook}:")
            report.append(f"      Triggered: {perf['triggered']} times")
            report.append(f"      Captured: {perf['captured']} memories")
            report.append(f"      Success Rate: {perf['capture_rate']:.1f}%")
            
        report.append(f"\n🤖 Automation Levels:")
        for level, count in summary['automation_effectiveness'].items():
            report.append(f"   {level}: {count} captures")
            
        report.append("\n" + "="*60)
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Create tracker
    tracker = MemoryStatsTracker()
    
    # Record some test captures
    tracker.record_capture("DECISION", "memory_context_hook", "full", "test_session")
    tracker.record_capture("SECURITY", "post_tool_use_hook", "full", "test_session")
    tracker.record_capture("PATTERN", "pattern_extraction_hook", "semi", "test_session")
    
    # Record hook triggers
    tracker.record_hook_trigger("memory_context_hook", captured=True)
    tracker.record_hook_trigger("memory_context_hook", captured=False)
    tracker.record_hook_trigger("post_tool_use_hook", captured=True)
    
    # Print report
    print(tracker.format_report())