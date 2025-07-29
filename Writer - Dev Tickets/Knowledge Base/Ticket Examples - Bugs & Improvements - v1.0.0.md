# Ticket Examples - Bugs & Improvements

## 1. 🐛 BUG TICKET EXAMPLES

### 🔍 Example 1: Search Filter Reset Bug

```markdown
### ❖ Bug: Search Filters Reset on Back Navigation

**User Value:** Keep selected filters when navigating back to search results

**Business Goal:** Reduce user frustration and abandonment (23% drop-off rate)

---

## ◆ Current Behavior
1. User applies multiple filters
2. User clicks on a search result
3. User clicks browser back button
4. **Bug:** All filters are cleared

---

## ✓ Expected Behavior
- Filters persist when navigating back
- Selected filters remain visible
- Results show filtered state

---

## → Designs & References
- [Figma - Expected Filter State](link)
- [Video - Current Bug Behavior](link)

**Notice:** This worked correctly before v2.3 release.

---

## ✓ Success Criteria
- [ ] 100% of filters persist on back navigation
- [ ] Filter state restored within 100ms
- [ ] Works across all major browsers

---

## ⊗ Dependencies
- Requires: Browser history API investigation (#1454)
- Blocks: Search analytics accuracy (#1455)
```

---

### 📊 Example 2: Data Display Bug

```markdown
### ❖ Bug: Incorrect Total Calculation in Reports

**User Value:** See accurate financial totals they can trust

**Business Goal:** Maintain data integrity and user confidence

---

## ◆ Current Behavior
- Subtotals calculate correctly
- **Bug:** Grand total shows $0.00 when negative values present
- Only affects reports with mixed positive/negative values

---

## ✓ Expected Behavior
- Grand total sums all values correctly
- Handles positive and negative numbers
- Displays proper currency formatting

---

## ◈ Steps to Reproduce
1. Create report with transactions
2. Include at least one refund (negative value)
3. View report summary
4. Observe incorrect total

---

## → Designs & References
- [Screenshot - Incorrect Total](link)
- [Screenshot - Expected Display](link)

---

## ✓ Success Criteria
- [ ] Totals calculate correctly 100% of time
- [ ] Negative values display in red
- [ ] Currency formatting preserved

---

## ⊗ Dependencies
- Related: Report export feature (#2234)
- Blocks: Financial dashboard (#2240)
```

---

### 📱 Example 3: Mobile Responsiveness Bug

```markdown
### ❖ Bug: Navigation Menu Overlaps Content on iPad

**User Value:** Use the app effectively on tablet devices

**Business Goal:** Support growing tablet user base (15% of traffic)

---

## ◆ Current Behavior
- Desktop (>1024px): Menu displays correctly
- Mobile (<768px): Hamburger menu works
- **Bug:** iPad (768-1024px): Menu overlaps main content

---

## ✓ Expected Behavior
- Menu adapts to available space
- No content overlap at any viewport
- Smooth transition between layouts

---

## → Designs & References
- [Screenshot - iPad Overlap Issue](link)
- [Figma - Responsive Breakpoints](link)

---

## ✓ Success Criteria
- [ ] No overlap 768px to 1024px viewports
- [ ] Menu items remain accessible
- [ ] Tested on iPad Air, iPad Pro

---

## ⊗ Dependencies
- Related: Design system updates (#3301)
```

---

## 2. 💡 IMPROVEMENT TICKET EXAMPLES

### ⚡ Example 1: Performance Improvement

```markdown
### ❖ Improvement: Faster Chart Loading

**User Value:** See data instantly without waiting

**Business Goal:** Reduce dashboard bounce rate by 25%

---

## ◈ Current Performance
- Initial load: 3-5 seconds
- Subsequent loads: 2-3 seconds  
- Mobile: 5-7 seconds

---

## ◆ Target Performance
- Initial load: <1 second
- Subsequent loads: <500ms
- Mobile: <2 seconds

---

## → Designs & References
- [Figma - Loading States](link)
- [Figma - Progressive Enhancement](link)

**Notice:** Show skeleton loaders during data fetch.

---

## ◇ Requirements
- Implement progressive data loading
- Add skeleton states while loading
- Cache rendered charts for session
- Lazy load below-fold charts

---

## ✓ Success Criteria
- [ ] 90% of charts load in <1 second
- [ ] 25% reduction in bounce rate
- [ ] Performance budget: 200KB JS max

---

## ⊗ Dependencies
- Requires: Performance monitoring setup (#1501)
- Requires: CDN configuration (#1502)
- Blocks: Mobile app integration (#1520)
```

---

### 🎯 Example 2: UX Improvement

```markdown
### ❖ Improvement: Bulk Action Efficiency

**User Value:** Manage multiple items 5x faster

**Business Goal:** Increase power user satisfaction (NPS +10)

---

## ◈ Current State
- Users select items one by one
- Actions apply individually
- No keyboard shortcuts
- 8 clicks to delete 5 items

---

## ◇ Requirements
- **Select all** → Checkbox in header
- **Shift+click** → Range selection
- **Bulk actions bar** → Appears with selection
- **Keyboard shortcuts** → Delete, archive, move

---

## → Designs & References
- [Figma - Selection States](link)
- [Figma - Bulk Action Bar](link)

---

## ✓ Success Criteria
- [ ] Bulk actions complete in <2 seconds
- [ ] Selection state persists during scroll
- [ ] Undo available for 10 seconds
- [ ] 80% reduction in clicks for bulk tasks

---

## ⊗ Dependencies
- Requires: Selection state management (#4421)
- Enhances: Keyboard navigation (#4422)
```

---

### 📈 Example 3: Data Accuracy Improvement

```markdown
### ❖ Improvement: Real-time Sync Indicators

**User Value:** Know instantly when data is current

**Business Goal:** Reduce "stale data" support tickets by 60%

---

## ◈ Current State
- No sync status shown
- Users unsure if data is current
- Manual refresh required
- 40+ tickets/month about old data

---

## ◇ Requirements
- **Last synced timestamp** → Shows on all data views
- **Auto-refresh** → Every 5 minutes when tab active
- **Sync in progress** → Loading indicator
- **Sync failed** → Error state with retry

---

## → Designs & References

### ◻︎ Status Indicators
- [Figma - Sync States](link)
- [Figma - Error Messages](link)

### ◻︎ Positioning
- [Figma - Desktop Layout](link)
- [Figma - Mobile Layout](link)

---

## ✓ Success Criteria
- [ ] Sync status always visible
- [ ] Updates complete within 3 seconds
- [ ] 60% reduction in stale data tickets
- [ ] Works offline with clear messaging

---

## ⊗ Dependencies
- Requires: WebSocket connection (#5501)
- Related: Offline mode (#5502)
```

---

## 3. 🎨 SPECIALIZED PATTERNS

### 🐛 Bug Ticket Structure

1. **Title Format:** `Bug: [Feature] - [Specific Issue]`
2. **Current vs Expected:** Always show both states
3. **Reproduction Steps:** When not obvious
4. **Evidence:** Screenshots, videos, or logs
5. **Regression Note:** If it worked before

### 💡 Improvement Ticket Structure

1. **Title Format:** `Improvement: [Feature Enhancement]`
2. **Current State:** Metrics or user pain
3. **Target State:** Measurable improvement
4. **Requirements:** Specific changes needed
5. **Success Metrics:** Quantifiable outcomes

---

## 4. 📊 DECISION CRITERIA

### 🐛 Bug vs Improvement

**Bug Indicators:**
- Feature doesn't work as designed
- Regression from previous version
- Data integrity issue
- Crashes or errors
- Accessibility failure

**Improvement Indicators:**
- Feature works but slowly
- UX could be better
- New user need emerged
- Efficiency opportunity
- Technical debt reduction

### 🎯 Priority Signals

**High Priority:**
- Data loss or corruption
- Security vulnerability
- Blocks user workflow
- Affects >20% of users
- Revenue impact

**Medium Priority:**
- Workaround exists
- Affects <20% of users
- Performance degradation
- Visual inconsistency

**Low Priority:**
- Edge case scenario
- Minor visual issue
- Nice-to-have enhancement
- Affects <5% of users

---

## 5. ⚠️ COMMON PITFALLS TO AVOID

### 🐛 In Bug Tickets
- ⊗ Don't assume the cause
- ⊗ Don't mix multiple bugs
- ⊗ Don't skip reproduction steps
- ⊗ Don't forget browser/device info
- ⊗ Don't omit the business impact

### 💡 In Improvement Tickets
- ⊗ Don't make changes without metrics
- ⊗ Don't assume user preferences
- ⊗ Don't skip current state analysis
- ⊗ Don't forget success measurement
- ⊗ Don't bundle unrelated improvements