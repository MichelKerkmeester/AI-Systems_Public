# Product Owner - Template: Text Mode - v0.310

## 📋 Table of Contents

1. [✏️ TEXT MODE OVERVIEW](#✏️-text-mode-overview)
2. [🔧 COMPONENT DESCRIPTIONS](#🔧-component-descriptions)
3. [🔍 FEATURE DESCRIPTIONS](#🔍-feature-descriptions)
4. [🎯 TECHNICAL IMPLEMENTATION NOTES](#🎯-technical-implementation-notes)
5. [💡 BUSINESS LOGIC DESCRIPTIONS](#💡-business-logic-descriptions)
6. [📋 TICKET DESCRIPTIONS](#📋-ticket-descriptions)
7. [📚 DOCUMENTATION SNIPPETS](#📚-documentation-snippets)

---

## 1. ✏️ TEXT MODE OVERVIEW

### Command: `$text`

- **Purpose:** Create technical descriptions for components, features, and implementations
- **Output:** Always as artifact
- **Thinking Rounds:** 1-2 (minimal complexity)
- **Focus:** Clear technical descriptions for tickets, specs, and documentation
- **Primary Use:** Component descriptions, implementation notes, technical summaries
- **Format:** Markdown-ready for Jira, Linear, GitHub Issues

---

## 2. 🔧 COMPONENT DESCRIPTIONS

### UI Component Template
```markdown
# Component: [ComponentName]

## Brief Description
"A [type] component that [primary function] by [method]. It [key behavior] and provides [main value]."

## Detailed Description
"The [ComponentName] handles [primary responsibility] within [system/feature]. It accepts [input type] and renders [output type], managing [state/data] internally. Integrates with [related components] to provide [combined functionality]. Optimized for [use case] with [optimization detail]."

## Props/Parameters
- `data`: [Type] - [Purpose and validation]
- `onAction`: Function - [Trigger condition and return]
- `config`: Object - [Configuration options]
- `isEnabled`: Boolean - [Controls behavior]

## Technical Notes
- State: [How state is managed]
- Performance: [Optimization approach]
- Dependencies: [Required libraries]
- Accessibility: [WCAG compliance level]

## Usage
"Use when [scenario]. Effective for [use case] where [requirement]. Avoid for [anti-pattern] due to [reason]."
```

### Form Component Template
```markdown
# Form: [FormName]

## Brief Description
"A [validation-type] form that [collects/processes] [data type] with [key feature]."

## Field Specifications
- `emailField`: Email validation, required, triggers [action]
- `passwordField`: Min 8 chars, complexity rules
- `selectField`: Dynamic options from [source]
- `dateField`: Date picker with [constraints]

## Validation
- Field-level: [onChange/onBlur] validation
- Form-level: Cross-field validation for [relationships]
- Async: Server validation for [unique checks]

## Submission
"On submit: [validates] → [sends to endpoint] → [success action] or [error handling]."
```

---

## 3. 🔍 FEATURE DESCRIPTIONS

### Feature Overview Template
```markdown
# Feature: [FeatureName]

## One-Line Summary
"[Feature] enables [capability] through [method]."

## Ticket Description
"Implement [feature] to allow users to [primary action]. This provides [benefit] by [technical approach]. Integrates with [existing system] ensuring [continuity]."

## Technical Specification
"The [feature] system provides [capability] through [architecture]. Processes [input] using [algorithm] to produce [output]. Leverages [technology] with [performance characteristic], maintaining [constraint] while delivering [metric]."

## User Documentation
"[Feature] helps you [accomplish goal] by [user-friendly explanation]. When you [trigger], the system [behavior], allowing you to [outcome]. Best used when [use case]."

## Priority
"Critical for [business goal]. Blocks [dependent feature]. Enables [future capability]."
```

### Dashboard Feature Template
```markdown
# Dashboard: [DashboardName]

## Brief Description
"Real-time [metric type] dashboard displaying [data categories] with [update frequency]."

## Technical Architecture
"Aggregates data from [sources] using [method]. Renders [number] widgets with [visualization types], updating via [WebSocket/polling]. Data cached at [level] for [duration]."

## Widgets
- `MetricCard`: Displays [KPI] with [trend]
- `ChartWidget`: Renders [chart type] for [data]
- `FilterBar`: Controls [data scope]
- `DataTable`: Paginated with [features]

## Performance
"Handles [volume] data points with [latency] render time. Optimized using [technique]."
```

---

## 4. 🎯 TECHNICAL IMPLEMENTATION NOTES

### Implementation Note Template
```markdown
# Implementation: [Feature/Component]

## Approach
"Implement using [pattern] to achieve [goal]. Provides [benefits] while maintaining [constraints]."

## Technical Details
- **Algorithm**: [Specific algorithm] for [processing]
- **Data Flow**: [Source] → [Transform] → [Destination]
- **State**: [Redux/Context/Local] for [scope]
- **Caching**: [Level] cache with [TTL]
- **Security**: Validate [where], sanitize [what]

## Performance
"Optimize for [metric] by [technique]. Expected [throughput/latency]."

## Testing
"Unit test [components]. Integration test [flows]. Performance test with [load]."
```

### Optimization Note Template
```markdown
# Optimization: [Area]

## Current State
"Currently [problem] causing [impact]. Measured [metric] shows [value]."

## Proposed Solution
"Implement [optimization] to reduce [metric] by [percentage]. Involves [changes] to [components]."

## Implementation Phases
- **Phase 1**: [Quick wins] - [timeframe]
- **Phase 2**: [Major changes] - [timeframe]
- **Phase 3**: [Fine tuning] - [timeframe]

## Expected Impact
"Reduce [metric] from [current] to [target]. Improve [UX aspect] by [measurement]."
```

---

## 5. 💡 BUSINESS LOGIC DESCRIPTIONS

### Business Rule Template
```markdown
# Rule: [RuleName]

## Brief Description
"[Enforces/Calculates/Validates] [business concept] based on [conditions]."

## Logic
"When [trigger], evaluate [criteria] to determine [outcome]. If [condition A], then [action A]. Else if [condition B], then [action B]. Default: [fallback]."

## Formula
```
IF (condition1 AND condition2) THEN
  result = calculation
ELSE IF (condition3) THEN  
  result = alternative
ELSE
  result = default
```

## Dependencies
"Requires [data] from [sources]. Must execute [before/after] [other rule]."

## Edge Cases
"Handles [null values] by [approach]. When [race condition], [resolution]."
```

### Workflow Template
```markdown
# Workflow: [WorkflowName]

## Brief Description
"Orchestrates [process] through [number] stages with [decision points]."

## Stages
1. **Initiation**: [Trigger] creates [entity] with [initial state]
2. **Processing**: [Actor] performs [action] resulting in [state change]
3. **Validation**: System checks [criteria] before [progression]
4. **Completion**: [Final action] marks [end state]

## Transitions
"Move from [Stage A] to [Stage B] when [condition]. Revert to [Stage C] if [error]."

## Automation
"Auto-advance when [criteria met]. Send notifications at [stages]. Timeout after [duration]."
```

---

## 6. 📋 TICKET DESCRIPTIONS

### Bug Fix Template
```markdown
# Bug: [Issue Name]

## Brief Description
"[Component] incorrectly [behavior] when [condition], causing [impact]."

## Details
"The [component] fails to [expected behavior] under [conditions]. Occurs because [root cause]. Users experience [symptoms] resulting in [business impact]."

## Reproduction
"Navigate to [location]. Perform [action]. Observe [incorrect result] instead of [expected]."

## Technical Context
"Bug exists in [code location] where [technical explanation]. Affects [data flow]."

## Fix Approach
"[Solution description]. Update [component] to [correct behavior]."
```

### Feature Implementation Template
```markdown
# Feature: [Feature Name]

## Brief Description
"Add [capability] to allow [user group] to [action] achieving [outcome]."

## Details
"Implement [feature description] enabling users to [specific actions]. Integrates with [existing components] and provides [new capabilities]. Uses [technical approach] ensuring [performance]."

## User Story
"As a [user type], I want to [action] so that [benefit]."

## Technical Scope
"Requires changes to [components]. Adds [new elements]. Modifies [existing flows]."

## Acceptance Criteria
- User can [complete primary flow]
- System [validates correctly]
- Performance meets [thresholds]
- Tests pass [coverage requirement]
```

---

## 7. 📚 DOCUMENTATION SNIPPETS

### How It Works Template
```markdown
# How [Feature] Works

## Overview
"[Feature] operates by [high-level process] to achieve [goal]."

## Process
"When you [initiate action], the system [step 1]. This triggers [step 2] which [transformation]. The result is [step 3] before [outcome]. Throughout, [monitoring] ensures [quality]."

## Technical Details
"[Component A] handles [responsibility], while [Component B] manages [other responsibility]. Data flows from [source] through [pipeline] to [destination]."

## Example
"User wants to [use case]: They [action] with [data]. System [processes] in [time]. Result shows [output]."
```

### Configuration Template
```markdown
# Configuration: [Setting Name]

## Brief Description
"Controls [behavior/feature] affecting [system aspect]."

## Details
"Determines [detailed behavior] of [system/feature]. When set to [value A], system [behavior A]. When [value B], it [behavior B]. Default [value] recommended for [use case]."

## Valid Values
- `value1`: [Effect and when to use]
- `value2`: [Effect and when to use]
- `value3`: [Effect and when to use]

## Impact
"Affects [components/performance]. Requires [restart/refresh]. Interacts with [other settings]."

## Examples
"For [use case 1], set to [value]. For [use case 2], use [value] to achieve [goal]."
```

---

*Concise technical descriptions for tickets, specs, and documentation. All outputs as artifacts.*