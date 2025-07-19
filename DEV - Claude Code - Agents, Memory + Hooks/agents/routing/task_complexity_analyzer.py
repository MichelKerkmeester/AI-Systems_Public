"""
Task Complexity Analyzer for Multi-Agent System

Analyzes task complexity to determine:
1. Which model to route the task to (Claude, Kimi Pro, etc.)
2. How many agents might be needed
3. Resource allocation requirements
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import re


class TaskType(Enum):
    """Types of development tasks"""
    ARCHITECTURE = "architecture"
    DESIGN = "design"
    DEBUG = "debug"
    TROUBLESHOOT = "troubleshoot"
    SEARCH = "search"
    READ = "read"
    EDIT = "edit"
    REFACTOR = "refactor"
    TEST = "test"
    DOCUMENT = "document"
    REVIEW = "review"
    ANALYSIS = "analysis"
    SYNTHESIS = "synthesis"


class ComplexityLevel(Enum):
    """Task complexity levels"""
    TRIVIAL = 0  # < 3 score
    SIMPLE = 1   # 3-5 score
    MEDIUM = 2   # 6-8 score
    COMPLEX = 3  # 9-12 score
    CRITICAL = 4 # > 12 score


@dataclass
class TaskAnalysis:
    """Results of task complexity analysis"""
    complexity_score: int
    complexity_level: ComplexityLevel
    task_type: TaskType
    files_affected: int
    requires_full_context: bool
    requires_reasoning: bool
    requires_creativity: bool
    estimated_tokens: int
    recommended_model: str
    reasoning: List[str]


class TaskComplexityAnalyzer:
    """Analyzes task complexity for intelligent model routing"""
    
    def __init__(self):
        self.task_patterns = {
            TaskType.ARCHITECTURE: [
                r"design\s+(?:system|architecture)",
                r"create\s+(?:framework|structure)",
                r"plan\s+(?:implementation|system)"
            ],
            TaskType.DEBUG: [
                r"(?:fix|debug|troubleshoot)\s+(?:error|bug|issue)",
                r"(?:investigate|diagnose)\s+problem"
            ],
            TaskType.SEARCH: [
                r"(?:find|search|locate)\s+(?:in|for)",
                r"where\s+is",
                r"list\s+all"
            ],
            TaskType.READ: [
                r"(?:read|show|display)\s+(?:file|content)",
                r"what\s+(?:is|does)",
                r"explain"
            ],
            TaskType.EDIT: [
                r"(?:edit|modify|update|change)\s+(?:file|code)",
                r"add\s+(?:to|in)",
                r"remove\s+from"
            ],
            TaskType.REFACTOR: [
                r"refactor",
                r"restructure",
                r"optimize\s+code",
                r"improve\s+(?:performance|structure)"
            ],
            TaskType.TEST: [
                r"(?:test|verify)",
                r"write\s+tests?",
                r"check\s+(?:if|that)"
            ],
            TaskType.REVIEW: [
                r"review\s+(?:code|changes)",
                r"check\s+(?:quality|security)",
                r"analyze\s+(?:code|implementation)"
            ],
            TaskType.SYNTHESIS: [
                r"(?:combine|merge|synthesize)",
                r"integrate\s+(?:results|outputs)",
                r"resolve\s+conflicts?"
            ]
        }
    
    def analyze_task(self, task_description: str, 
                    context: Optional[Dict[str, Any]] = None) -> TaskAnalysis:
        """
        Analyze a task to determine its complexity and routing requirements
        
        Args:
            task_description: Natural language description of the task
            context: Optional context with additional info (files, history, etc.)
            
        Returns:
            TaskAnalysis with complexity score and recommendations
        """
        context = context or {}
        
        # Detect task type
        task_type = self._detect_task_type(task_description)
        
        # Calculate complexity score
        score = 0
        reasoning = []
        
        # File scope analysis
        files_affected = context.get('files_affected', 0)
        if files_affected == 0:
            # Estimate from description
            files_affected = self._estimate_file_scope(task_description)
        
        if files_affected > 5:
            score += 3
            reasoning.append(f"Multiple files affected ({files_affected})")
        elif files_affected > 1:
            score += 1
            reasoning.append(f"Few files affected ({files_affected})")
        
        # Task type complexity
        type_scores = {
            TaskType.ARCHITECTURE: 5,
            TaskType.DESIGN: 5,
            TaskType.DEBUG: 3,
            TaskType.TROUBLESHOOT: 3,
            TaskType.REFACTOR: 3,
            TaskType.SYNTHESIS: 4,
            TaskType.REVIEW: 2,
            TaskType.TEST: 2,
            TaskType.EDIT: 1,
            TaskType.SEARCH: 0,
            TaskType.READ: 0,
            TaskType.DOCUMENT: 1,
            TaskType.ANALYSIS: 2
        }
        
        type_score = type_scores.get(task_type, 1)
        score += type_score
        if type_score >= 3:
            reasoning.append(f"Complex task type: {task_type.value}")
        
        # Context requirements
        requires_full_context = self._requires_full_context(task_description, task_type)
        if requires_full_context:
            score += 2
            reasoning.append("Requires full codebase context")
        
        # Reasoning requirements
        requires_reasoning = self._requires_reasoning(task_description, task_type)
        if requires_reasoning:
            score += 3
            reasoning.append("Requires complex reasoning")
        
        # Creativity requirements
        requires_creativity = self._requires_creativity(task_description, task_type)
        if requires_creativity:
            score += 2
            reasoning.append("Requires creative problem solving")
        
        # Determine complexity level
        if score < 3:
            complexity_level = ComplexityLevel.TRIVIAL
        elif score <= 5:
            complexity_level = ComplexityLevel.SIMPLE
        elif score <= 8:
            complexity_level = ComplexityLevel.MEDIUM
        elif score <= 12:
            complexity_level = ComplexityLevel.COMPLEX
        else:
            complexity_level = ComplexityLevel.CRITICAL
        
        # Estimate tokens
        estimated_tokens = self._estimate_tokens(
            task_description, files_affected, complexity_level
        )
        
        # Recommend model
        recommended_model = self._recommend_model(
            complexity_level, task_type, requires_reasoning, requires_creativity
        )
        
        return TaskAnalysis(
            complexity_score=score,
            complexity_level=complexity_level,
            task_type=task_type,
            files_affected=files_affected,
            requires_full_context=requires_full_context,
            requires_reasoning=requires_reasoning,
            requires_creativity=requires_creativity,
            estimated_tokens=estimated_tokens,
            recommended_model=recommended_model,
            reasoning=reasoning
        )
    
    def _detect_task_type(self, description: str) -> TaskType:
        """Detect the primary task type from description"""
        description_lower = description.lower()
        
        for task_type, patterns in self.task_patterns.items():
            for pattern in patterns:
                if re.search(pattern, description_lower):
                    return task_type
        
        # Default based on keywords
        if "analyze" in description_lower:
            return TaskType.ANALYSIS
        elif "document" in description_lower:
            return TaskType.DOCUMENT
        else:
            return TaskType.EDIT
    
    def _estimate_file_scope(self, description: str) -> int:
        """Estimate number of files affected from description"""
        # Look for file references
        file_patterns = [
            r'\.(?:py|js|ts|tsx|jsx|css|html|json|md|yaml|yml)',
            r'(?:file|module|component)s?\b',
            r'(?:all|every|each)\s+(?:file|module|component)s?',
            r'(?:entire|whole)\s+(?:codebase|project|system)'
        ]
        
        description_lower = description.lower()
        
        if re.search(r'(?:entire|whole)\s+(?:codebase|project|system)', description_lower):
            return 10  # Large scope
        elif re.search(r'(?:all|every|multiple)\s+(?:file|module|component)s?', description_lower):
            return 5   # Medium scope
        elif len(re.findall(file_patterns[0], description)) > 1:
            return len(re.findall(file_patterns[0], description))
        else:
            return 1   # Single file default
    
    def _requires_full_context(self, description: str, task_type: TaskType) -> bool:
        """Determine if task requires full codebase context"""
        context_indicators = [
            r'(?:entire|whole|full)\s+(?:codebase|project|system)',
            r'(?:all|every)\s+(?:file|module|component)s?',
            r'(?:architecture|structure|design)\s+(?:of|for)',
            r'(?:refactor|restructure)\s+(?:entire|whole)',
            r'dependencies',
            r'integration'
        ]
        
        description_lower = description.lower()
        
        # Task types that typically need full context
        if task_type in [TaskType.ARCHITECTURE, TaskType.DESIGN, TaskType.REFACTOR]:
            return True
        
        # Check for context indicators
        for pattern in context_indicators:
            if re.search(pattern, description_lower):
                return True
        
        return False
    
    def _requires_reasoning(self, description: str, task_type: TaskType) -> bool:
        """Determine if task requires complex reasoning"""
        reasoning_indicators = [
            r'(?:why|how|explain)',
            r'(?:debug|diagnose|troubleshoot)',
            r'(?:optimize|improve)\s+(?:performance|efficiency)',
            r'(?:design|architect|plan)',
            r'(?:analyze|evaluate|assess)',
            r'(?:decide|choose|determine)\s+(?:best|optimal)',
            r'trade-?off'
        ]
        
        description_lower = description.lower()
        
        # Task types that typically need reasoning
        if task_type in [TaskType.ARCHITECTURE, TaskType.DESIGN, TaskType.DEBUG, 
                         TaskType.TROUBLESHOOT, TaskType.SYNTHESIS]:
            return True
        
        # Check for reasoning indicators
        for pattern in reasoning_indicators:
            if re.search(pattern, description_lower):
                return True
        
        return False
    
    def _requires_creativity(self, description: str, task_type: TaskType) -> bool:
        """Determine if task requires creative problem solving"""
        creativity_indicators = [
            r'(?:create|design|build)\s+(?:new|novel|innovative)',
            r'(?:implement|develop)\s+(?:solution|approach)',
            r'from\s+scratch',
            r'(?:architect|structure)\s+(?:new|system)',
            r'(?:innovative|creative|novel)\s+(?:solution|approach)'
        ]
        
        description_lower = description.lower()
        
        # Task types that typically need creativity
        if task_type in [TaskType.ARCHITECTURE, TaskType.DESIGN]:
            return True
        
        # Check for creativity indicators
        for pattern in creativity_indicators:
            if re.search(pattern, description_lower):
                return True
        
        return False
    
    def _estimate_tokens(self, description: str, files: int, 
                        complexity: ComplexityLevel) -> int:
        """Estimate token usage for the task"""
        base_tokens = len(description.split()) * 2  # Rough estimate
        
        # File-based multiplier
        file_multiplier = min(files * 500, 5000)  # Cap at 5k per file set
        
        # Complexity multiplier
        complexity_multipliers = {
            ComplexityLevel.TRIVIAL: 1,
            ComplexityLevel.SIMPLE: 2,
            ComplexityLevel.MEDIUM: 5,
            ComplexityLevel.COMPLEX: 10,
            ComplexityLevel.CRITICAL: 20
        }
        
        complexity_mult = complexity_multipliers[complexity]
        
        return base_tokens + (file_multiplier * complexity_mult)
    
    def _recommend_model(self, complexity: ComplexityLevel, task_type: TaskType,
                        requires_reasoning: bool, requires_creativity: bool) -> str:
        """Recommend the best model for the task"""
        # Critical tasks always use Claude
        if complexity == ComplexityLevel.CRITICAL:
            return "claude-opus-4"
        
        # Tasks requiring creativity or complex reasoning use Claude
        if requires_creativity or (requires_reasoning and complexity.value >= 2):
            return "claude-opus-4"
        
        # Synthesis always uses Claude
        if task_type == TaskType.SYNTHESIS:
            return "claude-opus-4"
        
        # Security-related tasks use Claude
        if task_type == TaskType.REVIEW and "security" in str(task_type):
            return "claude-opus-4"
        
        # Simple tasks can use Kimi Pro
        if complexity in [ComplexityLevel.TRIVIAL, ComplexityLevel.SIMPLE]:
            if task_type in [TaskType.SEARCH, TaskType.READ, TaskType.EDIT]:
                return "kimi-pro"
        
        # Analysis tasks can use Gemini via MCP
        if task_type == TaskType.ANALYSIS and not requires_creativity:
            return "gemini-mcp"
        
        # Default to Claude for safety
        return "claude-opus-4"