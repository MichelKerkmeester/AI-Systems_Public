# MCP (Model Context Protocol) Documentation

## Table of Contents

- [Directory Structure](#directory-structure)
- [Overview](#overview)
- [What is MCP?](#what-is-mcp)
- [Available MCP Servers](#available-mcp-servers)
  - [Core MCP Servers](#core-mcp-servers)
  - [Memory System](#memory-system)
- [Common Patterns](#common-patterns)
  - [1. Tool Invocation](#1-tool-invocation)
  - [2. Resource Access](#2-resource-access)
  - [3. Chaining Operations](#3-chaining-operations)
- [Integration Guidelines](#integration-guidelines)
  - [Setup Process](#setup-process)
  - [Best Practices](#best-practices)
  - [Hook Integration](#hook-integration)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
  - [Debug Commands](#debug-commands)
  - [Getting Help](#getting-help)
## Directory Structure

```
mcp/
├── desktop-commander/
│   └── README.md # Overview and navigation
├── gemini/
│   └── README.md # Overview and navigation
├── github/
│   └── README.md # Overview and navigation
├── n8n/
│   └── README.md # Overview and navigation
├── sequential-thinking/
│   └── README.md # Overview and navigation
└── README.md # Overview and navigation
```

## Overview

This directory contains documentation for all MCP servers integrated with Claude Code, providing extended capabilities for development, automation, and integration with external services.

## What is MCP?

Model Context Protocol (MCP) is a standardized protocol that allows Claude to interact with external tools and services. MCP servers act as bridges between Claude and various systems, providing:

- **Extended Capabilities**: Access to tools beyond Claude's built-in functionality
- **Service Integration**: Connect to GitHub, databases, APIs, and more
- **Custom Tools**: Create specialized tools for your workflow
- **Resource Access**: Read from external data sources

## Available MCP Servers

### Core MCP Servers

1. **[Sequential Thinking](./sequential-thinking/)** 
   - Structured problem-solving and decision-making
   - Step-by-step reasoning with metadata
   - Thought export/import capabilities

2. **[Gemini](./gemini/)**
   - Quick AI-powered code analysis
   - Codebase understanding
   - Pattern recognition

3. **[GitHub](./github/)**
   - Repository management
   - Issue and PR operations
   - Workflow automation

4. **[n8n](./n8n/)**
   - Workflow automation
   - API integrations
   - Data processing pipelines

5. **[Desktop Commander](./desktop-commander/)** *(Optional)*
   - File system operations
   - Process management
   - Enhanced CLI capabilities

### Memory System

6. **[Graphiti](../graphiti/)**
   - Knowledge graph management
   - Context persistence
   - Memory retrieval
   *(Note: Graphiti documentation is maintained separately)*

## Common Patterns

### 1. Tool Invocation
```python
# MCP tools are called like any other tool
result = mcp__github__create_issue(
    owner="user",
    repo="project",
    title="Bug report",
    body="Description"
)
```

### 2. Resource Access
```python
# List available resources
resources = ListMcpResourcesTool(server="github")

# Read specific resource
content = ReadMcpResourceTool(
    server="github",
    uri="github://repos/user/project"
)
```

### 3. Chaining Operations
```python
# Example: Create issue, then assign it
issue = mcp__github__create_issue(...)
mcp__github__update_issue(
    issue_number=issue["number"],
    assignees=["username"]
)
```

## Integration Guidelines

### Setup Process
1. **Installation**: Each MCP has specific installation requirements
2. **Configuration**: Usually involves API keys or credentials
3. **Activation**: Some MCPs require Claude restart (desktop only)
4. **Verification**: Test basic operations to ensure connectivity

### Best Practices
- **Error Handling**: Always handle MCP failures gracefully
- **Rate Limiting**: Respect API limits of integrated services
- **Caching**: Use MCP caching features when available
- **Security**: Never hardcode credentials in scripts

### Hook Integration
MCPs work seamlessly with the hook system:
```python
# In a hook
if self.should_use_github():
    mcp__github__create_issue(...)
```

## Troubleshooting

### Common Issues

1. **MCP Not Available**
   - Check if MCP is listed in settings
   - Verify installation completed
   - Desktop app: May need restart

2. **Authentication Failures**
   - Verify API keys/tokens are correct
   - Check token permissions
   - Ensure credentials are not expired

3. **Rate Limiting**
   - Implement exponential backoff
   - Cache results when possible
   - Use batch operations

4. **Connection Errors**
   - Check network connectivity
   - Verify service URLs
   - Check firewall/proxy settings

### Debug Commands
```bash
# List all MCP resources
/logic mcp list

# Test specific MCP
/logic mcp test github

# Check MCP status
/logic mcp status
```

### Getting Help
- Individual MCP docs have specific troubleshooting
- Check service-specific error messages
- Use `/logic help mcp` for general MCP help

---

*For Graphiti memory system documentation, see [../graphiti/](../graphiti/)*
*For general Claude Code help, see [../logic/](../logic/)*