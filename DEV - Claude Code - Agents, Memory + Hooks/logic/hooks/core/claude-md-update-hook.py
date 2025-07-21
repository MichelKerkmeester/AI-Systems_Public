#!/usr/bin/env python3
"""
CLAUDE.md Auto-Update Hook

Automatically updates the CLAUDE.md file when new hooks, scripts, or commands
are added to the system. Extracts documentation about what could go wrong
and maintains the Hook Automation Warnings section.

What it does:
- Monitors changes to hooks, scripts, and commands directories
- Extracts automation details and potential pitfalls from docstrings
- Updates CLAUDE.md's Hook Automation Warnings section
- Preserves manual edits while adding new content

What could go wrong:
- Missing important pitfalls if not documented in hook files
- Overwriting manual edits if markers are modified
- Not detecting hooks that use non-standard documentation
- Creating duplicate entries if hook names change
"""

import os
import re
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

try:
    from logic.shared.hook_base import HookBase
    from logic.shared.hook_formatters import MessageFormatter
except ImportError:
    # Fallback for standalone execution
    class HookBase:
        def __init__(self, name):
            self.name = name
            self.project_root = Path(__file__).parent.parent.parent.parent
    
    class MessageFormatter:
        @staticmethod
        def format_warning(msg): return f"⚠️ {msg}"
        @staticmethod
        def format_info(msg): return f"ℹ️ {msg}"


class ClaudeMdUpdateHook(HookBase):
    def __init__(self):
        super().__init__("ClaudeMdUpdate")
        self.claude_md_path = self.project_root / "CLAUDE.md"
        self.hooks_dir = self.project_root / ".claude" / "hooks"
        self.scripts_dir = self.project_root / ".claude" / "scripts"
        self.commands_dir = self.project_root / ".claude" / "logic" / "commands"
        
        # Patterns to extract from hook files
        self.extraction_patterns = {
            "purpose": r"(?:What it does:|automates?:|functionality:)\s*\n((?:[-•]\s*.*\n)*)",
            "pitfalls": r"(?:What could.*go wrong.*:|might.*miss:|blind spots?:)\s*\n((?:[-•]\s*.*\n)*)",
            "mistakes": r"(?:Common mistakes.*:|avoid:|don't:)\s*\n((?:[-•]\s*.*\n)*)"
        }
        
        # Section markers in CLAUDE.md
        self.section_start = "## 🚨 HOOK AUTOMATION WARNINGS"
        self.section_end = "**Remember:** Hooks are safety nets"
        
    def should_trigger(self, tool_name: str, args: Dict) -> bool:
        """Check if we should update CLAUDE.md"""
        if tool_name not in ["Write", "Edit", "MultiEdit"]:
            return False
            
        file_path = args.get("file_path", "")
        
        # Check if modifying relevant files
        relevant_paths = [
            ".claude/logic/hooks/",
            ".claude/logic/scripts/",
            ".claude/logic/commands/",
            "settings.json"
        ]
        
        return any(path in file_path for path in relevant_paths)
    
    def post_tool_use(self, tool_name: str, args: Dict, result: Any):
        """Update CLAUDE.md after relevant changes"""
        if not self.should_trigger(tool_name, args):
            return
        
        try:
            # Analyze all hooks
            hook_analysis = self.analyze_all_hooks()
            
            if hook_analysis:
                # Update CLAUDE.md
                self.update_claude_md(hook_analysis)
                
                print(MessageFormatter.format_info(
                    "CLAUDE.md updated with new hook warnings"
                ))
        except Exception as e:
            print(MessageFormatter.format_warning(
                f"Failed to update CLAUDE.md: {str(e)}"
            ))
    
    def analyze_all_hooks(self) -> Dict[str, Dict]:
        """Analyze all hook files for documentation"""
        hook_data = {}
        
        # Scan all hook directories
        for category_dir in self.hooks_dir.iterdir():
            if not category_dir.is_dir() or category_dir.name.startswith('.'):
                continue
                
            for hook_file in category_dir.glob("*.py"):
                if hook_file.name.startswith('__'):
                    continue
                    
                analysis = self.analyze_hook_file(hook_file)
                if analysis:
                    category = self.categorize_hook(hook_file.stem)
                    if category not in hook_data:
                        hook_data[category] = {}
                    hook_data[category][hook_file.stem] = analysis
        
        return hook_data
    
    def analyze_hook_file(self, hook_path: Path) -> Optional[Dict]:
        """Extract documentation from a hook file"""
        try:
            content = hook_path.read_text()
            
            # Extract docstring
            docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
            if not docstring_match:
                return None
                
            docstring = docstring_match.group(1)
            
            analysis = {
                "purpose": [],
                "pitfalls": [],
                "mistakes": []
            }
            
            # Extract each type of information
            for key, pattern in self.extraction_patterns.items():
                match = re.search(pattern, docstring, re.MULTILINE | re.IGNORECASE)
                if match:
                    items = match.group(1).strip().split('\n')
                    analysis[key] = [
                        item.strip().lstrip('-•').strip() 
                        for item in items if item.strip()
                    ]
            
            # Also check for inline comments about pitfalls
            pitfall_comments = re.findall(
                r'#\s*(?:PITFALL|WARNING|GOTCHA):\s*(.+)', 
                content
            )
            analysis["pitfalls"].extend(pitfall_comments)
            
            return analysis if any(analysis.values()) else None
            
        except Exception:
            return None
    
    def categorize_hook(self, hook_name: str) -> str:
        """Categorize hook by name"""
        categories = {
            "quality": "Quality Hook",
            "security": "Security Hook", 
            "memory": "Memory Hook",
            "pattern": "Pattern Extraction",
            "task": "Task Management",
            "session": "Session Management",
            "context": "Context Management"
        }
        
        for key, category in categories.items():
            if key in hook_name.lower():
                return category
                
        return "Other Hooks"
    
    def update_claude_md(self, hook_data: Dict[str, Dict]):
        """Update CLAUDE.md with new hook warnings"""
        if not self.claude_md_path.exists():
            return
            
        content = self.claude_md_path.read_text()
        
        # Find the hook warnings section
        start_idx = content.find(self.section_start)
        if start_idx == -1:
            # Section doesn't exist, add it
            self.add_warnings_section(content, hook_data)
            return
            
        end_idx = content.find(self.section_end, start_idx)
        if end_idx == -1:
            print(MessageFormatter.format_warning(
                "Could not find end marker for hook warnings section"
            ))
            return
            
        # Generate new section content
        new_section = self.generate_warnings_section(hook_data)
        
        # Replace section content
        before = content[:start_idx]
        after = content[end_idx:]
        
        new_content = before + new_section + "\n\n" + after
        
        # Add update timestamp as comment
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_content = new_content.replace(
            self.section_start,
            f"{self.section_start}\n<!-- Auto-updated: {timestamp} -->"
        )
        
        self.claude_md_path.write_text(new_content)
    
    def generate_warnings_section(self, hook_data: Dict[str, Dict]) -> str:
        """Generate the warnings section content"""
        lines = [self.section_start, ""]
        lines.append("### What Hooks Automate (But You Might Still Break)")
        lines.append("")
        lines.append("Even with hooks enabled, these mistakes can still happen:")
        lines.append("")
        
        category_num = 1
        for category, hooks in hook_data.items():
            # Aggregate pitfalls for this category
            all_pitfalls = []
            all_mistakes = []
            
            for hook_name, analysis in hooks.items():
                all_pitfalls.extend(analysis.get("pitfalls", []))
                all_mistakes.extend(analysis.get("mistakes", []))
            
            # Remove duplicates while preserving order
            pitfalls = list(dict.fromkeys(all_pitfalls))
            mistakes = list(dict.fromkeys(all_mistakes))
            
            if pitfalls or mistakes:
                lines.append(f"#### {category_num}. {category} Pitfalls")
                
                # Add pitfalls
                for pitfall in pitfalls[:4]:  # Limit to 4 most important
                    lines.append(f"- ❌ **{self.format_pitfall(pitfall)}**")
                
                # Add mistakes if different from pitfalls
                for mistake in mistakes[:2]:  # Add up to 2 mistakes
                    if not any(mistake.lower() in p.lower() for p in pitfalls):
                        lines.append(f"- ❌ **{self.format_pitfall(mistake)}**")
                
                lines.append("")
                category_num += 1
        
        return "\n".join(lines)
    
    def format_pitfall(self, pitfall: str) -> str:
        """Format a pitfall for display"""
        # Clean up the pitfall text
        pitfall = pitfall.strip()
        
        # Add explanation if not present
        if " - " not in pitfall:
            # Try to add a brief explanation
            if "test" in pitfall.lower():
                pitfall += " - Hook reminds but can't force"
            elif "secret" in pitfall.lower():
                pitfall += " - Scanner might miss this"
            elif "memory" in pitfall.lower():
                pitfall += " - Not automated, requires manual action"
            elif "pattern" in pitfall.lower():
                pitfall += " - Auto-extraction has limits"
            elif "task" in pitfall.lower():
                pitfall += " - File operations bypass checks"
        
        return pitfall
    
    def add_warnings_section(self, content: str, hook_data: Dict[str, Dict]):
        """Add warnings section if it doesn't exist"""
        # Find where to insert (after automation section)
        insert_after = "## 4. 🤖 AUTOMATION & HOOKS"
        
        idx = content.find(insert_after)
        if idx == -1:
            print(MessageFormatter.format_warning(
                "Could not find automation section to insert warnings"
            ))
            return
            
        # Find the next section
        next_section_idx = content.find("\n## ", idx + len(insert_after))
        if next_section_idx == -1:
            next_section_idx = len(content)
            
        # Generate section
        new_section = self.generate_warnings_section(hook_data)
        
        # Insert before the next section
        before = content[:next_section_idx]
        after = content[next_section_idx:]
        
        new_content = before + "\n\n" + new_section + "\n\n" + self.section_end + "\n" + after
        
        self.claude_md_path.write_text(new_content)


def main():
    """Test the hook"""
    hook = ClaudeMdUpdateHook()
    
    # Analyze all hooks
    print("Analyzing hooks...")
    analysis = hook.analyze_all_hooks()
    
    # Display results
    for category, hooks in analysis.items():
        print(f"\n{category}:")
        for hook_name, data in hooks.items():
            print(f"  {hook_name}:")
            if data['pitfalls']:
                print(f"    Pitfalls: {len(data['pitfalls'])}")
            if data['mistakes']:
                print(f"    Mistakes: {len(data['mistakes'])}")


if __name__ == "__main__":
    main()