# macOS Computer Use - Application Intelligence - v1.0.0

App-specific best practices, shortcuts, and automation patterns for macOS applications.

## Table of Contents
1. [🌐 SAFARI](#1--safari)
2. [📧 MAIL](#2--mail)
3. [📝 NOTES & TEXTEDIT](#3--notes--textedit)
4. [🔍 FINDER](#4--finder)
5. [⚙️ SYSTEM SETTINGS](#5-️-system-settings)
6. [📅 CALENDAR](#6--calendar)
7. [💬 MESSAGES](#7--messages)
8. [🎵 MUSIC](#8--music)
9. [📸 PHOTOS](#9--photos)
10. [🛠️ TERMINAL](#10-️-terminal)
11. [📊 NUMBERS & EXCEL](#11--numbers--excel)
12. [🎨 PAGES & WORD](#12--pages--word)
13. [🎬 KEYNOTE & POWERPOINT](#13--keynote--powerpoint)
14. [💼 PRODUCTIVITY APPS](#14--productivity-apps)
15. [🌍 CHROME & FIREFOX](#15--chrome--firefox)

---

## 1. 🌐 SAFARI

### Key Elements
```yaml
ui_structure:
  toolbar:
    - Back/Forward buttons (x: 50-150, y: 50)
    - Address bar (center, y: 50)
    - Share button (right side)
    - Downloads (right side)
    - Extensions (right side)
    - Sidebar toggle (left)
  
  tabs:
    - Tab bar (y: 85)
    - Tab groups menu
    - Private browsing indicator
    - Add tab button (+)
  
  content:
    - Web page (main area)
    - Reader mode button (in address bar)
    - Developer tools (bottom when open)
    
  sidebar:
    - Bookmarks
    - Reading List
    - History
    - Tab Groups
```

### Common Operations
```yaml
navigation:
  new_tab: ⌘T
  close_tab: ⌘W
  reopen_closed_tab: ⌘⇧T
  next_tab: ⌘⇧] or Control+Tab
  previous_tab: ⌘⇧[ or Control+⇧Tab
  specific_tab: ⌘[1-9]
  address_bar: ⌘L

browsing:
  back: ⌘[ or ⌘←
  forward: ⌘] or ⌘→
  refresh: ⌘R
  hard_refresh: ⌘⇧R
  stop_loading: ⌘. or Esc
  home_page: ⌘⇧H

bookmarks:
  add_bookmark: ⌘D
  bookmark_manager: ⌘⌥B
  bookmark_bar_toggle: ⌘⇧B
  add_to_reading_list: ⌘⇧D

view:
  zoom_in: ⌘+
  zoom_out: ⌘-
  actual_size: ⌘0
  reader_mode: ⌘⇧R
  full_screen: ⌘⌃F
  show_all_tabs: ⌘⇧\
  
developer:
  web_inspector: ⌘⌥I
  javascript_console: ⌘⌥C
  page_source: ⌘⌥U
```

### Automation Patterns
```yaml
web_research:
  steps:
    1. Open new window (⌘N)
    2. Create tab group for topic
    3. Open multiple search tabs
    4. Use Reader for articles (⌘⇧R)
    5. Add to Reading List (⌘⇧D)
    
  tips:
    - Hold ⌘ while clicking links to open in new tabs
    - Use ⌘K for quick website search
    - Pin important tabs (right-click → Pin Tab)

form_filling:
  navigation:
    - Tab: Next field
    - Shift+Tab: Previous field
    - Space: Toggle checkbox
    - Arrow keys: Select from dropdown
    - Return: Submit form
    
  autofill:
    - Safari suggests from Contacts
    - Passwords from iCloud Keychain
    - Credit cards saved securely

downloads:
  location: ~/Downloads/ by default
  shortcuts:
    - ⌘⌥L: Show downloads
    - Click to open file
    - Magnifying glass: Reveal in Finder
```

---

## 2. 📧 MAIL

### Key Elements
```yaml
ui_structure:
  sidebar:
    - Mailboxes section
      - Inbox
      - Sent
      - Drafts
      - Archive
      - Junk
      - Trash
    - Smart Mailboxes
    - Custom folders
  
  message_list:
    - From/Subject preview
    - Date/Time
    - Attachment indicator
    - Flag status
    - Read/Unread indicator
  
  message_view:
    - Headers (From, To, Subject)
    - Message body
    - Attachments area
    - Reply/Forward buttons
  
  compose_window:
    - To/Cc/Bcc fields
    - Subject line
    - Message body
    - Format bar
    - Attachment button
```

### Common Operations
```yaml
messages:
  new_message: ⌘N
  reply: ⌘R
  reply_all: ⌘⇧R
  forward: ⌘⇧F
  send: ⌘⇧D
  save_draft: ⌘S

organization:
  delete: Delete or Backspace
  archive: ⌘⌃A
  move_to_junk: ⌘⇧J
  flag_message: ⌘⇧L
  mark_as_read: ⌘⇧U
  mark_as_unread: ⌘⇧U (toggle)

navigation:
  next_message: ↓ or ]
  previous_message: ↑ or [
  next_unread: ⌘]
  previous_unread: ⌘[
  mailbox_list: ⌘⇧M
  search: ⌘⌥F

attachments:
  add_attachment: ⌘⇧A
  save_attachments: ⌘⇧S
  quick_look: Select + Space
  save_all: ⌘⌥⇧S
```

### Automation Patterns
```yaml
email_workflow:
  compose:
    1. New message (⌘N)
    2. Type recipient (auto-completes)
    3. Tab to subject
    4. Tab to body
    5. Format with ⌘B, ⌘I, ⌘U
    6. Attach files (drag or ⌘⇧A)
    7. Send (⌘⇧D)
    
  triage:
    1. Select message
    2. Quick actions:
       - Delete: Delete key
       - Archive: ⌘⌃A
       - Flag: ⌘⇧L
       - Reply: ⌘R
    3. Next message: ↓

  smart_mailboxes:
    - Create rules for automatic sorting
    - VIP senders for priority
    - Unread filter for focus
```

---

## 3. 📝 NOTES & TEXTEDIT

### Notes
```yaml
ui_structure:
  sidebar:
    - Folders list
    - All iCloud
    - Recently Deleted
    - Tags
  
  note_list:
    - Note previews
    - Date modified
    - First line preview
  
  editor:
    - Title area
    - Body text
    - Format bar
    - Attachments

operations:
  notes:
    new_note: ⌘N
    new_folder: ⌘⇧N
    delete_note: ⌘Delete
    search_notes: ⌘F
    pin_note: Click pin icon
  
  formatting:
    title: ⌘⇧T
    heading: ⌘⇧H
    body: ⌘⇧B
    bold: ⌘B
    italic: ⌘I
    underline: ⌘U
    
  lists:
    checklist: ⌘⇧L
    bulleted_list: ⌘⇧7
    numbered_list: ⌘⇧8
    
  organization:
    add_table: ⌘⌥T
    add_link: ⌘K
    attach_file: Click paperclip
    scan_document: Click camera icon
```

### TextEdit
```yaml
ui_structure:
  window:
    - Text area (main)
    - Format bar (top)
    - Ruler (optional)
    - Status bar (bottom)

operations:
  file:
    new: ⌘N
    open: ⌘O
    save: ⌘S
    save_as: ⌘⇧S
    duplicate: ⌘⇧S
    
  format:
    plain_text: ⌘⇧T
    rich_text: ⌘⇧R
    show_fonts: ⌘T
    show_colors: ⌘⇧C
    
  text_formatting:
    bold: ⌘B
    italic: ⌘I
    underline: ⌘U
    bigger: ⌘+
    smaller: ⌘-
    
  paragraph:
    align_left: ⌘{
    align_center: ⌘|
    align_right: ⌘}
    justify: ⌘⌥|
```

---

## 4. 🔍 FINDER

### Key Elements
```yaml
ui_structure:
  sidebar:
    favorites:
      - AirDrop
      - Recents
      - Applications
      - Desktop
      - Documents
      - Downloads
    icloud:
      - iCloud Drive
      - Shared
    locations:
      - Computer
      - Network
    tags:
      - Colored tags
      - Custom tags
  
  toolbar:
    - Back/Forward
    - View buttons
    - Arrange menu
    - Action menu
    - Search field
    - Share button
  
  main_area:
    - File/folder display
    - Path bar (bottom)
    - Status bar (bottom)
```

### Common Operations
```yaml
files_folders:
  new_folder: ⌘⇧N
  new_window: ⌘N
  new_tab: ⌘T
  duplicate: ⌘D
  make_alias: ⌘⌃A
  move_to_trash: ⌘Delete
  empty_trash: ⌘⇧Delete
  get_info: ⌘I
  quick_look: Space
  rename: Return (when selected)

navigation:
  go_to_folder: ⌘⇧G
  parent_folder: ⌘↑
  open_folder: ⌘↓
  back: ⌘[
  forward: ⌘]
  enclosing_folder: ⌘↑

view_options:
  as_icons: ⌘1
  as_list: ⌘2
  as_columns: ⌘3
  as_gallery: ⌘4
  show_path_bar: ⌘⌥P
  show_status_bar: ⌘/
  show_sidebar: ⌘⌥S
  show_preview: ⌘⇧P

locations:
  home: ⌘⇧H
  desktop: ⌘⇧D
  documents: ⌘⇧O
  downloads: ⌘⌥L
  applications: ⌘⇧A
  utilities: ⌘⇧U
  recent: ⌘⇧F
  computer: ⌘⇧C
  network: ⌘⇧K
  
search:
  find: ⌘F
  find_by_name: ⌘⇧F
  search_window: ⌘⌥F
```

### Automation Patterns
```yaml
file_management:
  organize_downloads:
    1. Go to Downloads (⌘⌥L)
    2. Sort by kind (View menu)
    3. Select similar files
    4. Create folder (⌘⇧N)
    5. Move files into folder
    
  batch_rename:
    1. Select multiple files
    2. Right-click → Rename
    3. Choose format/pattern
    4. Apply to all
    
  quick_actions:
    - Space: Preview without opening
    - ⌘I: Check file size/info
    - ⌘D: Duplicate before editing
    - ⌘⌥Y: Full-screen slideshow

smart_folders:
  create:
    1. File → New Smart Folder
    2. Set search criteria
    3. Save for reuse
  
  useful_criteria:
    - Kind: Image/PDF/Document
    - Date: Created/Modified
    - Size: Greater than
    - Tags: Specific colors
```

---

## 5. ⚙️ SYSTEM SETTINGS

### Navigation Structure
```yaml
main_categories:
  appearance:
    - General
    - Appearance
    - Accessibility
    - Control Center
    - Siri & Spotlight
    - Privacy & Security
    
  hardware:
    - Displays
    - Sound
    - Keyboard
    - Mouse/Trackpad
    - Printers & Scanners
    
  network:
    - Wi-Fi
    - Bluetooth
    - Network
    - VPN
    
  accounts:
    - Users & Groups
    - Internet Accounts
    - Passwords
    - Touch ID & Password

search_approach:
  1. Open System Settings (⌘Space → "System Settings")
  2. Use search box (⌘F)
  3. Type setting name
  4. Select from results
```

### Common Settings Automation
```yaml
display_settings:
  access: System Settings → Displays
  operations:
    - Arrangement: Drag displays
    - Resolution: Select from list
    - Night Shift: Schedule/toggle
    - True Tone: Toggle
    
sound_settings:
  access: System Settings → Sound
  operations:
    - Output device: Select from list
    - Input device: Select microphone
    - Volume: Slider adjustment
    - Sound effects: Toggle/select
    
network_settings:
  wifi:
    - Click Wi-Fi
    - Select network from list
    - Enter password if needed
    - Advanced: Configure DNS/Proxy
  
  bluetooth:
    - Toggle Bluetooth on/off
    - Connect to devices
    - Pair new device
    
privacy_security:
  permissions:
    - Camera: App toggles
    - Microphone: App toggles
    - Screen Recording: App toggles
    - Accessibility: App toggles
  
  security:
    - FileVault: Disk encryption
    - Firewall: Enable/configure
    - Privacy: Limit ad tracking
```

---

## 6. 📅 CALENDAR

### Key Elements & Operations
```yaml
ui_structure:
  sidebar:
    - Calendar list
    - Subscriptions
    - Shared calendars
  
  main_view:
    - Day/Week/Month/Year views
    - Mini calendar
    - Event details

operations:
  events:
    new_event: ⌘N
    duplicate: ⌘D
    delete: Delete
    edit: Double-click or Return
    
  views:
    day: ⌘1
    week: ⌘2
    month: ⌘3
    year: ⌘4
    
  navigation:
    today: ⌘T
    next: ⌘→
    previous: ⌘←
    go_to_date: ⌘⇧T
    
  search:
    find_events: ⌘F
    next_result: ⌘G
    previous_result: ⌘⇧G
```

---

## 7. 💬 MESSAGES

### Operations
```yaml
conversations:
  new_message: ⌘N
  delete_conversation: Delete
  search: ⌘F
  details: ⌘I
  
messages:
  send: Return
  new_line: ⌥Return
  emoji_picker: ⌘⌃Space
  tapback: Double-click message
  
navigation:
  next_conversation: ⌘]
  previous_conversation: ⌘[
  jump_to_selection: ⌘J
  
attachments:
  send_file: Drag or ⌘⇧A
  save_attachment: Drag to desktop
  quick_look: Space
```

---

## 8. 🎵 MUSIC

### Playback & Library
```yaml
playback:
  play_pause: Space
  next_track: ⌘→
  previous_track: ⌘←
  volume_up: ⌘↑
  volume_down: ⌘↓
  
library:
  search: ⌘F
  new_playlist: ⌘N
  new_smart_playlist: ⌘⌥N
  add_to_library: ⌘A
  show_in_library: ⌘L
  
view:
  songs: ⌘1
  albums: ⌘2
  artists: ⌘3
  playlists: ⌘4
  
playback_controls:
  shuffle: ⌘S
  repeat: ⌘R
  up_next: ⌘U
  mini_player: ⌘⇧M
```

---

## 9. 📸 PHOTOS

### Operations
```yaml
viewing:
  zoom_in: ⌘+
  zoom_out: ⌘-
  actual_size: ⌘0
  full_screen: ⌘⌃F
  slideshow: ⌘⌥S
  
editing:
  edit_mode: Return
  rotate: ⌘R
  enhance: ⌘⇧E
  duplicate: ⌘D
  revert: ⌘Z (multiple times)
  
organization:
  new_album: ⌘N
  new_smart_album: ⌘⌥N
  add_to_album: Drag or ⌘⇧A
  favorite: ⌘.
  hide: ⌘H
  delete: ⌘Delete
  
import_export:
  import: ⌘⇧I
  export: ⌘⇧E
  
info:
    get_info: ⌘I
    keywords: ⌘K
    faces: Show faces in info
```

---

## 10. 🛠️ TERMINAL

### Operations
```yaml
window_management:
  new_window: ⌘N
  new_tab: ⌘T
  close_tab: ⌘W
  next_tab: ⌘⇧]
  previous_tab: ⌘⇧[
  
text_operations:
  clear_screen: ⌘K or clear
  clear_line: ⌃U
  clear_to_end: ⌃K
  
navigation:
  beginning_of_line: ⌃A
  end_of_line: ⌃E
  forward_word: ⌥→
  backward_word: ⌥←
  
history:
  previous_command: ↑
  next_command: ↓
  search_history: ⌃R
  
process_control:
  interrupt: ⌃C
  suspend: ⌃Z
  quit: ⌃D
  background: ⌃Z then bg
  
copy_paste:
  copy: ⌘C
  paste: ⌘V
  select_all: ⌘A
```

---

## 11. 📊 NUMBERS & EXCEL

### Numbers
```yaml
operations:
  sheets_tables:
    new_sheet: ⇧⌘N
    new_table: ⌥⌘T
    delete_table: Select → Delete
    
  cells:
    edit_cell: Return or double-click
    accept_edit: Return
    cancel_edit: Esc
    fill_down: ⌘D
    fill_right: ⌘R
    
  formulas:
    sum: ⌘⇧K
    function_browser: fn+f
    accept_suggestion: Tab
    
  formatting:
    bold: ⌘B
    italic: ⌘I
    underline: ⌘U
    format_panel: ⌥⌘I
```

### Excel
```yaml
operations:
  navigation:
    next_sheet: ⌃Page Down
    previous_sheet: ⌃Page Up
    go_to: ⌃G
    
  selection:
    select_column: ⌃Space
    select_row: ⇧Space
    extend_selection: ⇧+Arrow
    
  data:
    autosum: ⌘⇧T
    filter: ⌘⇧F
    sort: Data menu
    pivot_table: Insert → PivotTable
```

---

## 12. 🎨 PAGES & WORD

### Pages
```yaml
operations:
  document:
    new: ⌘N
    save: ⌘S
    duplicate: ⌘⇧S
    export: File → Export To
    
  formatting:
    styles: ⌘⌥⇧T
    bold: ⌘B
    italic: ⌘I
    underline: ⌘U
    
  layout:
    columns: Format → Layout
    page_break: ⌘Return
    section_break: Format → Section
```

### Word
```yaml
operations:
  view:
    print_layout: ⌘⌥P
    outline: ⌘⌥O
    draft: ⌘⌥N
    
  formatting:
    styles_pane: ⌘⌥⇧S
    paragraph: ⌘⌥M
    font: ⌘D
    
  review:
    track_changes: ⌘⇧E
    new_comment: ⌘⌥A
    accept_change: Accept button
```

---

## 13. 🎬 KEYNOTE & POWERPOINT

### Keynote
```yaml
operations:
  slides:
    new_slide: ⌘⇧N
    duplicate: ⌘D
    delete: Delete
    skip: Right-click → Skip Slide
    
  presentation:
    play: ⌘⌥P
    rehearse: ⌘⌥R
    presenter_display: ⌘⌥P with external display
    
  objects:
    text_box: Click T in toolbar
    shape: Shape menu
    image: Media → Choose
    group: ⌘⌥G
    ungroup: ⌘⌥⇧G
```

### PowerPoint
```yaml
operations:
  slides:
    new_slide: ⌘⇧N
    layout: Right-click → Layout
    duplicate: ⌘D
    
  slideshow:
    from_beginning: ⌘⇧Return
    from_current: ⌘Return
    presenter_view: ⌥Return
    
  animations:
    animation_pane: View → Animation Pane
    add_animation: Animations tab
    preview: Preview button
```

---

## 14. 💼 PRODUCTIVITY APPS

### Slack
```yaml
shortcuts:
  navigation:
    quick_switcher: ⌘K
    previous_channel: ⌥↑
    next_channel: ⌥↓
    direct_messages: ⌘⇧K
    
  messages:
    new_message: ⌘N
    edit_last: ↑ (in empty field)
    mark_unread: ⌥Click
    
  formatting:
    bold: ⌘B
    italic: ⌘I
    code: ⌘⇧C
    code_block: ⌘⌥⇧C
```

### Zoom
```yaml
shortcuts:
  meeting:
    mute_unmute: ⌘⇧A
    video_toggle: ⌘⇧V
    screen_share: ⌘⇧S
    record: ⌘⇧R
    
  participants:
    show_hide: ⌘U
    raise_hand: ⌥Y
    
  chat:
    open_chat: ⌘⇧H
    screenshot: ⌘⇧T
```

---

## 15. 🌍 CHROME & FIREFOX

### Chrome
```yaml
operations:
  tabs:
    new_tab: ⌘T
    new_incognito: ⌘⇧N
    close_tab: ⌘W
    reopen_closed: ⌘⇧T
    
  developer:
    developer_tools: ⌘⌥I
    javascript_console: ⌘⌥J
    inspect_element: Right-click → Inspect
    
  bookmarks:
    bookmark_manager: ⌘⌥B
    bookmark_page: ⌘D
    bookmark_all_tabs: ⌘⇧D
```

### Firefox
```yaml
operations:
  tabs:
    new_tab: ⌘T
    new_private_window: ⌘⇧P
    tab_groups: ⌘⇧E
    
  developer:
    web_console: ⌘⌥K
    inspector: ⌘⌥I
    debugger: ⌘⌥Z
    
  privacy:
    clear_recent_history: ⌘⇧Delete
    private_browsing: ⌘⇧P
```

---

## 🎯 Pattern Application

### Selection Logic
1. Check exact app name match
2. Identify UI elements via accessibility
3. Apply app-specific shortcuts
4. Use universal macOS patterns
5. Fall back to click operations

### Quality Standards
Every automation:
- Uses fastest method (shortcut > click)
- Verifies element presence
- Confirms action success
- Provides educational tips
- Suggests next actions

### Performance Guidelines
- Prefer keyboard shortcuts over clicking
- Cache application states
- Minimize accessibility tree traversals
- Batch similar operations
- Use native app features when available
- Learn from user patterns

### Cross-App Patterns
```yaml
universal_shortcuts:
  - ⌘, for Preferences works in most apps
  - ⌘Q quits any application
  - ⌘H hides current app
  - ⌘M minimizes window
  - ⌘W closes window/tab
  - ⌘N creates new item
  - ⌘O opens file
  - ⌘S saves current work
  - ⌘P prints
  - ⌘Z undoes last action
```

---

*This comprehensive application intelligence enables precise automation across all major macOS applications, using the most efficient methods available for each app.* 