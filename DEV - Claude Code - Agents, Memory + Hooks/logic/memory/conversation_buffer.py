#!/usr/bin/env python3
"""
Conversation Buffer V2 - Tracks user<->assistant exchanges with smart analysis
Automatically captures critical patterns and analyzes after 5 exchanges
Integrates with MemoryCaptureQueue for non-blocking memory capture
"""

import re
import threading
from datetime import datetime
from typing import List, Dict, Tuple, Optional, Any
from collections import defaultdict
from .memory_capture_queue import MemoryCaptureQueue


class ConversationBuffer:
    """Tracks conversation exchanges and extracts key insights for memory capture"""
    
    # Critical patterns that trigger immediate capture
    CRITICAL_PATTERNS = {
        'SECURITY': [
            r'(?i)(api[_\s-]?key|token|secret|password|credential|auth)',
            r'(?i)(vulnerability|exploit|security[_\s-]?(issue|hole|risk))',
            r'(?i)(exposed|leaked|compromised)'
        ],
        'BREAKING_CHANGE': [
            r'(?i)(breaking[_\s-]?change|migration|deprecat)',
            r'(?i)(backward[_\s-]?compat|major[_\s-]?version)',
            r'(?i)(will[_\s-]?break|not[_\s-]?compatible)'
        ],
        'ERROR_RESOLVED': [
            r'(?i)(fixed|resolved|solution[_\s-]?works|works[_\s-]?now)',
            r'(?i)(error[_\s-]?(fix|resolved)|bug[_\s-]?(fix|resolved))',
            r'(?i)(finally[_\s-]?working|issue[_\s-]?solved)'
        ],
        'DECISION': [
            r'(?i)(decided[_\s-]?to|will[_\s-]?use|choosing|selected)',
            r'(?i)(going[_\s-]?with|opted[_\s-]?for|best[_\s-]?approach)',
            r'(?i)(final[_\s-]?decision|conclusion[_\s-]?is)'
        ],
        'PATTERN': [
            r'(?i)(always[_\s-]?use|convention[_\s-]?is|best[_\s-]?practice)',
            r'(?i)(pattern[_\s-]?is|standard[_\s-]?approach|typical[_\s-]?way)',
            r'(?i)(established[_\s-]?pattern|common[_\s-]?practice)'
        ]
    }
    
    # Keywords for grouping related memories
    GROUP_KEYWORDS = {
        'architecture': ['component', 'structure', 'design', 'pattern', 'module'],
        'security': ['auth', 'token', 'credential', 'vulnerability', 'permission'],
        'performance': ['optimize', 'speed', 'cache', 'load', 'memory'],
        'api': ['endpoint', 'request', 'response', 'api', 'rest', 'graphql'],
        'ui': ['interface', 'button', 'form', 'display', 'style', 'css'],
        'data': ['database', 'query', 'model', 'schema', 'migration'],
        'testing': ['test', 'spec', 'coverage', 'assertion', 'mock'],
        'deployment': ['deploy', 'build', 'ci/cd', 'production', 'release']
    }
    
    def __init__(self, auto_analyze_threshold: int = 5):
        """
        Initialize the conversation buffer
        
        Args:
            auto_analyze_threshold: Number of exchanges before automatic analysis
        """
        self._exchanges: List[Tuple[str, str, datetime]] = []
        self._lock = threading.RLock()
        self._auto_analyze_threshold = auto_analyze_threshold
        self._memory_queue = MemoryCaptureQueue()
        self._captured_memories: List[str] = []
        self._analysis_in_progress = False
        
    def add_exchange(self, role: str, content: str) -> Optional[Dict[str, Any]]:
        """
        Add an exchange to the buffer
        
        Args:
            role: 'user' or 'assistant'
            content: The message content
            
        Returns:
            Analysis result if triggered, None otherwise
        """
        with self._lock:
            # Add exchange with timestamp
            self._exchanges.append((role, content, datetime.now()))
            
            # Check for critical patterns
            critical_match = self._check_critical_patterns(content)
            if critical_match:
                # Immediate capture for critical patterns
                return self._capture_critical_memory(critical_match, content)
            
            # Check if we should auto-analyze
            if len(self._exchanges) >= self._auto_analyze_threshold:
                return self._analyze_and_capture()
                
        return None
    
    def _check_critical_patterns(self, content: str) -> Optional[Tuple[str, str]]:
        """
        Check content for critical patterns
        
        Args:
            content: Message content to check
            
        Returns:
            Tuple of (pattern_type, matched_text) if found, None otherwise
        """
        for pattern_type, patterns in self.CRITICAL_PATTERNS.items():
            for pattern in patterns:
                match = re.search(pattern, content)
                if match:
                    return (pattern_type, match.group(0))
        return None
    
    def _capture_critical_memory(self, pattern_match: Tuple[str, str], content: str) -> Dict[str, Any]:
        """
        Capture a critical memory immediately
        
        Args:
            pattern_match: Tuple of (pattern_type, matched_text)
            content: Full content containing the pattern
            
        Returns:
            Capture result
        """
        pattern_type, matched_text = pattern_match
        
        # Get context from surrounding exchanges
        context = self._get_context_around_current()
        
        # Determine group based on pattern type
        group_id = self._determine_group(content)
        
        # Create memory
        memory_name = f"[{pattern_type}]: {matched_text[:50]}"
        memory_body = f"Critical pattern detected: {pattern_type}\n\n"
        memory_body += f"Matched: {matched_text}\n\n"
        memory_body += f"Full context:\n{context}\n\n"
        memory_body += f"Content: {content}"
        
        # Add to queue
        memory_id = self._memory_queue.add_memory(
            name=memory_name,
            body=memory_body,
            source='critical_pattern',
            group_id=group_id
        )
        
        self._captured_memories.append(memory_id)
        
        return {
            'type': 'critical_capture',
            'pattern_type': pattern_type,
            'memory_id': memory_id,
            'group_id': group_id
        }
    
    def _get_context_around_current(self, window: int = 2) -> str:
        """
        Get context from exchanges around the current one
        
        Args:
            window: Number of exchanges before current to include
            
        Returns:
            Formatted context string
        """
        start_idx = max(0, len(self._exchanges) - window - 1)
        relevant_exchanges = self._exchanges[start_idx:]
        
        context_lines = []
        for role, content, timestamp in relevant_exchanges:
            context_lines.append(f"[{timestamp.strftime('%H:%M:%S')}] {role}: {content[:200]}...")
            
        return "\n".join(context_lines)
    
    def _determine_group(self, content: str) -> str:
        """
        Determine the group ID based on content keywords
        
        Args:
            content: Content to analyze
            
        Returns:
            Group ID string
        """
        content_lower = content.lower()
        
        # Count keyword matches for each group
        group_scores = defaultdict(int)
        for group, keywords in self.GROUP_KEYWORDS.items():
            for keyword in keywords:
                if keyword in content_lower:
                    group_scores[group] += 1
        
        # Return group with highest score, or 'general' if no matches
        if group_scores:
            return max(group_scores.items(), key=lambda x: x[1])[0]
        return 'general'
    
    def _analyze_and_capture(self) -> Dict[str, Any]:
        """
        Analyze the conversation buffer and capture insights
        
        Returns:
            Analysis results
        """
        if self._analysis_in_progress:
            return {'type': 'analysis_skipped', 'reason': 'already_in_progress'}
            
        with self._lock:
            self._analysis_in_progress = True
            
            try:
                # Extract key insights
                decisions = self._extract_decisions()
                patterns = self._extract_patterns()
                problems_solved = self._extract_problems_solved()
                key_topics = self._extract_key_topics()
                
                # Group related insights
                memory_groups = self._group_insights(decisions, patterns, problems_solved, key_topics)
                
                # Capture memories
                captured_ids = []
                for group_name, insights in memory_groups.items():
                    if insights:
                        memory_id = self._capture_grouped_memory(group_name, insights)
                        captured_ids.append(memory_id)
                        self._captured_memories.append(memory_id)
                
                # Reset buffer after capture
                self._reset_buffer()
                
                return {
                    'type': 'auto_analysis',
                    'exchanges_analyzed': len(self._exchanges),
                    'memories_captured': len(captured_ids),
                    'memory_ids': captured_ids,
                    'insights': {
                        'decisions': len(decisions),
                        'patterns': len(patterns),
                        'problems_solved': len(problems_solved),
                        'key_topics': len(key_topics)
                    }
                }
                
            finally:
                self._analysis_in_progress = False
    
    def _extract_decisions(self) -> List[Dict[str, str]]:
        """Extract decision points from the conversation"""
        decisions = []
        
        for idx, (role, content, timestamp) in enumerate(self._exchanges):
            # Check for decision patterns
            for pattern in self.CRITICAL_PATTERNS['DECISION']:
                if re.search(pattern, content):
                    # Get context
                    context_start = max(0, idx - 1)
                    context_end = min(len(self._exchanges), idx + 2)
                    
                    context = []
                    for i in range(context_start, context_end):
                        r, c, _ = self._exchanges[i]
                        context.append(f"{r}: {c[:100]}...")
                    
                    decisions.append({
                        'content': content,
                        'role': role,
                        'timestamp': timestamp.isoformat(),
                        'context': '\n'.join(context)
                    })
                    break
        
        return decisions
    
    def _extract_patterns(self) -> List[Dict[str, str]]:
        """Extract coding patterns and conventions from the conversation"""
        patterns = []
        
        for role, content, timestamp in self._exchanges:
            # Check for pattern indicators
            for pattern in self.CRITICAL_PATTERNS['PATTERN']:
                match = re.search(pattern, content)
                if match:
                    patterns.append({
                        'pattern': match.group(0),
                        'content': content,
                        'role': role,
                        'timestamp': timestamp.isoformat()
                    })
                    break
        
        return patterns
    
    def _extract_problems_solved(self) -> List[Dict[str, str]]:
        """Extract problems that were solved during the conversation"""
        problems = []
        
        for idx, (role, content, timestamp) in enumerate(self._exchanges):
            # Check for error resolution patterns
            for pattern in self.CRITICAL_PATTERNS['ERROR_RESOLVED']:
                if re.search(pattern, content):
                    # Look back for the problem description
                    problem_description = None
                    for i in range(idx - 1, max(idx - 5, -1), -1):
                        prev_role, prev_content, _ = self._exchanges[i]
                        if 'error' in prev_content.lower() or 'issue' in prev_content.lower():
                            problem_description = prev_content
                            break
                    
                    problems.append({
                        'solution': content,
                        'problem': problem_description or 'Unknown problem',
                        'role': role,
                        'timestamp': timestamp.isoformat()
                    })
                    break
        
        return problems
    
    def _extract_key_topics(self) -> List[Tuple[str, int]]:
        """Extract key topics discussed in the conversation"""
        topic_counts = defaultdict(int)
        
        # Count occurrences of group keywords
        for _, content, _ in self._exchanges:
            content_lower = content.lower()
            for group, keywords in self.GROUP_KEYWORDS.items():
                for keyword in keywords:
                    if keyword in content_lower:
                        topic_counts[group] += 1
        
        # Return sorted by frequency
        return sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)
    
    def _group_insights(self, decisions: List[Dict], patterns: List[Dict], 
                       problems: List[Dict], topics: List[Tuple]) -> Dict[str, List]:
        """Group related insights together"""
        groups = defaultdict(list)
        
        # Group decisions
        for decision in decisions:
            group = self._determine_group(decision['content'])
            groups[group].append(('decision', decision))
        
        # Group patterns
        for pattern in patterns:
            group = self._determine_group(pattern['content'])
            groups[group].append(('pattern', pattern))
        
        # Group problems
        for problem in problems:
            group = self._determine_group(problem['solution'])
            groups[group].append(('problem_solved', problem))
        
        # Add top topics as context
        if topics:
            top_topic = topics[0][0]
            if top_topic not in groups:
                groups[top_topic] = []
            groups[top_topic].append(('topic_summary', {
                'topics': topics,
                'exchange_count': len(self._exchanges)
            }))
        
        return dict(groups)
    
    def _capture_grouped_memory(self, group_name: str, insights: List[Tuple]) -> str:
        """Capture a grouped memory with related insights"""
        # Build memory content
        memory_parts = [f"Conversation insights for {group_name}:\n"]
        
        for insight_type, data in insights:
            if insight_type == 'decision':
                memory_parts.append(f"\n**Decision Made:**")
                memory_parts.append(f"- {data['content'][:200]}...")
                memory_parts.append(f"  Context: {data['context']}")
                
            elif insight_type == 'pattern':
                memory_parts.append(f"\n**Pattern Identified:**")
                memory_parts.append(f"- {data['pattern']}: {data['content'][:150]}...")
                
            elif insight_type == 'problem_solved':
                memory_parts.append(f"\n**Problem Solved:**")
                memory_parts.append(f"- Problem: {data['problem'][:150]}...")
                memory_parts.append(f"- Solution: {data['solution'][:150]}...")
                
            elif insight_type == 'topic_summary':
                memory_parts.append(f"\n**Topics Discussed:**")
                for topic, count in data['topics'][:3]:
                    memory_parts.append(f"- {topic}: {count} mentions")
        
        memory_body = '\n'.join(memory_parts)
        
        # Create memory name
        insight_count = len(insights)
        memory_name = f"[CONVERSATION]: {group_name} - {insight_count} insights"
        
        # Add to queue
        return self._memory_queue.add_memory(
            name=memory_name,
            body=memory_body,
            source='conversation',
            group_id=group_name
        )
    
    def _reset_buffer(self) -> None:
        """Reset the conversation buffer after capture"""
        self._exchanges.clear()
    
    def force_analyze(self) -> Dict[str, Any]:
        """Force analysis regardless of exchange count"""
        with self._lock:
            if len(self._exchanges) == 0:
                return {'type': 'no_exchanges', 'message': 'No exchanges to analyze'}
            
            return self._analyze_and_capture()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get buffer statistics"""
        with self._lock:
            return {
                'exchanges_buffered': len(self._exchanges),
                'memories_captured': len(self._captured_memories),
                'analysis_threshold': self._auto_analyze_threshold,
                'analysis_in_progress': self._analysis_in_progress,
                'queue_stats': self._memory_queue.get_stats()
            }
    
    def get_exchanges(self) -> List[Tuple[str, str, str]]:
        """Get all exchanges (for debugging)"""
        with self._lock:
            return [(role, content, ts.isoformat()) for role, content, ts in self._exchanges]


# Thread-safe singleton instance
_conversation_buffer_instance = None
_conversation_buffer_lock = threading.Lock()


def get_conversation_buffer() -> ConversationBuffer:
    """Get the singleton conversation buffer instance"""
    global _conversation_buffer_instance
    
    with _conversation_buffer_lock:
        if _conversation_buffer_instance is None:
            _conversation_buffer_instance = ConversationBuffer()
        return _conversation_buffer_instance


# Example usage and testing
if __name__ == "__main__":
    # Get buffer instance
    buffer = get_conversation_buffer()
    
    # Simulate a conversation
    print("=== Conversation Buffer V2 Test ===\n")
    
    # Add some exchanges
    buffer.add_exchange("user", "I'm getting an authentication error with the API")
    buffer.add_exchange("assistant", "Let me help you debug the authentication issue. What error message are you seeing?")
    buffer.add_exchange("user", "It says 'Invalid API_KEY format'")
    buffer.add_exchange("assistant", "The error indicates your API key might be malformed. The convention is to always use uppercase for environment variables.")
    
    # This should trigger immediate capture (SECURITY pattern)
    result = buffer.add_exchange("user", "Oh, I see! I was exposing my API_KEY in the client code. That's a security vulnerability!")
    print(f"Critical capture result: {result}\n")
    
    # Add more exchanges
    buffer.add_exchange("assistant", "Exactly! That's a security issue. Always keep API keys on the server side only.")
    
    # Force analysis (would normally happen after 5 exchanges)
    analysis_result = buffer.force_analyze()
    print(f"Analysis result: {analysis_result}\n")
    
    # Get stats
    stats = buffer.get_stats()
    print(f"Buffer stats: {stats}")