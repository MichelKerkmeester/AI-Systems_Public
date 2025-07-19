# /workflow - Development Phase Management

## Purpose
Guide development through structured phases that enhance Webflow sites with JavaScript.

## Usage
- `/workflow` - Interactive mode (AI suggests best approach)
- `/workflow [mode]` - Direct mode selection
- `/w` - Short alias

## Modes
- **auto** - AI analyzes and chooses entire path
- **explore** - Understand current Webflow setup and constraints
- **plan** - Design JavaScript architecture
- **code** - Implementation guidance with safe patterns
- **research** - Analysis only, no implementation
- **iterate** - Incremental improvements

## Quick Access
- `/workflow-auto` or `/wa`
- `/workflow-plan` or `/wp`
- `/workflow-implement` or `/wi`

## Behavior
1. Analyze current project state (files, git status, todos)
2. Consider Webflow constraints and existing structure
3. Suggest most appropriate phase
4. Guide through selected phase with specific focus

## Gemini Enhancement
For complex codebases (20+ files), optional Gemini analysis reduces tokens by ~70%.