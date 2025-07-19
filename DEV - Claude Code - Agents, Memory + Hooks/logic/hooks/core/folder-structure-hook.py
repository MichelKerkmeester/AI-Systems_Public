#!/usr/bin/env python3
"""
Folder Structure Validation Hook

Ensures files are created in the correct locations and prevents duplicate
folder structures. Automatically suggests correct paths when files are
being created in wrong locations.

What it does:
- Monitors file operations to detect incorrect paths
- Suggests correct locations based on file type
- Updates hardcoded paths in documentation
- Prevents creation of duplicate folder structures
- Maintains consistency across the project

What could go wrong:
- False positives for legitimate new directories
- Performance impact on large file operations
- Path corrections might break external references
- Conflicts with user's intentional structure changes
"""

import os
import re
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any

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
        @staticmethod
        def format_suggestion(msg): return f"💡 {msg}"


class FolderStructureHook(HookBase):
    def __init__(self):
        super().__init__("FolderStructure")
        
        # Define correct folder structure
        self.correct_structure = {
            # Documentation should go to y__docs
            "docs": ".claude/y__docs/",
            "documentation": ".claude/y__docs/",
            "doc": ".claude/y__docs/",
            
            # Archive locations
            "archive": ".claude/z__archive/",
            "archived": ".claude/z__archive/",
            
            # Standard directories
            "agents": ".claude/agents/",
            "hooks": ".claude/logic/hooks/",
            "logic": ".claude/logic/",
            "project": ".claude/project/",
            "scripts": ".claude/scripts/",
            
            # Knowledge files
            "knowledge": ".claude/project/knowledge/",
            "patterns": ".claude/project/knowledge/",
            "facts": ".claude/project/knowledge/",
            "constraints": ".claude/project/knowledge/",
            
            # Tasks
            "tasks": ".claude/project/tasks/",
            "todos": ".claude/project/tasks/",
            
            # Sessions
            "sessions": ".claude/project/sessions/",
            "session": ".claude/project/sessions/"
        }
        
        # Incorrect path patterns to detect
        self.incorrect_patterns = {
            r"\.claude/docs/": ".claude/y__docs/",
            r"\.claude/project/docs/": ".claude/y__docs/",
            r"\.claude/documentation/": ".claude/y__docs/",
            r"\.claude/project/documentation/": ".claude/y__docs/",
            r"\.claude/archive/": ".claude/z__archive/",
            r"\.claude/project/archive/": ".claude/z__archive/"
        }
        
    def pre_tool_use(self, tool_name: str, args: Dict) -> Optional[Dict]:
        """Check file paths before operations"""
        if tool_name not in ["Write", "Edit", "MultiEdit"]:
            return None
            
        file_path = str(args.get("file_path", ""))
        if not file_path:
            return None
            
        # Check for incorrect paths
        suggestion = self.check_path(file_path)
        if suggestion:
            # Block creation in .claude/docs/ directory
            if ".claude/docs/" in file_path and ".claude/docs/README.md" not in file_path:
                print(MessageFormatter.format_error(
                    f"❌ BLOCKED: Cannot create files in deprecated location: {file_path}"
                ))
                print(MessageFormatter.format_suggestion(
                    f"✅ Use this location instead: {suggestion}"
                ))
                
                # Return error to block the operation
                return {
                    "error": f"File creation blocked. Use {suggestion} instead of {file_path}",
                    "suggestion": suggestion
                }
            
            # For other incorrect paths, just warn
            print(MessageFormatter.format_warning(
                f"File being created in incorrect location: {file_path}"
            ))
            print(MessageFormatter.format_suggestion(
                f"Suggested location: {suggestion}"
            ))
            
            # Don't block non-docs paths, just warn
            return None
        
        # Check for kebab-case naming convention for markdown files
        if file_path.endswith(".md"):
            filename = Path(file_path).name
            # Skip README files and CLAUDE.md
            if filename not in ["README.md", "CLAUDE.md"]:
                # Check if filename follows kebab-case
                if not self.is_kebab_case(filename[:-3]):  # Remove .md extension
                    print(MessageFormatter.format_warning(
                        f"⚠️  Markdown filename should use kebab-case: {filename}"
                    ))
                    kebab_name = self.to_kebab_case(filename[:-3]) + ".md"
                    print(MessageFormatter.format_suggestion(
                        f"✅ Suggested name: {kebab_name}"
                    ))
                    
                    # For new files in .claude/, enforce kebab-case
                    if ".claude/" in file_path and tool_name == "Write":
                        suggested_path = str(Path(file_path).parent / kebab_name)
                        return {
                            "error": f"Markdown files must use kebab-case. Use {kebab_name} instead of {filename}",
                            "suggestion": suggested_path
                        }
            
        return None
    
    def post_tool_use(self, tool_name: str, args: Dict, result: Any):
        """Check for incorrect references after file operations"""
        if tool_name not in ["Write", "Edit", "MultiEdit"]:
            return
            
        file_path = str(args.get("file_path", ""))
        
        # If editing documentation or scripts, check for incorrect paths
        if any(doc_type in file_path for doc_type in [".md", ".py", ".json"]):
            self.check_and_fix_references(file_path)
    
    def check_path(self, file_path: str) -> Optional[str]:
        """Check if path is incorrect and suggest correction"""
        path_str = str(file_path)
        
        # Check against incorrect patterns
        for pattern, correct_base in self.incorrect_patterns.items():
            if re.search(pattern, path_str):
                # Extract the relative part after the incorrect base
                match = re.search(pattern + r"(.+)", path_str)
                if match:
                    relative_part = match.group(1)
                    
                    # Special handling for nested structures
                    if "y__docs" in relative_part:
                        # Remove redundant y__docs if present
                        relative_part = relative_part.replace("y__docs/", "")
                    
                    suggested = os.path.join(correct_base, relative_part)
                    return suggested
        
        # Check for files that should be in specific locations
        filename = os.path.basename(file_path)
        
        # Knowledge files
        if filename in ["facts.json", "patterns.json", "constraints.json", "security-patterns.json"]:
            if ".claude/project/knowledge/" not in path_str:
                return f".claude/project/knowledge/{filename}"
        
        # Hook files
        if filename.endswith("-hook.py") and ".claude/logic/hooks/" not in path_str:
            # Determine hook category from filename
            category = self.determine_hook_category(filename)
            return f".claude/logic/hooks/{category}/{filename}"
        
        return None
    
    def determine_hook_category(self, filename: str) -> str:
        """Determine which category a hook belongs to"""
        categories = {
            "quality": ["quality", "lint", "format"],
            "security": ["security", "scan", "auth"],
            "memory": ["memory", "graphiti", "context"],
            "session": ["session", "save", "restore"],
            "core": ["system", "folder", "claude-md", "pattern", "task", "workflow"]
        }
        
        filename_lower = filename.lower()
        for category, keywords in categories.items():
            if any(keyword in filename_lower for keyword in keywords):
                return category
                
        return "core"  # Default category
    
    def is_kebab_case(self, name: str) -> bool:
        """Check if a name follows kebab-case convention"""
        # Kebab case: lowercase letters, numbers, and hyphens only
        # Must not start or end with hyphen
        # No consecutive hyphens
        import re
        pattern = r'^[a-z0-9]+(-[a-z0-9]+)*$'
        return bool(re.match(pattern, name))
    
    def to_kebab_case(self, name: str) -> str:
        """Convert a name to kebab-case"""
        import re
        # Replace spaces, underscores with hyphens
        name = re.sub(r'[\s_]+', '-', name)
        # Insert hyphens before capital letters (for camelCase)
        name = re.sub(r'([a-z])([A-Z])', r'\1-\2', name)
        # Convert to lowercase
        name = name.lower()
        # Replace multiple hyphens with single hyphen
        name = re.sub(r'-+', '-', name)
        # Remove leading/trailing hyphens
        name = name.strip('-')
        # Remove any non-alphanumeric characters except hyphens
        name = re.sub(r'[^a-z0-9-]', '', name)
        return name
    
    def check_and_fix_references(self, file_path: str):
        """Check file for incorrect path references"""
        try:
            path = Path(file_path)
            if not path.exists():
                return
                
            content = path.read_text()
            original_content = content
            
            # Check for incorrect path references in content
            fixes_made = []
            
            for pattern, correct_base in self.incorrect_patterns.items():
                matches = re.finditer(pattern + r"([^\s\"'`]+)", content)
                for match in matches:
                    full_path = match.group(0)
                    relative_part = match.group(1)
                    
                    # Skip if it's just explaining the structure
                    if any(skip in content[max(0, match.start()-50):match.end()+50] 
                           for skip in ["incorrect", "wrong", "should be", "not", "avoid"]):
                        continue
                    
                    correct_path = correct_base + relative_part
                    content = content.replace(full_path, correct_path)
                    fixes_made.append((full_path, correct_path))
            
            # Only write if changes were made
            if content != original_content and fixes_made:
                # Log the fixes
                print(MessageFormatter.format_info(
                    f"Fixed {len(fixes_made)} incorrect path references in {file_path}:"
                ))
                for old, new in fixes_made[:3]:  # Show first 3
                    print(f"  • {old} → {new}")
                if len(fixes_made) > 3:
                    print(f"  • ... and {len(fixes_made) - 3} more")
                    
        except Exception as e:
            # Don't fail silently, but don't break the operation
            print(MessageFormatter.format_warning(
                f"Could not check references in {file_path}: {e}"
            ))
    
    def validate_structure(self) -> Dict[str, Any]:
        """Validate entire folder structure"""
        issues = []
        
        # Check for duplicate/incorrect directories
        claude_dir = self.project_root / ".claude"
        
        # Check for incorrect docs directory
        if (claude_dir / "docs").exists():
            issues.append({
                "type": "incorrect_directory",
                "path": ".claude/docs/",
                "suggestion": "Move contents to .claude/y__docs/"
            })
        
        # Check for files in wrong locations
        for root, dirs, files in os.walk(claude_dir):
            root_path = Path(root)
            
            # Check each file
            for file in files:
                file_path = root_path / file
                relative_path = file_path.relative_to(self.project_root)
                
                suggestion = self.check_path(str(relative_path))
                if suggestion:
                    issues.append({
                        "type": "misplaced_file",
                        "path": str(relative_path),
                        "suggestion": suggestion
                    })
        
        return {
            "valid": len(issues) == 0,
            "issues": issues
        }


def main():
    """Test the hook"""
    hook = FolderStructureHook()
    
    # Test path checking
    test_paths = [
        ".claude/docs/technical/test.md",
        ".claude/documentation/api.md",
        ".claude/project/docs/readme.md",
        ".claude/logic/hooks/test-hook.py",
        ".claude/project/patterns.json"
    ]
    
    print("Testing path validation:\n")
    for path in test_paths:
        suggestion = hook.check_path(path)
        if suggestion:
            print(f"❌ {path}")
            print(f"   → {suggestion}\n")
        else:
            print(f"✅ {path}\n")
    
    # Validate current structure
    print("\nValidating folder structure:")
    result = hook.validate_structure()
    
    if result["valid"]:
        print("✅ Folder structure is correct!")
    else:
        print(f"❌ Found {len(result['issues'])} issues:")
        for issue in result["issues"]:
            print(f"\n  • {issue['type']}: {issue['path']}")
            print(f"    Suggestion: {issue['suggestion']}")


if __name__ == "__main__":
    main()