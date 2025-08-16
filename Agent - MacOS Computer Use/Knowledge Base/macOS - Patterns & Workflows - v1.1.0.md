# macOS Computer Use - Patterns & Workflows - v1.1.0

Comprehensive pattern library for natural language to macOS UI operation mapping with streamlined 3-mode system.

## Table of Contents
1. [🎯 INTENT RECOGNITION ENGINE](#1--intent-recognition-engine)
2. [📱 APPLICATION PATTERNS](#2--application-patterns)
3. [🖱️ INTERACTION PATTERNS](#3-️-interaction-patterns)
4. [⌨️ KEYBOARD PATTERNS](#4-️-keyboard-patterns)
5. [🔄 WORKFLOW PATTERNS](#5--workflow-patterns)
6. [🪟 WINDOW MANAGEMENT](#6--window-management)
7. [📋 FORM AUTOMATION](#7--form-automation)
8. [🔍 SEARCH & FINDING PATTERNS](#8--search--finding-patterns)
9. [📊 COMPOSITE WORKFLOWS](#9--composite-workflows)
10. [⚡ QUICK OPERATIONS](#10--quick-operations)

---

## 1. 🎯 INTENT RECOGNITION ENGINE

### Confidence Scoring
| Confidence | Range | Action | Mode | Example |
|------------|-------|--------|------|---------|
| **Exact** | >0.95 | Execute immediately | Quick | "click Safari" |
| **High** | 0.80-0.95 | Proceed with defaults | Quick/Interactive | "open browser" |
| **Medium** | 0.50-0.79 | Confirm understanding | Interactive | "do something online" |
| **Low** | <0.50 | Use interactive mode | Interactive | "help with computer" |

### Pattern Matching Hierarchy
```
1. Exact Match → Direct operation execution (Quick mode)
2. Application Recognition → Identify target app
3. Action Detection → Determine operation type
4. Element Inference → Find UI elements (Interactive mode)
5. Context Application → Use current state
```

### Mode Selection Logic
```yaml
mode_selection:
  explicit_mode:
    $q_or_$quick: Quick mode
    $w_or_$workflow: Workflow mode
    $int_or_$interactive: Interactive mode
  
  implicit_selection:
    single_clear_action: Quick mode potential
    multi_app_sequence: Workflow mode
    element_finding: Interactive mode
    text_composition: Interactive mode
    vague_request: Interactive mode
    default: Interactive mode
```

---

## 2. 📱 APPLICATION PATTERNS

### Browser Operations
**Triggers:** `browse, search, web, internet, online, google, website`
**Default Mode:** Interactive (Quick for simple URL navigation)

**Safari Implementation:**
```yaml
open_browser:
  - open_application_and_traverse("Safari")
  - Wait for window
  - Focus address bar (⌘L)

search_web:
  - Open Safari
  - Click address bar or press ⌘L
  - type_and_traverse("search query")
  - press_key_and_traverse("Return")

new_tab:
  - press_key_and_traverse("T", modifiers: ["Command"])
  
navigate_to_url:
  - press_key_and_traverse("L", modifiers: ["Command"])
  - type_and_traverse("https://example.com")
  - press_key_and_traverse("Return")
```

### Mail Operations
**Triggers:** `email, message, compose, send mail, inbox, reply`
**Default Mode:** Interactive (guides through composition)

**Implementation:**
```yaml
compose_email:
  mode: Interactive
  steps:
    - open_application_and_traverse("Mail")
    - press_key_and_traverse("N", modifiers: ["Command"])
    - Guide through recipient
    - Guide through subject
    - Assist with body composition
    - Confirm before sending
  
check_email:
  mode: Quick
  steps:
    - open_application_and_traverse("Mail")
    - Click Inbox
    - Review messages
```

### Document Creation
**Triggers:** `write, document, note, text, type, draft, compose`
**Default Mode:** Interactive for complex, Quick for simple

**Implementation:**
```yaml
create_document:
  complex_document:
    mode: Interactive
    guide_through:
      - Document type selection
      - Structure planning
      - Content assistance
      - Formatting help
  
  simple_note:
    mode: Quick
    steps:
      - Open TextEdit/Notes
      - Create new (⌘N)
      - Ready for typing
```

### System Settings
**Triggers:** `settings, preferences, configure, setup, system`
**Default Mode:** Interactive (helps navigate to correct setting)

**Implementation:**
```yaml
open_settings:
  - open_application_and_traverse("System Settings")
  - Search for specific setting (guided)
  - Navigate to pane
  - Adjust as needed
```

---

## 3. 🖱️ INTERACTION PATTERNS

### Click Patterns
| Trigger | Operation | Mode | Target |
|---------|-----------|------|--------|
| "click [element]" | click_and_traverse | Quick | Named element |
| "find and click [element]" | search + click | Interactive | Unknown location |
| "press [button]" | click_and_traverse | Quick | Button by label |
| "select [option]" | click_and_traverse | Quick | Menu/dropdown item |
| "locate [element]" | refresh + search | Interactive | Find element |

### Type Patterns
| Trigger | Operation | Mode | Behavior |
|---------|-----------|------|----------|
| "$q type [text]" | type_and_traverse | Quick | Direct input |
| "write [long text]" | guided composition | Interactive | Paragraph with help |
| "enter [text]" | type_and_traverse | Quick | Field input |
| "compose [document]" | structured writing | Interactive | Guided composition |
| "fill [field] with [text]" | Click + type | Quick | Form filling |

### Selection Patterns
```yaml
select_text:
  single_word: Double-click
  paragraph: Triple-click
  all: ⌘A
  range: Click and drag
  
select_multiple_items:
  consecutive: Click first, Shift+Click last
  individual: ⌘+Click each item
  all_in_view: ⌘A
```

---

## 4. ⌨️ KEYBOARD PATTERNS

### Universal Shortcuts
```yaml
file_operations:
  new: ⌘N
  open: ⌘O
  save: ⌘S
  save_as: ⌘⇧S
  close: ⌘W
  quit: ⌘Q
  print: ⌘P
  
edit_operations:
  undo: ⌘Z
  redo: ⌘⇧Z
  cut: ⌘X
  copy: ⌘C
  paste: ⌘V
  select_all: ⌘A
  find: ⌘F
  
text_formatting:
  bold: ⌘B
  italic: ⌘I
  underline: ⌘U
```

---

## 5. 🔄 WORKFLOW PATTERNS

### Research Workflow
**Mode:** Workflow ($w)
```yaml
trigger: "research [topic]"
steps:
  1_setup:
    - Open Safari
    - Create new window
    
  2_search:
    - Multiple search tabs
    - Various sources
    
  3_collect:
    - Copy information
    - Switch between tabs
    
  4_document:
    - Open Notes/Pages
    - Organize findings
    
  5_save:
    - Save document
    - Name appropriately
```

### Email Workflow
**Mode:** Interactive (default) or Workflow ($w)
```yaml
trigger: "send email about [topic]"
interactive_mode:
  - Guided recipient entry
  - Subject line assistance
  - Body composition help
  - Attachment guidance
  - Send confirmation

workflow_mode:
  - Automated multi-step
  - Batch operations
  - Template application
```

### Document Workflow
**Mode:** Interactive for composition, Workflow for automation
```yaml
trigger: "create [type] document"
interactive_approach:
  - Type selection help
  - Structure guidance
  - Content assistance
  - Formatting help
  
workflow_approach:
  - Template selection
  - Auto-population
  - Batch processing
```

---

## 6. 🪟 WINDOW MANAGEMENT

### Window Operations
**Mode:** Quick for simple, Interactive for complex arrangements
```yaml
arrange_windows:
  quick_mode:
    maximize: Click green button
    minimize: ⌘M
    close: ⌘W
    
  interactive_mode:
    guided_split_screen:
      - Help position first window
      - Guide second window
      - Confirm arrangement
```

---

## 7. 📋 FORM AUTOMATION

### Form Detection
**Mode:** Interactive (default for forms)
```yaml
identify_fields:
  interactive_guidance:
    - Scan all fields
    - Explain each type
    - Guide through filling
    - Validate entries
```

### Form Filling Strategy
```yaml
interactive_fill:
  1. Detect all fields
  2. Ask for information
  3. Fill systematically
  4. Review with user
  5. Submit with confirmation

quick_fill:
  1. Click first field
  2. Type content
  3. Tab navigation
  4. Submit
```

---

## 8. 🔍 SEARCH & FINDING PATTERNS

### Element Finding
**Mode:** Interactive (absorbed from Navigate mode)
```yaml
trigger: "find [element]", "where is [button]", "locate [menu]"
mode: Interactive
operation:
  find_element:
    - Refresh UI tree
    - Search by name/type
    - Check common locations
    - Present options
    - Guide to element
    
  common_locations:
    - Menu bar items
    - Toolbar buttons
    - Context menus
    - Preferences
    - Status bar
```

### Spotlight Search
**Mode:** Quick
```yaml
trigger: "search for [item]"
operation:
  - press_key_and_traverse("Space", ["Command"])
  - type_and_traverse("search query")
  - Arrow keys to select
  - Return to open
```

### In-App Search
**Mode:** Quick for simple, Interactive for complex
```yaml
trigger: "search for [text] in [app]"
quick_search:
  - ⌘F
  - Type search term
  - Enter
  
interactive_search:
  - Guide to search feature
  - Help with search syntax
  - Navigate results
  - Select best match
```

---

## 9. 📊 COMPOSITE WORKFLOWS

### Research & Document
**Mode:** Workflow
```yaml
trigger: "$w research and write about [topic]"
workflow:
  research_phase:
    - Browser automation
    - Tab management
    - Information gathering
    
  document_phase:
    - Document creation
    - Content organization
    - Formatting
    - Export
```

### Text Composition Workflows
**Mode:** Interactive (absorbed from Type mode)
```yaml
trigger: "help me write [document type]"
mode: Interactive
approach:
  guided_composition:
    - Determine purpose
    - Structure content
    - Assist with tone
    - Provide templates
    - Review and refine
    
  examples:
    - Business emails
    - Reports
    - Creative writing
    - Technical documentation
```

---

## 10. ⚡ QUICK OPERATIONS

### Top 20 Operations (Streamlined)

| Trigger | Operation | Mode | Time | Confidence |
|---------|-----------|------|------|------------|
| "open [app]" | open_application_and_traverse | Quick | 1s | 0.95 |
| "click [button]" | click_and_traverse | Quick | <1s | 0.95 |
| "$q type [text]" | type_and_traverse | Quick | Variable | 0.95 |
| "find [element]" | element search | Interactive | 3s | 0.85 |
| "write [content]" | guided composition | Interactive | Variable | 0.85 |
| "close window" | ⌘W | Quick | <1s | 0.95 |
| "new tab" | ⌘T | Quick | <1s | 0.95 |
| "save file" | ⌘S | Quick | 1s | 0.95 |
| "copy this" | ⌘C | Quick | <1s | 0.95 |
| "paste here" | ⌘V | Quick | <1s | 0.95 |
| "undo" | ⌘Z | Quick | <1s | 0.95 |
| "search [text]" | ⌘F → type | Quick | 2s | 0.90 |
| "quit app" | ⌘Q | Quick | 1s | 0.95 |
| "minimize" | ⌘M | Quick | <1s | 0.95 |
| "switch apps" | ⌘Tab | Quick | 1s | 0.95 |
| "spotlight" | ⌘Space | Quick | 1s | 0.95 |
| "screenshot" | ⌘⇧4 | Quick | 2s | 0.90 |
| "select all" | ⌘A | Quick | <1s | 0.95 |
| "refresh" | ⌘R | Quick | 1s | 0.95 |
| "help me [task]" | guided assistance | Interactive | Variable | 0.90 |

### Pattern Matching Priority

1. **Explicit mode command** → Use specified mode
2. **Exact app/element match** → Quick execution
3. **Known shortcut pattern** → Quick mode
4. **Element finding needed** → Interactive mode
5. **Text composition** → Interactive mode
6. **Multi-app workflow** → Workflow mode
7. **Ambiguous request** → Interactive mode (default)

### Performance Optimization by Mode

**Quick Mode:**
- Direct execution
- No questions
- Immediate action
- Simple operations

**Interactive Mode:**
- Element finding
- Text composition
- Guided assistance
- Complex operations
- Educational approach

**Workflow Mode:**
- Multi-app orchestration
- Batch operations
- Complex sequences
- Minimal interaction

---

*This pattern library enables instant understanding and execution of natural language requests for macOS automation using a streamlined 3-mode system. The consolidation of Navigate and Type functionality into Interactive mode simplifies the user experience while maintaining all capabilities.*