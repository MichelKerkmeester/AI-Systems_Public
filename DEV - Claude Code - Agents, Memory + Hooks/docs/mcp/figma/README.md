# Figma MCP Documentation

## Overview

The Figma MCP server enables direct integration with Figma designs, allowing Claude to generate UI code from Figma components, extract design tokens, and maintain consistency between design and implementation.

## Key Features

- **Code Generation**: Convert Figma designs to production code
- **Design Tokens**: Extract colors, typography, spacing values
- **Component Mapping**: Link Figma components to code implementations
- **Image Export**: Get visual references of designs
- **Design System Rules**: Generate consistent coding patterns

## Available Tools

### 1. `mcp__figma-dev-mode-mcp-server__get_code`
Generate UI code from a Figma node.

**Parameters:**
- `nodeId`: The Figma node ID (e.g., "123:456" or "123-456")
- `clientFrameworks`: Comma-separated frameworks (e.g., "react,typescript")
- `clientLanguages`: Programming languages (e.g., "javascript,css")
- `clientName`: MCP client name (e.g., "claude code")

**Example:**
```python
{
    "nodeId": "123:456",
    "clientFrameworks": "react,tailwind",
    "clientLanguages": "typescript,css",
    "clientName": "claude code"
}
```

**Note:** Always call `get_image` after this to get visual context.

### 2. `mcp__figma-dev-mode-mcp-server__get_variable_defs`
Get design token definitions from a node.

**Parameters:**
- `nodeId`: The Figma node ID
- `clientFrameworks`: Framework context
- `clientLanguages`: Language context
- `clientName`: Client identifier

**Returns:**
Variable definitions like:
```json
{
    "colors/primary": "#FF6B6B",
    "spacing/medium": "16px",
    "typography/heading": "32px bold Inter"
}
```

### 3. `mcp__figma-dev-mode-mcp-server__get_code_connect_map`
Get component-to-code mappings.

**Parameters:**
- `nodeId`: The Figma node ID
- `clientFrameworks`: Framework context
- `clientLanguages`: Language context
- `clientName`: Client identifier

**Returns:**
```json
{
    "1:2": {
        "codeConnectSrc": "https://github.com/project/components/Button.tsx",
        "codeConnectName": "Button"
    }
}
```

### 4. `mcp__figma-dev-mode-mcp-server__get_image`
Get a visual preview of the design.

**Parameters:**
- `nodeId`: The Figma node ID
- `clientFrameworks`: Framework context
- `clientLanguages`: Language context
- `clientName`: Client identifier

**Important:** Always use after `get_code` for visual context.

### 5. `mcp__figma-dev-mode-mcp-server__create_design_system_rules`
Generate design system documentation.

**Parameters:**
- `clientFrameworks`: Target frameworks
- `clientLanguages`: Target languages
- `clientName`: Client identifier

## Usage Workflow

### Converting a Design to Code

1. **Extract Node ID from URL**
   ```
   URL: https://figma.com/design/abc123/MyDesign?node-id=45-678
   Node ID: 45:678
   ```

2. **Generate Code**
   ```python
   get_code(nodeId="45:678", clientFrameworks="react,tailwind")
   ```

3. **Get Visual Reference**
   ```python
   get_image(nodeId="45:678")  # Always do this!
   ```

4. **Extract Design Tokens**
   ```python
   get_variable_defs(nodeId="45:678")
   ```

### Working with Component Libraries

1. **Get Component Mappings**
   ```python
   get_code_connect_map(nodeId="component-id")
   ```

2. **Check Existing Implementation**
   - Use returned GitHub URLs to find existing code
   - Maintain consistency with established patterns

3. **Generate Missing Components**
   - Use `get_code` for components without mappings
   - Follow design system rules

## Best Practices

### 1. Always Get Visual Context
```python
# ❌ Wrong: Code without visual reference
code = get_code(nodeId="123:456")

# ✅ Right: Code with visual verification
code = get_code(nodeId="123:456")
image = get_image(nodeId="123:456")
```

### 2. Framework-Specific Generation
```python
# React + TypeScript + Tailwind
{
    "clientFrameworks": "react,tailwind",
    "clientLanguages": "typescript,css"
}

# Vue + JavaScript + CSS
{
    "clientFrameworks": "vue",
    "clientLanguages": "javascript,css"
}
```

### 3. Maintain Design Tokens
```python
# Extract tokens first
tokens = get_variable_defs(nodeId="root-node")

# Use in generated code
const colors = {
    primary: tokens["colors/primary"],
    secondary: tokens["colors/secondary"]
}
```

### 4. Component Reusability
- Check `get_code_connect_map` before creating new components
- Reuse existing implementations when available
- Update mappings when creating new components

## Integration with Webflow

When working with Webflow projects:

1. **Extract Figma Design Tokens**
   ```python
   tokens = get_variable_defs(nodeId="design-system-node")
   ```

2. **Convert to CSS Variables**
   ```css
   :root {
       --color-primary: #FF6B6B;
       --spacing-medium: 1rem;
   }
   ```

3. **Apply to Webflow Components**
   ```css
   [data-component="button"] {
       background-color: var(--color-primary);
       padding: var(--spacing-medium);
   }
   ```

## Common Patterns

### Responsive Component Generation
```python
# Get desktop version
desktop_code = get_code(nodeId="desktop-variant")

# Get mobile version
mobile_code = get_code(nodeId="mobile-variant")

# Combine with responsive CSS
```

### Design System Extraction
```python
# 1. Get root design system node
system_rules = create_design_system_rules()

# 2. Extract all tokens
tokens = get_variable_defs(nodeId="system-root")

# 3. Generate token files
# - colors.css
# - typography.css
# - spacing.css
```

### Component Library Setup
```python
# 1. Map all components
mappings = get_code_connect_map(nodeId="component-library")

# 2. Generate missing components
for component in missing_components:
    code = get_code(nodeId=component.id)
    image = get_image(nodeId=component.id)
```

## Troubleshooting

### Node ID Issues
- Ensure ID format: "123:456" or "123-456"
- Extract from Figma URL correctly
- Check if node exists and is accessible

### Code Generation Problems
- Verify framework/language parameters
- Check if design is properly structured
- Ensure Dev Mode is enabled in Figma

### Missing Design Tokens
- Confirm variables are defined in Figma
- Check token scope (file vs team library)
- Verify node has access to variables

## Tips for Optimal Usage

1. **Batch Operations**: Get all related nodes in sequence
2. **Cache Design Tokens**: Store frequently used tokens
3. **Version Control**: Track component mappings in git
4. **Visual QA**: Always compare generated code with design
5. **Progressive Enhancement**: Start with basic structure, add interactions

## Related Documentation
- [Webflow Integration](../webflow/README.md)
- [CSS Best Practices](../../scripts/css-best-practices.md)
- [Component Architecture](../../technical/component-architecture.md)