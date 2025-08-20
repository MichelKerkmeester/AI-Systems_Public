# Figma MCP - MCP Knowledge - v2.0.0

Streamlined design extraction and style application reference for Webflow site building with standardized performance metrics and comprehensive design patterns.

## Table of Contents
1. [🚀 Quick Activation](#1--quick-activation)
2. [🎨 Core Operations](#2--core-operations)
3. [✅ Webflow Design Patterns](#3--webflow-design-patterns)
4. [💬 Conversation Patterns](#4--conversation-patterns)
5. [🎯 Design Tokens](#5--design-tokens)
6. [🚨 Error Recovery](#6--error-recovery)
7. [📊 Performance Metrics](#7--performance-metrics)
8. [🔄 Integration Triggers](#8--integration-triggers)
9. [⚠️ API Error Codes](#9--api-error-codes)
10. [📌 Quick Reference](#10--quick-reference)

---

## 1. 🚀 Quick Activation

### When to Trigger Figma MCP

**Automatic Triggers from Webflow Context:**
```yaml
Explicit Triggers:
  - "import from Figma"
  - "apply design system"
  - "sync with mockup"
  - "extract styles"
  - "get design specs"
  - "update from prototype"
  - "check design tokens"
  - "import components"

Implicit Triggers (Auto-detect):
  - Design file URL mentioned
  - Component creation requested
  - Style system needed
  - Typography setup mentioned
  - Color palette required
  - When consistency check needed
```

**Context Detection Matrix:**
```yaml
Design Import:
  Trigger: Figma file shared or referenced
  Action: Extract complete design system
  Time: 30-45 seconds
  Coverage: Colors, typography, spacing, components
  API Calls: 15-25
  
Style Sync:
  Trigger: Design updates mentioned
  Action: Re-fetch latest styles
  Elements: Auto-detect changes
  Validation: Check consistency
  Time: 15-20 seconds
  API Calls: 8-12
  
Component Mapping:
  Trigger: Component creation requested
  Action: Map Figma to Webflow elements
  Mapping: Auto-generate classes
  Time: 20-30 seconds
  API Calls: 10-15
  
Token Extraction:
  Trigger: Design system needed
  Action: Extract all design tokens
  Output: CSS variables, classes
  Time: 10-15 seconds
  API Calls: 5-8
```

**Integration Decision Tree:**
```
Design Integration Needed?
├─ New site setup?
│  └─ Full design import (30-45s)
├─ Style update?
│  └─ Sync specific tokens (15-20s)
├─ Component needed?
│  └─ Extract and map (20-30s)
├─ Consistency check?
│  └─ Validate against Figma (10-15s)
└─ Manual request?
   └─ Execute specific extraction
```

---

## 2. 🎨 Core Operations

### Essential Design Operations with Performance Data

**Extract Design System:**
```yaml
Operation: Full design extraction
Extracts:
  - Color palette (all variants)
  - Typography (all text styles)
  - Spacing system (8px grid)
  - Effects (shadows, blurs)
  - Border styles

Performance:
  - Initial scan: 3-5 seconds
  - Token extraction: 8-12 seconds
  - Style generation: 5-8 seconds
  - Total time: 30-45 seconds
  - API calls: 15-25
  - Rate limit: 60/minute

Output:
  - CSS variables
  - Webflow classes
  - Design documentation
  - Token JSON
```

**Import Typography:**
```yaml
Operation: Text styles extraction
Captures:
  - Font families
  - Font weights
  - Font sizes (responsive)
  - Line heights
  - Letter spacing
  - Text transforms

Performance:
  - Detection: 1 second per style
  - Conversion: 2 seconds per style
  - Class generation: 1 second per style
  - Total per style: 4 seconds
  - Full set (10-15 styles): 40-60 seconds
  - API calls: 2 per style
  - Rate limit: 60/minute

Webflow Mapping:
  - H1-H6 tags
  - Body text classes
  - Link styles
  - Rich text presets
```

**Extract Components:**
```yaml
Operation: Component mapping
Processes:
  - Buttons (all states)
  - Cards (variations)
  - Navigation (responsive)
  - Forms (field types)
  - Modals (interactions)

Performance:
  - Component scan: 3-5 seconds
  - Property extraction: 5-8 seconds
  - State mapping: 3-5 seconds
  - Webflow generation: 8-12 seconds
  - Total time: 20-30 seconds
  - API calls: 10-15
  - Rate limit: 60/minute

Success Indicators:
  - All variants captured
  - States preserved
  - Interactions mapped
  - Classes generated
```

**Color System Import:**
```yaml
Operation: Color extraction
Includes:
  - Primary colors
  - Secondary colors
  - Neutral palette
  - Semantic colors (success, error)
  - Opacity variations

Performance:
  - Palette scan: 2 seconds
  - Variant generation: 3-5 seconds
  - Contrast check: 2 seconds
  - CSS generation: 2 seconds
  - Total time: 10-15 seconds
  - API calls: 5-8
  - Rate limit: 60/minute

Output:
  - CSS custom properties
  - Webflow swatches
  - Accessibility report
  - Color documentation
```

---

## 3. ✅ Webflow Design Patterns

### Comprehensive Design Integration Workflows

**Pattern: Complete Design System Import**
```yaml
Trigger: "import Figma design system"
Complexity: High
Time: 30-45 seconds
API Calls: 15-25
Coverage: 95%

Process:
  1. Connect to Figma file (3s)
  2. Scan all frames (5s)
  3. Extract color tokens (5s)
  4. Import typography (15s)
  5. Map components (10s)
  6. Generate spacing (3s)
  7. Create Webflow classes (4s)
  8. Document system (0s - async)

Success Criteria:
  - All colors imported
  - Typography mapped
  - Components ready
  - Spacing consistent
  - Documentation complete

Failure Recovery:
  - Retry connection once
  - Report missing elements
  - Continue with available
  - Provide manual options
```

**Pattern: Component Library Sync**
```yaml
Trigger: "sync Figma components"
Complexity: Medium
Time: 20-30 seconds
API Calls: 10-15
Coverage: 90%

Process:
  1. Identify components (3s)
  2. Extract properties (5s)
  3. Map to Webflow (8s)
  4. Generate symbols (5s)
  5. Create interactions (5s)
  6. Apply auto-layout (3s)
  7. Test responsive (1s)

Validation Points:
  - Component structure intact
  - Properties preserved
  - States functional
  - Responsive behavior
  - Interactions working
```

**Pattern: Style Update Check**
```yaml
Trigger: "check for design updates"
Complexity: Low
Time: 10-15 seconds
API Calls: 5-8
Coverage: 100%

Process:
  1. Connect to Figma API (2s)
  2. Check version history (2s)
  3. Compare with current (3s)
  4. Identify changes (2s)
  5. Report differences (2s)
  6. Suggest updates (2s)
  7. Apply if approved (3s)

Change Detection:
  - Color modifications
  - Typography updates
  - Spacing adjustments
  - New components
  - Deleted elements
```

---

## 4. 💬 Conversation Patterns

### Simple Triggers with Performance Context

**Basic Design Import:**
```
User: "import my Figma design"
Figma MCP: "I'll import your Figma design system!
        
        Extracting from Figma:
        🎨 File: Your Design System v2.0
        📊 Found: 12 colors, 8 text styles, 15 components
        ⚙️ Processing: Colors, Typography, Spacing
        ⏱️ Estimated time: 30-45 seconds
        
        Importing now...
        
        ✅ Design system imported successfully!
        • Colors: 12 swatches created
        • Typography: 8 text styles mapped
        • Components: 15 symbols ready
        • Spacing: 8px grid applied
        
        Would you like to:
        • Apply to existing pages?
        • Create style guide?
        • Map to CMS templates?"
```

**Component Sync with Results:**
```
User: "sync button component"
Figma MCP: "Syncing button component from Figma!
        
        Component Analysis:
        🔍 Component: Button
        📋 Variants: 4 detected
        🎨 States: Default, Hover, Active, Disabled
        
        Extracting properties:
        • Size variants: Small, Medium, Large
        • Style variants: Primary, Secondary, Ghost
        • Icons: Leading, Trailing options
        
        [Mapping to Webflow...]
        ✅ Primary button class created
        ✅ Size modifiers added
        ✅ Hover states configured
        
        ✅ Button component synced!
        • 12 total combinations available
        • All states functional
        • Responsive sizing applied
        • Time taken: 20 seconds
        
        Preview in Designer to test!"
```

### Figma-Specific Interaction Patterns

| User Says | Figma Response | Coverage | Time | Success Rate |
|-----------|---------------|----------|------|--------------|
| "import design" | "Extracting full system!" | Complete import | 30-45s | 95% |
| "get colors" | "Importing color palette..." | Colors only | 10-15s | 100% |
| "sync typography" | "Fetching text styles!" | Typography | 40-60s | 98% |
| "check components" | "Scanning components..." | Component audit | 15-20s | 92% |
| "apply spacing" | "Extracting grid system!" | Layout grid | 10-15s | 95% |
| "update styles" | "Checking for changes..." | Differential sync | 15-20s | 90% |

---

## 5. 🎯 Design Tokens

### Token Extraction Categories

| Token Type | Properties Extracted | Webflow Application | Performance | Priority |
|------------|---------------------|-------------------|-------------|----------|
| **Colors** | Hex, RGB, HSL, opacity | Global swatches | 1s/color | P1 Critical |
| **Typography** | Family, size, weight, line-height | Text classes | 4s/style | P1 Critical |
| **Spacing** | Margins, padding, gaps | Utility classes | 2s/set | P2 Important |
| **Shadows** | Offset, blur, spread, color | Effect classes | 2s/shadow | P2 Important |
| **Borders** | Width, style, color, radius | Border classes | 1s/style | P3 Optional |
| **Transitions** | Duration, easing, delay | Animation classes | 2s/animation | P3 Optional |

### Design System Structure

**Color Token Organization:**
```yaml
Primary Colors:
  - primary-100: Lightest
  - primary-300: Light
  - primary-500: Base
  - primary-700: Dark
  - primary-900: Darkest

Semantic Colors:
  - success: Green variants
  - warning: Yellow variants
  - error: Red variants
  - info: Blue variants

Neutrals:
  - gray-50 to gray-900
  - black: #000000
  - white: #FFFFFF

Application:
  - CSS variables created
  - Webflow swatches added
  - Classes auto-generated
```

---

## 6. 🚨 Error Recovery

### Common Issues & Solutions with Success Rates

**Figma Connection Failed:**
```yaml
Issue: Cannot access Figma file
Frequency: 10% of operations
Root Causes:
  - File permissions
  - API token expired
  - Network timeout
  - File deleted/moved

Solution Cascade:
  1. Check file permissions (30% success)
  2. Refresh API token (50% success)
  3. Retry with delay (70% success)
  4. Request new share link (90% success)
  5. Manual style input (100% success)

Recovery time: 15-30 seconds
User notification: Automatic
```

**Component Mapping Issues:**
```yaml
Issue: Component structure incompatible
Frequency: 15% of imports
Root Causes:
  - Complex auto-layout
  - Nested components
  - Custom properties
  - Plugin-generated content

Solution Steps:
  1. Simplify structure (40% fix)
  2. Flatten components (60% fix)
  3. Manual mapping (80% fix)
  4. Recreate in Webflow (95% fix)
  5. Skip problematic (100% fix)

Recovery time: 30-45 seconds
Debug info: Provided automatically
```

---

## 7. 📊 Performance Metrics

### Design Import Performance

**Import Speed by Complexity:**
```yaml
Simple (5-10 elements):
  - Scan time: 3-5 seconds
  - Extraction: 5-8 seconds
  - Application: 3-5 seconds
  - Total: 10-15 seconds
  - API calls: 5-8

Medium (10-30 elements):
  - Scan time: 5-8 seconds
  - Extraction: 10-15 seconds
  - Application: 8-12 seconds
  - Total: 20-30 seconds
  - API calls: 10-15

Complex (30+ elements):
  - Scan time: 8-12 seconds
  - Extraction: 15-20 seconds
  - Application: 10-15 seconds
  - Total: 30-45 seconds
  - API calls: 15-25

Enterprise (100+ elements):
  - Scan time: 15-20 seconds
  - Extraction: 30-40 seconds
  - Application: 20-30 seconds
  - Total: 60-90 seconds
  - API calls: 30-50
```

**Token Extraction Metrics:**
```yaml
Processing Speed by Token Type:
  Colors: 10 per second
  Text styles: 0.25 per second (4s each)
  Components: 0.067 per second (15s each)
  Effects: 0.5 per second (2s each)
  Spacing: 0.5 per second (2s each)

Rate Limits:
  - Figma API: 60 requests/minute
  - Warning threshold: 50 requests/minute
  - Auto-throttle: 55 requests/minute
```

---

## 8. 🔄 Integration Triggers

### Webflow-Specific Integration Points

**Design System Application:**
```yaml
Trigger Points:
  - New site creation
  - Style system setup
  - Component library build
  - Design update available

Automatic Actions:
  - Extract from Figma
  - Generate Webflow classes
  - Apply to elements
  - Create documentation
  - Set up variables

Integration time: 30-45 seconds
Coverage: 95% of design system
API calls: 15-25
Rate limit: 60/minute
```

---

## 9. ⚠️ API Error Codes

### Figma API Error Reference

| Error Code | Meaning | User Message | Recovery Action |
|------------|---------|--------------|-----------------|
| 403 | Forbidden | "Cannot access Figma file" | Check permissions |
| 404 | Not Found | "Figma file not found" | Verify URL |
| 429 | Rate Limited | "Too many requests" | Wait 60 seconds |
| 500 | Server Error | "Figma service issue" | Retry in 5 minutes |
| TIMEOUT | Network Issue | "Connection timeout" | Check network |

### Webflow Integration Errors

| Error Code | Meaning | User Message | Recovery Action |
|------------|---------|--------------|-----------------|
| INVALID_TOKEN | Bad design token | "Token format invalid" | Validate format |
| DUPLICATE_CLASS | Class exists | "Style already exists" | Merge or rename |
| LIMIT_EXCEEDED | Too many tokens | "Token limit reached" | Consolidate styles |
| SYNC_FAILED | Update failed | "Could not sync" | Manual update |

---

## 10. 📌 Quick Reference

### Instant Operations

| Task | Command | Coverage | Time | API Calls | Result |
|------|---------|----------|------|-----------|--------|
| **Import all** | "import Figma design" | Full system | 30-45s | 15-25 | Complete design |
| **Get colors** | "extract color palette" | All colors | 10-15s | 5-8 | Swatches created |
| **Sync text** | "import typography" | All text styles | 40-60s | 10-15 | Classes ready |
| **Get component** | "import button" | Single component | 15-20s | 5-8 | Symbol created |
| **Check updates** | "check for changes" | Differential | 10-15s | 5-8 | Change log |

### Rate Limit Management

```yaml
API Limits:
  - Maximum: 60 requests/minute
  - Warning: 50 requests/minute
  - Auto-throttle: 55 requests/minute
  - Recovery: Wait 60 seconds
  
Best Practices:
  - Batch similar operations
  - Cache extracted tokens
  - Use differential sync
  - Monitor usage in real-time
```

---

*This intelligence document provides comprehensive guidance for importing and syncing Figma designs with Webflow sites using Figma MCP. All operations include standardized performance metrics and API rate limit management.*