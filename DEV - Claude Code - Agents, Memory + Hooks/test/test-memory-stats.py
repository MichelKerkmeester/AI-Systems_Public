#!/usr/bin/env python3
"""Test memory statistics tracking"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "hooks" / "memory"))

from memory_stats import MemoryStatsTracker

def test_statistics_tracking():
    """Test comprehensive statistics tracking"""
    
    print("=== Testing Memory Statistics Tracking ===\n")
    
    # Create a test stats file
    test_stats_file = Path(__file__).parent / "test_memory_stats.json"
    tracker = MemoryStatsTracker(test_stats_file)
    
    # Simulate various captures over different days
    patterns = [
        ("DECISION", "memory_context_hook", "full"),
        ("SECURITY", "post_tool_use_hook", "full"),
        ("RESOLVED", "memory_context_hook", "semi"),
        ("PATTERN", "pattern_extraction_hook", "semi"),
        ("OPTIMIZATION", "post_tool_use_hook", "full"),
        ("ERROR_FIX", "post_tool_use_hook", "full"),
        ("USER_FEEDBACK", "memory_context_hook", "semi"),
        ("CONFIG_CHANGE", "post_tool_use_hook", "full"),
        ("LEARNING", "conversation_buffer", "full"),
        ("BEST_PRACTICE", "memory_context_hook", "semi")
    ]
    
    # Record captures
    print("Recording test captures...")
    for i, (pattern, source, level) in enumerate(patterns):
        tracker.record_capture(pattern, source, level, f"test_session_{i//3}")
        print(f"  ✓ Captured: {pattern} from {source} (level: {level})")
    
    # Record hook triggers
    print("\nRecording hook performance...")
    tracker.record_hook_trigger("memory_context_hook", captured=True)
    tracker.record_hook_trigger("memory_context_hook", captured=True)
    tracker.record_hook_trigger("memory_context_hook", captured=False)
    tracker.record_hook_trigger("post_tool_use_hook", captured=True)
    tracker.record_hook_trigger("post_tool_use_hook", captured=True)
    tracker.record_hook_trigger("post_tool_use_hook", captured=True)
    tracker.record_hook_trigger("pattern_extraction_hook", captured=True)
    
    # Get and display summary
    print("\n" + "="*60)
    print(tracker.format_report())
    
    # Test specific metrics
    print("\n=== Detailed Metrics ===")
    
    summary = tracker.get_summary()
    
    print(f"\nPattern Distribution:")
    for pattern, percentage in summary['pattern_distribution'].items():
        print(f"  {pattern}: {percentage:.1f}%")
    
    print(f"\nTop Patterns:")
    for pattern, count in summary['top_patterns']:
        print(f"  {pattern}: {count} captures")
    
    print(f"\nHook Performance:")
    for hook, perf in summary['hook_performance'].items():
        print(f"  {hook}: {perf['capture_rate']:.1f}% success rate")
    
    # Clean up test file
    test_stats_file.unlink()
    print("\n✅ Statistics tracking test complete!")


def test_daily_averages():
    """Test daily average calculations"""
    
    print("\n\n=== Testing Daily Averages ===\n")
    
    test_stats_file = Path(__file__).parent / "test_daily_stats.json"
    tracker = MemoryStatsTracker(test_stats_file)
    
    # Simulate captures over multiple days
    today = datetime.now().date()
    
    # Add historical data
    tracker.stats["daily_captures"] = {
        (today - timedelta(days=6)).isoformat(): 8,
        (today - timedelta(days=5)).isoformat(): 12,
        (today - timedelta(days=4)).isoformat(): 15,
        (today - timedelta(days=3)).isoformat(): 10,
        (today - timedelta(days=2)).isoformat(): 20,
        (today - timedelta(days=1)).isoformat(): 18,
        today.isoformat(): 25
    }
    tracker.stats["total_captures"] = sum(tracker.stats["daily_captures"].values())
    
    # Calculate averages
    avg_7d = tracker.get_daily_average(7)
    avg_30d = tracker.get_daily_average(30)
    
    print(f"Daily captures (last 7 days):")
    for date, count in sorted(tracker.stats["daily_captures"].items())[-7:]:
        print(f"  {date}: {count} captures")
    
    print(f"\n7-day average: {avg_7d:.1f} captures/day")
    print(f"30-day average: {avg_30d:.1f} captures/day")
    
    # Clean up
    test_stats_file.unlink(missing_ok=True)
    print("\n✅ Daily average test complete!")


if __name__ == "__main__":
    test_statistics_tracking()
    test_daily_averages()