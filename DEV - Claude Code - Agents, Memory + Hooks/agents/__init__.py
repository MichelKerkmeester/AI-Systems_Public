"""
Multi-Agent System for anobel.nl

Provides intelligent orchestration of multiple agents with model routing
for optimal performance and cost efficiency.
"""

from .routing import (
    TaskComplexityAnalyzer,
    TaskAnalysis,
    TaskType,
    ComplexityLevel,
    ModelSelector,
    ModelSelection,
    ModelProvider
)

__all__ = [
    'TaskComplexityAnalyzer',
    'TaskAnalysis', 
    'TaskType',
    'ComplexityLevel',
    'ModelSelector',
    'ModelSelection',
    'ModelProvider'
]

# Version info
__version__ = "1.0.0"
__author__ = "Claude Code Assistant"