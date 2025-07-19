# n8n MCP Documentation

## Table of Contents

- [Overview](#overview)
  - [Key Features](#key-features)
- [Connection Setup](#connection-setup)
  - [1. n8n Instance Requirements](#1-n8n-instance-requirements)
  - [2. Generate API Key](#2-generate-api-key)
  - [3. Configure MCP](#3-configure-mcp)
  - [4. Verify Connection](#4-verify-connection)
- [Workflow Examples](#workflow-examples)
  - [Basic HTTP Workflow](#basic-http-workflow)
  - [Slack Integration](#slack-integration)
  - [Database Operations](#database-operations)
- [Automation Patterns](#automation-patterns)
  - [1. Webhook Processing](#1-webhook-processing)
  - [2. Scheduled Tasks](#2-scheduled-tasks)
  - [3. AI Integration](#3-ai-integration)
- [Node Operations](#node-operations)
  - [Discovering Nodes](#discovering-nodes)
  - [Validating Configurations](#validating-configurations)
  - [Working with Templates](#working-with-templates)
- [Best Practices](#best-practices)
  - [1. Node Discovery](#1-node-discovery)
  - [2. Configuration Validation](#2-configuration-validation)
  - [3. Error Handling](#3-error-handling)
  - [4. Performance Optimization](#4-performance-optimization)
  - [5. AI Node Usage](#5-ai-node-usage)
## Overview

n8n MCP provides integration with n8n workflow automation platform, enabling creation and management of automated workflows, API integrations, and data processing pipelines.

### Key Features
- Access to 400+ integration nodes
- Workflow creation and management
- Node configuration validation
- Template library access
- AI-capable node identification
- Real-time workflow execution

## Connection Setup

### 1. n8n Instance Requirements
- n8n instance running (cloud or self-hosted)
- API access enabled
- API key generated

### 2. Generate API Key
In n8n:
1. Go to Settings → API
2. Create new API key
3. Copy the key

### 3. Configure MCP
```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-n8n"],
      "env": {
        "N8N_API_KEY": "${N8N_API_KEY}",
        "N8N_BASE_URL": "https://your-instance.n8n.cloud"
      }
    }
  }
}
```

### 4. Verify Connection
```python
# Test connection
stats = mcp__n8n__get_database_statistics()
print(f"Connected! {stats['total_nodes']} nodes available")
```

## Workflow Examples

### Basic HTTP Workflow
```python
# Find HTTP node
http_node = mcp__n8n__get_node_essentials(
    nodeType="nodes-base.httpRequest"
)

# Create workflow configuration
workflow = {
    "nodes": [
        {
            "name": "HTTP Request",
            "type": "nodes-base.httpRequest",
            "position": [250, 300],
            "parameters": {
                "method": "GET",
                "url": "https://api.example.com/data",
                "responseFormat": "json"
            }
        }
    ],
    "connections": {}
}

# Validate workflow
validation = mcp__n8n__validate_workflow(workflow=workflow)
```

### Slack Integration
```python
# Get Slack node info
slack_node = mcp__n8n__get_node_essentials(
    nodeType="nodes-base.slack"
)

# Configure Slack message
slack_config = {
    "name": "Send Slack Message",
    "type": "nodes-base.slack",
    "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#notifications",
        "text": "Deployment completed successfully!"
    }
}

# Validate configuration
validation = mcp__n8n__validate_node_operation(
    nodeType="nodes-base.slack",
    config=slack_config["parameters"]
)
```

### Database Operations
```python
# Search for database nodes
db_nodes = mcp__n8n__search_nodes(
    query="database postgres mysql",
    mode="OR"
)

# Get PostgreSQL node
postgres = mcp__n8n__get_node_for_task(
    task="query_database"
)

# Configure query
db_config = {
    "operation": "executeQuery",
    "query": "SELECT * FROM users WHERE active = true",
    "options": {
        "queryBatching": "transaction"
    }
}
```

## Automation Patterns

### 1. Webhook Processing
```python
# Create webhook workflow
webhook_workflow = {
    "nodes": [
        {
            "name": "Webhook",
            "type": "nodes-base.webhook",
            "position": [250, 300],
            "parameters": {
                "path": "github-webhook",
                "method": "POST"
            }
        },
        {
            "name": "Process Data",
            "type": "nodes-base.function",
            "position": [450, 300],
            "parameters": {
                "functionCode": """
                const payload = items[0].json;
                if (payload.action === 'opened') {
                    return [{
                        json: {
                            issue: payload.issue.number,
                            title: payload.issue.title,
                            notify: true
                        }
                    }];
                }
                return [];
                """
            }
        }
    ],
    "connections": {
        "Webhook": {
            "main": [[{"node": "Process Data", "type": "main", "index": 0}]]
        }
    }
}
```

### 2. Scheduled Tasks
```python
# Daily report workflow
scheduled_workflow = mcp__n8n__get_templates_for_task(
    task="scheduling"
)

# Find cron node
cron = mcp__n8n__search_nodes(
    query="cron schedule",
    mode="OR"
)

# Configure daily run
schedule_config = {
    "name": "Daily Trigger",
    "type": "nodes-base.cron",
    "parameters": {
        "cronExpression": "0 9 * * *"  # 9 AM daily
    }
}
```

### 3. AI Integration
```python
# List AI-capable nodes
ai_nodes = mcp__n8n__list_ai_tools()

# Get OpenAI node
openai = mcp__n8n__get_node_essentials(
    nodeType="nodes-base.openAi"
)

# Configure AI task
ai_config = {
    "resource": "text",
    "operation": "complete",
    "model": "gpt-4",
    "prompt": "Analyze this customer feedback: {{$json.feedback}}",
    "maxTokens": 150
}
```

## Node Operations

### Discovering Nodes
```python
# List all trigger nodes
triggers = mcp__n8n__list_nodes(
    category="trigger",
    limit=200
)

# Search for specific functionality
email_nodes = mcp__n8n__search_nodes(
    query="email send gmail outlook",
    mode="OR"
)

# Get node documentation
docs = mcp__n8n__get_node_documentation(
    nodeType="nodes-base.gmail"
)
```

### Validating Configurations
```python
# Validate node configuration
validation = mcp__n8n__validate_node_operation(
    nodeType="nodes-base.httpRequest",
    config={
        "method": "POST",
        "url": "https://api.example.com",
        "sendBody": True,
        "bodyParameters": {
            "values": [
                {"name": "key", "value": "value"}
            ]
        }
    }
)

# Check for missing fields
minimal_check = mcp__n8n__validate_node_minimal(
    nodeType="nodes-base.slack",
    config={"resource": "message"}
)
```

### Working with Templates
```python
# Find templates for task
templates = mcp__n8n__get_templates_for_task(
    task="data_sync"
)

# Get specific template
template = mcp__n8n__get_template(
    templateId=templates[0]["id"]
)

# Search templates
chatbot_templates = mcp__n8n__search_templates(
    query="chatbot"
)
```

## Best Practices

### 1. Node Discovery
```python
# Always check node availability first
def ensure_node_exists(node_type):
    try:
        node = mcp__n8n__get_node_info(nodeType=node_type)
        return True
    except:
        return False
```

### 2. Configuration Validation
```python
# Validate before deployment
def safe_workflow_create(workflow):
    # Validate entire workflow
    validation = mcp__n8n__validate_workflow(
        workflow=workflow,
        options={"validateNodes": True}
    )
    
    if validation["valid"]:
        return create_workflow(workflow)
    else:
        handle_errors(validation["errors"])
```

### 3. Error Handling
```python
# Handle node-specific errors
def configure_node_safely(node_type, config):
    # Check dependencies
    deps = mcp__n8n__get_property_dependencies(
        nodeType=node_type
    )
    
    # Validate minimal requirements
    validation = mcp__n8n__validate_node_minimal(
        nodeType=node_type,
        config=config
    )
    
    if validation["missing"]:
        raise ValueError(f"Missing required fields: {validation['missing']}")
```

### 4. Performance Optimization
- Cache node information
- Use `get_node_essentials` for quick info
- Batch validation operations
- Limit search results appropriately

### 5. AI Node Usage
```python
# Any node can be an AI tool
tool_info = mcp__n8n__get_node_as_tool_info(
    nodeType="nodes-base.slack"
)

# Configure for AI agent
ai_tool_config = {
    "tool": "nodes-base.slack",
    "description": tool_info["description"],
    "parameters": tool_info["required_params"]
}
```

---

*See also: [Workflow Automation](../../logic/automation.md) | [MCP Overview](../README.md)*