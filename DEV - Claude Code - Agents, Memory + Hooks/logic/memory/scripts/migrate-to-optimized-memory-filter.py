#!/usr/bin/env python3
"""
Migration script to switch from original to optimized memory filter
Includes configuration updates and performance testing
"""

import json
import time
import sys
from pathlib import Path
from typing import Dict, Any, List

# Add logic directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import both filters for comparison
from memory.crawl4ai_memory_filter import Crawl4AIMemoryFilter
from memory.crawl4ai_memory_filter_optimized import OptimizedCrawl4AIMemoryFilter

def load_test_data() -> List[Dict[str, Any]]:
    """Load sample test data for performance comparison"""
    return [
        {
            'url': 'https://docs.anobel.nl/components/slider',
            'title': 'Slider Component',
            'text': 'const slider = document.querySelector(".slider"); // Slater init pattern'
        },
        {
            'url': 'https://example.com/blog/post',
            'title': 'Blog Post',
            'text': 'This is a general blog post with no code content.'
        },
        {
            'url': 'https://anobel.nl/.claude/logic/hooks/memory.py',
            'title': 'Memory Hook',
            'text': 'class MemoryHook: def process(self): # Important pattern'
        },
        {
            'url': 'https://cdn.example.com/style.css',
            'title': 'Stylesheet',
            'text': 'body { margin: 0; }'
        },
        {
            'url': 'https://api.anobel.nl/v1/components',
            'title': 'API Endpoint',
            'text': 'GET /components - Returns list of all components'
        }
    ] * 20  # Multiply for more realistic load

def benchmark_filter(filter_class, test_data: List[Dict], name: str) -> Dict[str, Any]:
    """Benchmark a filter implementation"""
    print(f"\n🧪 Benchmarking {name}...")
    
    # Initialize filter
    if name == "Optimized":
        config = {
            'thresholds': {'neo4j': 0.8, 'supabase': 0.2},
            'features': {'use_batching': True, 'use_caching': True}
        }
        filter = filter_class(config)
    else:
        filter = filter_class()
    
    # Process all test data
    start_time = time.time()
    results = []
    
    for item in test_data:
        result = filter.process_crawled_content(item)
        results.append(result)
    
    # For optimized filter, wait for queue processing
    if hasattr(filter, 'shutdown'):
        time.sleep(2)  # Allow queue to process
        filter.shutdown()
    
    end_time = time.time()
    
    # Calculate metrics
    total_time = end_time - start_time
    avg_time = total_time / len(test_data)
    
    # Get stats if available
    stats = filter.get_stats() if hasattr(filter, 'get_stats') else {}
    
    return {
        'name': name,
        'total_time': total_time,
        'avg_time_ms': avg_time * 1000,
        'throughput': len(test_data) / total_time,
        'stats': stats
    }

def compare_results(original_results: List[Dict], optimized_results: List[Dict]):
    """Compare results between filters"""
    print("\n📊 Results Comparison:")
    
    # Count storage decisions
    original_storage = {'neo4j': 0, 'supabase': 0, 'both': 0, 'none': 0}
    optimized_storage = {'neo4j': 0, 'supabase': 0, 'both': 0, 'none': 0, 'queued': 0}
    
    for result in original_results:
        storage = result.get('storage', 'none')
        original_storage[storage] = original_storage.get(storage, 0) + 1
    
    for result in optimized_results:
        storage = result.get('storage', result.get('status', 'none'))
        optimized_storage[storage] = optimized_storage.get(storage, 0) + 1
    
    print("\nStorage Distribution:")
    print(f"Original:  {original_storage}")
    print(f"Optimized: {optimized_storage}")

def update_configuration():
    """Update configuration files for optimized filter"""
    print("\n🔧 Updating Configuration...")
    
    # Create memory filter config
    config = {
        "memory_filter": {
            "implementation": "optimized",
            "thresholds": {
                "neo4j": 0.8,
                "supabase": 0.2,
                "entity_extraction": 0.7
            },
            "performance": {
                "batch_size": 20,
                "max_queue_size": 1000,
                "worker_threads": 4,
                "cache_size": 1000,
                "circuit_breaker_threshold": 5
            },
            "features": {
                "use_batching": True,
                "use_caching": True,
                "use_circuit_breaker": True,
                "collect_metrics": True
            }
        }
    }
    
    config_path = Path(__file__).parent.parent.parent / 'config' / 'memory_filter_config.json'
    config_path.parent.mkdir(exist_ok=True)
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Configuration saved to: {config_path}")

def main():
    """Run the migration process"""
    print("🚀 Memory Filter Migration Tool")
    print("=" * 50)
    
    # Load test data
    test_data = load_test_data()
    print(f"\n📚 Loaded {len(test_data)} test items")
    
    # Benchmark original filter
    original_benchmark = benchmark_filter(
        Crawl4AIMemoryFilter, 
        test_data[:10],  # Use smaller set for original
        "Original Filter"
    )
    
    # Benchmark optimized filter
    optimized_benchmark = benchmark_filter(
        OptimizedCrawl4AIMemoryFilter,
        test_data,  # Full set for optimized
        "Optimized Filter"
    )
    
    # Display results
    print("\n📈 Performance Comparison:")
    print(f"\nOriginal Filter:")
    print(f"  - Average time: {original_benchmark['avg_time_ms']:.2f}ms per item")
    print(f"  - Throughput: {original_benchmark['throughput']:.2f} items/second")
    
    print(f"\nOptimized Filter:")
    print(f"  - Average time: {optimized_benchmark['avg_time_ms']:.2f}ms per item")
    print(f"  - Throughput: {optimized_benchmark['throughput']:.2f} items/second")
    
    # Calculate improvement
    speedup = original_benchmark['avg_time_ms'] / optimized_benchmark['avg_time_ms']
    print(f"\n🎯 Performance Improvement: {speedup:.1f}x faster")
    
    # Update configuration
    update_configuration()
    
    # Display optimized stats
    if 'stats' in optimized_benchmark and optimized_benchmark['stats']:
        print("\n📊 Optimized Filter Statistics:")
        stats = optimized_benchmark['stats']
        
        if 'cache' in stats:
            print(f"  - Cache hit rate: {stats['cache']['hit_rate']:.1%}")
        
        if 'entity_extractions_skipped' in stats:
            print(f"  - Entity extractions skipped: {stats['entity_extractions_skipped']}")
        
        if 'storage_distribution' in stats:
            print(f"  - Storage distribution: {stats['storage_distribution']}")
    
    print("\n✅ Migration Complete!")
    print("\n📝 Next Steps:")
    print("1. Update imports to use OptimizedCrawl4AIMemoryFilter")
    print("2. Monitor performance metrics via get_stats()")
    print("3. Adjust thresholds based on storage costs")
    print("4. Enable/disable features via configuration")

if __name__ == '__main__':
    main()