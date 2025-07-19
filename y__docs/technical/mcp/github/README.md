# GitHub MCP Documentation

## Table of Contents

- [Overview](#overview)
  - [Key Features](#key-features)
- [Authentication Setup](#authentication-setup)
  - [1. Generate Personal Access Token](#1-generate-personal-access-token)
  - [2. Configure MCP](#2-configure-mcp)
  - [3. Verify Setup](#3-verify-setup)
- [Common Operations](#common-operations)
  - [Repository Management](#repository-management)
  - [Issue Management](#issue-management)
  - [Pull Request Operations](#pull-request-operations)
  - [Workflow Management](#workflow-management)
- [Workflow Integration](#workflow-integration)
  - [Automated PR Creation](#automated-pr-creation)
  - [Issue Automation](#issue-automation)
  - [CI/CD Integration](#cicd-integration)
- [API Reference](#api-reference)
  - [Key Functions](#key-functions)
    - [Repository Operations](#repository-operations)
    - [Issue Operations](#issue-operations)
    - [PR Operations](#pr-operations)
    - [Workflow Operations](#workflow-operations)
- [Best Practices](#best-practices)
  - [1. Error Handling](#1-error-handling)
  - [2. Rate Limiting](#2-rate-limiting)
  - [3. Security](#3-security)
  - [4. Performance](#4-performance)
  - [5. Notifications](#5-notifications)
## Overview

GitHub MCP provides comprehensive GitHub API access, enabling repository management, issue tracking, pull request operations, and workflow automation directly from Claude Code.

### Key Features
- Repository management (create, fork, clone)
- Issue and PR operations
- Workflow and Actions control
- Code search across repositories
- Notification management
- File operations

## Authentication Setup

### 1. Generate Personal Access Token
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic) with scopes:
   - `repo` (full control)
   - `workflow` (update workflows)
   - `notifications` (access notifications)
   - `user` (read user info)

### 2. Configure MCP
Add to environment:
```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

Or in `.claude/settings.json`:
```json
{
  "mcpServers": {
    "github-mcp-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### 3. Verify Setup
```python
# Test authentication
me = mcp__github-mcp-server__get_me()
print(f"Authenticated as: {me['login']}")
```

## Common Operations

### Repository Management
```python
# Create repository
repo = mcp__github-mcp-server__create_repository(
    name="my-new-project",
    description="A new project",
    private=True,
    autoInit=True
)

# Fork repository
fork = mcp__github-mcp-server__fork_repository(
    owner="original-owner",
    repo="cool-project"
)

# Get repository contents
contents = mcp__github-mcp-server__get_file_contents(
    owner="myusername",
    repo="myproject",
    path="src/"
)
```

### Issue Management
```python
# Create issue
issue = mcp__github-mcp-server__create_issue(
    owner="myusername",
    repo="myproject",
    title="Bug: Navigation not responsive",
    body="The navigation menu doesn't work on mobile devices",
    labels=["bug", "ui"],
    assignees=["myusername"]
)

# Update issue
mcp__github-mcp-server__update_issue(
    owner="myusername",
    repo="myproject",
    issue_number=issue["number"],
    state="closed"
)

# Search issues
results = mcp__github-mcp-server__search_issues(
    query="is:open label:bug repo:myusername/myproject"
)
```

### Pull Request Operations
```python
# Create PR
pr = mcp__github-mcp-server__create_pull_request(
    owner="myusername",
    repo="myproject",
    title="Feature: Add dark mode",
    head="feature/dark-mode",
    base="main",
    body="Implements dark mode toggle\n\n- [x] CSS variables\n- [x] Toggle button\n- [x] Persistence"
)

# Review PR
mcp__github-mcp-server__create_and_submit_pull_request_review(
    owner="myusername",
    repo="myproject",
    pullNumber=pr["number"],
    body="LGTM! Great implementation",
    event="APPROVE"
)

# Merge PR
mcp__github-mcp-server__merge_pull_request(
    owner="myusername",
    repo="myproject",
    pullNumber=pr["number"],
    merge_method="squash"
)
```

### Workflow Management
```python
# Run workflow
mcp__github-mcp-server__run_workflow(
    owner="myusername",
    repo="myproject",
    workflow_id="ci.yml",
    ref="main",
    inputs={"environment": "production"}
)

# Check workflow status
runs = mcp__github-mcp-server__list_workflow_runs(
    owner="myusername",
    repo="myproject",
    workflow_id="ci.yml",
    status="in_progress"
)

# Re-run failed jobs
mcp__github-mcp-server__rerun_failed_jobs(
    owner="myusername",
    repo="myproject",
    run_id=runs[0]["id"]
)
```

## Workflow Integration

### Automated PR Creation
```python
# In hook or automation
def create_feature_pr(feature_name, changes):
    # Create branch
    mcp__github-mcp-server__create_branch(
        owner="myusername",
        repo="myproject",
        branch=f"feature/{feature_name}",
        from_branch="main"
    )
    
    # Push changes
    mcp__github-mcp-server__push_files(
        owner="myusername",
        repo="myproject",
        branch=f"feature/{feature_name}",
        message=f"Add {feature_name}",
        files=changes
    )
    
    # Create PR
    pr = mcp__github-mcp-server__create_pull_request(
        owner="myusername",
        repo="myproject",
        title=f"Feature: {feature_name}",
        head=f"feature/{feature_name}",
        base="main",
        body=generate_pr_description(feature_name, changes)
    )
    
    return pr
```

### Issue Automation
```python
# Auto-label issues based on content
def auto_label_issue(issue):
    content = f"{issue['title']} {issue['body']}".lower()
    labels = []
    
    if "bug" in content or "error" in content:
        labels.append("bug")
    if "feature" in content or "enhancement" in content:
        labels.append("enhancement")
    if "security" in content:
        labels.append("security")
    
    if labels:
        mcp__github-mcp-server__update_issue(
            owner=issue["repository"]["owner"]["login"],
            repo=issue["repository"]["name"],
            issue_number=issue["number"],
            labels=labels
        )
```

### CI/CD Integration
```python
# Deploy on successful merge
def deploy_on_merge(pr):
    if pr["merged"]:
        # Run deployment workflow
        mcp__github-mcp-server__run_workflow(
            owner=pr["base"]["repo"]["owner"]["login"],
            repo=pr["base"]["repo"]["name"],
            workflow_id="deploy.yml",
            ref="main",
            inputs={
                "pr_number": str(pr["number"]),
                "environment": "production"
            }
        )
```

## API Reference

### Key Functions

#### Repository Operations
- `create_repository`: Create new repo
- `fork_repository`: Fork existing repo
- `get_file_contents`: Read files/directories
- `create_or_update_file`: Create/update single file
- `push_files`: Push multiple files
- `delete_file`: Delete file

#### Issue Operations
- `create_issue`: Create new issue
- `update_issue`: Update existing issue
- `get_issue`: Get issue details
- `list_issues`: List repository issues
- `search_issues`: Search across GitHub
- `add_issue_comment`: Add comment

#### PR Operations
- `create_pull_request`: Create PR
- `update_pull_request`: Update PR
- `merge_pull_request`: Merge PR
- `get_pull_request`: Get PR details
- `list_pull_requests`: List PRs
- `search_pull_requests`: Search PRs

#### Workflow Operations
- `run_workflow`: Trigger workflow
- `list_workflows`: List workflows
- `list_workflow_runs`: List runs
- `rerun_workflow_run`: Re-run workflow
- `cancel_workflow_run`: Cancel run

## Best Practices

### 1. Error Handling
```python
try:
    pr = mcp__github-mcp-server__create_pull_request(...)
except Exception as e:
    if "already exists" in str(e):
        # Handle existing PR
        pass
    else:
        raise
```

### 2. Rate Limiting
- GitHub API has rate limits (5000/hour authenticated)
- Implement caching for read operations
- Batch operations when possible

### 3. Security
- Never commit tokens to repository
- Use environment variables
- Implement token rotation

### 4. Performance
```python
# Cache user info
if not hasattr(self, '_github_user'):
    self._github_user = mcp__github-mcp-server__get_me()
return self._github_user
```

### 5. Notifications
```python
# Check notifications efficiently
notifications = mcp__github-mcp-server__list_notifications(
    filter="only_participating"
)

# Mark as read in batch
if notifications:
    mcp__github-mcp-server__mark_all_notifications_read()
```

---

*See also: [Workflow Automation](../../logic/automation.md) | [MCP Overview](../README.md)*