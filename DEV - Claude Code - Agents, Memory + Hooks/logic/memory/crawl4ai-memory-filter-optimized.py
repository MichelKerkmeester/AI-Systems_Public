#!/usr/bin/env python3
"""
Optimized Smart Memory Filtering System for Crawl4AI
Improved performance with batching, caching, and higher Neo4j threshold
"""

import json
import re
import time
import threading
from typing import Dict, List, Optional, Tuple, Any, Set
from datetime import datetime
from urllib.parse import urlparse
from collections import Counter, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue, Empty
from functools import lru_cache

# ─────────────────────────────────────────────────────────────
# Performance Utilities
# ─────────────────────────────────────────────────────────────

class LRUCache:
    """Simple LRU cache implementation"""
    def __init__(self, maxsize: int = 1000):
        self.cache = {}
        self.order = deque()
        self.maxsize = maxsize
        self.hits = 0
        self.misses = 0
        self.lock = threading.Lock()
    
    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.cache:
                self.hits += 1
                self.order.remove(key)
                self.order.append(key)
                return self.cache[key]
            self.misses += 1
            return None
    
    def put(self, key: str, value: Any):
        with self.lock:
            if key in self.cache:
                self.order.remove(key)
            elif len(self.cache) >= self.maxsize:
                oldest = self.order.popleft()
                del self.cache[oldest]
            
            self.cache[key] = value
            self.order.append(key)
    
    def get_stats(self) -> Dict[str, int]:
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': self.hits / max(1, self.hits + self.misses),
            'size': len(self.cache)
        }

class CircuitBreaker:
    """Circuit breaker for Neo4j failures"""
    def __init__(self, failure_threshold: int = 5, reset_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure = None
        self.is_open = False
        self.lock = threading.Lock()
    
    def record_success(self):
        with self.lock:
            self.failure_count = 0
            self.is_open = False
    
    def record_failure(self):
        with self.lock:
            self.failure_count += 1
            self.last_failure = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.is_open = True
    
    def can_proceed(self) -> bool:
        with self.lock:
            if not self.is_open:
                return True
            
            # Check if timeout has passed
            if time.time() - self.last_failure > self.reset_timeout:
                self.is_open = False
                self.failure_count = 0
                return True
            
            return False

class PerformanceMetrics:
    """Collect and track performance metrics"""
    def __init__(self):
        self.processing_times = deque(maxlen=1000)
        self.queue_depths = deque(maxlen=100)
        self.storage_distribution = Counter()
        self.entity_extractions_skipped = 0
        self.total_processed = 0
        self.start_time = time.time()
        self.lock = threading.Lock()
    
    def record_processing_time(self, duration: float):
        with self.lock:
            self.processing_times.append(duration)
    
    def record_queue_depth(self, depth: int):
        with self.lock:
            self.queue_depths.append(depth)
    
    def record_storage_decision(self, decision: str):
        with self.lock:
            self.storage_distribution[decision] += 1
            self.total_processed += 1
    
    def skip_entity_extraction(self):
        with self.lock:
            self.entity_extractions_skipped += 1
    
    def get_stats(self) -> Dict[str, Any]:
        with self.lock:
            avg_processing = sum(self.processing_times) / len(self.processing_times) if self.processing_times else 0
            avg_queue_depth = sum(self.queue_depths) / len(self.queue_depths) if self.queue_depths else 0
            
            return {
                'avg_processing_time_ms': avg_processing * 1000,
                'avg_queue_depth': avg_queue_depth,
                'storage_distribution': dict(self.storage_distribution),
                'entity_extractions_skipped': self.entity_extractions_skipped,
                'total_processed': self.total_processed,
                'uptime_seconds': time.time() - self.start_time,
                'throughput_per_second': self.total_processed / max(1, time.time() - self.start_time)
            }

# ─────────────────────────────────────────────────────────────
# Optimized Relevance Scorer
# ─────────────────────────────────────────────────────────────

class OptimizedRelevanceScorer:
    """Optimized scorer with pre-compiled patterns and caching"""
    
    def __init__(self):
        # Pre-compile all regex patterns
        self.compiled_patterns = {}
        self._compile_patterns()
        
        # Early rejection patterns
        self.reject_extensions = {'.css', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.woff', '.woff2', '.ttf'}
        self.reject_paths = {'/static/', '/assets/', '/images/', '/fonts/', '/media/'}
        
        # Graph-worthy content types
        self.graph_worthy_types = {
            'code_file', 'config_file', 'api_endpoint', 'component_definition',
            'architecture_diagram', 'system_specification', 'integration_guide'
        }
        
        # Updated thresholds (Neo4j increased to 0.8)
        self.relevance_thresholds = {
            'neo4j': 0.8,           # Increased from 0.6
            'supabase': 0.2,        # Unchanged
            'entity_extraction': 0.7 # New threshold
        }
    
    def _compile_patterns(self):
        """Pre-compile all regex patterns for performance"""
        patterns_to_compile = {
            'code_patterns': [
                r'Slater', r'Webflow', r'DOMContentLoaded', r'Vite',
                r'component', r'module', r'service', r'handler',
                r'init\(\)', r'window\.', r'document\.', r'export',
                r'import', r'require', r'class\s+\w+', r'function\s+\w+'
            ],
            'architecture_patterns': [
                r'architecture', r'pattern', r'design', r'structure',
                r'implementation', r'integration', r'API', r'endpoint',
                r'workflow', r'pipeline', r'system', r'framework'
            ],
            'documentation_patterns': [
                r'README', r'CONTRIBUTING', r'CHANGELOG', r'LICENSE',
                r'guide', r'tutorial', r'reference', r'specification',
                r'best practices', r'conventions', r'standards'
            ],
            'project_specific': [
                r'anobel\.nl', r'\.claude', r'MCP', r'hook',
                r'memory', r'agent', r'TodoWrite', r'compliance',
                r'validation', r'knowledge', r'facts\.json', r'patterns\.json'
            ]
        }
        
        for category, patterns in patterns_to_compile.items():
            self.compiled_patterns[category] = [
                re.compile(pattern, re.IGNORECASE) for pattern in patterns
            ]
    
    def quick_reject(self, url: str) -> bool:
        """Fast rejection based on URL patterns"""
        url_lower = url.lower()
        
        # Check file extensions
        for ext in self.reject_extensions:
            if url_lower.endswith(ext):
                return True
        
        # Check paths
        for path in self.reject_paths:
            if path in url_lower:
                return True
        
        return False
    
    def should_extract_entities(self, score: float) -> bool:
        """Determine if entity extraction is worth the cost"""
        return score >= self.relevance_thresholds['entity_extraction']
    
    @lru_cache(maxsize=1000)
    def score_url_cached(self, url: str) -> float:
        """Cached URL scoring"""
        score = 0.0
        url_lower = url.lower()
        
        # Documentation paths
        doc_paths = ['/docs/', '/documentation/', '/guide/', '/api/', '/reference/']
        if any(path in url_lower for path in doc_paths):
            score += 0.5
        
        # Code repository paths
        code_paths = ['/src/', '/lib/', '/components/', '/modules/', '/services/']
        if any(path in url_lower for path in code_paths):
            score += 0.7
        
        # Project-specific paths
        if 'anobel.nl' in url or '.claude' in url:
            score += 0.8
        
        return min(1.0, score)
    
    def score_content_fast(self, content: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
        """Optimized content scoring with early exits"""
        start_time = time.time()
        
        url = content.get('url', '')
        text = content.get('text', '')
        
        # Quick reject check
        if self.quick_reject(url):
            return 0.0, {'rejected_early': True}
        
        # Initialize metadata
        metadata = {
            'matched_patterns': [],
            'content_type': 'general_content',
            'entity_count': 0,
            'relationship_count': 0,
            'code_density': 0.0,
            'processing_time': 0
        }
        
        # URL scoring (cached)
        url_score = self.score_url_cached(url)
        score = url_score * 0.2
        
        # Fast content type detection
        metadata['content_type'] = self._detect_content_type_fast(url, text[:1000])
        
        # Pattern matching with early exit
        pattern_score, matched = self._score_patterns_optimized(text)
        score += pattern_score * 0.5
        metadata['matched_patterns'] = matched
        
        # Code density (only if promising)
        if score > 0.3:
            code_density = self._calculate_code_density_fast(text)
            score += code_density * 0.3
            metadata['code_density'] = code_density
        
        # Entity extraction (only if above threshold)
        if self.should_extract_entities(score):
            entities, relationships = self._extract_graph_elements_fast(text)
            metadata['entity_count'] = len(entities)
            metadata['relationship_count'] = len(relationships)
            
            # Boost for many entities/relationships
            if len(entities) > 5:
                score += 0.2
            if len(relationships) > 3:
                score += 0.1
        
        score = min(1.0, max(0.0, score))
        metadata['processing_time'] = time.time() - start_time
        
        return score, metadata
    
    def _detect_content_type_fast(self, url: str, text_sample: str) -> str:
        """Fast content type detection using URL and text sample"""
        url_lower = url.lower()
        
        # URL-based detection
        if '/api/' in url_lower or '/docs/api' in url_lower:
            return 'api_endpoint'
        elif any(ext in url_lower for ext in ['.js', '.ts', '.py', '.java']):
            return 'code_file'
        elif any(ext in url_lower for ext in ['.json', '.yaml', '.toml']):
            return 'config_file'
        
        # Quick text-based detection
        if 'function' in text_sample or 'class' in text_sample or 'def' in text_sample:
            return 'code_file'
        
        return 'general_content'
    
    def _score_patterns_optimized(self, text: str) -> Tuple[float, List[str]]:
        """Optimized pattern matching with pre-compiled regex"""
        score = 0.0
        matched_patterns = []
        
        # Limit text size for pattern matching
        text_sample = text[:10000] if len(text) > 10000 else text
        
        for category, patterns in self.compiled_patterns.items():
            category_matches = 0
            for pattern in patterns:
                if pattern.search(text_sample):
                    category_matches += 1
                    matched_patterns.append(f"{category}:{pattern.pattern}")
                    
                    # Early exit if high score
                    if category_matches >= 5:
                        break
            
            if category_matches > 0:
                score += min(0.5, category_matches * 0.1)
            
            # Early exit if max score reached
            if score >= 1.0:
                break
        
        return min(1.0, score), matched_patterns
    
    def _calculate_code_density_fast(self, text: str) -> float:
        """Fast code density calculation"""
        if not text:
            return 0.0
        
        # Sample text if too large
        sample_size = 5000
        if len(text) > sample_size:
            text = text[:sample_size]
        
        # Quick indicators
        code_indicators = text.count('{') + text.count('}') + text.count(';')
        lines = text.count('\n') + 1
        
        # Simple density calculation
        density = min(1.0, code_indicators / (lines * 2))
        
        return density
    
    def _extract_graph_elements_fast(self, text: str) -> Tuple[List[Dict], List[Dict]]:
        """Fast entity extraction with limits"""
        entities = []
        relationships = []
        
        # Limit text for extraction
        text_sample = text[:5000] if len(text) > 5000 else text
        
        # Quick extraction with limits
        max_entities = 20
        
        # Components
        for pattern in self.compiled_patterns['code_patterns'][:5]:  # Limit patterns checked
            matches = pattern.findall(text_sample)
            for match in matches[:5]:  # Limit matches per pattern
                if len(entities) < max_entities:
                    entities.append({
                        'type': 'Component',
                        'name': match if isinstance(match, str) else str(match),
                        'properties': {}
                    })
        
        return entities, relationships

# ─────────────────────────────────────────────────────────────
# Batch Processing and Queue Management
# ─────────────────────────────────────────────────────────────

class BatchProcessor:
    """Handles batch processing of crawled content"""
    
    def __init__(self, batch_size: int = 20, max_workers: int = 4):
        self.batch_size = batch_size
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.neo4j_batch = []
        self.supabase_batch = []
        self.batch_lock = threading.Lock()
    
    def add_to_batch(self, storage_type: str, data: Dict[str, Any]):
        """Add data to appropriate batch"""
        with self.batch_lock:
            if storage_type == 'neo4j':
                self.neo4j_batch.append(data)
                if len(self.neo4j_batch) >= self.batch_size:
                    self._flush_neo4j_batch()
            elif storage_type == 'supabase':
                self.supabase_batch.append(data)
                if len(self.supabase_batch) >= self.batch_size:
                    self._flush_supabase_batch()
    
    def _flush_neo4j_batch(self):
        """Flush Neo4j batch - called with lock held"""
        if not self.neo4j_batch:
            return
        
        batch = self.neo4j_batch[:]
        self.neo4j_batch.clear()
        
        # Submit batch write to executor
        self.executor.submit(self._write_neo4j_batch, batch)
    
    def _flush_supabase_batch(self):
        """Flush Supabase batch - called with lock held"""
        if not self.supabase_batch:
            return
        
        batch = self.supabase_batch[:]
        self.supabase_batch.clear()
        
        # Submit batch write to executor
        self.executor.submit(self._write_supabase_batch, batch)
    
    def _write_neo4j_batch(self, batch: List[Dict]):
        """Write batch to Neo4j - placeholder for actual implementation"""
        # TODO: Implement actual Neo4j batch write via MCP
        print(f"[BatchProcessor] Writing {len(batch)} items to Neo4j")
    
    def _write_supabase_batch(self, batch: List[Dict]):
        """Write batch to Supabase - placeholder for actual implementation"""
        # TODO: Implement actual Supabase batch write
        print(f"[BatchProcessor] Writing {len(batch)} items to Supabase")
    
    def flush_all(self):
        """Flush all pending batches"""
        with self.batch_lock:
            self._flush_neo4j_batch()
            self._flush_supabase_batch()
    
    def shutdown(self):
        """Shutdown batch processor"""
        self.flush_all()
        self.executor.shutdown(wait=True)

# ─────────────────────────────────────────────────────────────
# Optimized Memory Filter
# ─────────────────────────────────────────────────────────────

class OptimizedCrawl4AIMemoryFilter:
    """Optimized memory filter with batching, caching, and improved thresholds"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        # Default configuration
        default_config = {
            'thresholds': {
                'neo4j': 0.8,
                'supabase': 0.2,
                'entity_extraction': 0.7
            },
            'performance': {
                'batch_size': 20,
                'max_queue_size': 1000,
                'worker_threads': 4,
                'cache_size': 1000,
                'circuit_breaker_threshold': 5
            },
            'features': {
                'use_batching': True,
                'use_caching': True,
                'use_circuit_breaker': True,
                'collect_metrics': True
            }
        }
        
        self.config = {**default_config, **(config or {})}
        
        # Initialize components
        self.scorer = OptimizedRelevanceScorer()
        self.url_cache = LRUCache(self.config['performance']['cache_size'])
        self.processing_queue = Queue(maxsize=self.config['performance']['max_queue_size'])
        self.batch_processor = BatchProcessor(
            batch_size=self.config['performance']['batch_size'],
            max_workers=self.config['performance']['worker_threads']
        )
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=self.config['performance']['circuit_breaker_threshold']
        )
        self.metrics = PerformanceMetrics()
        
        # Initialize running flag before starting thread
        self.running = True
        
        # Start background processing thread
        self.processing_thread = threading.Thread(target=self._process_queue, daemon=True)
        self.processing_thread.start()
    
    def process_crawled_content(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Add content to processing queue"""
        try:
            # Add to queue with timeout
            self.processing_queue.put(content, timeout=5)
            self.metrics.record_queue_depth(self.processing_queue.qsize())
            
            # Return async acknowledgment
            return {
                'status': 'queued',
                'queue_depth': self.processing_queue.qsize(),
                'message': 'Content queued for processing'
            }
        except:
            return {
                'status': 'rejected',
                'message': 'Queue full - apply backpressure'
            }
    
    def _process_queue(self):
        """Background thread for processing queue"""
        while self.running:
            batch = []
            
            # Collect batch
            deadline = time.time() + 1  # 1 second deadline
            while len(batch) < self.config['performance']['batch_size'] and time.time() < deadline:
                try:
                    item = self.processing_queue.get(timeout=0.1)
                    batch.append(item)
                except Empty:
                    if batch:  # Process partial batch if we have items
                        break
                    continue
            
            if batch:
                self._process_batch(batch)
    
    def _process_batch(self, batch: List[Dict[str, Any]]):
        """Process a batch of content items"""
        start_time = time.time()
        
        # Process items in parallel
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for item in batch:
                future = executor.submit(self._process_single_item, item)
                futures.append(future)
            
            # Collect results
            for future in as_completed(futures):
                try:
                    result = future.result()
                    self._handle_processed_item(result)
                except Exception as e:
                    print(f"Error processing item: {e}")
        
        # Record batch processing time
        batch_time = time.time() - start_time
        self.metrics.record_processing_time(batch_time / len(batch))
    
    def _process_single_item(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single content item"""
        url = content.get('url', '')
        
        # Check cache first
        if self.config['features']['use_caching']:
            cached_result = self.url_cache.get(url)
            if cached_result:
                return cached_result
        
        # Score content
        score, metadata = self.scorer.score_content_fast(content)
        
        # Check if entity extraction was skipped
        if score < self.scorer.relevance_thresholds['entity_extraction']:
            self.metrics.skip_entity_extraction()
        
        # Decide storage
        storage_decision = self._decide_storage(score, metadata)
        self.metrics.record_storage_decision(storage_decision)
        
        # Prepare result
        result = {
            'url': url,
            'storage': storage_decision,
            'relevance_score': score,
            'metadata': metadata,
            'timestamp': datetime.now().isoformat()
        }
        
        # Prepare storage-specific data
        if storage_decision in ['neo4j', 'both']:
            result['neo4j_data'] = self._prepare_neo4j_data(content, metadata)
        
        if storage_decision in ['supabase', 'both']:
            result['supabase_data'] = self._prepare_supabase_data(content, metadata)
        
        # Cache result
        if self.config['features']['use_caching']:
            self.url_cache.put(url, result)
        
        return result
    
    def _handle_processed_item(self, result: Dict[str, Any]):
        """Handle a processed item - send to appropriate storage"""
        storage = result.get('storage', 'none')
        
        if storage == 'none':
            return
        
        # Use circuit breaker for Neo4j
        if storage in ['neo4j', 'both'] and self.circuit_breaker.can_proceed():
            try:
                if self.config['features']['use_batching']:
                    self.batch_processor.add_to_batch('neo4j', result['neo4j_data'])
                else:
                    # Direct write (placeholder)
                    pass
                self.circuit_breaker.record_success()
            except Exception as e:
                self.circuit_breaker.record_failure()
                print(f"Neo4j write failed: {e}")
                # Fallback to Supabase only
                storage = 'supabase'
        
        if storage in ['supabase', 'both']:
            if self.config['features']['use_batching']:
                self.batch_processor.add_to_batch('supabase', result['supabase_data'])
            else:
                # Direct write (placeholder)
                pass
    
    def _decide_storage(self, score: float, metadata: Dict[str, Any]) -> str:
        """Decide storage location based on score and metadata"""
        content_type = metadata.get('content_type', '')
        
        # Always store graph-worthy types in both
        if content_type in self.scorer.graph_worthy_types:
            return 'both'
        
        # Check thresholds
        if score >= self.config['thresholds']['neo4j']:
            return 'both'
        elif score >= self.config['thresholds']['supabase']:
            return 'supabase'
        else:
            return 'none'
    
    def _prepare_neo4j_data(self, content: Dict[str, Any], metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare data for Neo4j storage"""
        return {
            'url': content.get('url', ''),
            'title': content.get('title', ''),
            'content_type': metadata['content_type'],
            'entity_count': metadata.get('entity_count', 0),
            'relationship_count': metadata.get('relationship_count', 0),
            'relevance_score': metadata.get('relevance_score', 0),
            'matched_patterns': metadata.get('matched_patterns', []),
            'summary': self._generate_summary(content.get('text', '')),
            'metadata': {
                'crawled_at': datetime.now().isoformat(),
                'code_density': metadata.get('code_density', 0)
            }
        }
    
    def _prepare_supabase_data(self, content: Dict[str, Any], metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare data for Supabase storage"""
        return {
            'url': content.get('url', ''),
            'title': content.get('title', ''),
            'full_text': content.get('text', ''),
            'content_type': metadata['content_type'],
            'relevance_score': metadata.get('relevance_score', 0),
            'metadata': {
                'crawled_at': datetime.now().isoformat(),
                'code_density': metadata.get('code_density', 0)
            }
        }
    
    def _generate_summary(self, text: str, max_length: int = 500) -> str:
        """Generate summary for Neo4j"""
        if len(text) <= max_length:
            return text
        
        # Take first meaningful content
        lines = text.split('\n')
        summary = []
        current_length = 0
        
        for line in lines:
            line = line.strip()
            if line and current_length + len(line) < max_length:
                summary.append(line)
                current_length += len(line)
            elif current_length > 200:  # Minimum summary length
                break
        
        return '\n'.join(summary) + '...' if summary else text[:max_length] + '...'
    
    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive statistics"""
        base_stats = self.metrics.get_stats()
        
        # Add cache stats
        if self.config['features']['use_caching']:
            base_stats['cache'] = self.url_cache.get_stats()
        
        # Add queue stats
        base_stats['queue'] = {
            'current_depth': self.processing_queue.qsize(),
            'max_size': self.config['performance']['max_queue_size']
        }
        
        # Add circuit breaker status
        base_stats['circuit_breaker'] = {
            'is_open': self.circuit_breaker.is_open,
            'failure_count': self.circuit_breaker.failure_count
        }
        
        return base_stats
    
    def shutdown(self):
        """Graceful shutdown"""
        print("Shutting down Optimized Memory Filter...")
        self.running = False
        
        # Process remaining items
        while not self.processing_queue.empty():
            time.sleep(0.1)
        
        # Flush batches
        self.batch_processor.shutdown()
        
        # Final stats
        print("Final statistics:", json.dumps(self.get_stats(), indent=2))

# ─────────────────────────────────────────────────────────────
# Usage Example
# ─────────────────────────────────────────────────────────────

def example_usage():
    """Example usage of the optimized filter"""
    
    # Create filter with custom config
    config = {
        'thresholds': {
            'neo4j': 0.8,  # High threshold
            'supabase': 0.2,
            'entity_extraction': 0.7
        },
        'performance': {
            'batch_size': 20,
            'max_queue_size': 1000,
            'worker_threads': 4
        }
    }
    
    filter = OptimizedCrawl4AIMemoryFilter(config)
    
    # Example content
    test_content = {
        'url': 'https://docs.anobel.nl/components/slider',
        'title': 'Slider Component Documentation',
        'text': '''
        # Slider Component
        
        The slider component uses Slater for initialization without DOMContentLoaded.
        
        ```javascript
        const initSlider = () => {
            const slider = document.querySelector('.slider');
            // Component initialization
        };
        
        initSlider();
        ```
        '''
    }
    
    # Process content (async)
    result = filter.process_crawled_content(test_content)
    print("Queue result:", result)
    
    # Let it process
    time.sleep(2)
    
    # Get stats
    print("\nStatistics:", json.dumps(filter.get_stats(), indent=2))
    
    # Shutdown
    filter.shutdown()

if __name__ == '__main__':
    example_usage()