# Ticket Examples - Partial Input Handling

## 1. 🔧 HANDLING INCOMPLETE INPUTS

This section shows how the system intelligently handles partial tickets, visual descriptions, and incomplete specifications across ALL modes.

---

## 2. 📝 PARTIAL TICKET EXAMPLES

### 📋 Example 1: Technical List → Full Ticket

**Input:**
```
Add user settings:
- Change password
- Update email
- Toggle notifications  
- Delete account
- Export data
```

**Standard Mode ($s) Enhancement:**
```markdown
### ❖ User Account Settings

**User Value:** Manage your account preferences and data in one secure location

**Business Goal:** Reduce support tickets by 60% through self-service account management

---

## ◇ Requirements
**Account Management:**
- Change password with current password verification
- Update email with confirmation flow
- Toggle email/push notifications by type
- Delete account with confirmation and data export
- Export all user data in JSON/CSV format

**Security & UX:**
- Require password for sensitive changes
- Show last modified dates for settings
- Confirmation emails for critical changes
- 30-day recovery window for deletions

---

## → Designs & References
- **Needs:** Settings page UI mockups
- **Needs:** Email confirmation templates
- Standard password requirements apply

---

## ✓ Success Criteria
- [ ] All settings changes save within 1 second
- [ ] Confirmation emails sent within 30 seconds
- [ ] Data export completes within 2 minutes
- [ ] Delete account includes data download
- [ ] Mobile-responsive settings interface

---

## ⊗ Dependencies
- Requires: Email service for confirmations (#1001)
- Requires: Data export infrastructure (#1002)
- Impacts: Authentication system (#1003)
```

---

### 🖼️ Example 2: Screenshot Description → Ticket

**Input:**
```
$s Here's our new dashboard design [screenshot showing analytics with date picker, 3 charts, and export button]
```

**System Extracts and Enhances:**
```markdown
### ❖ Analytics Dashboard

**User Value:** Monitor key business metrics at a glance with customizable date ranges

**Business Goal:** Enable data-driven decisions across all team levels

---

## ◇ Requirements
**Extracted from screenshot:**
- Date range picker (custom ranges + presets)
- Line chart for trend analysis
- Bar chart for comparisons  
- Pie chart for distributions
- Export functionality (PDF/CSV icons visible)

**Inferred requirements:**
- Real-time data refresh
- Responsive chart sizing
- Loading states during data fetch
- Empty states for no data
- Error handling for failed loads

---

## → Designs & References
- [Dashboard Screenshot](link)
- **Notice:** Charts use company color palette
- **Notice:** Export icons suggest PDF and CSV formats

---

## ✓ Success Criteria
- [ ] Charts load within 2 seconds
- [ ] Date picker includes last 7/30/90 days
- [ ] Export generates valid files
- [ ] Charts are interactive (hover states)
- [ ] Mobile view stacks charts vertically

---

## ⊗ Dependencies
- Requires: Analytics API endpoints (#2001)
- Requires: Chart library selection (#2002)
```

---

## 3. 🎛️ MODE-SPECIFIC HANDLING

### 🚀 Quick Mode ($q) - Minimal Enhancement

**Input:**
```
$q login with SSO
```

**Enhanced:**
```markdown
### ❖ SSO Login

**User Value:** Sign in quickly using your company credentials

**Business Goal:** Increase adoption through simplified authentication

---

## ◇ Requirements
- Single sign-on with SAML 2.0
- Auto-redirect for known domains
- Support Google Workspace and Microsoft

---

## ✓ Success Criteria
- [ ] SSO login works in <3 seconds
- [ ] Supports major providers
- [ ] Mobile browser compatible
```

---

### 🔧 Complex Mode ($c) - Deep Analysis

**Input (Same partial ticket):**
```
$c login with SSO
```

**Enhanced with Deep Analysis:**
```markdown
### ❖ Enterprise SSO Integration

---

# ⌘ About

Implementing SSO is critical for enterprise adoption. Our competitors all offer it, and 73% of enterprise deals require SSO as a baseline feature.

**User Value:** Access the platform seamlessly with existing corporate credentials

**Business Goal:** Unlock enterprise market segment (projected $2M ARR)

---

## ◇ Phase 1: Foundation (Week 1-2)
- SAML 2.0 protocol implementation
- Identity provider configuration UI
- Metadata exchange handling
- Session management architecture

---

## ◇ Phase 2: Major Providers (Week 3-4)
- Google Workspace integration
- Microsoft Azure AD/Entra ID
- Okta configuration
- Auth0 compatibility

---

## ◇ Phase 3: Enterprise Features (Week 5-6)
- Just-in-time provisioning
- Group/role mapping
- SCIM user management
- Multi-domain support

---

## ✓ Success Criteria
- [ ] Support top 5 identity providers
- [ ] Login completes in <3 seconds
- [ ] 99.9% authentication uptime
- [ ] Automatic user provisioning works
- [ ] Audit logs for all SSO events

---

## ⊗ Dependencies
- Requires: Security audit (#4001)
- Requires: Session management upgrade (#4002)
- Blocks: Enterprise tier launch (#4100)

---

## ⚠ Risks
- **Complexity:** Each IdP has quirks
- **Testing:** Need test accounts for each provider
- **Security:** SSO bypass vulnerabilities
- **Support:** Enterprise customers expect 24/7 help
```

---

## 4. 🎨 VISUAL INPUT PATTERNS

### 🖼️ Pattern: UI Component Detection

When users describe or show UI elements, extract:

| Visual Element | Extracted Requirement |
|----------------|----------------------|
| Button | User action + expected outcome |
| Form field | Data input + validation rules |
| Dropdown | Selection options + default state |
| Toggle | Binary choice + state persistence |
| Chart | Data visualization + interaction |
| Table | Data display + sorting/filtering |
| Modal | Overlay interaction + dismiss behavior |
| Navigation | User flow + active states |

### 🔍 Pattern: Missing Element Detection

The system identifies what's typically missing:

**Has Requirements, Missing:**
- User value → Derive from functionality
- Business goal → Infer from feature type
- Success criteria → Generate from requirements

**Has Design, Missing:**
- Edge cases → Extract from UI states
- Performance needs → Infer from interactions  
- Dependencies → Identify from data shown

**Has Technical Specs, Missing:**
- User perspective → Transform technical to human
- Business impact → Connect to metrics
- Validation criteria → Create from specs

---

## 5. 💬 INTELLIGENT QUESTIONING

When enhancement isn't enough, ask smart questions:

### ❌ Instead of: "What's missing?"

**✅ Ask specifically:**
- "I see a dashboard design. What key metrics should it track?"
- "This login flow looks good. Should it support social logins too?"
- "The export feature is clear. What file formats do users need?"
- "I notice filters. Should the filtered state persist between sessions?"

### 🎯 Pattern-Based Questions:

**For E-commerce Features:**
- "Should this work with guest checkout?"
- "Does this need to handle multiple currencies?"

**For Data Features:**
- "What's the expected data volume?"
- "How fresh does the data need to be?"

**For User Features:**
- "Should this respect role-based permissions?"
- "Does this need audit logging?"

---

## 6. ✅ QUALITY PRINCIPLES

### 🎯 Extraction Accuracy
- Only extract what's clearly present or strongly implied
- Mark assumptions with **"Inferred:"**
- Flag gaps with **"Needs:"**
- Don't over-interpret simple requests

### 🎛️ Mode Respect
- Quick mode: Don't over-engineer simple requests
- Standard mode: Balance enhancement with clarity
- Complex mode: Explore all implications
- Epic mode: Find all hidden child tickets

### 👤 User Intent
- Enhance without changing