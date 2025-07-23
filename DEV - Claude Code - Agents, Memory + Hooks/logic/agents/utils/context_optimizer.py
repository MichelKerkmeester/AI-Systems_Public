#!/usr/bin/env python3
"""
Context optimization for different models in Unified Agent Architecture v3
"""

import re
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class OptimizedContext:
    """Optimized context for a specific model"""
    content: str
    token_count: int
    truncated: bool
    metadata: Dict[str, Any]

class ContextOptimizer:
    """Optimize context for different model requirements"""
    
    # Model-specific context limits
    MODEL_LIMITS = {
        'qwen3_simple': 4000,
        'qwen3_coder': 50000,
        'gemini_flash': 100000,
        'gemini_pro': 100000,
        'opus': 20000
    }
    
    # Token estimation (rough: 1 token ≈ 4 characters)
    CHARS_PER_TOKEN = 4
    
    def __init__(self):
        self.compression_strategies = {
            'qwen3_simple': self._compress_for_simple,
            'qwen3_coder': self._compress_for_coder,
            'gemini_flash': self._compress_for_analysis,
            'gemini_pro': self._compress_for_analysis,
            'opus': self._compress_for_validation
        }
    
    def optimize(self, content: str, model: str, 
                task_type: str = "general") -> OptimizedContext:
        """
        Optimize content for specific model and task
        """
        # Get model limit
        token_limit = self.MODEL_LIMITS.get(model, 10000)
        current_tokens = self._estimate_tokens(content)
        
        # If within limits, return as-is
        if current_tokens <= token_limit * 0.8:  # Keep 20% buffer
            return OptimizedContext(
                content=content,
                token_count=current_tokens,
                truncated=False,
                metadata={'original_tokens': current_tokens}
            )
        
        # Apply model-specific compression
        compression_func = self.compression_strategies.get(model, self._compress_default)
        compressed_content = compression_func(content, token_limit, task_type)
        
        return OptimizedContext(
            content=compressed_content,
            token_count=self._estimate_tokens(compressed_content),
            truncated=True,
            metadata={
                'original_tokens': current_tokens,
                'compression_ratio': len(compressed_content) / len(content),
                'strategy': model
            }
        )
    
    def _compress_for_simple(self, content: str, limit: int, task_type: str) -> str:
        """
        Aggressive compression for simple tasks
        Focus on essential code only
        """
        # Remove all comments and docstrings
        content = self._remove_comments(content)
        content = self._remove_docstrings(content)
        
        # Remove empty lines
        lines = [l for l in content.split('\n') if l.strip()]
        content = '\n'.join(lines)
        
        # If still too large, extract relevant section
        if self._estimate_tokens(content) > limit * 0.8:
            # Try to find the main function or class
            if task_type == "function":
                content = self._extract_function(content)
            elif task_type == "class":
                content = self._extract_class(content)
            else:
                # Take the most relevant middle section
                content = self._extract_middle_section(content, limit)
        
        return content
    
    def _compress_for_coder(self, content: str, limit: int, task_type: str) -> str:
        """
        Moderate compression for coding tasks
        Preserve structure and important comments
        """
        # Keep important comments but remove verbose ones
        content = self._remove_verbose_comments(content)
        
        # Compress whitespace
        content = self._compress_whitespace(content)
        
        # If still too large, prioritize recent code
        if self._estimate_tokens(content) > limit * 0.8:
            # Split into sections and prioritize
            sections = self._split_into_sections(content)
            content = self._prioritize_sections(sections, limit, task_type)
        
        return content
    
    def _compress_for_analysis(self, content: str, limit: int, task_type: str) -> str:
        """
        Minimal compression for analysis tasks
        Preserve as much context as possible
        """
        # Only remove excessive whitespace
        content = self._normalize_whitespace(content)
        
        # If still too large, chunk intelligently
        if self._estimate_tokens(content) > limit * 0.8:
            # Create overlapping chunks for better analysis
            chunks = self._create_analysis_chunks(content, limit)
            # Return the most relevant chunk based on task
            content = self._select_best_chunk(chunks, task_type)
        
        return content
    
    def _compress_for_validation(self, content: str, limit: int, task_type: str) -> str:
        """
        Smart compression for validation tasks
        Focus on security-critical and complex sections
        """
        # Prioritize security-critical code
        critical_sections = self._extract_critical_sections(content)
        
        # Add complexity hotspots
        complex_sections = self._extract_complex_sections(content)
        
        # Combine and fit within limit
        combined = "\n\n".join(critical_sections + complex_sections)
        
        if self._estimate_tokens(combined) > limit * 0.8:
            # Truncate less important parts
            combined = self._smart_truncate(combined, limit)
        
        return combined
    
    def _compress_default(self, content: str, limit: int, task_type: str) -> str:
        """Default compression strategy"""
        # Remove comments and normalize whitespace
        content = self._remove_comments(content)
        content = self._normalize_whitespace(content)
        
        # Simple truncation if still too large
        if self._estimate_tokens(content) > limit * 0.8:
            max_chars = int(limit * self.CHARS_PER_TOKEN * 0.8)
            content = content[:max_chars] + "\n... [truncated]"
        
        return content
    
    def _estimate_tokens(self, content: str) -> int:
        """Estimate token count"""
        return len(content) // self.CHARS_PER_TOKEN
    
    def _remove_comments(self, content: str) -> str:
        """Remove all comments from code"""
        # Remove single-line comments
        content = re.sub(r'(?<!:)//.*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)
        
        # Remove multi-line comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        
        return content
    
    def _remove_docstrings(self, content: str) -> str:
        """Remove docstrings from Python code"""
        # Remove triple-quoted strings
        content = re.sub(r'""".*?"""', '""', content, flags=re.DOTALL)
        content = re.sub(r"'''.*?'''", "''", content, flags=re.DOTALL)
        
        return content
    
    def _remove_verbose_comments(self, content: str) -> str:
        """Remove only verbose/redundant comments"""
        lines = content.split('\n')
        result = []
        
        for line in lines:
            # Keep important comments (TODO, FIXME, WARNING, etc.)
            if re.search(r'#.*(?:TODO|FIXME|WARNING|IMPORTANT|NOTE)', line, re.IGNORECASE):
                result.append(line)
            # Remove obvious comments
            elif re.search(r'#\s*(?:Initialize|Set|Get|Return|Check)', line, re.IGNORECASE):
                # Remove comment but keep code
                result.append(re.sub(r'#.*$', '', line).rstrip())
            else:
                result.append(line)
        
        return '\n'.join(result)
    
    def _compress_whitespace(self, content: str) -> str:
        """Compress excessive whitespace"""
        # Replace multiple blank lines with single
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # Remove trailing whitespace
        lines = [line.rstrip() for line in content.split('\n')]
        
        return '\n'.join(lines)
    
    def _normalize_whitespace(self, content: str) -> str:
        """Normalize whitespace without aggressive removal"""
        # Replace tabs with spaces
        content = content.replace('\t', '    ')
        
        # Remove trailing whitespace
        lines = [line.rstrip() for line in content.split('\n')]
        
        # Remove excessive blank lines (more than 2)
        result = []
        blank_count = 0
        for line in lines:
            if not line:
                blank_count += 1
                if blank_count <= 2:
                    result.append(line)
            else:
                blank_count = 0
                result.append(line)
        
        return '\n'.join(result)
    
    def _extract_function(self, content: str) -> str:
        """Extract the most relevant function"""
        # Find all functions
        functions = re.findall(
            r'(def\s+\w+.*?(?=\ndef|\nclass|\Z))',
            content,
            re.DOTALL
        )
        
        if functions:
            # Return the longest function (likely most important)
            return max(functions, key=len)
        
        return content[:1000]  # Fallback
    
    def _extract_class(self, content: str) -> str:
        """Extract the most relevant class"""
        # Find all classes
        classes = re.findall(
            r'(class\s+\w+.*?(?=\nclass|\Z))',
            content,
            re.DOTALL
        )
        
        if classes:
            # Return the longest class
            return max(classes, key=len)
        
        return content[:1000]  # Fallback
    
    def _extract_middle_section(self, content: str, limit: int) -> str:
        """Extract the middle section of code"""
        target_chars = int(limit * self.CHARS_PER_TOKEN * 0.8)
        
        if len(content) <= target_chars:
            return content
        
        # Take middle section
        start = (len(content) - target_chars) // 2
        end = start + target_chars
        
        # Adjust to line boundaries
        lines = content.split('\n')
        line_starts = [0]
        for line in lines:
            line_starts.append(line_starts[-1] + len(line) + 1)
        
        # Find line boundaries
        start_line = next(i for i, pos in enumerate(line_starts) if pos >= start)
        end_line = next(i for i, pos in enumerate(line_starts) if pos >= end)
        
        return '\n'.join(lines[start_line:end_line])
    
    def _split_into_sections(self, content: str) -> List[str]:
        """Split content into logical sections"""
        sections = []
        
        # Split by class definitions
        class_sections = re.split(r'(?=^class\s+\w+)', content, flags=re.MULTILINE)
        sections.extend(s for s in class_sections if s.strip())
        
        # Split by function definitions if no classes
        if len(sections) <= 1:
            func_sections = re.split(r'(?=^def\s+\w+)', content, flags=re.MULTILINE)
            sections = [s for s in func_sections if s.strip()]
        
        return sections
    
    def _prioritize_sections(self, sections: List[str], limit: int, task_type: str) -> str:
        """Prioritize sections based on relevance"""
        # Score each section
        scored_sections = []
        for section in sections:
            score = 0
            
            # Prefer sections with task-related keywords
            if task_type in section.lower():
                score += 10
            
            # Prefer longer sections (more context)
            score += min(len(section) / 1000, 5)
            
            # Prefer sections with more functions/classes
            score += len(re.findall(r'def\s+\w+', section))
            score += len(re.findall(r'class\s+\w+', section)) * 2
            
            scored_sections.append((score, section))
        
        # Sort by score
        scored_sections.sort(reverse=True, key=lambda x: x[0])
        
        # Take sections until limit reached
        result = []
        current_tokens = 0
        target_tokens = int(limit * 0.8)
        
        for score, section in scored_sections:
            section_tokens = self._estimate_tokens(section)
            if current_tokens + section_tokens <= target_tokens:
                result.append(section)
                current_tokens += section_tokens
        
        return '\n\n'.join(result)
    
    def _extract_critical_sections(self, content: str) -> List[str]:
        """Extract security-critical sections"""
        critical_patterns = [
            r'(?:password|token|key|secret|auth|security)',
            r'(?:eval|exec|subprocess|os\.system)',
            r'(?:sql|query|database|injection)',
            r'(?:encrypt|decrypt|hash|crypto)'
        ]
        
        sections = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            for pattern in critical_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Extract surrounding context (±10 lines)
                    start = max(0, i - 10)
                    end = min(len(lines), i + 11)
                    section = '\n'.join(lines[start:end])
                    sections.append(f"# Critical section around line {i}\n{section}")
                    break
        
        return sections
    
    def _extract_complex_sections(self, content: str) -> List[str]:
        """Extract high-complexity sections"""
        sections = []
        
        # Find deeply nested code
        lines = content.split('\n')
        max_indent = 0
        complex_start = 0
        
        for i, line in enumerate(lines):
            if line.strip():
                indent = len(line) - len(line.lstrip())
                if indent > max_indent:
                    max_indent = indent
                    complex_start = i
                elif indent < max_indent - 8:  # End of complex section
                    if max_indent > 12:  # At least 3 levels deep
                        start = max(0, complex_start - 5)
                        section = '\n'.join(lines[start:i])
                        sections.append(f"# Complex section (indent: {max_indent})\n{section}")
                    max_indent = indent
        
        return sections
    
    def _smart_truncate(self, content: str, limit: int) -> str:
        """Intelligently truncate content"""
        target_chars = int(limit * self.CHARS_PER_TOKEN * 0.8)
        
        if len(content) <= target_chars:
            return content
        
        # Try to truncate at a logical boundary
        truncated = content[:target_chars]
        
        # Find last complete function/class
        last_def = truncated.rfind('\ndef ')
        last_class = truncated.rfind('\nclass ')
        
        cut_point = max(last_def, last_class)
        if cut_point > target_chars // 2:
            truncated = content[:cut_point]
        
        return truncated + "\n\n# ... [truncated for context limit]"
    
    def _create_analysis_chunks(self, content: str, limit: int) -> List[str]:
        """Create overlapping chunks for analysis"""
        chunk_size = int(limit * self.CHARS_PER_TOKEN * 0.7)
        overlap = chunk_size // 4
        
        chunks = []
        pos = 0
        
        while pos < len(content):
            chunk = content[pos:pos + chunk_size]
            chunks.append(chunk)
            pos += chunk_size - overlap
        
        return chunks
    
    def _select_best_chunk(self, chunks: List[str], task_type: str) -> str:
        """Select the most relevant chunk for the task"""
        if not chunks:
            return ""
        
        # Score chunks based on task relevance
        best_score = -1
        best_chunk = chunks[0]
        
        for chunk in chunks:
            score = 0
            
            # Check for task-related keywords
            if task_type in chunk.lower():
                score += 10
            
            # Prefer chunks with more code structure
            score += len(re.findall(r'def\s+\w+', chunk))
            score += len(re.findall(r'class\s+\w+', chunk)) * 2
            
            if score > best_score:
                best_score = score
                best_chunk = chunk
        
        return best_chunk