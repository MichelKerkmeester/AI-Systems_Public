# Product Owner - Template: Doc Mode - v0.102

## 📋 TABLE OF CONTENTS

1. [📚 DOC MODE OVERVIEW](#1-📚-doc-mode-overview)
2. [📊 DOCUMENTATION TYPES](#2-📊-documentation-types)
3. [📝 USER GUIDE TEMPLATE](#3-📝-user-guide-template)
4. [🔧 TECHNICAL DOCUMENTATION TEMPLATE](#4-🔧-technical-documentation-template)
5. [📖 API DOCUMENTATION TEMPLATE](#5-📖-api-documentation-template)
6. [✏️ DOCUMENT FORMATTING MODE](#6-✏️-document-formatting-mode)
7. [🎨 FORMATTING STANDARDS](#7-🎨-formatting-standards)
8. [💬 INTERACTIVE QUESTIONS](#8-💬-interactive-questions)

---

## 1. 📚 DOC MODE OVERVIEW

### COMMAND: `$doc`

- **Purpose:** Create documentation or format existing text
- **Output:** Always as artifact
- **Thinking Rounds:** 6-10
- **Challenge Activation:** 6+ rounds (for complexity)
- **Two Modes:**
  - **Creation:** Write new documentation
  - **Formatting:** Clean up and structure existing text

---

## 2. 📊 DOCUMENTATION TYPES

### SUPPORTED FORMATS
| Type | Use Case | Typical Length |
|------|----------|----------------|
| **User Guide** | End-user instructions | 2-10 pages |
| **Technical Docs** | Developer/API docs | 5-20 pages |
| **API Reference** | Endpoint documentation | Variable |
| **README** | Project overview | 1-3 pages |
| **Tutorial** | Step-by-step guide | 3-8 pages |
| **FAQ** | Questions & answers | 2-5 pages |
| **Formatted** | Clean up existing | Same as input |

### FORMATTING LEVELS (FOR EXISTING TEXT)
| Level | Changes Applied | Use When |
|-------|----------------|----------|
| **Minimal** | Headers, bullets, emphasis | Quick cleanup |
| **Standard** | Structure, TOC, sections | Full organization |
| **Deep** | Complete rewrite, restructure | Major overhaul |

---

## 3. 📝 USER GUIDE TEMPLATE

```markdown
# [Product Name] User Guide

## TABLE OF CONTENTS
- [Getting Started](#getting-started)
- [Key Features](#key-features)
- [Basic Usage](#basic-usage)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)
- [Support](#support)

---

## GETTING STARTED

### WHAT IS [PRODUCT NAME]?
[Brief description of the product and its value proposition]

### SYSTEM REQUIREMENTS
- Requirement 1
- Requirement 2
- Requirement 3

### INSTALLATION
1. Step one with clear instructions
2. Step two with any important notes
3. Step three with verification

---

## KEY FEATURES

### FEATURE 1: [NAME]
**What it does:** [Description]
**Why use it:** [Value proposition]
**How to access:** [Navigation path]

### FEATURE 2: [NAME]
**What it does:** [Description]
**Why use it:** [Value proposition]
**How to access:** [Navigation path]

---

## BASIC USAGE

### TASK 1: [COMMON TASK]

1. **Open the application**
   - Click on [icon/menu]
   - Navigate to [location]

2. **Select your option**
   - Choose from [list]
   - Configure [settings]

3. **Complete the action**
   - Click [button]
   - Verify [result]

💡 **Tip:** [Helpful hint for this task]

### TASK 2: [ANOTHER COMMON TASK]

1. **Navigate to [section]**
2. **Input your data**
3. **Save your work**

⚠️ **Important:** [Critical information]

---

## ADVANCED FEATURES

### CUSTOMIZATION OPTIONS
- **Themes:** How to change appearance
- **Settings:** Configuration options
- **Shortcuts:** Keyboard combinations

### INTEGRATION CAPABILITIES
- **Export options:** Available formats
- **Import features:** Supported file types
- **API access:** For developers

---

## TROUBLESHOOTING

### COMMON ISSUES

**Problem:** [Description]
**Solution:** [Step-by-step fix]

**Problem:** [Description]
**Solution:** [Step-by-step fix]

### ERROR MESSAGES

| Error | Meaning | Solution |
|-------|---------|----------|
| Error 101 | [Description] | [Fix] |
| Error 202 | [Description] | [Fix] |

---

## SUPPORT

### CONTACT INFORMATION
- **Email:** support@example.com
- **Phone:** 1-800-EXAMPLE
- **Hours:** Monday-Friday, 9am-5pm EST

### ADDITIONAL RESOURCES
- [Knowledge Base](link)
- [Video Tutorials](link)
- [Community Forum](link)

---

**Document Version:** 1.0
**Last Updated:** [Date]
**Next Review:** [Date]
```

---

## 5. 🔧 TECHNICAL DOCUMENTATION TEMPLATE

```markdown
# [System/Component] Technical Documentation

## TABLE OF CONTENTS
- [Overview](#overview)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Development](#development)
- [Deployment](#deployment)
- [Monitoring](#monitoring)

---

## OVERVIEW

### PURPOSE
[Technical description of what this system/component does]

### KEY COMPONENTS
1. **Component A:** [Description]
2. **Component B:** [Description]
3. **Component C:** [Description]

### DEPENDENCIES
- Dependency 1 (version)
- Dependency 2 (version)
- Dependency 3 (version)

---

## ARCHITECTURE

### SYSTEM DESIGN
```
┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Server    │
└─────────────┘     └─────────────┘
       │                   │
       ▼                   ▼
┌─────────────┐     ┌─────────────┐
│    Cache    │     │   Database  │
└─────────────┘     └─────────────┘
```

### DATA FLOW
1. Request initiated from client
2. Server processes request
3. Database query executed
4. Response formatted
5. Cache updated
6. Response sent to client

---

## INSTALLATION

### PREREQUISITES
```bash
# Check Node version
node --version  # Should be 16+

# Check npm version
npm --version   # Should be 8+
```

### SETUP STEPS
```bash
# Clone repository
git clone https://github.com/example/repo.git

# Install dependencies
npm install

# Configure environment
cp .env.example .env

# Run migrations
npm run migrate

# Start development server
npm run dev
```

---

## CONFIGURATION

### ENVIRONMENT VARIABLES
```env
# Application
APP_NAME=MyApp
APP_ENV=development
APP_PORT=3000

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
DB_USER=admin
DB_PASS=secret

# Cache
REDIS_HOST=localhost
REDIS_PORT=6379
```

### CONFIGURATION FILE
```json
{
  "app": {
    "name": "MyApp",
    "version": "1.0.0",
    "debug": true
  },
  "features": {
    "authentication": true,
    "caching": true,
    "logging": true
  }
}
```

---

## API REFERENCE

### AUTHENTICATION
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secretpass"
}

Response: 200 OK
{
  "token": "jwt_token_here",
  "user": { ... }
}
```

### ENDPOINTS

#### GET /api/users
Retrieve list of users

**Parameters:**
- `page` (integer): Page number
- `limit` (integer): Items per page

**Response:**
```json
{
  "data": [...],
  "pagination": { ... }
}
```

---

## DEVELOPMENT

### LOCAL SETUP
```bash
# Install dev dependencies
npm install --save-dev

# Run tests
npm test

# Run linter
npm run lint

# Build for production
npm run build
```

### CODING STANDARDS
- Use ESLint configuration
- Follow conventional commits
- Write tests for new features
- Document all public APIs

---

## DEPLOYMENT

### PRODUCTION BUILD
```bash
# Build application
npm run build

# Run production server
npm run start:prod
```

### DOCKER DEPLOYMENT
```dockerfile
FROM node:16-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

---

## MONITORING

### HEALTH CHECK
```http
GET /health

Response: 200 OK
{
  "status": "healthy",
  "uptime": 3600,
  "version": "1.0.0"
}
```

### METRICS
- **Response Time:** < 200ms p95
- **Error Rate:** < 0.1%
- **Uptime:** > 99.9%

### LOGGING
```javascript
// Log levels
logger.debug('Debug message');
logger.info('Info message');
logger.warn('Warning message');
logger.error('Error message');
```

---

**Documentation Version:** 1.0
**API Version:** v1
**Last Updated:** [Date]
```

---

## 6. 📖 API DOCUMENTATION TEMPLATE

```markdown
# [API Name] Documentation

## TABLE OF CONTENTS
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Base URL](#base-url)
- [Rate Limiting](#rate-limiting)
- [Endpoints](#endpoints)
- [Error Handling](#error-handling)
- [Examples](#examples)

---

## INTRODUCTION

### API OVERVIEW
[Description of what the API does and its main features]

### GETTING STARTED
1. Register for an API key
2. Include key in requests
3. Make your first call

---

## AUTHENTICATION

### API KEY AUTHENTICATION
```http
GET /api/resource
Authorization: Bearer YOUR_API_KEY
```

### OAUTH 2.0
```http
POST /oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id=YOUR_CLIENT_ID
&client_secret=YOUR_CLIENT_SECRET
```

---

## BASE URL

### ENVIRONMENTS
| Environment | URL |
|------------|-----|
| Production | `https://api.example.com/v1` |
| Staging | `https://staging-api.example.com/v1` |
| Development | `http://localhost:3000/v1` |

---

## RATE LIMITING

### LIMITS
- **Standard:** 100 requests/minute
- **Premium:** 1000 requests/minute
- **Enterprise:** Unlimited

### HEADERS
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1623456789
```

---

## ENDPOINTS

### RESOURCES

#### CREATE RESOURCE
```http
POST /api/resources
Content-Type: application/json

{
  "name": "Resource Name",
  "type": "resource_type",
  "metadata": {}
}
```

**Response: 201 Created**
```json
{
  "id": "res_123",
  "name": "Resource Name",
  "type": "resource_type",
  "metadata": {},
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### GET RESOURCE
```http
GET /api/resources/{id}
```

**Response: 200 OK**
```json
{
  "id": "res_123",
  "name": "Resource Name",
  "type": "resource_type",
  "metadata": {},
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### UPDATE RESOURCE
```http
PATCH /api/resources/{id}
Content-Type: application/json

{
  "name": "Updated Name"
}
```

**Response: 200 OK**
```json
{
  "id": "res_123",
  "name": "Updated Name",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### DELETE RESOURCE
```http
DELETE /api/resources/{id}
```

**Response: 204 No Content**

---

## ERROR HANDLING

### ERROR RESPONSE FORMAT
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource was not found",
    "details": {
      "resource_id": "res_123"
    }
  }
}
```

### COMMON ERROR CODES
| Code | HTTP Status | Description |
|------|------------|-------------|
| `INVALID_REQUEST` | 400 | Request validation failed |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Access denied |
| `NOT_FOUND` | 404 | Resource not found |
| `RATE_LIMITED` | 429 | Too many requests |
| `SERVER_ERROR` | 500 | Internal server error |

---

## EXAMPLES

### JAVASCRIPT
```javascript
const response = await fetch('https://api.example.com/v1/resources', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  }
});

const data = await response.json();
console.log(data);
```

### PYTHON
```python
import requests

headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

response = requests.get(
    'https://api.example.com/v1/resources',
    headers=headers
)

data = response.json()
print(data)
```

### CURL
```bash
curl -X GET https://api.example.com/v1/resources \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

---

**API Version:** v1
**Documentation Version:** 1.0
**Last Updated:** [Date]
```

---

## 7. ✏️ DOCUMENT FORMATTING MODE

### FORMATTING PROCESS
```markdown
User: $doc format my requirements document

System: I'll format your existing document. 📚

**How many thinking rounds should I use? (6-10)**

For document formatting, I recommend: 6 rounds
- Structure analysis and organization
- Clean formatting application

Your choice?

[WAIT FOR USER INPUT]

User: 6

System: Perfect! For formatting:

Which level of formatting would you prefer?
- **Minimal:** Headers, bullets, light emphasis (recommended)
- **Standard:** Full structure with TOC, sections
- **Deep:** Complete reorganization and rewrite

Your choice? (minimal/standard/deep)

[WAIT FOR USER RESPONSE]

User: minimal

System: Great! Please paste your document and I'll apply minimal formatting.

[USER PASTES DOCUMENT]

[SYSTEM FORMATS WITH:]
- Clear headers
- Organized bullets
- Proper emphasis
- Clean spacing
- Logical flow
```

### MINIMAL FORMATTING EXAMPLE
```markdown
# INPUT (UNFORMATTED):
project requirements
we need a login system that works with email and password
users should be able to reset passwords
admin users need different permissions
the system should remember users
security is important
use modern standards

# OUTPUT (MINIMAL FORMATTING):

# Project Requirements

## Authentication System

### Core Features
- **Email/password login** - Standard authentication flow
- **Password reset** - Self-service password recovery
- **Remember me** - Persistent sessions for returning users

### User Roles
- **Standard users** - Basic access permissions
- **Admin users** - Extended permissions and controls

### Security Requirements
- Modern authentication standards
- Secure password storage
- Session management
- HTTPS enforcement
```

### STANDARD FORMATTING EXAMPLE
```markdown
# [Adds complete structure with TOC, detailed sections, and subsections]
```

### DEEP FORMATTING EXAMPLE
```markdown
# [Complete rewrite with enhanced clarity, professional structure, and comprehensive organization]
```

---

## 8. 🎨 FORMATTING STANDARDS

### DOCUMENT STRUCTURE
1. **Title:** Clear and descriptive
2. **Table of Contents:** For documents > 3 sections
3. **Sections:** Logical grouping
4. **Subsections:** 2-3 levels maximum
5. **Conclusion:** Summary or next steps

### TEXT FORMATTING
- **Headers:** Hierarchical (H1 → H2 → H3)
- **Emphasis:** Bold for key terms, italic for examples
- **Lists:** Bullets for unordered, numbers for sequential
- **Code:** Backticks for inline, blocks for multi-line
- **Links:** Descriptive text, not raw URLs

### VISUAL ELEMENTS
- **Tables:** For comparative data
- **Diagrams:** ASCII art or mermaid
- **Callouts:** Tips, warnings, notes
- **Dividers:** Between major sections
- **Spacing:** Consistent throughout

### TONE & STYLE
- **Professional:** Clear and concise
- **Consistent:** Same voice throughout
- **Active voice:** Preferred over passive
- **Present tense:** For current state
- **Future tense:** For plans/roadmap

---

## 9. 💬 INTERACTIVE QUESTIONS

### CREATION MODE FLOW
```markdown
User: $doc user guide for auth system

System: Let's create your authentication system user guide! 📚

**How many thinking rounds should I use? (6-10)**

Based on user guide complexity, I recommend: 7 rounds
- Comprehensive coverage needed
- Multiple user flows
- Security considerations

Your choice?

[WAIT FOR USER INPUT]

User: 7

System: Good choice! Let me clarify the scope:

1. **Target audience?** (end-users/developers/both)
2. **Include screenshots?** (yes/no/placeholders)
3. **Technical depth?** (basic/intermediate/advanced)

[WAIT FOR ANSWERS]

User:
1. end-users
2. placeholders
3. basic

[SYSTEM CREATES USER-FRIENDLY GUIDE WITH PLACEHOLDER IMAGES]
```

### FORMATTING MODE FLOW
```markdown
User: $doc format [pastes messy text]

System: I'll help format your document! 📚

**How many thinking rounds should I use? (6-10)**

For this formatting task, I recommend: 6 rounds
- Text organization
- Structure improvement

Your choice?

[WAIT FOR USER INPUT]

User: 6

System: Which formatting level?
- **Minimal:** Light touch-up
- **Standard:** Full structure
- **Deep:** Complete rewrite

Your choice?

[WAIT FOR USER RESPONSE]

[THEN FORMATS ACCORDING TO SELECTION]
```

### DETECTION PATTERNS
```python
def detect_doc_type(request):
    """Auto-detect documentation type needed"""

    doc_types = {
        'user_guide': ['guide', 'manual', 'how to', 'tutorial'],
        'technical': ['api', 'developer', 'technical', 'implementation'],
        'readme': ['readme', 'overview', 'introduction'],
        'format': ['format', 'clean up', 'structure', 'organize']
    }

    request_lower = request.lower()
    for doc_type, keywords in doc_types.items():
        if any(k in request_lower for k in keywords):
            return doc_type

    return 'user_guide'  # Default
```

---

*All documentation delivered as artifacts. Support both creation and formatting modes. Always ask thinking rounds and wait. For formatting, ask level preference. Use clear structure and professional tone. Include all necessary sections for completeness.*
