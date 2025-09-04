# Product Owner - Template: Text Mode - v1.0.0

## 📋 Table of Contents

1. [✏️ TEXT MODE OVERVIEW](#️-text-mode-overview)
2. [📝 TEXT SNIPPET TYPES](#-text-snippet-types)
3. [💬 ERROR MESSAGES](#-error-messages)
4. [📧 EMAIL TEMPLATES](#-email-templates)
5. [📄 DESCRIPTIONS](#-descriptions)
6. [🔔 NOTIFICATIONS](#-notifications)
7. [📢 MARKETING COPY](#-marketing-copy)
8. [🎯 TEXT FORMATTING RULES](#-text-formatting-rules)
9. [💬 INTERACTIVE QUESTIONS](#-interactive-questions)
10. [📦 PLATFORM INTEGRATION](#-platform-integration)

---

## ✏️ TEXT MODE OVERVIEW

### Command: `$text`

- **Purpose:** Create quick text snippets, descriptions, and copy
- **Output:** Always as artifact
- **Thinking Rounds:** 1-2 (minimal complexity)
- **Challenge Activation:** Rarely (only if overly complex)
- **Typical Length:** 1-5 sentences or 20-100 words

---

## 📝 TEXT SNIPPET TYPES

### Quick Reference

| Type | Use Case | Length | Tone |
|------|----------|--------|------|
| Error Message | User-facing errors | 1-2 sentences | Clear, helpful |
| Success Message | Confirmations | 1 sentence | Positive, concise |
| Email | Communication | 3-10 sentences | Professional |
| Description | Feature/product | 2-4 sentences | Informative |
| Notification | Alerts/updates | 1-2 sentences | Direct |
| Marketing | Promotional | 2-5 sentences | Engaging |
| Help Text | UI assistance | 1-3 sentences | Friendly |
| Button Label | CTA text | 2-5 words | Action-oriented |

---

## 💬 ERROR MESSAGES

### Template Structure

```markdown
# Error Message: [Context]

## User-Friendly Version
"[What happened in plain language]. [What to do next]. [Optional: Where to get help]"

## Technical Details (if needed)
Error Code: [XXX]
Context: [When this appears]
Severity: [Low/Medium/High]
```

### Examples

```markdown
# Error Message: Payment Failed

## User-Friendly Version
"We couldn't process your payment. Please check your card details and try again. If the problem persists, contact support."

## Technical Details
Error Code: PAY-401
Context: Checkout process
Severity: High
```

```markdown
# Error Message: File Upload

## User-Friendly Version
"Your file is too large. Please choose a file under 10MB."

## Technical Details
Error Code: UPLOAD-413
Context: File upload dialog
Severity: Low
```

---

## 📧 EMAIL TEMPLATES

### Professional Email Template

```markdown
# Email: [Purpose]

## Subject Line
"[Clear, specific subject - 5-10 words]"

## Body
Hi [Name],

[Opening - context/purpose in 1 sentence]

[Main point - 1-2 sentences with key information]

[Call to action or next steps - 1 sentence]

[Closing]
[Signature]

## Metadata
- Tone: [Professional/Casual/Formal]
- Urgency: [High/Medium/Low]
- Recipients: [Individual/Team/Company-wide]
```

### Example

```markdown
# Email: Feature Launch Announcement

## Subject Line
"New Dashboard Features Now Available"

## Body
Hi Team,

We're excited to announce that the new analytics dashboard is now live.

You can access real-time metrics, customizable reports, and automated insights directly from your account. The features are designed to help you make data-driven decisions faster.

Please explore the new dashboard and share any feedback through the in-app feedback tool.

Best regards,
Product Team

## Metadata
- Tone: Professional
- Urgency: Medium
- Recipients: Company-wide
```

---

## 📄 DESCRIPTIONS

### Product/Feature Description Template

```markdown
# Description: [Feature/Product Name]

## Short Version (20-30 words)
"[One sentence capturing the essence and value]"

## Medium Version (50-75 words)
"[What it is]. [Key benefit]. [How it works or what makes it unique]. [Target audience or use case]."

## Long Version (100-150 words)
"[Comprehensive description with context, features, benefits, and differentiators]"

## Keywords
[Relevant terms for SEO/searchability]
```

### Example

```markdown
# Description: Smart Analytics Dashboard

## Short Version
"Real-time analytics dashboard that transforms your data into actionable insights with AI-powered recommendations."

## Medium Version
"Smart Analytics Dashboard provides real-time visibility into your key metrics. Get AI-powered insights that highlight trends and anomalies automatically. Built for teams who need to make data-driven decisions quickly without complex analysis. Customizable views ensure everyone sees what matters most to them."

## Long Version
"Transform your raw data into strategic insights with our Smart Analytics Dashboard. This powerful tool combines real-time data processing with artificial intelligence to surface the metrics that matter most. Unlike traditional dashboards that simply display numbers, our solution actively analyzes patterns, detects anomalies, and provides actionable recommendations. Perfect for growth teams, product managers, and executives who need to make informed decisions quickly. Features customizable widgets, automated reports, and seamless integrations with your existing tools."

## Keywords
analytics, dashboard, real-time, AI, insights, data visualization, metrics
```

---

## 🔔 NOTIFICATIONS

### In-App Notification Template

```markdown
# Notification: [Type]

## Message
"[Main message - 1 sentence]. [Optional action or detail]."

## Variants
- Success: "[Positive confirmation]"
- Warning: "[Alert with action]"
- Info: "[Neutral update]"
- Error: "[Problem with solution]"

## Display Properties
- Duration: [Temporary/Persistent]
- Action: [None/Button/Link]
- Priority: [Low/Normal/High]
```

### Examples

```markdown
# Notification: Save Status

## Message
"Your changes have been saved automatically."

## Variants
- Success: "All changes saved successfully."
- Warning: "Unable to save. Retrying..."
- Info: "Saving in progress..."
- Error: "Save failed. Please try again."

## Display Properties
- Duration: Temporary (3 seconds)
- Action: None
- Priority: Normal
```

---

## 📢 MARKETING COPY

### Marketing Message Template

```markdown
# Marketing Copy: [Campaign/Feature]

## Headline
"[Attention-grabbing statement - 5-10 words]"

## Subheadline
"[Supporting statement that elaborates - 10-15 words]"

## Body Copy
"[2-3 sentences expanding on value proposition and benefits]"

## Call to Action
"[Action verb + benefit - 3-5 words]"

## Variations
- A/B Test Version: "[Alternative approach]"
- Social Media: "[Condensed for platform]"
- Email: "[Personalized version]"
```

### Example

```markdown
# Marketing Copy: Premium Upgrade

## Headline
"Unlock Your Full Potential"

## Subheadline
"Get advanced features that help you work smarter, not harder"

## Body Copy
"Join thousands of professionals who've upgraded to Premium. Access unlimited projects, advanced analytics, and priority support. Transform the way you work with tools designed for growth."

## Call to Action
"Start Free Trial"

## Variations
- A/B Test Version: "Ready to Level Up?" 
- Social Media: "🚀 Go Premium and unlock unlimited projects, advanced analytics, and more!"
- Email: "Hi [Name], you're just one click away from Premium features..."
```

---

## 🎯 TEXT FORMATTING RULES

### General Guidelines

- ✅ **Clarity First:** Simple language over complex
- ✅ **Active Voice:** "You can..." not "It is possible to..."
- ✅ **Specific Actions:** "Click Save" not "Proceed"
- ✅ **Positive Framing:** "To continue, add..." not "Can't continue without..."
- ✅ **Consistent Tone:** Match brand voice
- ✅ **No Jargon:** Unless for technical audience
- ✅ **Scannable:** Key information upfront

### Length Guidelines

| Type | Ideal Length | Maximum |
|------|-------------|---------|
| Error Message | 1-2 sentences | 3 sentences |
| Button Label | 2-3 words | 4 words |
| Tooltip | 5-10 words | 15 words |
| Description | 2-4 sentences | 6 sentences |
| Email | 50-150 words | 250 words |
| Notification | 1 sentence | 2 sentences |

### Tone Matrix

| Audience | Formality | Examples |
|----------|-----------|----------|
| End Users | Friendly | "Let's get started!" |
| Developers | Technical | "API key required" |
| Enterprise | Professional | "Please contact your administrator" |
| Marketing | Engaging | "Discover what's possible" |

---

## 💬 Interactive Questions

Quick questions for text creation.

**Reference:** Full interactive flows → `Product Owner - Interactive Mode.md`

```markdown
1. "What type of text? [error/email/description/notification/marketing/other]"
2. "Context or where will this appear?"
3. [If error] "What went wrong and what should user do?"
4. [If email] "Purpose and recipient?"
5. [If description] "What are we describing?"
```

---

## 📦 Platform Integration

Text snippets rarely need platform integration, but available if needed.

**Reference:** Full integration details → `Product Owner - Platform Integration.md`

```markdown
📦 **Add to your workspace?**

1. **ClickUp** - As document or comment
2. **Skip** - Keep as artifact only (typical)

Which option? (1 or 2)
```

**Note:** Most users skip platform integration for text snippets (90% skip rate).

---

*Quick text creation with minimal complexity. All outputs as artifacts. Challenge mode rarely activated.*