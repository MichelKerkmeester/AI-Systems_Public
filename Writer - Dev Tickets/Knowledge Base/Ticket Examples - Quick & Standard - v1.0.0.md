# Ticket Examples - Quick & Standard

## 1. 📊 MODE COMPARISON

### 🎯 Same Request, Different Modes

**Request:** "We need search filters"

---

### 🚀 `$q` Quick Mode Example

```markdown
### ❖ Search Filters

**User Value:** Find what they need faster

**Business Goal:** Reduce bounce rate on search page

---

## ◇ Requirements
- Filter by category and date
- Show active filters
- Clear all filters option

---

## → Designs & References
- [Figma - Search Filters](link)

---

## ✓ Success Criteria
- [ ] Filters work on mobile
- [ ] Results update instantly
- [ ] Users can combine filters
```

---

### 📋 `$s` Standard Mode Example

```markdown
### ❖ Advanced Search Filters

**User Value:** Find relevant results faster with category and date filters

**Business Goal:** Reduce search abandonment rate (currently 67%)

---

## ◇ Requirements
- User can filter by category, date range, and status
- Filters update results without page refresh
- Selected filters remain visible and removable
- Mobile-responsive filter panel

---

## → Designs & References
- [Figma - Search Filters](link)
- Filters collapse on mobile to save space

---

## ✓ Success Criteria
- [ ] Results update within 300ms of filter change
- [ ] Users can combine multiple filters
- [ ] Filter state persists during session

---

## ⊗ Dependencies
- Requires: API filter endpoint (#1234)
- Blocks: Saved searches feature (#1240)
```

---

## 2. 🚀 QUICK MODE EXAMPLES ($q)

### 📸 Example 1: User Profile Update

```markdown
### ❖ Profile Picture Upload

**User Value:** Personalize their account with a profile photo

**Business Goal:** Increase user engagement and account completion

---

## ◇ Requirements
- Upload image from device
- Basic image cropping
- Replace existing photo

---

## ✓ Success Criteria
- [ ] Images upload successfully
- [ ] 5MB max file size enforced
- [ ] Supports JPG, PNG formats
```

---

### 🔔 Example 2: Notification Toggle

```markdown
### ❖ Email Notification Settings

**User Value:** Control which emails they receive

**Business Goal:** Reduce unsubscribe rate by 30%

---

## ◇ Requirements
- Toggle for each notification type
- Save preferences immediately
- Show last updated timestamp

---

## → Designs & References
- [Figma - Settings Page](link)

---

## ✓ Success Criteria
- [ ] Changes save without page refresh
- [ ] Users see confirmation message
- [ ] Preferences persist across sessions
```

---

## 3. 📋 STANDARD MODE EXAMPLES ($s)

### 📊 Example 1: Data Export Feature

```markdown
### ❖ Transaction Export

**User Value:** Download their transaction history for accounting purposes

**Business Goal:** Reduce support requests for transaction data by 50%

---

## ◇ Requirements
- Export transactions by date range
- Support CSV and PDF formats
- Include all transaction details
- Email download link for large exports

---

## → Designs & References
- [Figma - Export Modal](link)
- [Figma - Email Template](link)

**Notice:** PDFs over 10MB sent via email link

---

## ✓ Success Criteria
- [ ] Exports complete within 30 seconds
- [ ] CSV includes all data fields
- [ ] PDF formatted for printing
- [ ] Email sent for files over 10MB

---

## ⊗ Dependencies
- Requires: PDF generation service (#2001)
- Requires: Email service upgrade (#2002)
```

---

### 🎨 Example 2: Dashboard Customization

```markdown
### ❖ Widget Management

**User Value:** Customize dashboard to show most relevant information

**Business Goal:** Improve daily active usage by highlighting key features

---

## ◇ Requirements
- **Drag widgets** → Rearrange dashboard layout
- **Add/remove widgets** → From widget library
- **Resize widgets** → Small, medium, large options
- **Save layout** → Persists for user account

---

## → Designs & References

### ◻︎ Interactions
- [Figma - Widget Library](link)
- [Figma - Drag States](link)

### ◻︎ Layouts
- [Figma - Size Options](link)
- [Figma - Mobile View](link)

**Notice:** Mobile shows single column layout

---

## ✓ Success Criteria
- [ ] Layout saves within 500ms
- [ ] Drag preview shows during move
- [ ] Maximum 12 widgets per dashboard
- [ ] Mobile layout auto-adjusts

---

## ⊗ Dependencies
- Requires: Widget API v2 (#3100)
- Blocks: Shared dashboards (#3150)
```

---

### 🔍 Example 3: Search Autocomplete

```markdown
### ❖ Smart Search Suggestions

**User Value:** Find what they're looking for with fewer keystrokes

**Business Goal:** Increase search-to-conversion rate by 25%

---

## ◇ Requirements
- Show suggestions after 2 characters
- Display top 5 matching results
- Highlight matched text in suggestions
- Keyboard navigation through results

---

## → Designs & References
- [Figma - Autocomplete Dropdown](link)
- [Figma - Keyboard States](link)

---

## ✓ Success Criteria
- [ ] Suggestions appear within 100ms
- [ ] Clicking suggestion triggers search
- [ ] Arrow keys navigate suggestions
- [ ] Escape key closes dropdown

---

## ⊗ Dependencies
- Requires: Search index optimization (#4001)
- Related: Recent searches feature (#4002)
```

---

## 4. 🧭 MODE SELECTION PATTERNS

### 🚀 When to Use Quick Mode ($q)
- Single, focused feature
- Clear requirements
- Minimal dependencies
- Can be built in 1-3 days
- Limited design complexity

### 📋 When to Use Standard Mode ($s)
- Multiple requirements
- Needs design references
- Has dependencies
- Requires 3-5 days
- Success criteria need detail

### ⬆️ Quick to Standard Escalation
If during Quick mode you find:
- Multiple user flows needed
- Dependencies emerge
- Design complexity increases
- Success criteria multiply

→ Switch to Standard mode for clarity

---

## 5. ✅ QUALITY MARKERS

### 🚀 Well-Written Quick Ticket
- ✓ Under 150 words
- ✓ 3-5 requirements max
- ✓ Clear success criteria
- ✓ One primary user action

### 📋 Well-Written Standard Ticket
- ✓ Under 300 words
- ✓ Organized requirements
- ✓ Design references included
- ✓ Dependencies noted
- ✓ Measurable success criteria