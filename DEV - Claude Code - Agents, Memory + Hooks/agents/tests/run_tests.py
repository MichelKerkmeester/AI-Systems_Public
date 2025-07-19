#!/usr/bin/env python3
"""
Multi-Agent System Test Runner

Run all tests with coverage reporting.
"""

import sys
import subprocess
from pathlib import Path
import argparse


def run_unit_tests():
    """Run unit tests with coverage"""
    print("🧪 Running Unit Tests...")
    print("=" * 60)
    
    cmd = [
        sys.executable, "-m", "pytest",
        "unit/",
        "-v",
        "--cov=..",
        "--cov-report=term-missing",
        "--cov-report=html:coverage_html"
    ]
    
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0


def run_integration_tests():
    """Run integration tests"""
    print("\n🔗 Running Integration Tests...")
    print("=" * 60)
    
    cmd = [
        sys.executable, "-m", "pytest",
        "integration/",
        "-v"
    ]
    
    result = subprocess.run(cmd, cwd=Path(__file__).parent)
    return result.returncode == 0


def run_performance_benchmarks():
    """Run performance benchmarks"""
    print("\n⚡ Running Performance Benchmarks...")
    print("=" * 60)
    
    # Run routing benchmarks
    routing_benchmark = Path(__file__).parent / "performance" / "benchmark_routing.py"
    result = subprocess.run([sys.executable, str(routing_benchmark)])
    
    return result.returncode == 0


def run_specific_test(test_path: str):
    """Run a specific test file"""
    print(f"🎯 Running specific test: {test_path}")
    print("=" * 60)
    
    cmd = [
        sys.executable, "-m", "pytest",
        test_path,
        "-v",
        "-s"  # Show print statements
    ]
    
    result = subprocess.run(cmd)
    return result.returncode == 0


def main():
    """Main test runner"""
    parser = argparse.ArgumentParser(description="Multi-Agent System Test Runner")
    parser.add_argument(
        "--type",
        choices=["all", "unit", "integration", "performance"],
        default="all",
        help="Type of tests to run"
    )
    parser.add_argument(
        "--file",
        help="Run specific test file"
    )
    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Generate coverage report"
    )
    
    args = parser.parse_args()
    
    print("🚀 Multi-Agent System Test Suite")
    print("================================\n")
    
    if args.file:
        # Run specific test
        success = run_specific_test(args.file)
    else:
        # Run test suites
        results = {
            "unit": True,
            "integration": True,
            "performance": True
        }
        
        if args.type in ["all", "unit"]:
            results["unit"] = run_unit_tests()
        
        if args.type in ["all", "integration"]:
            results["integration"] = run_integration_tests()
        
        if args.type in ["all", "performance"]:
            results["performance"] = run_performance_benchmarks()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 Test Summary")
        print("=" * 60)
        
        for test_type, passed in results.items():
            if args.type == "all" or args.type == test_type:
                status = "✅ PASSED" if passed else "❌ FAILED"
                print(f"{test_type.capitalize()}: {status}")
        
        success = all(results.values())
    
    if args.coverage and args.type in ["all", "unit"]:
        print("\n📈 Coverage report generated in: coverage_html/index.html")
    
    # Exit code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()