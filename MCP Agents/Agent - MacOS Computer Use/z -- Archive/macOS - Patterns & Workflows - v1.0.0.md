# macOS Computer Use - Patterns & Workflows - v1.0.0

Comprehensive pattern library for natural language to macOS UI operation mapping.

## Table of Contents
1. [🎯 INTENT RECOGNITION ENGINE](#1--intent-recognition-engine)
2. [📱 APPLICATION PATTERNS](#2--application-patterns)
3. [🖱️ INTERACTION PATTERNS](#3-️-interaction-patterns)
4. [⌨️ KEYBOARD PATTERNS](#4-️-keyboard-patterns)
5. [🔄 WORKFLOW PATTERNS](#5--workflow-patterns)
6. [🪟 WINDOW MANAGEMENT](#6--window-management)
7. [📋 FORM AUTOMATION](#7--form-automation)
8. [🔍 SEARCH PATTERNS](#8--search-patterns)
9. [📊 COMPOSITE WORKFLOWS](#9--composite-workflows)
10. [⚡ QUICK OPERATIONS](#10--quick-operations)

---

## 1. 🎯 INTENT RECOGNITION ENGINE

### Confidence Scoring
| Confidence | Range | Action | Example |
|------------|-------|--------|---------|
| **Exact** | >0.95 | Execute immediately | "click Safari" |
| **High** | 0.80-0.95 | Proceed with defaults | "open browser" |
| **Medium** | 0.50-0.79 | Confirm understanding | "do something online" |
| **Low** | <0.50 | Use interactive mode | "help with computer" |

### Pattern Matching Hierarchy
```
1. Exact Match → Direct operation execution
2. Application Recognition → Identify target app
3. Action Detection → Determine operation type
4. Element Inference → Find UI elements
5. Context Application → Use current state
```

---

## 2. 📱 APPLICATION PATTERNS

### Browser Operations
**Triggers:** `browse, search, web, internet, online, google, website`

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

**Implementation:**
```yaml
compose_email:
  - open_application_and_traverse("Mail")
  - press_key_and_traverse("N", modifiers: ["Command"])
  - Click "To" field
  - Type recipient
  - Tab to Subject
  - Type subject
  - Tab to body
  
check_email:
  - open_application_and_traverse("Mail")
  - Click Inbox
  - Review messages
  
reply_to_email:
  - Select message
  - press_key_and_traverse("R", modifiers: ["Command"])
```

### Document Creation
**Triggers:** `write, document, note, text, type, draft`

**Implementation:**
```yaml
create_document:
  apps:
    simple: "TextEdit", "Notes"
    rich: "Pages", "Microsoft Word"
  operations:
    - Open chosen app
    - Create new (⌘N)
    - Begin typing or wait
    
save_document:
  - press_key_and_traverse("S", modifiers: ["Command"])
  - Type filename
  - Choose location
  - Click Save
```

### System Settings
**Triggers:** `settings, preferences, configure, setup, system`

**Implementation:**
```yaml
open_settings:
  - open_application_and_traverse("System Settings")
  - Search for specific setting
  - Navigate to pane
  - Adjust as needed
  
common_settings:
  wifi: Network → Wi-Fi
  bluetooth: Bluetooth
  display: Displays
  sound: Sound
  privacy: Privacy & Security
```

### Calendar Operations
**Triggers:** `calendar, event, meeting, schedule, appointment`

**Implementation:**
```yaml
create_event:
  - open_application_and_traverse("Calendar")
  - press_key_and_traverse("N", modifiers: ["Command"])
  - Fill event details
  - Set date/time
  - Add invitees if needed
  
check_calendar:
  - open_application_and_traverse("Calendar")
  - Navigate to date
  - Review events
```

---

## 3. 🖱️ INTERACTION PATTERNS

### Click Patterns
| Trigger | Operation | Target |
|---------|-----------|--------|
| "click [element]" | click_and_traverse | Named element |
| "press [button]" | click_and_traverse | Button by label |
| "select [option]" | click_and_traverse | Menu/dropdown item |
| "choose [item]" | click_and_traverse | List selection |
| "tap [element]" | click_and_traverse | Touch-style interaction |
| "hit [button]" | click_and_traverse | Button press |

### Type Patterns
| Trigger | Operation | Behavior |
|---------|-----------|----------|
| "type [text]" | type_and_traverse | Direct input |
| "write [text]" | type_and_traverse | Paragraph input |
| "enter [text]" | type_and_traverse | Field input |
| "fill [field] with [text]" | Click field → type | Form filling |
| "input [text]" | type_and_traverse | General input |
| "paste [text]" | ⌘V after positioning | Paste operation |

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

### Drag Operations
```yaml
drag_file:
  - Click and hold file
  - Move to destination
  - Release
  
drag_to_trash:
  - Select item(s)
  - Drag to Trash in Dock
  
drag_window:
  - Click title bar
  - Drag to new position
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
  find_replace: ⌘⇧F
  
text_formatting:
  bold: ⌘B
  italic: ⌘I
  underline: ⌘U
  
navigation:
  spotlight: ⌘Space
  app_switch: ⌘Tab
  window_switch: ⌘`
  mission_control: F3 or Control+↑
  show_desktop: F11
  launchpad: F4
```

### Browser Shortcuts
```yaml
tabs:
  new_tab: ⌘T
  close_tab: ⌘W
  reopen_tab: ⌘⇧T
  next_tab: ⌘⇧] or Control+Tab
  prev_tab: ⌘⇧[ or Control+⇧Tab
  tab_1_through_9: ⌘1 through ⌘9
  
navigation:
  address_bar: ⌘L
  back: ⌘[ or ⌘←
  forward: ⌘] or ⌘→
  refresh: ⌘R
  hard_refresh: ⌘⇧R
  home: ⌘⇧H
  
bookmarks:
  bookmark_page: ⌘D
  bookmark_manager: ⌘⌥B
  bookmark_bar: ⌘⇧B
  
view:
  zoom_in: ⌘+
  zoom_out: ⌘-
  actual_size: ⌘0
  full_screen: ⌘⌃F
  reader_mode: ⌘⇧R
  developer_tools: ⌘⌥I
```

### Finder Shortcuts
```yaml
files_folders:
  new_folder: ⌘⇧N
  new_window: ⌘N
  duplicate: ⌘D
  get_info: ⌘I
  quick_look: Space
  rename: Return (when selected)
  move_to_trash: ⌘Delete
  empty_trash: ⌘⇧Delete
  
navigation:
  parent_folder: ⌘↑
  open_folder: ⌘↓
  back: ⌘[
  forward: ⌘]
  go_to_folder: ⌘⇧G
  
locations:
  home: ⌘⇧H
  desktop: ⌘⇧D
  documents: ⌘⇧O
  downloads: ⌘⌥L
  applications: ⌘⇧A
  utilities: ⌘⇧U
  
views:
  as_icons: ⌘1
  as_list: ⌘2
  as_columns: ⌘3
  as_gallery: ⌘4
```

---

## 5. 🔄 WORKFLOW PATTERNS

### Research Workflow
```yaml
trigger: "research [topic]"
steps:
  1_setup:
    - Open Safari
    - Create new window (⌘N)
    
  2_search:
    - Tab 1: Google search for topic
    - Tab 2: Wikipedia article
    - Tab 3: News search
    - Tab 4: Academic sources
    
  3_collect:
    - Copy relevant information
    - Switch between tabs (⌘⇧])
    
  4_document:
    - Open Notes/Pages
    - Create new document
    - Paste and organize findings
    
  5_save:
    - Save document (⌘S)
    - Name appropriately
```

### Email Workflow
```yaml
trigger: "send email about [topic]"
steps:
  1_prepare:
    - Gather necessary files
    - Copy relevant text
    
  2_compose:
    - Open Mail (or browser)
    - New message (⌘N)
    - Fill recipient field
    - Add subject line
    
  3_content:
    - Type or paste content
    - Format as needed (⌘B, ⌘I)
    
  4_attach:
    - Drag files or use ⌘⇧A
    - Verify attachments
    
  5_send:
    - Review email
    - Send (⌘⇧D)
```

### Document Workflow
```yaml
trigger: "create [type] document"
steps:
  1_launch:
    - Open appropriate app
    - Choose template if available
    
  2_structure:
    - Add title
    - Create outline
    - Set up sections
    
  3_content:
    - Fill in each section
    - Add formatting
    - Insert images/charts
    
  4_review:
    - Spell check (⌘;)
    - Preview if available
    
  5_finalize:
    - Save (⌘S)
    - Export if needed
    - Share or print
```

### Meeting Preparation
```yaml
trigger: "prepare for meeting"
steps:
  1_calendar:
    - Open Calendar
    - Find meeting details
    - Note attendees and time
    
  2_documents:
    - Open relevant files
    - Create agenda if needed
    - Prepare presentation
    
  3_communication:
    - Check recent emails
    - Review previous notes
    
  4_setup:
    - Open video app (Zoom/Teams)
    - Test audio/video
    - Share screen if needed
```

---

## 6. 🪟 WINDOW MANAGEMENT

### Window Operations
```yaml
arrange_windows:
  split_screen:
    left_half:
      - Hold window title bar
      - Drag to left edge
      - Release when highlighted
    right_half:
      - Hold window title bar
      - Drag to right edge
      - Release when highlighted
  
  maximize:
    method1: Click green button
    method2: Double-click title bar
    method3: ⌥+Click green button (old maximize)
  
  minimize:
    method1: Click yellow button
    method2: ⌘M
  
  close:
    method1: Click red button
    method2: ⌘W
    
  full_screen:
    enter: ⌘⌃F or green button
    exit: ⌘⌃F or Esc
```

### Mission Control
```yaml
mission_control:
  activate:
    - F3 or Control+↑
    - Three-finger swipe up (trackpad)
    
  operations:
    create_space: Click + in top right
    delete_space: Hover and click X
    move_window: Drag to different space
    switch_space: Click on space
    
  navigation:
    next_space: Control+→
    previous_space: Control+←
    specific_space: Control+[1-9]
```

### App Exposé
```yaml
app_expose:
  activate:
    - F10 or Control+↓
    - Three-finger swipe down
    
  usage:
    - Shows all windows of current app
    - Click to select window
    - Esc to cancel
```

---

## 7. 📋 FORM AUTOMATION

### Form Detection
```yaml
identify_fields:
  text_fields:
    - Look for input boxes
    - Check labels
    - Identify placeholders
    
  dropdowns:
    - Find select elements
    - Check for arrows
    - Look for option lists
    
  checkboxes:
    - Square boxes
    - Toggle elements
    
  radio_buttons:
    - Circular options
    - Single selection groups
    
  buttons:
    - Submit/Save/Continue
    - Cancel/Back
    - Action buttons
```

### Form Filling Strategy
```yaml
sequential_fill:
  1. Click first field
  2. Type content
  3. Tab to next field
  4. Repeat until complete
  5. Submit form

smart_fill:
  1. Detect all fields
  2. Plan fill order
  3. Use Tab navigation
  4. Handle dropdowns with arrows/space
  5. Check required fields
  6. Validate before submit

error_handling:
  - Check for validation messages
  - Correct invalid fields
  - Retry submission
```

### Common Form Patterns
```yaml
login_form:
  - Username/Email field
  - Password field
  - Remember me checkbox (optional)
  - Submit button
  
registration_form:
  - Personal info section
  - Account details
  - Password and confirmation
  - Terms acceptance
  - Submit
  
contact_form:
  - Name fields
  - Email
  - Subject/Category
  - Message textarea
  - Send button
```

---

## 8. 🔍 SEARCH PATTERNS

### Spotlight Search
```yaml
trigger: "find [item]", "search for [item]", "locate [item]"
operation:
  basic:
    - press_key_and_traverse("Space", ["Command"])
    - type_and_traverse("search query")
    - Arrow keys to select
    - Return to open
    
  advanced:
    - Add kind: filters (kind:pdf, kind:image)
    - Add date: filters (date:today, date:yesterday)
    - Add author: filters
    - Use boolean operators (AND, OR, NOT)
```

### In-App Search
```yaml
trigger: "search for [text] in [app]", "find [text]"
operation:
  standard_search:
    - Focus app
    - press_key_and_traverse("F", ["Command"])
    - type_and_traverse("search text")
    - Use ⌘G for next match
    - Use ⌘⇧G for previous match
    
  replace:
    - press_key_and_traverse("F", ["Command", "Option"])
    - Type find text
    - Tab to replace field
    - Type replacement
    - Replace or Replace All
```

### File Search
```yaml
trigger: "find file named [name]", "where is [file]"
operation:
  finder_search:
    - Open Finder
    - press_key_and_traverse("F", ["Command", "Option"])
    - Type filename
    - Add filters if needed
    - Review results
    
  smart_folder:
    - Create saved search
    - Set criteria
    - Save for reuse
```

---

## 9. 📊 COMPOSITE WORKFLOWS

### Research & Document
```yaml
trigger: "research and write about [topic]"
workflow:
  research_phase:
    1_setup:
      - Open Safari
      - Create tab group
      
    2_search:
      - Google search
      - Wikipedia
      - Academic sources
      - News articles
      
    3_collect:
      - Copy key points
      - Save important URLs
      - Screenshot if needed
  
  document_phase:
    1_create:
      - Open Pages/Word
      - Choose template
      
    2_structure:
      - Title page
      - Table of contents
      - Sections
      
    3_content:
      - Paste research
      - Write analysis
      - Add citations
      
    4_format:
      - Apply styles
      - Add images
      - Final formatting
      
    5_export:
      - Save document
      - Export as PDF
      - Share if needed
```

### Email with Attachments
```yaml
trigger: "email report with files"
workflow:
  prepare_files:
    - Open Finder
    - Navigate to files
    - Select multiple (⌘+Click)
    - Verify selection
  
  compose_email:
    - Open Mail
    - New message (⌘N)
    - Add recipients
    - Write subject
    - Compose body
    
  attach_files:
    method1: Drag files to email
    method2: Click attach (⌘⇧A)
    
  finalize:
    - Review attachments
    - Check recipients
    - Send (⌘⇧D)
```

### Presentation Creation
```yaml
trigger: "create presentation from outline"
workflow:
  setup:
    - Open Keynote/PowerPoint
    - Choose template
    - Set theme
    
  structure:
    - Title slide
    - Agenda/Contents
    - Section dividers
    - Content slides
    - Conclusion
    
  content:
    - Add text
    - Insert images
    - Create charts
    - Add animations
    
  review:
    - Run through slides
    - Check transitions
    - Verify timing
    
  export:
    - Save presentation
    - Export as PDF
    - Share link
```

### Data Processing
```yaml
trigger: "process spreadsheet data"
workflow:
  import:
    - Open Numbers/Excel
    - Import CSV/data file
    - Verify import
    
  clean:
    - Remove duplicates
    - Fix formatting
    - Handle missing data
    
  analyze:
    - Create formulas
    - Generate charts
    - Add pivot tables
    
  report:
    - Create summary
    - Export results
    - Share findings
```

---

## 10. ⚡ QUICK OPERATIONS

### Top 25 Operations

| Trigger | Operation | Time | Confidence |
|---------|-----------|------|------------|
| "open [app]" | open_application_and_traverse | 1s | 0.95 |
| "click [button]" | click_and_traverse | <1s | 0.95 |
| "type [text]" | type_and_traverse | Variable | 0.95 |
| "close window" | ⌘W | <1s | 0.95 |
| "new tab" | ⌘T | <1s | 0.95 |
| "save file" | ⌘S | 1s | 0.95 |
| "copy this" | ⌘C | <1s | 0.95 |
| "paste here" | ⌘V | <1s | 0.95 |
| "undo" | ⌘Z | <1s | 0.95 |
| "search [text]" | ⌘F → type | 2s | 0.90 |
| "quit app" | ⌘Q | 1s | 0.95 |
| "minimize" | ⌘M | <1s | 0.95 |
| "switch apps" | ⌘Tab | 1s | 0.95 |
| "spotlight" | ⌘Space | 1s | 0.95 |
| "screenshot" | ⌘⇧4 | 2s | 0.90 |
| "select all" | ⌘A | <1s | 0.95 |
| "refresh" | ⌘R | 1s | 0.95 |
| "back" | ⌘[ | <1s | 0.90 |
| "forward" | ⌘] | <1s | 0.90 |
| "zoom in" | ⌘+ | <1s | 0.95 |
| "zoom out" | ⌘- | <1s | 0.95 |
| "print" | ⌘P | 2s | 0.90 |
| "preferences" | ⌘, | 1s | 0.95 |
| "help" | ⌘? | 1s | 0.90 |
| "force quit" | ⌘⌥Esc | 2s | 0.90 |

### Pattern Matching Priority

1. **Exact app/element match** → Direct execution
2. **Known shortcut pattern** → Use keyboard
3. **Standard UI element** → Click operation
4. **Complex interaction** → Multi-step workflow
5. **Ambiguous request** → Interactive mode

### Performance Optimization

- **Prefer shortcuts** over clicking when available
- **Cache element positions** for repeated operations
- **Batch similar operations** together
- **Minimize traversals** by using smart targeting
- **Use native features** like Tab navigation

---

*This pattern library enables instant understanding and execution of natural language requests for macOS automation. By mapping triggers to UI operations efficiently, the assistant provides professional automation in seconds.*