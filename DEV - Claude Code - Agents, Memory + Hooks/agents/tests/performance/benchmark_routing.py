"""
Performance benchmarks for routing components

Measures speed and efficiency of task analysis and model selection.
"""

import time
import statistics
import asyncio
import sys
from pathlib import Path
from typing import List, Dict, Any

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from routing import TaskComplexityAnalyzer, ModelSelector


class RoutingBenchmark:
    """Benchmark routing performance"""
    
    def __init__(self):
        self.analyzer = TaskComplexityAnalyzer()
        self.selector = ModelSelector()
        self.results = {
            "task_analysis": [],
            "model_selection": [],
            "end_to_end": []
        }
    
    def benchmark_task_analysis(self, iterations: int = 1000) -> Dict[str, float]:
        """Benchmark task complexity analysis"""
        test_tasks = [
            "Fix typo in README",
            "Search for all occurrences of logger in the codebase",
            "Implement user authentication with OAuth2 and JWT tokens",
            "Refactor entire authentication system with new security requirements",
            "Analyze the codebase architecture and suggest improvements"
        ]
        
        times = []
        
        for _ in range(iterations):
            task = test_tasks[_ % len(test_tasks)]
            
            start = time.perf_counter()
            result = self.analyzer.analyze_task(task)
            end = time.perf_counter()
            
            times.append((end - start) * 1000)  # Convert to ms
        
        return {
            "mean_ms": statistics.mean(times),
            "median_ms": statistics.median(times),
            "min_ms": min(times),
            "max_ms": max(times),
            "std_dev_ms": statistics.stdev(times) if len(times) > 1 else 0,
            "p95_ms": sorted(times)[int(len(times) * 0.95)],
            "p99_ms": sorted(times)[int(len(times) * 0.99)]
        }
    
    def benchmark_model_selection(self, iterations: int = 1000) -> Dict[str, float]:
        """Benchmark model selection"""
        # Pre-generate analyses to isolate selection performance
        test_analyses = []
        test_tasks = [
            ("Fix typo", "developer"),
            ("Analyze architecture", "analyst"),
            ("Review security", "reviewer"),
            ("Merge results", "synthesis")
        ]
        
        for task_desc, agent_type in test_tasks:
            analysis = self.analyzer.analyze_task(task_desc)
            test_analyses.append((analysis, agent_type))
        
        times = []
        
        for i in range(iterations):
            analysis, agent_type = test_analyses[i % len(test_analyses)]
            
            start = time.perf_counter()
            result = self.selector.select_model(analysis, agent_type)
            end = time.perf_counter()
            
            times.append((end - start) * 1000)  # Convert to ms
        
        return {
            "mean_ms": statistics.mean(times),
            "median_ms": statistics.median(times),
            "min_ms": min(times),
            "max_ms": max(times),
            "std_dev_ms": statistics.stdev(times) if len(times) > 1 else 0,
            "p95_ms": sorted(times)[int(len(times) * 0.95)],
            "p99_ms": sorted(times)[int(len(times) * 0.99)]
        }
    
    def benchmark_end_to_end(self, iterations: int = 100) -> Dict[str, float]:
        """Benchmark complete routing pipeline"""
        test_cases = [
            ("Fix typo in README", "developer"),
            ("Implement new dashboard feature", "developer"),
            ("Analyze system performance bottlenecks", "analyst"),
            ("Review API security vulnerabilities", "reviewer"),
            ("Refactor authentication system", "developer")
        ]
        
        times = []
        
        for i in range(iterations):
            task_desc, agent_type = test_cases[i % len(test_cases)]
            
            start = time.perf_counter()
            
            # Full pipeline
            analysis = self.analyzer.analyze_task(task_desc)
            selection = self.selector.select_model(analysis, agent_type)
            
            end = time.perf_counter()
            
            times.append((end - start) * 1000)  # Convert to ms
        
        return {
            "mean_ms": statistics.mean(times),
            "median_ms": statistics.median(times),
            "min_ms": min(times),
            "max_ms": max(times),
            "std_dev_ms": statistics.stdev(times) if len(times) > 1 else 0,
            "p95_ms": sorted(times)[int(len(times) * 0.95)],
            "p99_ms": sorted(times)[int(len(times) * 0.99)]
        }
    
    def benchmark_context_impact(self) -> Dict[str, Any]:
        """Benchmark impact of context on performance"""
        base_task = "Update user profile functionality"
        
        # No context
        start = time.perf_counter()
        for _ in range(100):
            self.analyzer.analyze_task(base_task)
        no_context_time = (time.perf_counter() - start) / 100 * 1000
        
        # With file context
        file_context = {"files": ["user.py", "profile.py", "db.py", "api.py", "auth.py"]}
        start = time.perf_counter()
        for _ in range(100):
            self.analyzer.analyze_task(base_task, file_context)
        file_context_time = (time.perf_counter() - start) / 100 * 1000
        
        # With constraints
        constraint_context = {
            "constraints": ["backward compatibility", "zero downtime", "GDPR compliance"]
        }
        start = time.perf_counter()
        for _ in range(100):
            self.analyzer.analyze_task(base_task, constraint_context)
        constraint_context_time = (time.perf_counter() - start) / 100 * 1000
        
        return {
            "no_context_ms": no_context_time,
            "file_context_ms": file_context_time,
            "constraint_context_ms": constraint_context_time,
            "file_context_overhead": ((file_context_time - no_context_time) / no_context_time) * 100,
            "constraint_overhead": ((constraint_context_time - no_context_time) / no_context_time) * 100
        }
    
    def run_all_benchmarks(self) -> Dict[str, Any]:
        """Run all benchmarks and generate report"""
        print("🚀 Running Routing Performance Benchmarks...")
        print("-" * 50)
        
        # Task Analysis
        print("📊 Benchmarking Task Analysis...")
        analysis_results = self.benchmark_task_analysis(1000)
        print(f"  Mean: {analysis_results['mean_ms']:.2f}ms")
        print(f"  P95:  {analysis_results['p95_ms']:.2f}ms")
        print(f"  P99:  {analysis_results['p99_ms']:.2f}ms")
        
        # Model Selection
        print("\n📊 Benchmarking Model Selection...")
        selection_results = self.benchmark_model_selection(1000)
        print(f"  Mean: {selection_results['mean_ms']:.2f}ms")
        print(f"  P95:  {selection_results['p95_ms']:.2f}ms")
        print(f"  P99:  {selection_results['p99_ms']:.2f}ms")
        
        # End-to-End
        print("\n📊 Benchmarking End-to-End Pipeline...")
        e2e_results = self.benchmark_end_to_end(500)
        print(f"  Mean: {e2e_results['mean_ms']:.2f}ms")
        print(f"  P95:  {e2e_results['p95_ms']:.2f}ms")
        print(f"  P99:  {e2e_results['p99_ms']:.2f}ms")
        
        # Context Impact
        print("\n📊 Benchmarking Context Impact...")
        context_results = self.benchmark_context_impact()
        print(f"  No Context:    {context_results['no_context_ms']:.2f}ms")
        print(f"  File Context:  {context_results['file_context_ms']:.2f}ms (+{context_results['file_context_overhead']:.1f}%)")
        print(f"  Constraints:   {context_results['constraint_context_ms']:.2f}ms (+{context_results['constraint_overhead']:.1f}%)")
        
        print("\n" + "-" * 50)
        
        # Performance targets check
        print("\n✅ Performance Target Validation:")
        targets_met = []
        targets_missed = []
        
        # Target: <50ms for task analysis
        if analysis_results['p95_ms'] < 50:
            targets_met.append("Task Analysis P95 < 50ms ✓")
        else:
            targets_missed.append(f"Task Analysis P95 ({analysis_results['p95_ms']:.1f}ms) > 50ms ✗")
        
        # Target: <10ms for model selection
        if selection_results['p95_ms'] < 10:
            targets_met.append("Model Selection P95 < 10ms ✓")
        else:
            targets_missed.append(f"Model Selection P95 ({selection_results['p95_ms']:.1f}ms) > 10ms ✗")
        
        # Target: <60ms for end-to-end
        if e2e_results['p95_ms'] < 60:
            targets_met.append("End-to-End P95 < 60ms ✓")
        else:
            targets_missed.append(f"End-to-End P95 ({e2e_results['p95_ms']:.1f}ms) > 60ms ✗")
        
        for target in targets_met:
            print(f"  {target}")
        for target in targets_missed:
            print(f"  {target}")
        
        return {
            "task_analysis": analysis_results,
            "model_selection": selection_results,
            "end_to_end": e2e_results,
            "context_impact": context_results,
            "targets_met": len(targets_met),
            "targets_missed": len(targets_missed)
        }


def main():
    """Run benchmarks"""
    benchmark = RoutingBenchmark()
    results = benchmark.run_all_benchmarks()
    
    # Summary
    print(f"\n📈 Summary: {results['targets_met']}/{results['targets_met'] + results['targets_missed']} performance targets met")
    
    if results['targets_missed'] == 0:
        print("🎉 All performance targets achieved!")
    else:
        print("⚠️  Some performance targets need optimization")


if __name__ == "__main__":
    main()