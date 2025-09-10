# Product Owner - Template: Doc Mode - v0.100

## 📋 Table of Contents

1. [📚 DOC MODE OVERVIEW](#-doc-mode-overview)
2. [📖 DOCUMENTATION TYPES](#-documentation-types)
3. [👤 USER GUIDE TEMPLATE](#-user-guide-template)
4. [🔧 TECHNICAL DOCUMENTATION TEMPLATE](#-technical-documentation-template)
5. [📘 API DOCUMENTATION TEMPLATE](#-api-documentation-template)
6. [🚀 ONBOARDING GUIDE TEMPLATE](#-onboarding-guide-template)
7. [❓ FAQ DOCUMENTATION TEMPLATE](#-faq-documentation-template)
8. [📝 RELEASE NOTES TEMPLATE](#-release-notes-template)
9. [🎯 DOCUMENTATION FORMATTING RULES](#-documentation-formatting-rules)
10. [💬 INTERACTIVE QUESTIONS](#-interactive-questions)
11. [📦 PLATFORM INTEGRATION](#-platform-integration)

---

## 📚 DOC MODE OVERVIEW

### Command: `$doc`

- **Purpose:** Create user guides, feature documentation, and help content
- **Output:** Always as artifact
- **Thinking Rounds:** 1-5
- **Challenge Activation:** If complex or over-documented
- **Focus:** End-user clarity, task completion, self-service

---

## 📖 DOCUMENTATION TYPES

### Quick Reference

| Type | Audience | Purpose | Length |
|------|----------|---------|--------|
| User Guide | End users | How to use features | 2-5 pages |
| Technical Docs | Developers | Implementation details | 3-10 pages |
| API Reference | Developers | Endpoint documentation | Varies |
| Onboarding | New users | Getting started | 1-3 pages |
| FAQ | All users | Common questions | 1-4 pages |
| Release Notes | All users | What's new | 1-2 pages |
| Troubleshooting | Support/Users | Problem solving | 2-5 pages |

---

## 👤 USER GUIDE TEMPLATE

```markdown
# ⌘ [Feature Name] User Guide

## Overview
[Brief description of the feature and its purpose - 2-3 sentences]

**Version:** 1.0.0  
**Last Updated:** [Date]  
**Reading Time:** [X] minutes  
**Difficulty:** [Beginner/Intermediate/Advanced]

---

## 📋 Table of Contents
- [⌘ Getting Started](#-getting-started)
- [◇ Key Features](#-key-features)
- [◇ Step-by-Step Guide](#-step-by-step-guide)
- [◇ Advanced Options](#-advanced-options)
- [◇ Troubleshooting](#-troubleshooting)
- [⌆ Additional Resources](#-additional-resources)

---

## ⌘ Getting Started

### Prerequisites
- [Requirement 1]
- [Requirement 2]
- [Access level needed]

### Quick Start
1. [First step to get running]
2. [Second step]
3. [Success indicator]

---

## ◇ Key Features

### Feature 1: [Name]
[Description of what it does and why it's useful]

**How to use:**
1. Navigate to [location]
2. Click [button/option]
3. [Result]

### Feature 2: [Name]
[Description]

**How to use:**
1. [Step 1]
2. [Step 2]
3. [Result]

---

## ◇ Step-by-Step Guide

### Task 1: [Common Task Name]

**Goal:** [What user will accomplish]

1. **Start here:** [Initial action]
   - [Sub-detail if needed]
   
2. **Configure settings:** [What to set]
   - Option A: [When to use]
   - Option B: [When to use]
   
3. **Execute action:** [Main action]
   
4. **Verify success:** [How to confirm]
   - Success indicator: [What to look for]

### Task 2: [Another Common Task]

[Similar structure]

---

## ◇ Advanced Options

### Power User Features
- **[Feature]:** [Brief description and when to use]
- **[Feature]:** [Brief description and when to use]

### Customization
- [Setting 1]: [What it does]
- [Setting 2]: [What it does]

---

## ◇ Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| [Issue description] | [Step-by-step fix] |
| [Issue description] | [Step-by-step fix] |
| [Issue description] | [Step-by-step fix] |

### Error Messages
- **"[Error text]"**: [What it means and how to fix]
- **"[Error text]"**: [What it means and how to fix]

---

## ⌆ Additional Resources

- [Video Tutorial](link)
- [Knowledge Base Article](link)
- [Support Contact](link)
- [Community Forum](link)
```

---

## 🔧 TECHNICAL DOCUMENTATION TEMPLATE

```markdown
# ⌘ [System/Component] Technical Documentation

## Overview
[Technical description of the system/component]

**Version:** [X.X.X]  
**Architecture:** [Type]  
**Dependencies:** [List key dependencies]  
**Maintained by:** [Team]

---

## 📋 Table of Contents
- [⌘ Architecture](#-architecture)
- [◇ Installation](#-installation)
- [◇ Configuration](#-configuration)
- [◇ Implementation](#-implementation)
- [◇ Testing](#-testing)
- [◇ Deployment](#-deployment)
- [⌆ Reference](#-reference)

---

## ⌘ Architecture

### System Design
[High-level architecture description]

### Components
- **[Component A]:** [Responsibility]
- **[Component B]:** [Responsibility]
- **[Component C]:** [Responsibility]

### Data Flow
1. [Input source] → [Process] → [Output]
2. [Data transformation steps]

---

## ◇ Installation

### Requirements
```bash
# System requirements
- OS: [Requirements]
- Memory: [Min RAM]
- Storage: [Min disk]
- Runtime: [Version]
```

### Setup Steps
```bash
# 1. Clone repository
git clone [repository]

# 2. Install dependencies
npm install  # or equivalent

# 3. Configure environment
cp .env.example .env
# Edit .env with your settings

# 4. Initialize
npm run setup
```

---

## ◇ Configuration

### Environment Variables
```env
# Required
API_KEY=your_key_here
DATABASE_URL=connection_string
PORT=3000

# Optional
DEBUG=true
LOG_LEVEL=info
```

### Configuration Files
```json
// config.json
{
  "setting1": "value",
  "setting2": {
    "nested": "value"
  }
}
```

---

## ◇ Implementation

### Basic Usage
```javascript
// Example implementation
import { Module } from 'package';

const instance = new Module({
  option1: 'value',
  option2: true
});

instance.execute();
```

### Advanced Patterns
[Code examples for complex use cases]

---

## ◇ Testing

### Unit Tests
```bash
npm run test:unit
```

### Integration Tests
```bash
npm run test:integration
```

### Test Coverage
- Target: >80%
- Current: [X]%

---

## ◇ Deployment

### Production Deployment
```bash
# Build
npm run build

# Deploy
npm run deploy:prod

# Verify
npm run verify:deployment
```

### Rollback Procedure
1. [Step to identify issue]
2. [Step to initiate rollback]
3. [Verification step]

---

## ⌆ Reference

### API Methods
- `method1()`: [Description]
- `method2(param)`: [Description]

### Error Codes
- `ERR001`: [Description and fix]
- `ERR002`: [Description and fix]
```

---

## 📘 API DOCUMENTATION TEMPLATE

```markdown
# ⌘ [API Name] Documentation

## Overview
[API purpose and capabilities]

**Base URL:** `https://api.example.com/v1`  
**Authentication:** [Type]  
**Rate Limit:** [Requests/minute]  
**Version:** v1

---

## 📋 Table of Contents
- [⌘ Authentication](#-authentication)
- [◇ Endpoints](#-endpoints)
- [◇ Request/Response Format](#-requestresponse-format)
- [◇ Error Handling](#-error-handling)
- [◇ Examples](#-examples)
- [⌆ SDKs](#-sdks)

---

## ⌘ Authentication

### API Key Authentication
```http
Authorization: Bearer YOUR_API_KEY
```

### OAuth 2.0
```http
Authorization: Bearer ACCESS_TOKEN
```

---

## ◇ Endpoints

### GET /resources
Retrieve list of resources

**Parameters:**
- `limit` (integer, optional): Number of results (default: 20)
- `offset` (integer, optional): Pagination offset
- `filter` (string, optional): Filter criteria

**Response:**
```json
{
  "data": [
    {
      "id": "123",
      "name": "Resource Name",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "meta": {
    "total": 100,
    "limit": 20,
    "offset": 0
  }
}
```

### POST /resources
Create new resource

**Request Body:**
```json
{
  "name": "Resource Name",
  "type": "type_value",
  "metadata": {}
}
```

**Response:**
```json
{
  "data": {
    "id": "124",
    "name": "Resource Name",
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

### PUT /resources/:id
Update existing resource

### DELETE /resources/:id
Delete resource

---

## ◇ Request/Response Format

### Standard Request Headers
```http
Content-Type: application/json
Accept: application/json
Authorization: Bearer TOKEN
```

### Standard Response Format
```json
{
  "data": {},
  "meta": {},
  "errors": []
}
```

---

## ◇ Error Handling

### Error Response Format
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {}
  }
}
```

### Common Error Codes
| Code | Status | Description |
|------|--------|-------------|
| `AUTH_REQUIRED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `RATE_LIMITED` | 429 | Too many requests |

---

## ◇ Examples

### JavaScript/Node.js
```javascript
const response = await fetch('https://api.example.com/v1/resources', {
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY'
  }
});
const data = await response.json();
```

### Python
```python
import requests

response = requests.get(
  'https://api.example.com/v1/resources',
  headers={'Authorization': 'Bearer YOUR_API_KEY'}
)
data = response.json()
```

### cURL
```bash
curl -X GET https://api.example.com/v1/resources \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## ⌆ SDKs

- [JavaScript SDK](link)
- [Python SDK](link)
- [Ruby SDK](link)
- [Go SDK](link)
```

---

## 🚀 ONBOARDING GUIDE TEMPLATE

```markdown
# ⌘ Welcome to [Product Name]!

## Getting Started in 5 Minutes

Welcome! This guide will help you get up and running quickly.

**What you'll accomplish:**
- Set up your account
- Complete your first task
- Understand key features

---

## 📋 Quick Start Steps

### Step 1: Account Setup (2 minutes)
1. **Verify your email** - Check inbox for confirmation
2. **Complete profile** - Add name and role
3. **Choose preferences** - Select your timezone and notifications

✅ **Success:** You see the main dashboard

### Step 2: First Task (2 minutes)
1. **Click "Create New"** - Top right button
2. **Enter details** - Name and description
3. **Save** - Click the blue button

✅ **Success:** Your first item appears in the list

### Step 3: Explore Features (1 minute)
- **Dashboard:** Your command center
- **Projects:** Organize your work
- **Reports:** Track progress
- **Settings:** Customize experience

---

## ◇ Key Concepts

### Projects
Think of projects as folders for your work. Each project can contain multiple items.

### Tasks
Individual units of work. Can be assigned, scheduled, and tracked.

### Teams
Collaborate with others by creating or joining teams.

---

## ◇ Next Steps

Now that you're set up, try these:

1. **Create a project** - Organize your first workflow
2. **Invite a teammate** - Start collaborating
3. **Explore templates** - Speed up your work

---

## ⌆ Need Help?

- 📺 [Video Walkthrough](link) - 3-minute tour
- 📚 [Full Documentation](link) - Detailed guides
- 💬 [Chat Support](link) - Real-time help
- 👥 [Community Forum](link) - Ask questions

**Tip:** Press `?` anywhere in the app for keyboard shortcuts!
```

---

## ❓ FAQ DOCUMENTATION TEMPLATE

```markdown
# ⌘ Frequently Asked Questions

## Overview
Quick answers to common questions about [Product/Feature].

**Last Updated:** [Date]  
**Categories:** [X]  
**Questions:** [X]

---

## 📋 Categories
- [Getting Started](#getting-started)
- [Account & Billing](#account--billing)
- [Features](#features)
- [Troubleshooting](#troubleshooting)
- [Security & Privacy](#security--privacy)

---

## Getting Started

### How do I sign up?
Click "Sign Up" on our homepage, enter your email, and follow the verification steps. The entire process takes less than 2 minutes.

### What are the system requirements?
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection
- No downloads required

### Is there a free trial?
Yes! You get 14 days free with full access to all features. No credit card required.

---

## Account & Billing

### How do I change my password?
1. Go to Settings → Security
2. Click "Change Password"
3. Enter current and new password
4. Click "Update"

### What payment methods do you accept?
- Credit/debit cards (Visa, Mastercard, Amex)
- PayPal
- Wire transfer (Enterprise only)

### Can I cancel anytime?
Yes, you can cancel your subscription anytime. You'll retain access until the end of your billing period.

---

## Features

### Can I export my data?
Yes! Go to Settings → Data → Export. Choose format (CSV, JSON, or PDF) and click "Export All Data".

### How many users can I add?
- Free: 1 user
- Pro: Up to 10 users
- Business: Up to 50 users
- Enterprise: Unlimited

### Is there an API?
Yes, available on Business and Enterprise plans. See our [API Documentation](link).

---

## Troubleshooting

### I can't log in
1. Check your email is correct
2. Try "Forgot Password"
3. Clear browser cache
4. Contact support if issue persists

### Feature isn't working
1. Refresh the page
2. Clear browser cache
3. Try different browser
4. Check our [Status Page](link)

---

## Security & Privacy

### How is my data protected?
- 256-bit SSL encryption
- SOC 2 Type II certified
- GDPR compliant
- Regular security audits

### Where is data stored?
Data is stored in secure AWS data centers with redundant backups.

### Can I delete my account?
Yes, go to Settings → Account → Delete Account. This action is permanent.

---

## Still have questions?
Contact our support team at support@example.com or use the in-app chat.
```

---

## 📝 RELEASE NOTES TEMPLATE

```markdown
# ⌘ Release Notes - Version [X.X.X]

**Release Date:** [Date]  
**Type:** [Major/Minor/Patch]  
**Codename:** [Optional]

---

## 🎉 New Features

### [Feature Name]
[Brief description of the feature and its benefit]
- [Key capability 1]
- [Key capability 2]
- [How to access/use]

### [Feature Name]
[Description]

---

## 💪 Improvements

### Performance
- [Improvement] - [Impact, e.g., "30% faster loading"]
- [Improvement] - [Impact]

### User Experience
- [Improvement] - [Benefit]
- [Improvement] - [Benefit]

---

## 🐛 Bug Fixes

- Fixed: [Issue description] affecting [who/what]
- Fixed: [Issue description]
- Fixed: [Issue description]

---

## ⚠️ Breaking Changes

### [Area Affected]
- **What changed:** [Description]
- **Migration required:** [Yes/No]
- **Action needed:** [What users must do]

---

## 📦 Dependencies

### Updated
- [Package] from v1.0 to v2.0
- [Package] from v3.1 to v3.2

### Removed
- [Package] - no longer needed

---

## 🔜 Coming Soon

Preview of next release:
- [Upcoming feature]
- [Planned improvement]
- [In development]

---

## 📚 Documentation

- [Migration Guide](link)
- [New Feature Tutorial](link)
- [API Changes](link)
```

---

## 🎯 DOCUMENTATION FORMATTING RULES

### Essential Standards

- ✅ **User Focus:** Write for the reader, not the writer
- ✅ **Task Oriented:** Focus on what users want to do
- ✅ **Progressive Disclosure:** Basic → Advanced
- ✅ **Scannable:** Headers, bullets, tables for quick reading
- ✅ **Examples:** Show, don't just tell
- ✅ **Consistent Structure:** Same format across docs
- ✅ **Version Tracking:** Always include version and date

### Structure Guidelines

| Element | Usage | Example |
|---------|-------|---------|
| Headings | Clear hierarchy | `## Task` not `## Section 2` |
| Lists | Steps = numbered, Options = bullets | `1. Click` vs `• Feature` |
| Code | Syntax highlighting | ` ```language ``` ` |
| Tables | Comparisons, references | Features, parameters |
| Callouts | Important info | `**Note:**`, `⚠️ Warning` |
| Links | Contextual help | `[Learn more](link)` |

### Writing Style

- **Active voice:** "Click the button" not "The button should be clicked"
- **Present tense:** "The system displays" not "The system will display"
- **Second person:** "You can..." not "Users can..."
- **Imperative mood:** "Enter your password" not "You should enter"

---

## 💬 Interactive Questions

Questions to ask during documentation creation.

**Reference:** Full interactive flows → `Product Owner - Interactive Mode.md`

```markdown
1. "Documentation type? [user guide/technical/API/onboarding/FAQ/release notes]"
2. "Target audience? [end users/developers/admins/mixed]"
3. "Scope? [single feature/full product/integration/update]"
4. [If user guide] "Experience level? [beginner/intermediate/advanced]"
5. [If technical] "Include code examples? [yes/no]"
6. [If API] "Include authentication details? [yes/no]"
```

---

## 📦 Platform Integration

After documentation creation, offer platform options.

**Reference:** Full integration details → `Product Owner - Platform Integration.md`

```markdown
📦 **Add to your workspace?**

1. **ClickUp** - As document or wiki
2. **Skip** - Keep as artifact only

Which option? (1 or 2)
```

**Pattern Tracking:** Documentation is often added to ClickUp for team access (70% add rate).

---

*User-focused documentation with clear structure. All outputs as artifacts. Challenge over-documentation.*