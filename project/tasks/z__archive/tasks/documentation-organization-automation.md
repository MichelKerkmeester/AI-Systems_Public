# Documentation Organization & Automation

**Created:** 2025-01-19  
**Status:** To Do  
**Priority:** High  
**Estimated Effort:** 16-20 hours  
**Type:** Infrastructure & Documentation

## Overview

Comprehensive reorganization of the documentation structure with automated workflows for task management and documentation maintenance. This project will improve discoverability, prevent broken references, and establish sustainable documentation practices.

## Phase 1: Structure & Organization (4-5 hours)

### 1.1 Add Table of Contents
- [ ] Scan all documents in `/docs` directory
- [ ] Generate and add table of contents to each document
- [ ] Use consistent TOC format with anchor links
- [ ] Update existing TOCs where present

### 1.2 File Reorganization
- [ ] Move `/Users/michel_kerkmeester/AI & Dev/Websites/• anobel.nl/.claude/logic/shared/hooks-in-cc.md` to `/docs/technical/`
- [ ] Update all references to the moved file
- [ ] Verify no broken links after move

### 1.3 Create Directory READMEs
- [ ] Create README.md for `/docs` directory
  - Overview of documentation structure
  - Navigation guide
  - Documentation standards
- [ ] Create README.md for `/docs/logic` (rename from logic-help)
  - Rename directory from `logic-help` to `logic`
  - Create comprehensive index of logic documentation
  - Add quick navigation links

## Phase 2: Tasks Workflow Update (5-6 hours)

### 2.1 Task Management Hooks
- [ ] Create/update task management hooks for automated workflow
  - Auto-move completed tasks to `/completed`
  - Manage active tasks in `/active`
  - Handle task suggestions in `/to-do`
- [ ] Remove the `suggestion` folder (merge into `/to-do`)

### 2.2 Update CLAUDE.md
- [ ] Add requirement for spec folder creation before system changes
- [ ] Document the new task workflow
- [ ] Include examples of spec folder structure
- [ ] Add task lifecycle documentation

### 2.3 Archive System
- [ ] Create `z__archive` folder structure
- [ ] Implement system exclusion rules for Claude
  - Add to `.claudeignore` or equivalent
  - Ensure hooks skip this directory
  - Document archive policies
- [ ] Create archive management scripts

### 2.4 Automated Task Status Management
- [ ] Implement task lifecycle automation:
  ```
  /to-do → /active → /completed → /z__archive
  ```
- [ ] Create status transition triggers
- [ ] Add task metadata tracking
- [ ] Implement automatic archival after 30 days

## Phase 3: MCP Documentation (4-5 hours)

### 3.1 Create MCP Structure
- [ ] Create `/docs/mcp/` directory
- [ ] Create main README.md (excluding Graphiti)
  - MCP overview
  - Common patterns
  - Integration guidelines

### 3.2 Individual MCP Documentation
Create folders and documentation for each MCP:
- [ ] `/docs/mcp/sequential-thinking/`
  - Setup guide
  - Usage examples
  - Integration with hooks
- [ ] `/docs/mcp/gemini/`
  - Configuration
  - API usage
  - Best practices
- [ ] `/docs/mcp/github/`
  - Authentication setup
  - Common operations
  - Workflow integration
- [ ] `/docs/mcp/n8n/`
  - Connection setup
  - Workflow examples
  - Automation patterns
- [ ] `/docs/mcp/desktop-commander/` (optional)
  - Installation notes
  - CLI vs Desktop clarification
  - Feature comparison

### 3.3 MCP Integration Guide
- [ ] Create cross-MCP integration guide
- [ ] Document MCP communication patterns
- [ ] Add troubleshooting section

## Phase 4: Graphiti & Automation (3-4 hours)

### 4.1 Complete Graphiti Documentation
- [ ] Finalize documentation in `/docs/graphiti`
- [ ] Add practical examples
- [ ] Create troubleshooting guide
- [ ] Document memory patterns

### 4.2 Auto-Updating System
- [ ] Implement README auto-generation
  - Scan directories for changes
  - Update TOCs automatically
  - Maintain cross-references
- [ ] Create reference validation script
  - Check all internal links
  - Report broken references
  - Suggest fixes
- [ ] Schedule regular documentation audits

### 4.3 Documentation Automation
- [ ] Create documentation update hooks
- [ ] Implement change detection
- [ ] Auto-generate index files
- [ ] Maintain documentation graph

## Success Criteria

- [ ] All docs have current table of contents
- [ ] File structure is properly organized
- [ ] Task workflow automation is functional
- [ ] Complete MCP documentation exists
- [ ] Auto-update system prevents broken references
- [ ] Archive folder is excluded from system operations

## Testing Scenarios

### Scenario 1: Task Lifecycle
1. Create new task in `/to-do`
2. Activate task (moves to `/active`)
3. Complete task (moves to `/completed`)
4. Wait for archival (moves to `/z__archive`)

### Scenario 2: Documentation Update
1. Modify a document
2. Verify TOC updates automatically
3. Check cross-references remain valid
4. Confirm index files update

### Scenario 3: MCP Integration
1. Follow setup guide for each MCP
2. Test integration examples
3. Verify troubleshooting steps

## Dependencies

- Command system refactoring (95% complete)
- Existing hook infrastructure
- MCP configurations

## Deliverables

1. **Organized `/docs` structure** with consistent TOCs
2. **Automated task workflow** with lifecycle management
3. **Complete MCP documentation** (excluding Graphiti)
4. **Auto-updating system** for documentation maintenance
5. **Archive system** with proper exclusions

## Implementation Order

1. Phase 1 first (foundation)
2. Phase 3 can run parallel to Phase 2
3. Phase 4 depends on Phases 1-3

## Notes

- Maintain backward compatibility during reorganization
- Test all automated systems thoroughly
- Document the documentation system itself
- Consider future scalability

---

*Related to: Command system refactoring, Hook infrastructure*  
*Part of: Documentation improvement initiative*