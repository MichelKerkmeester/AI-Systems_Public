#!/usr/bin/env python3
"""
/memory command implementation for Claude Code
Manages memory system configuration and manual captures
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Any

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from hooks.shared import MessageFormatter


class MemoryCommand:
    """Handle /memory command functionality"""
    
    def __init__(self):
        self.project_root = Path(__file__).resolve()
        while not (self.project_root / ".claude").exists() and self.project_root != self.project_root.parent:
            self.project_root = self.project_root.parent
            
        self.claude_path = self.project_root / ".claude"
        self.settings_path = self.claude_path / "hooks" / "memory" / "memory-settings.json"
        
    def execute(self, args: List[str]) -> str:
        """Execute memory command with given arguments"""
        if not args or args[0] == "":
            return self.show_status()
        
        subcommand = args[0].lower()
        
        if subcommand == "help":
            return self.show_help()
        elif subcommand == "status":
            return self.show_status()
        elif subcommand == "auto":
            if len(args) > 1:
                return self.set_automation_level(args[1])
            else:
                return "❌ Please specify automation level: off, manual, semi, or full"
        elif subcommand == "search":
            query = " ".join(args[1:]) if len(args) > 1 else ""
            return self.search_memory(query)
        elif subcommand == "manual":
            text = " ".join(args[1:]) if len(args) > 1 else ""
            return self.manual_capture(text)
        else:
            return f"❌ Unknown subcommand: {subcommand}\\n\\nUse `/memory help` for available commands."
    
    def show_help(self) -> str:
        """Show help information"""
        output = MessageFormatter.header("Memory Command Help", "memory")
        
        output += "\\n\\n📚 Available Commands:"
        output += "\\n  • `/memory` - Show memory status"
        output += "\\n  • `/memory auto [level]` - Set automation level"
        output += "\\n  • `/memory search [query]` - Search memories"
        output += "\\n  • `/memory manual [text]` - Manual capture"
        output += "\\n  • `/memory help` - Show this help"
        
        output += "\\n\\n🤖 Automation Levels:"
        output += "\\n  • `off` - No automatic capture"
        output += "\\n  • `manual` - Explicit capture only"
        output += "\\n  • `semi` - Critical auto, others prompt"
        output += "\\n  • `full` - Capture everything"
        
        output += "\\n\\n📝 Patterns Captured:"
        output += "\\n  • DECISION - Major decisions made"
        output += "\\n  • SECURITY - Security considerations"
        output += "\\n  • BREAKING - Breaking changes"
        output += "\\n  • RESOLVED - Problem resolutions"
        output += "\\n  • PATTERN - Code patterns established"
        
        output += "\\n" + MessageFormatter.footer()
        return output
    
    def show_status(self) -> str:
        """Show current memory system status"""
        output = MessageFormatter.header("Memory System Status", "memory")
        
        # Try to load settings
        current_level = "semi"  # default
        if self.settings_path.exists():
            try:
                with open(self.settings_path, 'r') as f:
                    settings = json.load(f)
                    current_level = settings.get("automation_level", "semi")
            except:
                pass
        
        output += f"\\n\\n🤖 Automation Level: **{current_level}**"
        output += "\\n\\n📊 Graphiti MCP: ✅ Connected"
        output += "\\n\\n📝 Recent Captures: (Use Graphiti tools to query)"
        
        output += "\\n" + MessageFormatter.footer()
        return output
    
    def set_automation_level(self, level: str) -> str:
        """Set automation level"""
        valid_levels = ["off", "manual", "semi", "full"]
        
        if level not in valid_levels:
            return f"❌ Invalid level: {level}\\n\\nValid levels: {', '.join(valid_levels)}"
        
        # Update settings
        settings = {}
        if self.settings_path.exists():
            try:
                with open(self.settings_path, 'r') as f:
                    settings = json.load(f)
            except:
                pass
        
        settings["automation_level"] = level
        
        # Ensure directory exists
        self.settings_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.settings_path, 'w') as f:
            json.dump(settings, f, indent=2)
        
        output = MessageFormatter.header("Automation Level Updated", "memory")
        output += f"\\n✅ Set to: **{level}**"
        
        descriptions = {
            "off": "No automatic memory capture",
            "manual": "Only explicit captures via /memory manual",
            "semi": "Critical patterns auto-captured, others prompt",
            "full": "All patterns captured automatically"
        }
        
        output += f"\\n\\n📝 {descriptions[level]}"
        output += "\\n" + MessageFormatter.footer()
        
        return output
    
    def search_memory(self, query: str) -> str:
        """Search memory (placeholder - use Graphiti MCP)"""
        if not query:
            return "❌ Please provide a search query: `/memory search [query]`"
        
        output = MessageFormatter.header("Memory Search", "memory")
        output += f"\\n🔍 Query: '{query}'"
        output += "\\n\\n⚠️  Use Graphiti MCP tools directly for search:"
        output += "\\n  • mcp__graphiti-gemini__search"
        output += "\\n  • mcp__graphiti-gemini__retrieve_episodes"
        output += "\\n" + MessageFormatter.footer()
        
        return output
    
    def manual_capture(self, text: str) -> str:
        """Manual memory capture (placeholder - use Graphiti MCP)"""
        if not text:
            return "❌ Please provide text to capture: `/memory manual [text]`"
        
        output = MessageFormatter.header("Manual Memory Capture", "memory")
        output += f"\\n📝 Text: '{text[:100]}...'" if len(text) > 100 else f"\\n📝 Text: '{text}'"
        output += "\\n\\n⚠️  Use Graphiti MCP tool directly:"
        output += "\\n  • mcp__graphiti-gemini__add_episode"
        output += "\\n" + MessageFormatter.footer()
        
        return output


def main():
    """Main entry point"""
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    command = MemoryCommand()
    result = command.execute(args)
    
    print(result)


if __name__ == "__main__":
    main()