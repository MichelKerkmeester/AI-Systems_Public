#!/usr/bin/env python3
"""
Similarity Detector - Code Similarity Analysis Engine
Detects similar code blocks across files using AST analysis and multiple similarity metrics
"""

import re
import ast
import difflib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict
import hashlib
import json


@dataclass
class CodeBlock:
    """Represents a code block for similarity analysis"""
    file_path: Path
    start_line: int
    end_line: int
    content: str
    block_type: str  # 'function', 'class', 'method', 'module'
    name: Optional[str] = None
    ast_hash: Optional[str] = None
    token_hash: Optional[str] = None
    
    @property
    def line_count(self) -> int:
        return self.end_line - self.start_line + 1


@dataclass
class SimilarityMatch:
    """Represents a similarity match between two code blocks"""
    block1: CodeBlock
    block2: CodeBlock
    similarity_score: float  # 0-100
    structural_similarity: float  # AST-based similarity
    semantic_similarity: float  # Token/logic similarity
    textual_similarity: float  # String similarity
    match_type: str  # 'exact', 'near-duplicate', 'similar', 'pattern'
    
    @property
    def is_duplicate(self) -> bool:
        """Check if this is a duplicate (>90% similar)"""
        return self.similarity_score >= 90
    
    @property
    def is_near_duplicate(self) -> bool:
        """Check if this is a near-duplicate (70-90% similar)"""
        return 70 <= self.similarity_score < 90


class SimilarityDetector:
    """Main similarity detection engine for JavaScript/CSS code"""
    
    def __init__(self, project_root: Path = None):
        """Initialize similarity detector"""
        if project_root is None:
            current = Path.cwd()
            while not (current / ".claude").exists() and current != current.parent:
                current = current.parent
            self.project_root = current
        else:
            self.project_root = project_root
            
        self.src_path = self.project_root / "src"
        
        # Caching for performance
        self._block_cache = {}
        self._similarity_cache = {}
        
        # Configurable thresholds
        self.duplicate_threshold = 90
        self.near_duplicate_threshold = 70
        self.similarity_threshold = 50
        
    def detect_similar_code(
        self,
        search_paths: Optional[List[Path]] = None,
        min_lines: int = 5,
        file_types: List[str] = None
    ) -> List[SimilarityMatch]:
        """
        Detect similar code blocks across the codebase
        
        Args:
            search_paths: Paths to search (defaults to src/)
            min_lines: Minimum lines for a code block to be considered
            file_types: File extensions to analyze (defaults to .js, .css)
            
        Returns:
            List of similarity matches sorted by score
        
        Example:
            detector = SimilarityDetector()
            matches = detector.detect_similar_code(min_lines=10)
            for match in matches:
                if match.is_duplicate:
                    print(f"Duplicate found: {match.block1.name} and {match.block2.name}")
        """
        if search_paths is None:
            search_paths = [self.src_path] if self.src_path.exists() else []
            
        if file_types is None:
            file_types = ['.js', '.css']
            
        # Extract code blocks from all files
        all_blocks = []
        for path in search_paths:
            if path.exists():
                all_blocks.extend(self._extract_code_blocks(path, file_types, min_lines))
        
        # Find similar blocks
        matches = self._find_similar_blocks(all_blocks)
        
        # Sort by similarity score
        matches.sort(key=lambda x: x.similarity_score, reverse=True)
        
        return matches
    
    def _extract_code_blocks(
        self,
        path: Path,
        file_types: List[str],
        min_lines: int
    ) -> List[CodeBlock]:
        """Extract code blocks from files"""
        blocks = []
        
        for file_type in file_types:
            for file_path in path.rglob(f"*{file_type}"):
                if self._should_skip_file(file_path):
                    continue
                    
                try:
                    content = file_path.read_text()
                    
                    if file_type == '.js':
                        # Extract JavaScript blocks
                        js_blocks = self._extract_js_blocks(file_path, content, min_lines)
                        blocks.extend(js_blocks)
                    elif file_type == '.css':
                        # Extract CSS blocks
                        css_blocks = self._extract_css_blocks(file_path, content, min_lines)
                        blocks.extend(css_blocks)
                        
                except Exception as e:
                    # Skip files that can't be read
                    continue
                    
        return blocks
    
    def _extract_js_blocks(
        self,
        file_path: Path,
        content: str,
        min_lines: int
    ) -> List[CodeBlock]:
        """Extract JavaScript code blocks (functions, classes, methods)"""
        blocks = []
        lines = content.split('\n')
        
        # Regex patterns for different JavaScript constructs
        patterns = {
            'function': r'^(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(',
            'arrow_function': r'^(?:export\s+)?(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(',
            'class': r'^(?:export\s+)?class\s+(\w+)',
            'method': r'^\s+(?:async\s+)?(\w+)\s*\(',
        }
        
        current_block = None
        brace_count = 0
        
        for i, line in enumerate(lines):
            # Check for block start
            if current_block is None:
                for block_type, pattern in patterns.items():
                    match = re.match(pattern, line.strip())
                    if match:
                        current_block = {
                            'type': block_type,
                            'name': match.group(1) if match.lastindex else 'anonymous',
                            'start': i,
                            'content': [line],
                            'brace_count': line.count('{') - line.count('}')
                        }
                        brace_count = current_block['brace_count']
                        break
            else:
                # Continue collecting block content
                current_block['content'].append(line)
                brace_count += line.count('{') - line.count('}')
                
                # Check for block end
                if brace_count <= 0:
                    # Block complete
                    block_content = '\n'.join(current_block['content'])
                    
                    if len(current_block['content']) >= min_lines:
                        block = CodeBlock(
                            file_path=file_path,
                            start_line=current_block['start'] + 1,
                            end_line=i + 1,
                            content=block_content,
                            block_type=current_block['type'],
                            name=current_block['name']
                        )
                        
                        # Calculate hashes
                        block.ast_hash = self._calculate_ast_hash(block_content, 'javascript')
                        block.token_hash = self._calculate_token_hash(block_content)
                        
                        blocks.append(block)
                    
                    current_block = None
                    brace_count = 0
        
        return blocks
    
    def _extract_css_blocks(
        self,
        file_path: Path,
        content: str,
        min_lines: int
    ) -> List[CodeBlock]:
        """Extract CSS code blocks (rules, media queries)"""
        blocks = []
        lines = content.split('\n')
        
        # Regex patterns for CSS constructs
        patterns = {
            'rule': r'^([.#]?[\w\-\[\]="\':\s,>+~]+)\s*\{',
            'media': r'^@media\s+([^{]+)\{',
            'keyframes': r'^@keyframes\s+(\w+)\s*\{',
        }
        
        current_block = None
        brace_count = 0
        
        for i, line in enumerate(lines):
            # Check for block start
            if current_block is None:
                for block_type, pattern in patterns.items():
                    match = re.match(pattern, line.strip())
                    if match:
                        current_block = {
                            'type': block_type,
                            'name': match.group(1).strip(),
                            'start': i,
                            'content': [line],
                            'brace_count': line.count('{') - line.count('}')
                        }
                        brace_count = current_block['brace_count']
                        break
            else:
                # Continue collecting block content
                current_block['content'].append(line)
                brace_count += line.count('{') - line.count('}')
                
                # Check for block end
                if brace_count <= 0:
                    # Block complete
                    block_content = '\n'.join(current_block['content'])
                    
                    if len(current_block['content']) >= min_lines:
                        block = CodeBlock(
                            file_path=file_path,
                            start_line=current_block['start'] + 1,
                            end_line=i + 1,
                            content=block_content,
                            block_type='css_' + current_block['type'],
                            name=current_block['name']
                        )
                        
                        # Calculate hashes
                        block.token_hash = self._calculate_token_hash(block_content)
                        
                        blocks.append(block)
                    
                    current_block = None
                    brace_count = 0
        
        return blocks
    
    def _calculate_ast_hash(self, code: str, language: str) -> str:
        """Calculate AST-based hash for structural comparison"""
        if language != 'javascript':
            return ""
            
        try:
            # Normalize JavaScript to pseudo-AST representation
            # Remove comments and whitespace
            normalized = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
            normalized = re.sub(r'/\*[\s\S]*?\*/', '', normalized)
            
            # Normalize variable names to placeholders
            normalized = re.sub(r'\b(?:const|let|var)\s+(\w+)', r'VAR_\1', normalized)
            normalized = re.sub(r'\bfunction\s+(\w+)', r'FUNC_\1', normalized)
            
            # Remove string contents (keep quotes)
            normalized = re.sub(r'"[^"]*"', '""', normalized)
            normalized = re.sub(r"'[^']*'", "''", normalized)
            normalized = re.sub(r'`[^`]*`', '``', normalized)
            
            # Normalize whitespace
            normalized = ' '.join(normalized.split())
            
            # Create hash
            return hashlib.md5(normalized.encode()).hexdigest()
            
        except Exception:
            return ""
    
    def _calculate_token_hash(self, code: str) -> str:
        """Calculate token-based hash for semantic comparison"""
        # Extract meaningful tokens
        tokens = re.findall(r'\b\w+\b', code.lower())
        
        # Filter out common keywords
        keywords = {
            'function', 'var', 'let', 'const', 'if', 'else', 'for', 'while',
            'return', 'class', 'import', 'export', 'from', 'async', 'await',
            'try', 'catch', 'throw', 'new', 'this', 'super', 'extends'
        }
        
        meaningful_tokens = [t for t in tokens if t not in keywords and len(t) > 2]
        
        # Sort tokens to make order-independent
        meaningful_tokens.sort()
        
        # Create hash from tokens
        token_string = ' '.join(meaningful_tokens)
        return hashlib.md5(token_string.encode()).hexdigest()
    
    def _find_similar_blocks(self, blocks: List[CodeBlock]) -> List[SimilarityMatch]:
        """Find similar blocks using multiple similarity metrics"""
        matches = []
        
        # Group blocks by type for more efficient comparison
        blocks_by_type = defaultdict(list)
        for block in blocks:
            blocks_by_type[block.block_type].append(block)
        
        # Compare blocks of the same type
        for block_type, type_blocks in blocks_by_type.items():
            for i, block1 in enumerate(type_blocks):
                for block2 in type_blocks[i+1:]:
                    # Skip if from same file and overlapping
                    if (block1.file_path == block2.file_path and
                        not (block1.end_line < block2.start_line or
                             block2.end_line < block1.start_line)):
                        continue
                    
                    # Calculate similarity
                    similarity = self._calculate_similarity(block1, block2)
                    
                    if similarity.similarity_score >= self.similarity_threshold:
                        matches.append(similarity)
        
        return matches
    
    def _calculate_similarity(
        self,
        block1: CodeBlock,
        block2: CodeBlock
    ) -> SimilarityMatch:
        """Calculate similarity between two code blocks"""
        # Check cache first
        cache_key = (id(block1), id(block2))
        if cache_key in self._similarity_cache:
            return self._similarity_cache[cache_key]
        
        # Calculate different similarity metrics
        structural_sim = self._calculate_structural_similarity(block1, block2)
        semantic_sim = self._calculate_semantic_similarity(block1, block2)
        textual_sim = self._calculate_textual_similarity(block1, block2)
        
        # Weighted average
        weights = {
            'structural': 0.4,
            'semantic': 0.35,
            'textual': 0.25
        }
        
        similarity_score = (
            structural_sim * weights['structural'] +
            semantic_sim * weights['semantic'] +
            textual_sim * weights['textual']
        )
        
        # Determine match type
        if similarity_score >= 95:
            match_type = 'exact'
        elif similarity_score >= 90:
            match_type = 'near-duplicate'
        elif similarity_score >= 70:
            match_type = 'similar'
        else:
            match_type = 'pattern'
        
        match = SimilarityMatch(
            block1=block1,
            block2=block2,
            similarity_score=similarity_score,
            structural_similarity=structural_sim,
            semantic_similarity=semantic_sim,
            textual_similarity=textual_sim,
            match_type=match_type
        )
        
        # Cache result
        self._similarity_cache[cache_key] = match
        
        return match
    
    def _calculate_structural_similarity(
        self,
        block1: CodeBlock,
        block2: CodeBlock
    ) -> float:
        """Calculate structural similarity using AST hashes"""
        if not block1.ast_hash or not block2.ast_hash:
            # Fallback to line count similarity for non-JS files
            size_ratio = min(block1.line_count, block2.line_count) / max(block1.line_count, block2.line_count)
            return size_ratio * 100
        
        # Exact AST match
        if block1.ast_hash == block2.ast_hash:
            return 100.0
        
        # Calculate structure similarity based on code patterns
        patterns1 = self._extract_structural_patterns(block1.content)
        patterns2 = self._extract_structural_patterns(block2.content)
        
        if not patterns1 or not patterns2:
            return 0.0
        
        # Calculate Jaccard similarity
        intersection = patterns1.intersection(patterns2)
        union = patterns1.union(patterns2)
        
        return (len(intersection) / len(union)) * 100 if union else 0.0
    
    def _calculate_semantic_similarity(
        self,
        block1: CodeBlock,
        block2: CodeBlock
    ) -> float:
        """Calculate semantic similarity using token analysis"""
        if block1.token_hash == block2.token_hash:
            return 100.0
        
        # Extract meaningful tokens
        tokens1 = self._extract_semantic_tokens(block1.content)
        tokens2 = self._extract_semantic_tokens(block2.content)
        
        if not tokens1 or not tokens2:
            return 0.0
        
        # Calculate token overlap
        common_tokens = tokens1.intersection(tokens2)
        all_tokens = tokens1.union(tokens2)
        
        return (len(common_tokens) / len(all_tokens)) * 100 if all_tokens else 0.0
    
    def _calculate_textual_similarity(
        self,
        block1: CodeBlock,
        block2: CodeBlock
    ) -> float:
        """Calculate textual similarity using difflib"""
        # Normalize whitespace for comparison
        text1 = ' '.join(block1.content.split())
        text2 = ' '.join(block2.content.split())
        
        # Use sequence matcher
        matcher = difflib.SequenceMatcher(None, text1, text2)
        return matcher.ratio() * 100
    
    def _extract_structural_patterns(self, code: str) -> Set[str]:
        """Extract structural patterns from code"""
        patterns = set()
        
        # Control flow patterns
        for pattern in ['if', 'for', 'while', 'switch', 'try']:
            count = len(re.findall(rf'\b{pattern}\b', code))
            if count > 0:
                patterns.add(f"{pattern}:{count}")
        
        # Function calls
        func_calls = re.findall(r'(\w+)\s*\(', code)
        for func in func_calls:
            if func not in ['if', 'for', 'while', 'switch']:
                patterns.add(f"call:{func}")
        
        # Object/array access patterns
        if '.' in code:
            patterns.add('property_access')
        if '[' in code and ']' in code:
            patterns.add('array_access')
        
        return patterns
    
    def _extract_semantic_tokens(self, code: str) -> Set[str]:
        """Extract semantic tokens from code"""
        # Remove comments
        code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
        code = re.sub(r'/\*[\s\S]*?\*/', '', code)
        
        # Extract identifiers
        tokens = set(re.findall(r'\b[a-zA-Z_]\w*\b', code))
        
        # Filter out keywords and common words
        keywords = {
            'function', 'var', 'let', 'const', 'if', 'else', 'for', 'while',
            'return', 'class', 'import', 'export', 'from', 'async', 'await',
            'try', 'catch', 'throw', 'new', 'this', 'super', 'extends',
            'true', 'false', 'null', 'undefined', 'console', 'log'
        }
        
        return tokens - keywords
    
    def _should_skip_file(self, file_path: Path) -> bool:
        """Check if file should be skipped"""
        skip_patterns = [
            'node_modules',
            '.git',
            'dist',
            'build',
            '.cache',
            'vendor',
            'lib/external',
            'min.js',
            'min.css'
        ]
        
        path_str = str(file_path)
        return any(pattern in path_str for pattern in skip_patterns)
    
    def find_duplicates_for_file(
        self,
        file_path: Path,
        min_similarity: float = 70
    ) -> List[SimilarityMatch]:
        """
        Find all duplicates/similar code for a specific file
        
        Args:
            file_path: Path to the file to analyze
            min_similarity: Minimum similarity threshold
            
        Returns:
            List of similarity matches for this file
        """
        if not file_path.exists():
            return []
        
        # Extract blocks from target file
        file_type = file_path.suffix
        target_blocks = self._extract_code_blocks(
            file_path.parent,
            [file_type],
            min_lines=5
        )
        
        # Filter to only blocks from target file
        target_blocks = [b for b in target_blocks if b.file_path == file_path]
        
        if not target_blocks:
            return []
        
        # Extract blocks from rest of codebase
        all_blocks = self._extract_code_blocks(
            self.src_path,
            [file_type],
            min_lines=5
        )
        
        # Find matches
        matches = []
        for target_block in target_blocks:
            for other_block in all_blocks:
                if other_block.file_path == file_path:
                    continue
                    
                similarity = self._calculate_similarity(target_block, other_block)
                
                if similarity.similarity_score >= min_similarity:
                    matches.append(similarity)
        
        return sorted(matches, key=lambda x: x.similarity_score, reverse=True)
    
    def clear_cache(self):
        """Clear similarity detection caches"""
        self._block_cache.clear()
        self._similarity_cache.clear()