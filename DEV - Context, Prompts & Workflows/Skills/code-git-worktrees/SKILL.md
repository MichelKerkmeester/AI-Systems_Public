---
name: code-git-worktrees
description: Create isolated workspaces with minimal branching (main-focused by default). Uses short-lived temp branches that merge back to main immediately, keeping codebase unified while providing isolation benefits. Alternative strategies available for long-running features or experiments.
---

# Git Worktrees - Isolated Workspace Management

## 1. 📄 Description

Create isolated workspaces with minimal branching (main-focused by default). Uses short-lived temp branches that merge back to main immediately, keeping codebase unified while providing isolation benefits. Alternative strategies available for long-running features or experiments.

## 📋 Table of Contents

- [📄 Description](#description)
- [🎯 When to Use](#when-to-use)
- [🛠️ How It Works](#how-it-works)
- [📊 Inputs](#inputs)
- [🚀 Workflow](#workflow)
- [📋 Branch Strategy Guide](#branch-strategy-guide)
- [🎯 Decision Matrix](#decision-matrix)
- [⚠️ Common Mistakes](#common-mistakes)
- [📖 Rules](#rules)
- [💡 Example Workflows](#example-workflows)
- [🔗 Integration Points](#integration-points)
- [🔧 Troubleshooting](#troubleshooting)
- [📚 References](#references)
- [🎓 Success Criteria](#success-criteria)

.

## 2. 🎯 When to Use

**Use this skill when**:
- Starting feature work requiring isolation from current workspace
- Handling urgent hotfixes without disrupting feature development
- Reviewing pull requests locally without stashing work
- Comparing implementations side-by-side
- Testing dependency upgrades in isolation
- Running long builds/tests while continuing development
- Need to work on multiple contexts simultaneously

**Do NOT use this skill for**:
- Simple one-line quick fixes (just use regular git checkout)
- Working on single branch sequentially
- Very limited disk space environments
- When context switching overhead is minimal

**Core principle**: Systematic directory selection + safety verification = reliable isolation

.

## 3. 🛠️ How It Works

This skill creates isolated git worktrees - separate working directories sharing the same repository database. Each worktree can have a different branch checked out, allowing parallel work without context switching.

**Process Overview**:
1. Determine worktree directory location (priority: existing → AGENTS.md → ask user)
2. Verify safety (`.gitignore` check for project-local directories)
3. Create worktree with appropriate branch strategy
4. Run project setup (auto-detect and install dependencies)
5. Verify clean baseline (run tests)
6. Report location and status

**Branch Strategies**:
- **Main-focused (default)**: Work on main with minimal branching (short-lived temp branches)
- **Feature branches**: Create new branch per worktree (for long-running work)
- **Experimental**: Quick experiments with detached HEAD (no branch pollution)

.

## 4. 📊 Inputs

### Required Inputs

**Feature/Task Description**:
- **Type**: String
- **Description**: What you want to work on in the isolated worktree
- **Example**: "Implement user authentication modal"

### Optional Inputs

**Branch Strategy**:
- **Type**: String (enum)
- **Default**: `main_temp` ⭐
- **Options**:
  - `main_temp` - Short-lived branch that merges back to main immediately (default, recommended)
  - `feature_branch` - Create new feature branch (for long-running features)
  - `main_detached` - Detached HEAD on main (for quick experiments)
- **Description**: Controls branching approach
- **Example**: `main_temp` (keeps codebase on main with minimal branching)

**Branch Name** (if feature_branch):
- **Type**: String
- **Default**: Auto-generate from task description
- **Description**: Name for the feature branch
- **Example**: `feature/user-auth`

**Worktree Directory**:
- **Type**: String (path)
- **Default**: Auto-detect via priority system
- **Description**: Where to create the worktree
- **Priority**: Existing directory → AGENTS.md preference → Ask user
- **Example**: `.worktrees/`

.

## 5. 🚀 Workflow

### Step 1: Gather User Inputs

**Purpose**: Collect task description and branch strategy

**Actions**:
- Ask for feature/task description
- Confirm branch strategy (default: main_temp for most work)
- Determine branch name based on strategy

**Default Strategy**: `main_temp` (short-lived branches merging back to main)

**When to use other strategies**:
- `feature_branch`: Long-running features requiring PR review
- `main_detached`: Quick experiments without branch creation

**Validation**: `inputs_collected`

### Step 2: Directory Selection

**Purpose**: Determine where to create worktree

**Priority Order**:

1. **Check Existing Directories**
   ```bash
   ls -d .worktrees 2>/dev/null     # Preferred (hidden)
   ls -d worktrees 2>/dev/null      # Alternative
```
   **If found**: Use that directory. If both exist, `.worktrees` wins.

2. **Check AGENTS.md**
   ```bash
   grep -i "worktree.*directory" AGENTS.md 2>/dev/null
```
   **If preference specified**: Use it without asking.

3. **Ask User**
   If no directory exists and no AGENTS.md preference:
```text
   No worktree directory found. Where should I create worktrees?

   1. .worktrees/ (project-local, hidden)
   2. ~/.config/superpowers/worktrees/<project-name>/ (global location)

   Which would you prefer?
```

**Validation**: `directory_determined`

### Step 3: Safety Verification

**Purpose**: Ensure worktree directory won't pollute repository

**For Project-Local Directories** (`.worktrees/` or `worktrees/`):

**Critical Check**:
```bash
# Verify directory pattern in .gitignore
grep -q "^\.worktrees/$" .gitignore || grep -q "^worktrees/$" .gitignore
```

**If NOT in .gitignore**:
1. Add appropriate line to `.gitignore`
2. Ask for approval, then commit the change
3. Proceed with worktree creation

**Rationale**: Prevents accidentally committing worktree contents to repository.

**For Global Directory** (`~/.config/superpowers/worktrees/`):
- No `.gitignore` verification needed (outside project)

**Validation**: `safety_verified`

### Step 4: Create Worktree

**Purpose**: Create isolated workspace with appropriate branch

**Actions**:

1. **Detect Project Name**:
   ```bash
   project=$(basename "$(git rev-parse --show-toplevel)")
```

2. **Determine Path**:
   ```bash
   case $LOCATION in
     .worktrees|worktrees)
       path="$LOCATION/$BRANCH_NAME"
       ;;
     ~/.config/superpowers/worktrees/*)
       path="$HOME/.config/superpowers/worktrees/$project/$BRANCH_NAME"
       ;;
   esac
```

3. **Create Worktree** (strategy-dependent):

   **Feature Branch**:
   ```bash
   git worktree add "$path" -b "$BRANCH_NAME"
```

   **Main Temp** (short-lived branch):
   ```bash
   git worktree add "$path" -b "temp/$TASK_ID" main
```

   **Main Detached** (no branch):
   ```bash
   git worktree add --detach "$path" main
```

4. **Navigate**:
   ```bash
   cd "$path"
```

**Validation**: `worktree_created`

### Step 5: Project Setup

**Purpose**: Install dependencies and prepare environment

**Auto-Detection**:

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

**Validation**: `dependencies_installed`

### Step 6: Baseline Verification

**Purpose**: Ensure worktree starts in known-good state

**Actions**:
```bash
# Run project-appropriate tests
if [ -f package.json ]; then npm test; fi    # Node.js
if [ -f Cargo.toml ]; then cargo test; fi   # Rust
if [ -f pyproject.toml ] || [ -f requirements.txt ]; then pytest; fi  # Python
if [ -f go.mod ]; then go test ./...; fi    # Go
```

**If tests fail**:
- Report failures with details
- Ask: "Tests are failing. Proceed anyway or investigate first?"

**If tests pass**:
- Continue to final report

**Validation**: `baseline_verified`

### Step 7: Final Report

**Purpose**: Communicate location and status

**Report Format**:
```text
✓ Worktree ready at <full-path>
✓ Branch: <branch-name> (<strategy>)
✓ Tests passing (<N> tests, 0 failures)
✓ Ready to implement <feature-name>
```

**Validation**: `worktree_ready`

.

## 6. 📋 Branch Strategy Guide

### Main Temp (Default - Recommended) ⭐

**When to use**:
- Most development work (default choice)
- Quick fixes or small changes
- Want to keep codebase on main
- Immediate merge-back after testing
- Avoid long-lived feature branches

**Example**:
```bash
git worktree add .worktrees/quick-fix -b temp/fix-modal main
# ... make changes ...
cd ../.. && git checkout main && git merge temp/fix-modal
git branch -d temp/fix-modal
```

**Advantages**:
- Minimal branching, stays close to main
- Reduces merge conflicts
- Simpler mental model
- Branch cleanup automatic

**Best for**: 80% of development work

### Feature Branch

**When to use**:
- Long-running features (multiple days/weeks)
- Work that needs PR review before merging
- Complex features requiring multiple iterations
- When you want branch history preserved

**Example**:
```bash
git worktree add .worktrees/user-auth -b feature/user-auth
# ... develop feature ...
# Create PR, review, merge
```

**Best for**: Major features, team collaboration requiring review

### Main Detached (Experimental)

**When to use**:
- Quick experiments
- Testing ideas without creating branches
- Throwaway work

**Example**:
```bash
git worktree add --detach .worktrees/experiment main
# ... experiment ...
# If keeping: create branch and commit
# If discarding: just remove worktree
```

**Advantage**: No branch pollution

.

## 7. 🎯 Decision Matrix

| Situation | Directory Strategy | Branch Strategy |
|-----------|-------------------|-----------------|
| `.worktrees/` exists | Use it (verify .gitignore) | User preference |
| `worktrees/` exists | Use it (verify .gitignore) | User preference |
| Both exist | Use `.worktrees/` | User preference |
| Neither exists | Check AGENTS.md → Ask | User preference |
| Directory not in .gitignore | Add + commit immediately | User preference |
| Tests fail during baseline | Report + ask permission | User preference |
| No package.json/Cargo.toml | Skip dependency install | User preference |

.

## 8. ⚠️ Common Mistakes

**Skipping .gitignore verification**:
- **Problem**: Worktree contents get tracked, pollute git status
- **Fix**: Always check .gitignore before creating project-local worktree

**Assuming directory location**:
- **Problem**: Creates inconsistency, violates project conventions
- **Fix**: Follow priority: existing > AGENTS.md > ask

**Proceeding with failing tests**:
- **Problem**: Can't distinguish new bugs from pre-existing issues
- **Fix**: Report failures, get explicit permission to proceed

**Hardcoding setup commands**:
- **Problem**: Breaks on projects using different tools
- **Fix**: Auto-detect from project files (package.json, etc.)

**Avoid checking out the same branch in multiple worktrees**:
- **Problem**: Git prevents checking out the same branch in multiple worktrees
- **Fix**: Use different branches or detached HEAD for parallel work on the same codebase state

.

## 9. 📖 Rules

### ALWAYS

- Follow directory priority: existing > AGENTS.md > ask
- Verify .gitignore for project-local directories
- Auto-detect and run project setup
- Verify clean test baseline before reporting ready
- Ask for branch strategy if unclear
- Report full path and status when complete

### NEVER

- Create project-local worktree without .gitignore verification
- Skip baseline test verification
- Proceed with failing tests without asking
- Assume directory location when ambiguous
- Skip AGENTS.md check
- Checkout same branch in multiple worktrees

### ESCALATE IF

- Cannot determine project type for setup
- Tests fail consistently and user wants investigation
- Git operations fail (permissions, corruption)
- Worktree creation conflicts with existing worktree

.

## 10. 💡 Example Workflows

### Example 1: Main Temp (Default Workflow) ⭐

```text
User: "Quick fix for modal close button"
Claude: "I'm using the git-worktrees skill with main-focused strategy (default)."

[Step 1: Gather inputs - branch_strategy: main_temp (default)]
[Step 2: Directory selection - found .worktrees/]
[Step 3: Safety verification - .gitignore contains .worktrees/]
[Step 4: Create worktree with temp branch]
> git worktree add .worktrees/modal-fix -b temp/modal-fix main
[Step 5: Project setup]
> npm install
[Step 6: Baseline verification]
> npm test
✓ All tests passing

✓ Worktree ready at /Users/user/project/.worktrees/modal-fix
✓ Branch: temp/modal-fix (main_temp - merges back to main immediately)
✓ Tests passing
✓ Ready for quick fix

[After fix is committed and tested]
User: "Fix is done and tested"
Claude: "Merging back to main and cleaning up temp branch..."
> git checkout main && git merge temp/modal-fix && git branch -d temp/modal-fix
```

### Example 2: Feature Branch (Long-Running Work)

```text
User: "I need to implement user authentication - this will take a few days"

Claude: "I'm using the git-worktrees skill with feature branch strategy."

[Step 1: Gather inputs - branch_strategy: feature_branch]
[Step 2: Directory selection - found .worktrees/]
[Step 3: Safety verification - .gitignore contains .worktrees/]
[Step 4: Create worktree]
> git worktree add .worktrees/user-auth -b feature/user-auth
[Step 5: Project setup - detected Node.js]
> npm install
[Step 6: Baseline verification]
> npm test
✓ 47 tests passing

✓ Worktree ready at /Users/user/project/.worktrees/user-auth
✓ Branch: feature/user-auth (feature_branch)
✓ Tests passing (47 tests, 0 failures)
✓ Ready to implement user authentication
```

### Example 3: Main Detached (Experimental)

```text
User: "Want to experiment with a new approach, not sure if I'll keep it"

Claude: "I'm using detached HEAD worktree for experimentation."

[Step 1: Gather inputs - branch_strategy: main_detached]
[Step 2: Directory selection - found .worktrees/]
[Step 3: Safety verification - .gitignore contains .worktrees/]
[Step 4: Create worktree detached]
> git worktree add --detach .worktrees/experiment main
[Step 5: Project setup]
> npm install
[Step 6: Baseline verification]
> npm test

✓ Worktree ready at /Users/user/project/.worktrees/experiment
✓ Branch: detached HEAD at main (no branch created)
✓ Tests passing
✓ Ready for experimentation

[If keeping the changes]
User: "This worked great, let's keep it"
Claude: "Creating branch from detached HEAD..."
> cd .worktrees/experiment && git checkout -b feature/new-approach
> git add . && git commit -m "Experimental approach"
```

.

## 11. 🔗 Integration Points

### Called By
- **SpecKit workflows** - When implementation begins (Step 11)
- **brainstorming** (Phase 4) - When design approved and implementation follows
- Any skill needing isolated workspace

### Pairs With
- **finishing-a-development-branch** - Cleanup after work complete
- **executing-plans** or **subagent-driven-development** - Work happens in this worktree
- **code-debugger** - Debug in isolated worktree without affecting main work

### Interacts With
- **AGENTS.md** - Checks for worktree directory preferences
- **knowledge/code_standards.md** - Follows during implementation
- **Project test suite** - Runs for baseline verification

.

## 12. 🔧 Troubleshooting

### Worktree Creation Fails

**Symptom**: `fatal: cannot create worktree` error

**Common Causes**:
- Directory already exists
- Branch already checked out in another worktree
- Insufficient permissions

**Solutions**:
```bash
# Remove worktree safely
git worktree remove .worktrees/branch-name

# Check existing worktrees
git worktree list

# Prune stale references (if needed)
git worktree prune
```

### Tests Fail After Creation

**Symptom**: Baseline tests fail in new worktree

**Actions**:
1. Report failure details to user
2. Ask: "Tests failing. Options: (A) Investigate now (B) Proceed anyway (C) Abort"
3. If investigate: Use code-debugger skill
4. If proceed: Document that baseline is broken
5. If abort: Remove worktree

### Cannot Determine Project Type

**Symptom**: No package.json, Cargo.toml, requirements.txt, etc.

**Actions**:
1. Skip automated dependency install
2. Ask user: "Cannot detect project type. What command should I run to set up dependencies?"
3. Document command in AGENTS.md for future use

### Directory Not in .gitignore

**Symptom**: Worktree directory would be tracked by git

**Actions**:
1. Add appropriate pattern to .gitignore
2. Commit immediately: `git add .gitignore && git commit -m "chore: ignore worktree directories"`
3. Proceed with worktree creation

.

## 13. 📚 References

### Related Documentation
- specs/002-claude-skill-git-worktree/git-worktrees-guide.md - Complete conceptual guide
- specs/002-claude-skill-git-worktree/implementation-guide.md - Practical implementation
- specs/002-claude-skill-git-worktree/quick-reference.md - Command cheat sheet

### Knowledge Base
- knowledge/code_standards.md - Code standards to follow during implementation
- knowledge/debugging.md - If baseline tests fail

### External Resources
- [Git Documentation: git-worktree](https://git-scm.com/docs/git-worktree)
- [Superpowers using-git-worktrees skill](https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/SKILL.md)

.

## 14. 🎓 Success Criteria

**Worktree creation is successful when**:
- ✅ Directory selected following priority system
- ✅ Safety verification passed (`.gitignore` check)
- ✅ Worktree created with appropriate branch strategy
- ✅ Dependencies installed successfully
- ✅ Tests pass (baseline verified)
- ✅ User informed of location and status

**Quality gates**:
- Directory must be in `.gitignore` (if project-local)
- Tests must pass OR user explicitly approves proceeding with failures
- Full path and status reported to user
