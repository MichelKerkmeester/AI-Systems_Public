#!/usr/bin/env python3
"""
Code Reuse Analysis Engine
Enforces DRY principles and prevents unnecessary file creation
"""

from .reuse_analyzer import ReuseAnalyzer, ComponentMatch, ReuseScore
from .compliance_validator import ComplianceValidator, ValidationResult
from .justification_system import JustificationSystem, FileJustification
from .similarity_detector import SimilarityDetector, SimilarityMatch, CodeBlock
from .pattern_matcher import PatternMatcher, PatternViolation, PatternMatch, RefactoringOpportunity
from .consolidation_analyzer import ConsolidationAnalyzer, ConsolidationOpportunity, ConsolidationPlan, MigrationStep

__all__ = [
    # Reuse Analysis
    'ReuseAnalyzer',
    'ComponentMatch',
    'ReuseScore',
    # Compliance Validation
    'ComplianceValidator',
    'ValidationResult',
    # Justification System
    'JustificationSystem',
    'FileJustification',
    # Similarity Detection
    'SimilarityDetector',
    'SimilarityMatch',
    'CodeBlock',
    # Pattern Matching
    'PatternMatcher',
    'PatternViolation',
    'PatternMatch',
    'RefactoringOpportunity',
    # Consolidation Analysis
    'ConsolidationAnalyzer',
    'ConsolidationOpportunity',
    'ConsolidationPlan',
    'MigrationStep'
]