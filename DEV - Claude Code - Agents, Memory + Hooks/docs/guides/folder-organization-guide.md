# Folder Organization Guide

## Overview

This guide explains the folder organization principles for the Claude Code system, with special emphasis on the **user-managed z__archive folders** and proper task organization using sub-folders.

---

## 🚨 Critical Rule: z__archive is User-Managed Only

**IMPORTANT:** All `z__archive` folders throughout the system are **exclusively user-managed**. AI agents, automated processes, and hooks are **prohibited** from writing to these folders.

### Why This Matters
- **User Control**: Only you decide what gets archived and when
- **Preservation**: Prevents accidental archival of important work
- **Organization**: Allows manual curation of archived content
- **Security**: Ensures AI can't hide or move files without your knowledge

### How It Works
- The system will **suggest** files for archival after 30 days
- You manually review and move files to z__archive if desired
- AI operations automatically skip z__archive folders
- Hooks actively block any attempts to write to z__archive

---

## 📁 Task Organization with Sub-folders

**UPDATE**: Sub-folder organization is now **automatic**! When creating tasks, the system automatically places them in the appropriate sub-folder based on the task name. Both `/specs` and `/completed` directories use automatic categorization.

### Recommended Sub-folder Categories

#### For `/specs` (Task Specifications)
```
/specs/
├── features/          # New functionality specs
├── bugs/              # Bug fix specifications
├── enhancements/      # Improvement proposals
├── refactoring/       # Code restructuring plans
├── documentation/     # Documentation tasks
├── security/          # Security-related specs
├── performance/       # Performance optimization
├── testing/           # Test implementation specs
└── integrations/      # Third-party integrations
```

#### For `/completed` (Finished Tasks)
```
/completed/
├── features/          # Implemented features
│   ├── user-auth-system.md
│   └── payment-integration.md
├── bugs/              # Fixed bugs
│   ├── login-timeout-fix.md
│   └── data-sync-issue.md
├── refactoring/       # Completed refactors
│   ├── database-optimization.md
│   └── api-restructure.md
├── documentation/     # Written docs
│   ├── api-guide.md
│   └── user-manual.md
└── multi-agent/       # Multi-agent work
    ├── phase-1-summary.md
    └── final-report.md
```

#### For `/active` (Current Work)
While typically only one task is active, you can still use sub-folders when working on complex projects:
```
/active/
└── current-feature/
    ├── main-task.md
    ├── research-notes.md
    └── implementation-plan.md
```

---

## 🏷️ Naming Conventions

### Task Files
Use descriptive, kebab-case names:
- ✅ `user-authentication-system.md`
- ✅ `fix-login-timeout-issue.md`
- ✅ `refactor-database-queries.md`
- ❌ `task1.md`
- ❌ `TODO.md`
- ❌ `UserAuthSystem.md`

### Sub-folders
Keep sub-folder names:
- **Plural**: `features/`, not `feature/`
- **Lowercase**: `documentation/`, not `Documentation/`
- **Descriptive**: `refactoring/`, not `misc/`

---

## 🔄 Task Lifecycle with Sub-folders

1. **Creation** → `/specs/[category]/task-name.md`
2. **Activation** → `/active/task-name.md` (or `/active/[project]/`)
3. **Completion** → `/completed/[category]/YYYY-MM-DD-task-name.md`
4. **Archival** → `/z__archive/[category]/` (user-managed only)

### Example Flow
```bash
# 1. Task created
/specs/features/user-profile-system.md

# 2. Task activated
/active/user-profile-system.md

# 3. Task completed (with timestamp)
/completed/features/2025-01-21-user-profile-system.md

# 4. User manually archives (after review)
/z__archive/features/2025-01-21-user-profile-system.md
```

---

## 🤖 AI Agent Guidelines

When AI agents create files, they should:

1. **Always use sub-folders** for better organization
2. **Never write to z__archive** - these are user-managed only
3. **Follow naming conventions** - kebab-case, descriptive names
4. **Add timestamps** to completed tasks
5. **Ask when unsure** about the appropriate sub-folder

### Automatic Folder Selection
The system includes a `suggest_folder_for_task()` helper that analyzes task names and suggests appropriate sub-folders based on keywords:

- "feature", "add", "implement" → `/features/`
- "bug", "fix", "issue" → `/bugs/`
- "refactor", "optimize" → `/refactoring/`
- "doc", "guide" → `/documentation/`

---

## 📊 Benefits of This Organization

1. **Easy Navigation**: Find related tasks quickly
2. **Clear History**: See what types of work were done
3. **Better Analysis**: Understand project focus areas
4. **Clean Structure**: Avoid cluttered directories
5. **User Control**: You decide what gets archived

---

## 🔍 Finding Files

With proper organization, finding files becomes easier:

```bash
# Find all completed features
ls .claude/tasks/completed/features/

# Find all bug fixes in 2025
ls .claude/tasks/completed/bugs/2025-*

# Find all refactoring specs
ls .claude/tasks/specs/refactoring/
```

---

## 📝 Quick Reference

| Action | Location | Example |
|--------|----------|---------|
| Create spec | `/specs/[category]/` | `/specs/features/new-api.md` |
| Active task | `/active/` | `/active/current-work.md` |
| Complete task | `/completed/[category]/` | `/completed/bugs/2025-01-21-fix-timeout.md` |
| Archive (user only) | `/z__archive/[category]/` | `/z__archive/features/old-feature.md` |

---

## ⚠️ Common Mistakes to Avoid

1. ❌ Placing files directly in `/completed/` without sub-folders
2. ❌ AI agents attempting to write to `z__archive/`
3. ❌ Using spaces in filenames
4. ❌ Creating deeply nested sub-folders (keep it simple)
5. ❌ Forgetting timestamps on completed tasks

---

Remember: **z__archive folders are sacred user territory** - only you control what goes there!