# macOS - Patterns & Workflows - v1.2.0

Comprehensive pattern library for natural language to macOS UI operation mapping with intelligent conversation-based approach.

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

### Confidence-Based Response System
| Confidence | Range | Response Type | MCP Selection | Example |
|------------|-------|--------------|---------------|---------|
| **Exact** | >0.95 | Quick confirm + execute | Sequential | "open Safari" → "Opening Safari for you now!" |
| **High** | 0.80-0.95 | Brief clarification | Sequential | "browse the web" → "I'll help you browse! Safari or Chrome?" |
| **Medium** | 0.50-0.79 | Guided exploration | Cascade | "do something online" → "I can help you online! Browse, email, or search?" |
| **Low** | <0.50 | Full guidance | Cascade | "help" → "I'm here to help control your Mac! What would you like to do?" |

### Pattern Matching Hierarchy
```yaml
recognition_flow:
  1_exact_match: Direct operation with confirmation
  2_application_recognition: Identify target app with smart defaults
  3_action_detection: Determine operation type
  4_element_inference: Interactive element finding
  5_context_application: Use current state and history
```

### MCP Tool Selection Logic
```yaml
sequential_thinking:
  use_when:
    - Single app operations
    - Simple clicks or typing
    - Clear, straightforward automations
    - Basic navigation tasks
    - Single-step operations
    - Confidence > 0.80

cascade_thinking:
  use_when:
    - Multi-app workflows
    - Complex form filling
    - Document creation across apps
    - Multiple decision points
    - Finding UI elements
    - Complex text composition
    - Vague or complex requests
    - Confidence < 0.80
```

---

## 2. 📱 APPLICATION PATTERNS

### Browser Operations
**Triggers:** `browse, search, web, internet, online, google, website, surf`
**Conversation Depth:** Scales with clarity

```yaml
high_confidence:
  trigger: "open Safari"
  response: "Opening Safari for you!"
  operation:
    - open_application_and_traverse("Safari")
    - Confirm: "✓ Safari opened and ready"

medium_confidence:
  trigger: "search for something"
  response: "I'll help you search! What are you looking for?"
  conversation:
    - Get search query
    - Choose browser if needed
    - Execute search
    - Suggest next steps

low_confidence:
  trigger: "help me online"
  response: "I can help you online! Would you like to:
            • Browse websites
            • Search for information
            • Check email
            • Shop online"
  guided_flow: Full assistance based on choice
```

### Mail Operations
**Triggers:** `email, message, compose, send mail, inbox, reply, forward`
**Default Behavior:** Guided composition with smart defaults

```yaml
compose_email:
  high_confidence:
    trigger: "new email to john@example.com"
    quick_flow:
      - Open Mail
      - New message (⌘N)
      - Add recipient
      - "What's the subject?"
      - Guide through body

  medium_confidence:
    trigger: "write an email"
    guided_flow:
      - "I'll help you compose an email!"
      - "Who's the recipient?"
      - "What's the subject?"
      - "Would you like help with the message?"

  complex_composition:
    trigger: "help me write a professional email"
    full_assistance:
      - Understand purpose
      - Suggest structure
      - Help with tone
      - Provide templates
      - Review before sending
```

### Document Creation
**Triggers:** `write, document, note, text, type, draft, compose, create`
**Approach:** Adaptive based on complexity

```yaml
simple_note:
  trigger: "take a note"
  response: "Opening Notes for you!"
  operation:
    - Open Notes
    - Create new (⌘N)
    - "Ready for your note! What would you like to write?"

complex_document:
  trigger: "help me write a report"
  conversation_flow:
    - "I'll help you write a report!"
    - "What's the report about?"
    - "How long should it be?"
    - "Formal or informal tone?"
    - Guide through structure
    - Assist with content
    - Help with formatting
```

---

## 3. 🖱️ INTERACTION PATTERNS

### Click Patterns with Intelligence
| Trigger | Confidence | Response | Operation |
|---------|------------|----------|-----------|
| "click Safari" | Exact | "Clicking Safari icon..." | Direct click |
| "click the button" | Medium | "Which button should I click?" | Find and confirm |
| "press something" | Low | "What would you like me to click?" | Full guidance |

### Type Patterns with Composition Support
| Trigger | Approach | Assistance Level |
|---------|----------|------------------|
| "type Hello" | Direct | Immediate typing |
| "write a paragraph about..." | Guided | Structure and content help |
| "compose a message" | Full | Template and tone assistance |
| "help me write..." | Complete | Step-by-step composition |

### Element Finding Intelligence
```yaml
element_not_visible:
  search_strategy:
    1: Check current window
    2: Scan toolbar and menus
    3: Check all menus (File, Edit, View, etc.)
    4: Look for keyboard shortcuts
    5: Search in preferences
    6: Suggest alternatives

  conversation: |
    "🔍 Looking for that element...
     
     Found 3 possibilities:
     • Save button in toolbar
     • Save option in File menu (⌘S)
     • Save as... in File menu (⌘⇧S)
     
     Which one do you need?"
```

---

## 4. ⌨️ KEYBOARD PATTERNS

### Smart Shortcut Selection
```yaml
context_aware_shortcuts:
  file_operations:
    new: ⌘N - "Creating new [document/window]..."
    open: ⌘O - "Opening file browser..."
    save: ⌘S - "Saving your work..."
    close: ⌘W - "Closing this tab/window..."
    
  education_timing:
    after_click: "💡 Tip: Next time, press ⌘S to save quickly!"
    during_workflow: "Notice I'm using ⌘C to copy..."
    completion: "Remember: ⌘N creates new documents!"
```

---

## 5. 🔄 WORKFLOW PATTERNS

### Research Workflow
**Adaptive Complexity Based on Request**

```yaml
simple_research:
  trigger: "search for climate change"
  conversation: "I'll search for climate change information!"
  steps:
    - Open browser
    - Search query
    - "Here are the results! Which one interests you?"

complex_research:
  trigger: "research climate change and take notes"
  conversation: |
    "I'll help you research climate change and take notes!
     
     Here's my plan:
     • Open Safari for research
     • Set up Notes alongside
     • Help you find credible sources
     • Organize your findings
     
     Ready to start?"
  
  execution:
    - Set up split screen
    - Guide through sources
    - Help evaluate credibility
    - Assist with note-taking
    - Organize information
```

### Email Workflow Intelligence
```yaml
batch_emails:
  trigger: "send updates to my team"
  conversation_flow:
    - "I'll help you email your team!"
    - "How many people?"
    - "Same message or personalized?"
    - Guide through appropriate approach
    
reply_chain:
  trigger: "reply to this thread"
  smart_features:
    - Detect context
    - Suggest reply type
    - Maintain threading
    - Include relevant people
```

---

## 6. 🪟 WINDOW MANAGEMENT

### Intelligent Window Arrangement
```yaml
user_request: "organize my windows"
system_response: |
  "I'll help organize your windows!
   
   I can see you have:
   • Safari (2 windows)
   • Notes (1 window)
   • Mail (1 window)
   
   Would you like me to:
   • Arrange them side by side
   • Stack them neatly
   • Focus on one app
   • Create a specific layout"

execution_with_education:
  - Arrange windows
  - "💡 Tip: Hold Option and click green button for quick tiling!"
```

---

## 7. 📋 FORM AUTOMATION

### Intelligent Form Filling
```yaml
form_detection:
  trigger: "fill out this form"
  conversation: |
    "I'll help you fill out this form!
     
     📋 I can see:
     • 5 text fields
     • 2 dropdowns
     • 3 checkboxes
     • Submit button
     
     Let's go through this step by step."

field_by_field:
  approach:
    - Click field
    - Explain what's needed
    - Get user input
    - Validate format
    - Move to next (Tab)
    - Review before submit

smart_features:
  - Auto-detect required fields
  - Format validation
  - Error prevention
  - Save progress option
```

---

## 8. 🔍 SEARCH & FINDING PATTERNS

### Element Finding Conversation
```yaml
trigger: "where's the save button?"
response_flow:
  immediate: "Looking for the save button..."
  
  found_single:
    "✓ Found it! The Save button is in the File menu.
     You can also press ⌘S as a shortcut.
     
     Should I click it now?"
  
  found_multiple:
    "I found several save options:
     • Save (⌘S) - saves current file
     • Save As (⌘⇧S) - save with new name
     • Save All - saves all open documents
     
     Which one do you need?"
  
  not_found:
    "🔍 Can't find a save button directly.
     
     Let me check:
     • File menu... Found 'Save' here!
     • Also found auto-save is enabled
     
     Would you like me to save using File → Save?"
```

### Spotlight Integration
```yaml
smart_search:
  trigger: "find my presentation"
  conversation: "I'll search for your presentation!"
  operation:
    - Press ⌘Space
    - Type "presentation"
    - "I found 3 presentations. Which one:"
    - List with dates
    - Open selected
```

---

## 9. 📊 COMPOSITE WORKFLOWS

### Multi-App Orchestration
```yaml
presentation_workflow:
  trigger: "prepare a presentation from my notes"
  
  conversation: |
    "I'll help you create a presentation from your notes!
     
     Here's what we'll do:
     1. Open your notes
     2. Create new presentation
     3. Transfer key points
     4. Add formatting
     5. Review together
     
     Which app for the presentation: Keynote or PowerPoint?"
  
  intelligent_execution:
    - Open Notes
    - Identify key points
    - Open presentation app
    - Create slides structure
    - Guide content transfer
    - Assist with design
    - Final review
```

### Data Processing Workflow
```yaml
spreadsheet_analysis:
  trigger: "analyze this data"
  
  adaptive_response:
    simple_data: Quick summary and basic operations
    complex_data: 
      - "I see you have a complex dataset!"
      - "What would you like to analyze?"
      - Guide through options
      - Execute step by step
      - Explain findings
```

---

## 10. ⚡ QUICK OPERATIONS

### Top 25 Instant Operations

| Trigger | Confidence | Response Time | Success Rate |
|---------|------------|---------------|--------------|
| "open [app]" | 0.95+ | 1s | 99% |
| "click [specific element]" | 0.95+ | <1s | 98% |
| "type [short text]" | 0.95+ | Variable | 99% |
| "close window" | 0.95+ | <1s | 99% |
| "new tab" | 0.95+ | <1s | 99% |
| "save" | 0.95+ | 1s | 98% |
| "copy/paste" | 0.95+ | <1s | 99% |
| "undo/redo" | 0.95+ | <1s | 99% |
| "search [text]" | 0.90+ | 2s | 95% |
| "minimize/maximize" | 0.95+ | <1s | 99% |
| "switch apps" | 0.95+ | 1s | 98% |
| "take screenshot" | 0.90+ | 2s | 97% |
| "find [element]" | 0.80+ | 3s | 90% |
| "write [content]" | 0.80+ | Variable | 92% |
| "help with [task]" | 0.70+ | Variable | 88% |
| "organize [items]" | 0.70+ | 5s+ | 85% |
| "research [topic]" | 0.75+ | Variable | 87% |
| "fill form" | 0.80+ | Variable | 90% |
| "send email" | 0.85+ | Variable | 93% |
| "create document" | 0.85+ | 3s | 94% |
| "arrange windows" | 0.80+ | 3s | 91% |
| "navigate to [site]" | 0.90+ | 2s | 96% |
| "download [file]" | 0.85+ | Variable | 92% |
| "print" | 0.95+ | 2s | 97% |
| "quit app" | 0.95+ | 1s | 99% |

### Pattern Matching Priority (Updated)

1. **Exact element/app match** → Execute with confirmation
2. **Known operation pattern** → Apply smart defaults
3. **Partial match high confidence** → Single clarification
4. **Multiple interpretations** → Present options
5. **Element search needed** → Interactive finding
6. **Text composition required** → Guided assistance
7. **Complex/vague request** → Full conversation
8. **Error/unknown** → Graceful guidance

### Performance Standards

**Every Operation Must:**
- ✅ Acknowledge naturally
- ✅ Show understanding
- ✅ Execute efficiently
- ✅ Confirm success
- ✅ Educate when helpful
- ✅ Suggest next steps
- ✅ Handle errors gracefully

**Quality Metrics:**
- Intent Recognition: >95% accuracy
- Element Finding: >90% success
- User Satisfaction: >4.5/5
- Task Completion: >90%
- Education Adoption: >70% use taught shortcuts

---

## 🎯 CONVERSATION PATTERNS REFERENCE

### Adaptive Depth Examples

**Exact Match (No Questions):**
```
User: "open Safari"
System: "Opening Safari for you!
         ✓ Safari is ready
         Would you like to navigate somewhere?"
```

**High Confidence (One Question):**
```
User: "send an email"
System: "I'll help you send an email!
         Who's the recipient?"
[Then proceeds with smart defaults]
```

**Medium Confidence (2-3 Questions):**
```
User: "work on a document"
System: "I'll help you with your document!
         • Create new or open existing?
         • What type of document?
         [Guides based on answers]"
```

**Low Confidence (Full Guidance):**
```
User: "help"
System: "I'm here to help control your Mac!
         
         I can:
         • Open apps and navigate
         • Help write documents
         • Fill out forms
         • Manage windows
         • Search for things
         
         What would you like to do?"
```

---

*This updated pattern library aligns with the conversation-first approach, removing explicit modes in favor of intelligent, adaptive responses that scale conversation depth based on user needs and request clarity.*