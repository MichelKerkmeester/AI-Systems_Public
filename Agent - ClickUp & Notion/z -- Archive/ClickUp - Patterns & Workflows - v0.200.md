# ClickUp - Patterns & Workflows - v0.200

Complete pattern library for ClickUp workspace operations with built-in complexity challenges and simplification gates.

## 📋 Table of Contents

1. [🎯 Overview](#1--overview)
2. [🎯 Intent Patterns](#2--intent-patterns)
3. [📝 Creation Operation Patterns](#3--creation-operation-patterns)
4. [🚀 Workspace Patterns](#4--workspace-patterns)
5. [📊 Bulk Operation Patterns](#5--bulk-operation-patterns)
6. [🔧 Simplification Patterns](#6--simplification-patterns)
7. [🧠 ATLAS Thinking Patterns](#7--atlas-thinking-patterns)
8. [🚨 Recovery Patterns](#8--recovery-patterns)
9. [📈 Performance Metrics](#9--performance-metrics)
10. [📄 Pattern Learning](#10--pattern-learning)

---

## 1. 🎯 Overview

This document defines achievable patterns for ClickUp workspace operations, with every pattern including complexity challenges and simplification alternatives.

### Core Philosophy
- **Challenge first**: Question complexity before implementing
- **Minimal viable**: Start with essential features only
- **Performance aware**: Build for <5000 items
- **Pattern learning**: Adapt based on user preferences

### Performance Baseline
- Pattern recognition: <1 second
- Simple operations: 2-5 seconds
- Complex operations: 10-30 seconds
- Bulk operations: 1-2 seconds per item
- API rate limit: 60 requests/minute

---

## 2. 🎯 Intent Patterns

### Workspace Creation Intents

| User Says | Complexity | Challenge Point | Alternative | Thinking Rounds |
|-----------|-----------|-----------------|-------------|-----------------|
| "Create task" | Low | None | N/A | 1-2 |
| "Sprint board" | Medium | "Simple board?" | Basic list | 3-4 |
| "Complete CRM" | High | "Start minimal?" | Contacts only | 7-10 |
| "Everything" | Maximum | "Phase it?" | Core features | 8-10 |
| "Project system" | Medium | "How many projects?" | Single list | 4-6 |
| "Time tracking" | Medium | "Manual OK?" | No automation | 3-5 |

### Complexity Challenge Patterns

**Low Complexity Pattern:**
```python
def handle_simple_request(request):
    # No challenge needed
    thinking_rounds = 1-2
    execute_directly()
```

**Medium Complexity Pattern:**
```python
def handle_medium_request(request):
    challenge = "Would simpler work?"
    if user_accepts_simple:
        thinking_rounds = 2-3
        execute_minimal()
    else:
        thinking_rounds = 4-6
        execute_standard()
```

**High Complexity Pattern:**
```python
def handle_complex_request(request):
    challenge = "Start with 20% features?"
    if user_accepts_minimal:
        thinking_rounds = 3-4
        execute_core_only()
    else:
        thinking_rounds = 7-10
        execute_phased()
```

---

## 3. 📝 Creation Operation Patterns

### Pattern: Task Creation

**Pattern Name:** Minimal Task Creation
**Complexity:** Low
**Challenge:** None needed
**Time:** 2-3 seconds

**Implementation:**
```python
task_defaults = {
    'minimal': {
        'fields': ['name', 'status'],
        'views': ['list'],
        'automation': None
    },
    'standard': {
        'fields': ['name', 'status', 'priority', 'due_date'],
        'views': ['list', 'board'],
        'automation': 'due_date_reminder'
    }
}
```

**Challenge Gate:**
```markdown
If fields_requested > 5:
    "Do you need all fields initially?"
If automation_complex:
    "Manual process acceptable?"
```

### Pattern: Sprint Planning

**Pattern Name:** Agile Sprint System
**Complexity:** Medium
**Challenge:** "Simple sprints or full agile?"
**Time:** 15-20 seconds

**Minimal Version:**
```python
sprint_minimal = {
    'lists': 1,  # Current sprint only
    'fields': ['status', 'assignee', 'points'],
    'views': ['board'],
    'automation': None
}
```

**Standard Version:**
```python
sprint_standard = {
    'lists': 3,  # Backlog, Sprint, Done
    'fields': ['status', 'assignee', 'points', 'epic', 'priority'],
    'views': ['board', 'list', 'velocity'],
    'automation': ['sprint_rollover', 'capacity_alerts']
}
```

---

## 4. 🚀 Workspace Patterns

### Pattern: Agency Management

**Pattern Name:** Agency Workspace
**Complexity:** High
**Challenge:** ALWAYS present phased approach
**Default Thinking:** 7-10 rounds

**Phase 1 (Minimal):**
```python
agency_phase1 = {
    'structure': {
        'spaces': 1,
        'lists': 3,  # Clients, Projects, Tasks
        'fields': 4  # Essential only
    },
    'complexity': 'low',
    'thinking_rounds': 3-4
}
```

**Phase 2 (Standard):**
```python
agency_phase2 = {
    'structure': {
        'spaces': 1,
        'lists': 5,  # +Time, +Invoices
        'fields': 8,
        'automation': ['time_tracking', 'invoice_prep']
    },
    'complexity': 'medium',
    'thinking_rounds': 5-6
}
```

**Phase 3 (Complete):**
```python
agency_phase3 = {
    'structure': {
        'spaces': 3,  # Separate by function
        'lists': 12,
        'fields': 15,
        'automation': 'full_workflow'
    },
    'complexity': 'high',
    'thinking_rounds': 8-10
}
```

### Pattern: Personal Productivity

**Pattern Name:** Personal Task System
**Complexity:** Low
**Challenge:** "GTD or simple lists?"
**Default Thinking:** 2-3 rounds

**Simple Version:**
```python
personal_simple = {
    'lists': 1,  # Everything in one
    'fields': ['status', 'due_date'],
    'views': ['today', 'list']
}
```

**GTD Version:**
```python
personal_gtd = {
    'lists': 4,  # Inbox, Next, Waiting, Someday
    'fields': ['context', 'energy', 'time_required'],
    'views': ['context', 'today', 'weekly']
}
```

---

## 5. 📊 Bulk Operation Patterns

### Pattern: Mass Updates

**Pattern Name:** Bulk Task Updates
**Complexity:** Low-Medium
**Challenge:** "Update all or filter first?"

**Safe Bulk Pattern:**
```python
def bulk_update_safe(items, update):
    # Always confirm if >20 items
    if len(items) > 20:
        challenge = "Update all {len(items)} items?"
        
    # Batch for performance
    batch_size = 20
    for batch in chunks(items, batch_size):
        update_batch(batch)
        check_rate_limit()
```

### Pattern: Archive Operations

**Pattern Name:** Smart Archiving
**Complexity:** Low
**Challenge:** "Archive or delete?"

**Archive Strategy:**
```python
archive_patterns = {
    'simple': {
        'criteria': 'status=complete AND age>30days',
        'destination': '/Archive/',
        'maintain': False
    },
    'organized': {
        'criteria': 'custom_rules',
        'destination': '/Archive/[Year]/[Month]/',
        'maintain': True
    }
}
```

---

## 6. 🔧 Simplification Patterns

### Pattern: Field Reduction

**Problem:** User wants 15 custom fields
**Challenge:** "Which 5 are essential?"

**Simplification Strategy:**
```python
def simplify_fields(requested_fields):
    essential = identify_essential(requested_fields)
    nice_to_have = requested_fields - essential
    
    proposal = {
        'immediate': essential[:5],
        'phase_2': essential[5:8],
        'consider_later': nice_to_have
    }
    
    return proposal
```

### Pattern: Hierarchy Flattening

**Problem:** 5-level deep hierarchy requested
**Challenge:** "Would 2 levels be clearer?"

**Flattening Strategy:**
```python
def flatten_hierarchy(deep_structure):
    return {
        'original_levels': 5,
        'recommended_levels': 2,
        'organization': 'naming_convention',
        'benefits': ['easier_navigation', 'better_performance']
    }
```

---

## 7. 🧠 ATLAS Thinking Patterns

### Pattern: Complexity Assessment

**Pattern Name:** ATLAS Complexity Check
**Thinking Rounds:** Variable based on complexity

**Process:**
```python
def atlas_thinking_pattern(request):
    # Assess (Round 1)
    complexity = assess_complexity(request)
    
    # Challenge (Round 2)
    if complexity > threshold:
        challenge = generate_challenge(complexity)
        
    # Transform (Round 3-4)
    minimal = transform_to_minimal(request)
    
    # Layer (Round 4-6)
    if user_wants_more:
        enhanced = layer_essentials(minimal)
        
    # Synthesize (Final rounds)
    solution = optimize_for_use(enhanced or minimal)
    
    return solution
```

### Thinking Round Allocation
```python
def allocate_rounds(complexity, user_pattern):
    base_rounds = {
        'minimal': 1-2,
        'simple': 2-3,
        'standard': 4-6,
        'complex': 7-8,
        'maximum': 9-10
    }
    
    # Adjust for patterns
    if user_pattern.prefers_simple:
        return base_rounds - 1
    return base_rounds
```

---

## 8. 🚨 Recovery Patterns

### Pattern: Over-Engineering Recovery

**Error:** Created overly complex workspace
**User Impact:** Overwhelmed, low adoption

**REPAIR Protocol:**
```python
def repair_over_engineering():
    recognize = "Workspace too complex for team size"
    explain = "This complexity might hinder adoption"
    propose = [
        "Simplify to core features",
        "Phase rollout over time",
        "Archive and restart minimal"
    ]
    adapt = user_choice
    iterate = implement_solution
    record = {'lower_complexity_threshold': True}
```

### Pattern: Performance Recovery

**Error:** Structure causing performance issues
**User Impact:** Slow loading, timeouts

**Recovery Strategy:**
```python
def recover_performance():
    issues = identify_bottlenecks()
    
    if issues.list_size > 5000:
        solution = "split_lists"
    if issues.field_count > 10:
        solution = "reduce_fields"
    if issues.view_complexity:
        solution = "simplify_views"
        
    apply_solution(solution)
```

---

## 9. 📈 Performance Metrics

### Operation Performance Targets

| Operation | Target Time | API Calls | Success Rate | Complexity Check |
|-----------|------------|-----------|--------------|------------------|
| Create task | 2-3s | 1-2 | 98% | None |
| Create list | 5-10s | 3-5 | 95% | Fields check |
| Build workspace | 20-30s | 20-30 | 90% | Full challenge |
| Bulk update 50 | 30-60s | 50 | 85% | Confirm first |
| Archive old | 10-20s | 10-20 | 95% | Simple check |

### Complexity Reduction Metrics

```python
complexity_metrics = {
    'fields_reduced': 'average 60%',
    'lists_consolidated': 'average 50%',
    'automation_simplified': 'average 70%',
    'hierarchy_flattened': 'average 2 levels',
    'adoption_improved': '85% vs 45%'
}
```

---

## 10. 📄 Pattern Learning

### Tracked Patterns

```python
class PatternTracking:
    def __init__(self):
        self.preference_patterns = {
            'accepts_challenges': 0.0,
            'chooses_minimal': 0.0,
            'adds_complexity_later': 0.0,
            'average_thinking_rounds': 0.0
        }
        
        self.success_patterns = {
            'simplified_workspaces': [],
            'complex_workspaces': [],
            'abandoned_features': []
        }
        
        self.learning_insights = {
            'optimal_field_count': 0,
            'preferred_hierarchy': 0,
            'automation_appetite': 0.0
        }
```

### Adaptive Rules

1. **After 2 simplifications** → Default to minimal
2. **After 3 challenge accepts** → Lead with simple
3. **After complexity rejection** → Max 5 fields initially
4. **After successful pattern** → Reuse structure

### Pattern Application

**New User:**
```python
if interaction_count < 3:
    offer_guided_choices = True
    suggest_simple_first = True
    explain_benefits = True
```

**Simplicity Preferrer:**
```python
if patterns.accepts_challenges > 0.6:
    default_to_minimal = True
    skip_complex_options = True
    max_initial_fields = 4
```

**Power User:**
```python
if patterns.average_rounds > 7:
    allow_complex_initial = True
    still_challenge_excess = True
    focus_on_performance = True
```

---

## Quick Reference

### Can Do ✅
- Single tasks quickly
- Lists with views
- Basic automation
- Bulk operations
- Archive strategies
- Phased rollouts

### Challenge Always 🤔
- Multi-space systems
- 8+ custom fields
- Complex automation
- Deep hierarchies
- Everything requests

### Simplify To 📉
- Single space with folders
- 3-5 essential fields
- Manual processes first
- 2-level hierarchy max
- Phase complex rollouts

---

*Every pattern includes complexity challenges. Build minimal viable first. Learn from user choices. Create workspaces that get adopted, not admired.*