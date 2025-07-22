# Superdesign Canvas Integration Requirements (Revised for Windsurf)

## Overview
Integrate Superdesign's canvas visualization directly through Windsurf IDE while using Claude Code CLI for programmatic design generation, creating a powerful hybrid workflow.

## Background
- **Superdesign**: Extension available for Windsurf, VS Code, Cursor with React-based canvas
- **Claude Code**: CLI tool for automation and batch operations
- **Windsurf IDE**: User's IDE that supports Superdesign extension natively
- **Goal**: Leverage existing tools without building custom solutions

## Revised Approach: Configuration Over Code

### What We DON'T Need to Build
1. ❌ Custom canvas viewer component
2. ❌ File watching system
3. ❌ WebSocket communication
4. ❌ Browser-based interface
5. ❌ Vite plugin modifications

### What We WILL Use
1. ✅ **Superdesign Extension in Windsurf** - Native canvas visualization
2. ✅ **Claude Code CLI** - Design generation and automation
3. ✅ **Shared Directory** - Both tools read/write same location
4. ✅ **Existing Formats** - Superdesign's established file structure

### Integration Strategy
1. **Windsurf Side**
   - Install Superdesign from marketplace
   - Configure to watch project's `.superdesign/` directory
   - Use for visual review, iteration, and manual adjustments

2. **Claude Code Side**
   - Generate designs programmatically
   - Output to `.superdesign/design_iterations/`
   - Follow Superdesign's naming conventions
   - Batch operations and automation

### Code Reuse Becomes Tool Reuse
Instead of extending viteflow components, we:
- Use Superdesign's existing canvas implementation
- Leverage Windsurf's extension ecosystem
- Focus on integration patterns, not new development

## Requirements

### 1. Windsurf Configuration
- **Install**: Superdesign extension from Windsurf marketplace
- **Configure**: Point to project's `.superdesign/` directory
- **Usage**: Visual canvas for reviewing generated designs
- **Features**: All native Superdesign capabilities available

### 2. Claude Code Integration
- **Commands**: Design generation commands that output Superdesign format
- **Directory**: Write to `.superdesign/design_iterations/`
- **Naming**: Follow Superdesign conventions (design_1.html, design_1_1.html)
- **Automation**: Batch generation, variations, themed sets

### 3. Shared Directory Structure
- **Location**: `.superdesign/` in project root
- **Structure**:
  ```
  .superdesign/
  ├── design_iterations/     # Generated designs (both tools)
  │   ├── design_1.html      # From Claude Code
  │   ├── design_1_1.html    # Iteration from Windsurf
  │   └── design_2.html      # From Claude Code
  ├── moodboard/            # Reference images
  ├── design_system/        # Shared design tokens
  └── design.mdc            # Cursor config (if needed)
  ```

### 4. Workflow Integration
- **Design Generation**: Claude Code → `.superdesign/`
- **Visual Review**: Open Windsurf → View in Superdesign
- **Iteration**: Make changes in either tool
- **Version Control**: Git-friendly file structure

### 5. Command Structure
```bash
# Claude Code commands
cc design generate "hero section"     # Single design
cc design batch "landing page"       # Multiple variations
cc design theme --style="minimal"    # Themed generation
```

## Technical Constraints

### Must Use
1. Superdesign's native file format
2. Standard `.superdesign/` directory structure
3. Windsurf's extension capabilities
4. Claude Code's generation abilities

### Must Avoid
1. Building custom canvas viewers
2. Creating new file watching systems
3. Modifying existing viteflow components
4. Adding any new frontend code

## Success Criteria
1. Superdesign works natively in Windsurf
2. Claude Code generates compatible designs
3. Both tools share same directory seamlessly
4. No custom code required
5. Workflow is simple and efficient
6. All canvas features available without development

## Implementation Strategy
1. Install Superdesign in Windsurf (5 min)
2. Configure shared directory structure
3. Create Claude Code design commands
4. Test bidirectional workflow
5. Document setup process

## Advantages of Revised Approach
1. **Zero Development Time** - Use existing tools
2. **Full Feature Set** - All Superdesign features available
3. **Native Performance** - No browser overhead
4. **Simpler Maintenance** - No custom code to maintain
5. **Better Integration** - Direct IDE support