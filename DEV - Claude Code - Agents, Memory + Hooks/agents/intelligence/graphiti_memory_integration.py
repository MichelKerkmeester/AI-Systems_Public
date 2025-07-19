"""
Graphiti Memory Integration for Multi-Agent System

Enables agents to share knowledge and learn from each other's experiences.
"""

import json
import asyncio
from typing import Dict, Any, List, Optional, Set
from pathlib import Path
from datetime import datetime


class GraphitiMemoryIntegration:
    """Integrates Graphiti memory system with multi-agent orchestration"""
    
    def __init__(self):
        self.memory_types = {
            "fact": "Verified information about the codebase",
            "pattern": "Recurring code patterns and conventions", 
            "decision": "Architectural and design decisions",
            "issue": "Problems encountered and their solutions",
            "insight": "Agent-generated insights and learnings"
        }
        
        # In-memory cache for quick access
        self.memory_cache = {
            "facts": [],
            "patterns": [],
            "decisions": [],
            "issues": [],
            "insights": []
        }
        
        # Agent-specific memories
        self.agent_memories = {}
        
    async def store_agent_memory(self, agent_id: str, agent_type: str,
                               memory_type: str, content: Dict[str, Any]) -> str:
        """
        Store a memory from an agent
        
        Args:
            agent_id: Unique agent identifier
            agent_type: Type of agent (analyst, developer, etc.)
            memory_type: Type of memory (fact, pattern, decision, etc.)
            content: Memory content
            
        Returns:
            Memory ID
        """
        
        memory = {
            "id": self._generate_memory_id(),
            "agent_id": agent_id,
            "agent_type": agent_type,
            "type": memory_type,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "relevance_score": 1.0,
            "access_count": 0
        }
        
        # Store in appropriate cache
        cache_key = f"{memory_type}s"
        if cache_key in self.memory_cache:
            self.memory_cache[cache_key].append(memory)
        
        # Store agent-specific memory
        if agent_id not in self.agent_memories:
            self.agent_memories[agent_id] = []
        self.agent_memories[agent_id].append(memory)
        
        # In production: await graphiti_mcp.add_episode(...)
        await self._persist_to_graphiti(memory)
        
        return memory["id"]
    
    async def retrieve_relevant_memories(self, query: str, 
                                       agent_type: str = None,
                                       memory_types: List[str] = None,
                                       limit: int = 10) -> List[Dict[str, Any]]:
        """
        Retrieve memories relevant to a query
        
        Args:
            query: Search query
            agent_type: Filter by agent type
            memory_types: Filter by memory types
            limit: Maximum results
            
        Returns:
            List of relevant memories
        """
        
        # In production: results = await graphiti_mcp.search(query=query, limit=limit)
        
        relevant_memories = []
        
        # Search through all memory types if not specified
        if not memory_types:
            memory_types = list(self.memory_types.keys())
        
        for mem_type in memory_types:
            cache_key = f"{mem_type}s"
            if cache_key in self.memory_cache:
                for memory in self.memory_cache[cache_key]:
                    # Simple relevance check
                    if self._is_relevant(memory, query, agent_type):
                        memory["access_count"] += 1
                        relevant_memories.append(memory)
        
        # Sort by relevance and recency
        relevant_memories.sort(
            key=lambda m: (m["relevance_score"], m["timestamp"]), 
            reverse=True
        )
        
        return relevant_memories[:limit]
    
    async def share_memories_between_agents(self, from_agent: str, 
                                          to_agents: List[str],
                                          memory_filter: Dict[str, Any] = None):
        """
        Share memories from one agent to others
        
        Args:
            from_agent: Source agent ID
            to_agents: Target agent IDs
            memory_filter: Optional filter criteria
        """
        
        if from_agent not in self.agent_memories:
            return
        
        memories_to_share = self.agent_memories[from_agent]
        
        # Apply filter if provided
        if memory_filter:
            memories_to_share = [
                m for m in memories_to_share
                if self._matches_filter(m, memory_filter)
            ]
        
        # Share with target agents
        for to_agent in to_agents:
            if to_agent not in self.agent_memories:
                self.agent_memories[to_agent] = []
            
            for memory in memories_to_share:
                # Create a shared copy
                shared_memory = memory.copy()
                shared_memory["shared_from"] = from_agent
                shared_memory["shared_at"] = datetime.now().isoformat()
                
                self.agent_memories[to_agent].append(shared_memory)
    
    async def extract_patterns_from_results(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Extract patterns from multiple agent results
        
        Args:
            agent_results: Results from multiple agents
            
        Returns:
            Extracted patterns
        """
        
        patterns = []
        
        # Look for common elements across results
        common_files = self._find_common_files(agent_results)
        if common_files:
            patterns.append({
                "type": "file_pattern",
                "description": "Frequently modified files",
                "files": list(common_files),
                "confidence": len(common_files) / len(agent_results)
            })
        
        # Look for similar code changes
        common_changes = self._find_common_changes(agent_results)
        if common_changes:
            patterns.append({
                "type": "change_pattern",
                "description": "Common code modifications",
                "changes": common_changes,
                "confidence": 0.8
            })
        
        # Look for recurring issues
        common_issues = self._find_common_issues(agent_results)
        if common_issues:
            patterns.append({
                "type": "issue_pattern",
                "description": "Recurring problems",
                "issues": common_issues,
                "confidence": 0.7
            })
        
        # Store patterns as memories
        for pattern in patterns:
            await self.store_agent_memory(
                agent_id="pattern_extractor",
                agent_type="system",
                memory_type="pattern",
                content=pattern
            )
        
        return patterns
    
    async def resolve_memory_conflicts(self, memories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Resolve conflicts between different memories
        
        Args:
            memories: Potentially conflicting memories
            
        Returns:
            Resolved memories
        """
        
        resolved = []
        
        # Group memories by topic
        memory_groups = {}
        for memory in memories:
            topic = memory.get("content", {}).get("topic", "general")
            if topic not in memory_groups:
                memory_groups[topic] = []
            memory_groups[topic].append(memory)
        
        # Resolve conflicts within each group
        for topic, group_memories in memory_groups.items():
            if len(group_memories) == 1:
                resolved.extend(group_memories)
            else:
                # Use recency and agent expertise to resolve
                resolved_memory = self._resolve_conflict(group_memories)
                resolved.append(resolved_memory)
        
        return resolved
    
    def _is_relevant(self, memory: Dict[str, Any], query: str, agent_type: str = None) -> bool:
        """Check if memory is relevant to query"""
        
        # Convert to lowercase for comparison
        query_lower = query.lower()
        memory_content = json.dumps(memory.get("content", {})).lower()
        
        # Check query terms
        query_terms = query_lower.split()
        matches = sum(1 for term in query_terms if term in memory_content)
        
        # Check agent type filter
        if agent_type and memory.get("agent_type") != agent_type:
            return False
        
        # Relevant if at least 30% of terms match
        return matches >= len(query_terms) * 0.3
    
    def _matches_filter(self, memory: Dict[str, Any], filter_criteria: Dict[str, Any]) -> bool:
        """Check if memory matches filter criteria"""
        
        for key, value in filter_criteria.items():
            if key not in memory:
                return False
            if memory[key] != value:
                return False
        
        return True
    
    def _find_common_files(self, agent_results: List[Dict[str, Any]]) -> Set[str]:
        """Find files commonly referenced across agent results"""
        
        file_counts = {}
        
        for result in agent_results:
            files = result.get("files_analyzed", [])
            for file in files:
                file_counts[file] = file_counts.get(file, 0) + 1
        
        # Files referenced by at least 50% of agents
        threshold = len(agent_results) * 0.5
        return {f for f, count in file_counts.items() if count >= threshold}
    
    def _find_common_changes(self, agent_results: List[Dict[str, Any]]) -> List[str]:
        """Find common changes across agent results"""
        
        change_patterns = []
        
        # Look for similar change types
        change_types = {}
        for result in agent_results:
            changes = result.get("changes_made", [])
            for change in changes:
                change_type = change.get("type", "unknown")
                change_types[change_type] = change_types.get(change_type, 0) + 1
        
        # Common change types
        for change_type, count in change_types.items():
            if count >= len(agent_results) * 0.4:
                change_patterns.append(f"Common {change_type} modifications")
        
        return change_patterns
    
    def _find_common_issues(self, agent_results: List[Dict[str, Any]]) -> List[str]:
        """Find common issues across agent results"""
        
        issue_counts = {}
        
        for result in agent_results:
            issues = result.get("issues_found", [])
            for issue in issues:
                issue_type = issue.get("type", "unknown")
                issue_counts[issue_type] = issue_counts.get(issue_type, 0) + 1
        
        # Issues found by multiple agents
        common_issues = []
        for issue_type, count in issue_counts.items():
            if count >= 2:
                common_issues.append(f"{issue_type} (found by {count} agents)")
        
        return common_issues
    
    def _resolve_conflict(self, memories: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve conflict between memories using various strategies"""
        
        # Sort by timestamp (most recent first)
        memories.sort(key=lambda m: m["timestamp"], reverse=True)
        
        # Use the most recent memory as base
        resolved = memories[0].copy()
        
        # Merge insights from all memories
        all_insights = []
        for memory in memories:
            content = memory.get("content", {})
            if "insights" in content:
                all_insights.extend(content["insights"])
        
        if all_insights:
            resolved["content"]["insights"] = list(set(all_insights))
            resolved["content"]["conflict_resolution"] = {
                "method": "merge_insights",
                "source_memories": [m["id"] for m in memories],
                "resolved_at": datetime.now().isoformat()
            }
        
        return resolved
    
    async def _persist_to_graphiti(self, memory: Dict[str, Any]):
        """Persist memory to Graphiti (simulated)"""
        
        # In production, this would call:
        # await graphiti_mcp.add_episode(
        #     name=f"{memory['agent_type']}_{memory['type']}",
        #     episode_body=json.dumps(memory['content']),
        #     source=f"agent_{memory['agent_id']}"
        # )
        
        pass
    
    def _generate_memory_id(self) -> str:
        """Generate unique memory ID"""
        import uuid
        return f"mem_{uuid.uuid4().hex[:8]}"
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get statistics about stored memories"""
        
        stats = {
            "total_memories": sum(len(cache) for cache in self.memory_cache.values()),
            "by_type": {
                mem_type: len(self.memory_cache.get(f"{mem_type}s", []))
                for mem_type in self.memory_types
            },
            "by_agent": {
                agent_id: len(memories)
                for agent_id, memories in self.agent_memories.items()
            },
            "most_accessed": self._get_most_accessed_memories(5)
        }
        
        return stats
    
    def _get_most_accessed_memories(self, limit: int) -> List[Dict[str, Any]]:
        """Get most frequently accessed memories"""
        
        all_memories = []
        for cache in self.memory_cache.values():
            all_memories.extend(cache)
        
        # Sort by access count
        all_memories.sort(key=lambda m: m["access_count"], reverse=True)
        
        return [
            {
                "id": m["id"],
                "type": m["type"],
                "access_count": m["access_count"],
                "summary": str(m.get("content", {}))[:100]
            }
            for m in all_memories[:limit]
        ]


# Singleton instance
_memory_integration = None

def get_memory_integration() -> GraphitiMemoryIntegration:
    """Get or create memory integration instance"""
    global _memory_integration
    if _memory_integration is None:
        _memory_integration = GraphitiMemoryIntegration()
    return _memory_integration