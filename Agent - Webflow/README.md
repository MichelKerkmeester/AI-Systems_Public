# Webflow Agent - User Guide v0.400

The Webflow Agent is a full-stack development assistant that creates and manages Webflow sites through natural language. With Designer and Data API integration, it can build complete structures, design components, and manage content - transforming ideas into functioning Webflow sites.

## 📋 Table of Contents

- [🆕 What's New in v0.400](#whats-new-in-v0400)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🧠 How It Works](#how-it-works)
- [💬 Example Interactions](#example-interactions)
- [📊 What Gets Created](#what-gets-created)
- [🔧 Installing Webflow MCP](#installing-webflow-mcp)
- [🎨 Designer API Setup](#designer-api-setup)
- [🆘 Troubleshooting](#troubleshooting)
- [⚠️ Important Notes](#important-notes)
- [📦 Version History](#version-history)
- [📚 Resources](#resources)

---

## 🆕 What's New in v0.400

### Complete Transformation
- **Full Designer API Integration**: Create elements, styles, and components directly
- **Structure Creation**: Build collections and fields programmatically
- **Component Systems**: Design reusable components with variants
- **Responsive Design**: Control breakpoints and responsive behavior
- **Design Tokens**: Manage variables for consistent design systems

### Designer + Data API Coordination
- Create complete features from structure to design
- Build data-driven components
- Design responsive layouts with dynamic content
- Establish design systems with content management

### What Changed from v0.300
- ✅ **CAN NOW** create fields and collections
- ✅ **CAN NOW** build page structures
- ✅ **CAN NOW** create and apply styles
- ✅ **CAN NOW** register components
- ⚠️ **STILL** requires external URLs for images
- ⚠️ **REQUIRES** MCP Bridge App for Designer operations

---

## ✨ Key Features

### Complete Development Capabilities

**Designer API Features (NEW):**
- **Element Creation**: Build any element type on canvas
- **Style Management**: Create and apply CSS classes
- **Component Building**: Design reusable components
- **Responsive Control**: Manage breakpoints and layouts
- **Variable System**: Create design tokens
- **Real-time Preview**: See changes instantly in Designer

**Data API Features (Enhanced):**
- **Collection Creation**: Build complete data structures
- **Field Management**: Add any field type to collections
- **Relationship Design**: Create references between collections
- **Content Operations**: Full CRUD on items
- **Publishing Control**: Manage draft/live states
- **SEO Optimization**: Meta tags and structured data

**Integrated Workflows:**
- Create blog with structure and templates
- Build e-commerce catalogs with components
- Design landing pages with dynamic content
- Establish complete design systems
- Develop responsive layouts
- Manage multi-language sites

### Remaining Limitations
- ⚠️ **Image uploads** require external URLs (Cloudinary, S3)
- ⚠️ **Companion app** required for Designer operations
- ⚠️ **Authorization** requires owner/admin access

---

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Webflow Agent"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - Webflow - v0.400.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 6 essential documents to your project:
- `Agent - MCP - Webflow - v0.400.md` (Main agent)
- `Webflow - MCP Knowledge - v0.300.md` (Full API knowledge)
- `Webflow - Interactive Intelligence - v0.300.md` (Conversation patterns)
- `Webflow - Patterns & Workflows - v0.300.md` (Development patterns)
- `Webflow - ATLAS Thinking Framework - v0.300.md` (Adaptive thinking)
- `README.md` (This guide)

### Step 4: Install Webflow MCP Server
Follow the installation guide in the [Installing Webflow MCP](#installing-webflow-mcp) section below.

### Step 5: Setup Designer Access
1. Open your site in Webflow Designer
2. Press 'E' to open Apps panel
3. Launch "Webflow MCP Bridge App"
4. Keep it open for Designer operations

### Step 6: Start Building!
You can now:
```
Create complete blog with categories
Build hero component with animations
Design responsive navigation
Setup e-commerce catalog
Create design system
Build landing pages
```

---

## 🧠 How It Works

### Full Stack Development Flow

The system coordinates Designer and Data APIs to create complete Webflow features:

| Request Type | APIs Used | Creates | Time |
|--------------|-----------|---------|------|
| **"Create blog"** | Data | Collections, fields, relationships | 10-15s |
| **"Build hero"** | Designer | Elements, styles, component | 10-12s |
| **"Design page"** | Both | Structure + visual design | 20-30s |
| **"Setup e-commerce"** | Both | Products + components | 30-45s |

### Capability Matrix

**Immediate Execution:**
```
User: "Create product catalog"
System: "Creating product structure...
✅ Products collection created
✅ 12 fields added
✅ Categories linked
✅ Ready for content!"
```

**Designer Operations (App Required):**
```
User: "Build card component"
System: "Checking Designer connection...
✅ MCP Bridge App connected
Creating card component...
✅ Elements structured
✅ Styles applied
✅ Component registered!"
```

**Full Stack Coordination:**
```
User: "Create blog with templates"
System: "Building complete blog system...
Data: ✅ Collections created
Design: ✅ Components built
Integration: ✅ Connected
Ready for content!"
```

---

## 💬 Example Interactions

### Creating Complete Structures
```
User: Create a team directory with profiles

System: How many thinking rounds should I use? (1-10)
Recommended: 5 rounds (structure + components)

User: 5

System: Creating team directory system!

Data Structure:
✅ Team Members collection created:
   - name, role, bio
   - profile_image (URL)
   - email, phone
   - department (reference)
   - social_links

✅ Departments collection created
✅ Relationships configured

Design Components:
✅ Team card component created
✅ Profile layout designed
✅ Responsive grid applied

Ready to add team members!
```

### Building Design Systems
```
User: Create a design system with typography and colors

System: Building design system...

Typography Scale:
✅ 8 heading styles created
✅ 3 body text styles
✅ Responsive sizing applied

Color System:
✅ Primary palette (5 shades)
✅ Secondary palette (5 shades)
✅ Neutral scale (10 shades)
✅ Semantic colors (success, warning, error)

✅ Variables registered
✅ Styles ready to apply

Design system complete!
```

### Full Page Development
```
User: Design a landing page with hero, features, and testimonials

System: Creating complete landing page...

Structure:
✅ Features collection created
✅ Testimonials collection created
✅ Fields configured

Components:
✅ Hero section with CTA
✅ 3-column feature grid
✅ Testimonial carousel
✅ Responsive breakpoints

Styling:
✅ Consistent design tokens
✅ Hover interactions
✅ Mobile optimization

Page ready for content!
Time: 35 seconds
```

---

## 📊 What Gets Created

### Blog System Example
```javascript
// Data Structure Created
Collections: {
  BlogPosts: {
    fields: ['title', 'content', 'excerpt', 'featured_image', 
             'author', 'categories', 'published_date', 'meta_fields']
  },
  Authors: {
    fields: ['name', 'bio', 'avatar', 'social_links']
  },
  Categories: {
    fields: ['name', 'slug', 'description']
  }
}

// Components Created
Components: {
  BlogCard: 'Responsive card with image, title, excerpt',
  AuthorBio: 'Author information block',
  CategoryFilter: 'Dynamic filtering component'
}

// Styles Applied
Styles: {
  Typography: 'Complete scale from h1 to body',
  Colors: 'Brand palette with semantic colors',
  Layout: 'Grid system with responsive breakpoints'
}
```

### Performance Metrics
- Collection creation: 3-5 seconds
- Field addition: 1-2 seconds per field
- Component building: 5-10 seconds
- Style application: 1-2 seconds
- Full feature: 20-45 seconds

---

## 🔧 Installing Webflow MCP

### Recommended: OAuth Remote Setup

Add to Claude Desktop config:

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "webflow": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.webflow.com/sse"]
    }
  }
}
```

After saving:
1. Restart Claude Desktop (Cmd/Ctrl + R)
2. Browser opens for OAuth authorization
3. Authorize the sites you want to access
4. MCP Bridge App auto-installs to authorized sites

### Alternative: Token-Based Setup

```json
{
  "mcpServers": {
    "webflow": {
      "command": "npx",
      "args": ["-y", "@webflow/mcp-server"],
      "env": {
        "WEBFLOW_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

Get your token from [Webflow API Settings](https://webflow.com/dashboard/account/apps).

---

## 🎨 Designer API Setup

### Enabling Designer Operations

1. **Open Webflow Designer**
   - Navigate to your project
   - Open in Designer mode

2. **Launch MCP Bridge App**
   - Press 'E' to open Apps panel
   - Find "Webflow MCP Bridge App"
   - Click to launch
   - Keep open during session

3. **Verify Connection**
   - App shows "Connected" status
   - Agent confirms Designer access
   - Ready for visual operations

### Designer Capabilities
With the app connected, you can:
- Create any element type
- Apply styles and CSS
- Build components
- Manage responsive design
- Control animations
- Set interactions

---

## 🆘 Troubleshooting

### Common Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **"Cannot create elements"** | App disconnected | Open MCP Bridge App in Designer |
| **"Designer unavailable"** | App not running | Launch app from Apps panel |
| **"Cannot upload images"** | API limitation | Use Cloudinary/S3 URLs |
| **"Unauthorized"** | Not owner/admin | Get proper permissions |
| **"Rate limit hit"** | Too many requests | Wait 60 seconds |
| **"Collection exists"** | Duplicate name | Use unique names |

### Designer Connection Issues

**App Won't Connect:**
1. Refresh Designer
2. Re-launch MCP Bridge App
3. Check authorization status
4. Re-authenticate if needed

**Operations Failing:**
1. Verify app shows "Connected"
2. Check console for errors
3. Try simpler operation first
4. Restart app if needed

### Performance Tips
- Keep operations under 50 API calls/minute
- Batch similar operations
- Create structures before content
- Build components once, reuse many times

---

## ⚠️ Important Notes

### Full Stack Capabilities
- **Structure creation** - Collections, fields, relationships
- **Visual design** - Elements, styles, components
- **Content management** - Full CRUD operations
- **Publishing control** - Draft/live states
- **SEO optimization** - Meta tags, structured data
- **Responsive design** - Breakpoint management
- **Component systems** - Reusable design patterns
- **Design tokens** - Variables for consistency

### Requirements
- **MCP Bridge App** - Must be open for Designer operations
- **Authorization** - Owner/admin access required
- **External images** - URLs required (no direct upload)
- **Rate limits** - 60 requests per minute
- **Node.js** - Version 22.3.0+ for MCP server

### Best Practices
1. Create data structure first
2. Build reusable components
3. Apply consistent styles
4. Use design tokens
5. Plan responsive behavior
6. Optimize for performance
7. Include SEO from start

---

## 📦 Version History

### v0.400 (Current - Major Update)
- **Designer API integration** - Full visual development
- **Structure creation** - Collections and fields
- **Component building** - Reusable design systems
- **Style management** - CSS and design tokens
- **Complete transformation** - From content-only to full-stack

### v0.300 (Deprecated)
- Limited to content management only
- Could not create fields or structures
- Required Designer for all structure
- Many workarounds needed

### v0.200 (Deprecated)
- Initial reality-based approach
- Transparent about limitations
- Content management focus

### v0.100 (Deprecated)
- Initial release with incorrect claims

---

## 📚 Resources

### Essential Links
- [Webflow MCP Server](https://github.com/webflow/mcp-server) - Official repository
- [Designer API Docs](https://developers.webflow.com/designer/reference) - Designer capabilities
- [Data API Docs](https://developers.webflow.com/data/reference) - Data operations
- [MCP Protocol](https://modelcontextprotocol.io/) - Protocol documentation

### Quick References
- [Get API Token](https://webflow.com/dashboard/account/apps)
- [Webflow Designer](https://webflow.com/designer)
- [Claude Desktop](https://claude.ai/download)
- [Cloudinary](https://cloudinary.com/) - Image hosting

### API Capabilities

**Designer API:**
- Elements: Create, modify, position
- Styles: Classes, CSS, responsive
- Components: Build, register, reuse
- Variables: Design tokens, colors

**Data API:**
- Collections: Create with fields
- Items: Full CRUD operations
- Publishing: Draft/live control
- SEO: Meta tags, slugs

### Support
- [Webflow Support](https://support.webflow.com)
- [Developer Forum](https://forum.webflow.com)
- Email: developers@webflow.com

---

*Full-stack Webflow development through natural language. Create structures, design components, manage content. From idea to live site, all through conversation.*