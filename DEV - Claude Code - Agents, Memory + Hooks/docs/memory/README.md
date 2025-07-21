# 🧠 Graphiti Memory System

## Table of Contents

- [Directory Structure](#directory-structure)
- [🚀 Quick Start](#-quick-start)
  - [Essential Commands](#essential-commands)
  - [Automatic Capture Patterns (Semi-Auto Mode)](#automatic-capture-patterns-semi-auto-mode)
- [🔧 Setup & Configuration](#-setup-configuration)
  - [Requirements](#requirements)
  - [Verification Scripts](#verification-scripts)
- [📊 Viewing Memories](#-viewing-memories)
  - [1. Via Claude Code](#1-via-claude-code)
  - [2. Neo4j Browser (Visual)](#2-neo4j-browser-visual)
  - [3. Direct Database Check](#3-direct-database-check)
- [🤖 Automation Settings](#-automation-settings)
- [📂 File Structure](#-file-structure)
- [🆕 Auto-Context Loading](#-auto-context-loading)
- [🛠️ Troubleshooting](#-troubleshooting)
  - ["Missing indexes" error](#missing-indexes-error)
  - [Neo4j not connecting](#neo4j-not-connecting)
  - [MCP showing stale data](#mcp-showing-stale-data)
  - [View database location](#view-database-location)
- [💡 Best Practices](#-best-practices)
```
graphiti/
├── README.md # Overview and navigation
├── memory-verifcation-guide.md # Testing and verification
└── practical-examples.md # Real-world usage examples
```

## 🚀 Quick Start

### Essential Commands
```bash
/memory                      # Check status
/memory search "keyword"     # Search memories  
/memory manual "insight"     # Add memory manually
/memory auto [off|manual|semi|full]  # Set automation level
```

### Automatic Capture Patterns (Semi-Auto Mode)
- `DECISION:` → Architectural decisions (auto)
- `SECURITY:` → Security implementations (auto)
- `BREAKING:` → Breaking changes (auto)
- `RESOLVED:` → Bug fixes (prompts)
- `PATTERN:` → Code patterns (prompts)

## 🔧 Setup & Configuration

### Requirements
- Neo4j Desktop running on port 7687
- Configuration in `.env`:
  ```
  NEO4J_URI=neo4j://127.0.0.1:7687
  NEO4J_USER=neo4j
  NEO4J_PASSWORD=your_password
  ```

### Verification Scripts
```bash
# Initialize database schema (run once)
python3 .claude/logic/memory/initialize-neo4j-schema.py

# Check Neo4j status
python3 .claude/logic/memory/check-neo4j.py

# Clean all memories (careful!)
python3 .claude/logic/memory/cleanup-memories.py
```

## 📊 Viewing Memories

### 1. Via Claude Code
```bash
/memory                           # Status overview
/memory search "pattern"          # Search by keyword
mcp__graphiti-gemini__retrieve_episodes  # Get recent (in conversation)
```

### 2. Neo4j Browser (Visual)
1. Open Neo4j Desktop → "Open Neo4j Browser"
2. Or navigate to `http://localhost:7474`
3. Run queries:
   ```cypher
   // View all memories
   MATCH (e:Episode) RETURN e ORDER BY e.created_at DESC
   
   // Search memories
   MATCH (e:Episode) WHERE e.name CONTAINS 'PATTERN' RETURN e
   ```

### 3. Direct Database Check
```bash
# Quick memory count
python3 .claude/logic/memory/check-neo4j.py
```

## 🤖 Automation Settings

Located in `.claude/logic/memory/settings.json`:
- 🔴 **off**: No automatic capture
- 🔵 **manual**: Only on explicit command
- 🟡 **semi**: Auto-capture critical, prompt others (default)
- 🟢 **full**: Auto-capture all patterns

## 📂 File Structure

```
.claude/logic/memory/
├── README.md                    # This file
├── settings.json               # Automation config
├── stats.json                  # Capture metrics
├── initialize-neo4j-schema.py  # Setup script
├── check-neo4j.py             # Status checker
├── cleanup-memories.py        # Clean database
└── hooks/
    └── memory-context-hook-v2.py  # Auto-loads context
```

## 🆕 Auto-Context Loading

When you start a conversation, relevant memories are automatically loaded based on your prompt keywords. Disable with `"auto_context": false` in `.claude/settings.json`.

## 🛠️ Troubleshooting

### "Missing indexes" error
```bash
python3 .claude/logic/memory/initialize-neo4j-schema.py
```

### Neo4j not connecting
1. Ensure Neo4j Desktop is running
2. Start your database (green play button)
3. Verify `.env` credentials match Neo4j settings

### MCP showing stale data
Restart Claude Code CLI to refresh the connection

### View database location
```
/Users/michel_kerkmeester/Library/Application Support/neo4j-desktop/
```

## 💡 Best Practices

1. **Start conversations with context**: `/memory search "recent work"`
2. **Capture important decisions**: Use trigger patterns
3. **Review periodically**: Check memories to ensure quality
4. **Keep automation on semi**: Best balance of automation and control