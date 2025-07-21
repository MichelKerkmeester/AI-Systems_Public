#!/usr/bin/env python3
"""
Documentation Update Hook
Automatically maintains documentation when changes are detected
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

# Add parent directories to path
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import ToolHook, MessageFormatter

class DocUpdateHook(ToolHook):
    """Hook that automatically updates documentation"""
    
    def __init__(self):
        super().__init__()
        self.formatter = MessageFormatter()
        self.state_file = Path(__file__).parent.parent.parent / "state" / "doc-update-state.json"
        self.doc_updater = Path(__file__).parent.parent.parent / "scripts" / "doc-updater.py"
        
    def can_handle(self, request_data: dict) -> bool:
        """Check if this affects documentation"""
        # Trigger on documentation file changes
        if request_data.get("name") in ["Write", "Edit", "MultiEdit"]:
            file_path = request_data.get("arguments", {}).get("file_path", "")
            return ".claude/docs" in file_path and file_path.endswith(".md")
        
        # Also trigger on /save commands for periodic updates
        if request_data.get("name") == "save-command":
            return self._should_run_periodic_update()
            
        return False
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        """Process documentation updates"""
        # Load state
        state = self._load_state()
        
        # Check if we should run update
        if not self._should_update(state, request_data):
            return {"status": 0}
        
        # Run documentation updater
        try:
            result = subprocess.run(
                ["python3", str(self.doc_updater)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # Parse output
                output_lines = result.stdout.strip().split('\n')
                files_updated = 0
                broken_links = 0
                
                for line in output_lines:
                    if "Files updated:" in line:
                        files_updated = int(line.split(":")[1].strip())
                    elif "Broken links found:" in line:
                        broken_links = int(line.split(":")[1].strip())
                
                # Update state
                state["last_update"] = datetime.now().isoformat()
                state["update_count"] += 1
                state["total_files_updated"] += files_updated
                state["last_broken_links"] = broken_links
                self._save_state(state)
                
                # Generate output if issues found
                if broken_links > 0:
                    output = self._generate_broken_links_output(broken_links)
                    return {
                        "status": 0,
                        "output": output,
                        "priority": "high"
                    }
                elif files_updated > 0:
                    # Silent update for successful updates
                    return {
                        "status": 0,
                        "silent": True,
                        "metadata": {
                            "files_updated": files_updated
                        }
                    }
            
        except subprocess.TimeoutExpired:
            # Documentation update took too long
            return {
                "status": 0,
                "output": "Documentation update timed out. Run manually: `python3 .claude/logic/scripts/doc-updater.py`"
            }
        except Exception as e:
            # Log error but don't fail the operation
            return {
                "status": 0,
                "error": str(e)
            }
        
        return {"status": 0}
    
    def _load_state(self) -> Dict[str, Any]:
        """Load hook state"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        
        return {
            "last_update": None,
            "update_count": 0,
            "total_files_updated": 0,
            "last_broken_links": 0
        }
    
    def _save_state(self, state: Dict[str, Any]):
        """Save hook state"""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def _should_update(self, state: Dict[str, Any], request_data: dict) -> bool:
        """Determine if update should run"""
        # Always run on direct doc changes
        if request_data.get("name") in ["Write", "Edit", "MultiEdit"]:
            return True
        
        # Check periodic update interval (daily)
        if state["last_update"]:
            last_update = datetime.fromisoformat(state["last_update"])
            if datetime.now() - last_update < timedelta(hours=24):
                return False
        
        return True
    
    def _should_run_periodic_update(self) -> bool:
        """Check if periodic update is due"""
        state = self._load_state()
        
        if not state["last_update"]:
            return True
        
        last_update = datetime.fromisoformat(state["last_update"])
        return datetime.now() - last_update > timedelta(hours=24)
    
    def _generate_broken_links_output(self, count: int) -> str:
        """Generate output for broken links"""
        output = self.formatter.header("Documentation Issues Found", "docs")
        
        items = [
            f"⚠️ Found {count} broken link{'s' if count > 1 else ''} in documentation",
            "",
            "To view details and fix:",
            "`cat .claude/docs/UPDATE_REPORT.md`",
            "",
            "To manually run documentation update:",
            "`python3 .claude/logic/scripts/doc-updater.py`"
        ]
        
        output += self.formatter.section("Action Required", items, "warning")
        output += self.formatter.footer()
        
        return output

if __name__ == "__main__":
    # Hook integration
    from logic.shared import process_hook_request
    process_hook_request(DocUpdateHook)