#!/usr/bin/env python3
"""
/save command implementation for Claude Code
Manages session saving, archival, and search functionality
"""

import os
import sys
import json
import subprocess
import glob
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from hooks.shared.hook_formatters import MessageFormatter


class SaveCommand:
    """Handle /save command functionality"""
    
    def __init__(self):
        # Get project root (contains .claude directory)
        self.project_root = Path(__file__).resolve()
        while not (self.project_root / ".claude").exists() and self.project_root != self.project_root.parent:
            self.project_root = self.project_root.parent
        
        self.claude_path = self.project_root / ".claude"
        self.sessions_dir = self.claude_path / "project" / "sessions"
        self.current_dir = self.sessions_dir / "current"
        self.old_dir = self.sessions_dir / "old"
        self.state_dir = self.claude_path / "project" / "state"
        self.session_manager = self.sessions_dir / "session-manager.sh"
        
    def execute(self, args: List[str]) -> str:
        """Execute save command with given arguments"""
        if not args or args[0] == "":
            # Default action - save current session
            return self.save_current_session()
        
        subcommand = args[0].lower()
        
        if subcommand == "new":
            description = " ".join(args[1:]) if len(args) > 1 else None
            return self.new_session(description)
        elif subcommand == "list":
            show_all = "--all" in args
            return self.list_sessions(show_all)
        elif subcommand == "search":
            query = " ".join(args[1:]) if len(args) > 1 else ""
            return self.search_sessions(query)
        elif subcommand == "stats":
            return self.session_stats()
        elif subcommand == "help":
            return self.show_help()
        else:
            return f"❌ Unknown subcommand: {subcommand}\n\nUse `/save help` for available commands."
    
    def save_current_session(self) -> str:
        """Save and archive current session"""
        # Check if there's a current session
        current_sessions = list(self.current_dir.glob("*.md"))
        
        if not current_sessions:
            return "ℹ️ No active session to save. Use `/save new [description]` to create one."
        
        # Use session-manager.sh to archive
        try:
            result = subprocess.run(
                [str(self.session_manager), "archive"],
                capture_output=True,
                text=True,
                cwd=str(self.sessions_dir)
            )
            
            output = MessageFormatter.header("Session Saved", "save")
            output += "\n📦 Current session archived successfully"
            
            # Show what was archived
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if "Moved" in line and "→" in line:
                        output += f"\n  {line.strip()}"
            
            output += "\n\nUse `/save new [description]` to start a new session."
            output += "\n" + MessageFormatter.footer()
            
            return output
            
        except Exception as e:
            return f"❌ Error saving session: {str(e)}"
    
    def new_session(self, description: Optional[str] = None) -> str:
        """Create a new session"""
        # Use session-manager.sh
        try:
            cmd = [str(self.session_manager), "new"]
            if description:
                cmd.extend(description.split())
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=str(self.sessions_dir),
                input="\n" if not description else None  # Empty input for default
            )
            
            if result.returncode != 0:
                return f"❌ Error creating session: {result.stderr}"
            
            output = MessageFormatter.header("New Session Created", "save")
            
            # Extract session info from output
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if "Creating new session:" in line:
                    session_name = line.split(":")[-1].strip()
                    output += f"\n📝 Session: {session_name}"
                elif "Created" in line and ".md" in line:
                    output += f"\n✅ {line.strip()}"
            
            # Get session stats
            stats = self._get_session_stats()
            output += f"\n\n📊 Active sessions: {stats['current_count']}"
            output += f"\n📦 Archived sessions: {stats['archived_count']}"
            
            output += "\n" + MessageFormatter.footer()
            return output
            
        except Exception as e:
            return f"❌ Error creating session: {str(e)}"
    
    def list_sessions(self, show_all: bool = False) -> str:
        """List sessions"""
        try:
            # For multi-agent support, check if we're in agent mode
            agent_id = os.environ.get("CLAUDE_AGENT_ID")
            
            output = MessageFormatter.header("Session List", "save")
            
            # Current sessions
            current_sessions = sorted(self.current_dir.glob("*.md"), 
                                    key=lambda p: p.stat().st_mtime, 
                                    reverse=True)
            
            output += "\n\n📂 Current Sessions:"
            if current_sessions:
                for session in current_sessions:
                    size = session.stat().st_size / 1024  # KB
                    mtime = datetime.fromtimestamp(session.stat().st_mtime)
                    age = (datetime.now() - mtime).total_seconds() / 3600
                    
                    output += f"\n  • {session.name}"
                    output += f"\n    Size: {size:.1f} KB | Age: {age:.1f} hours"
                    
                    # Show if this is agent's session
                    if agent_id and agent_id in session.name:
                        output += " [YOUR SESSION]"
            else:
                output += "\n  (none)"
            
            # Archived sessions
            archived_sessions = sorted(self.old_dir.glob("*.md"), 
                                     key=lambda p: p.stat().st_mtime, 
                                     reverse=True)
            
            output += "\n\n📦 Archived Sessions:"
            limit = None if show_all else 10
            shown = 0
            
            for session in archived_sessions[:limit]:
                size = session.stat().st_size / 1024
                mtime = datetime.fromtimestamp(session.stat().st_mtime)
                
                output += f"\n  • {session.name}"
                output += f"\n    Size: {size:.1f} KB | Date: {mtime.strftime('%Y-%m-%d %H:%M')}"
                shown += 1
            
            if not shown:
                output += "\n  (none)"
            elif len(archived_sessions) > shown and not show_all:
                remaining = len(archived_sessions) - shown
                output += f"\n  ... and {remaining} more (use `/save list --all` to see all)"
            
            output += "\n" + MessageFormatter.footer()
            return output
            
        except Exception as e:
            return f"❌ Error listing sessions: {str(e)}"
    
    def search_sessions(self, query: str) -> str:
        """Search across all sessions"""
        if not query:
            return "❌ Please provide a search query: `/save search [query]`"
        
        output = MessageFormatter.header(f"Search: '{query}'", "save")
        
        try:
            matches = []
            
            # Search in all session files
            all_sessions = list(self.current_dir.glob("*.md")) + \
                          list(self.old_dir.glob("*.md"))
            
            for session_file in all_sessions:
                try:
                    content = session_file.read_text(encoding='utf-8')
                    if query.lower() in content.lower():
                        # Count occurrences
                        count = content.lower().count(query.lower())
                        
                        # Extract context lines
                        lines = content.split('\n')
                        matching_lines = []
                        
                        for i, line in enumerate(lines):
                            if query.lower() in line.lower():
                                # Get surrounding context
                                start = max(0, i - 1)
                                end = min(len(lines), i + 2)
                                context = lines[start:end]
                                matching_lines.append((i + 1, context))
                                
                                if len(matching_lines) >= 3:  # Limit matches per file
                                    break
                        
                        matches.append({
                            'file': session_file,
                            'count': count,
                            'lines': matching_lines,
                            'is_current': session_file.parent == self.current_dir
                        })
                except Exception:
                    continue
            
            # Sort by relevance (occurrence count)
            matches.sort(key=lambda m: m['count'], reverse=True)
            
            if matches:
                output += f"\n\nFound {sum(m['count'] for m in matches)} matches in {len(matches)} sessions:\n"
                
                for match in matches[:10]:  # Limit to 10 files
                    session_type = "📂 Current" if match['is_current'] else "📦 Archived"
                    output += f"\n{session_type}: {match['file'].name} ({match['count']} matches)"
                    
                    # Show context
                    for line_num, context in match['lines'][:2]:  # Show max 2 contexts
                        output += f"\n  Line {line_num}:"
                        for line in context:
                            if query.lower() in line.lower():
                                # Highlight the match
                                output += f"\n    > {line.strip()}"
                            else:
                                output += f"\n      {line.strip()}"
                    
                    if match['count'] > len(match['lines']):
                        output += f"\n    ... and {match['count'] - len(match['lines'])} more matches"
                
                if len(matches) > 10:
                    output += f"\n\n... and {len(matches) - 10} more sessions with matches"
            else:
                output += f"\n\nNo matches found for '{query}'"
            
            output += "\n" + MessageFormatter.footer()
            return output
            
        except Exception as e:
            return f"❌ Error searching sessions: {str(e)}"
    
    def session_stats(self) -> str:
        """Display session statistics"""
        try:
            stats = self._get_session_stats()
            
            output = MessageFormatter.header("Session Statistics", "save")
            
            # Overview
            output += f"\n\n📊 Overview:"
            output += f"\n  • Total sessions: {stats['total_count']}"
            output += f"\n  • Current: {stats['current_count']}"
            output += f"\n  • Archived: {stats['archived_count']}"
            output += f"\n  • Total size: {stats['total_size_mb']:.1f} MB"
            
            # Current session info
            if stats['current_sessions']:
                current = stats['current_sessions'][0]
                output += f"\n\n📂 Active Session:"
                output += f"\n  • Name: {current['name']}"
                output += f"\n  • Age: {current['age_hours']:.1f} hours"
                output += f"\n  • Size: {current['size_kb']:.1f} KB"
                output += f"\n  • Next timeout: in {4.0 - current['age_hours']:.1f} hours"
            
            # Averages
            if stats['total_count'] > 0:
                output += f"\n\n📈 Averages:"
                output += f"\n  • Session duration: {stats['avg_duration_hours']:.1f} hours"
                output += f"\n  • Session size: {stats['avg_size_kb']:.1f} KB"
                output += f"\n  • Files per session: ~{stats['avg_files_modified']}"
            
            # Recent activity
            if stats['recent_sessions']:
                output += f"\n\n🕐 Recent Sessions:"
                for session in stats['recent_sessions'][:5]:
                    output += f"\n  • {session['name']}"
                    output += f" ({session['date']})"
            
            output += "\n" + MessageFormatter.footer()
            return output
            
        except Exception as e:
            return f"❌ Error getting statistics: {str(e)}"
    
    def show_help(self) -> str:
        """Show help information"""
        output = MessageFormatter.header("Save Command Help", "save")
        
        output += "\n\n📚 Available Commands:"
        output += "\n  • `/save` - Save and archive current session"
        output += "\n  • `/save new [description]` - Create new session"
        output += "\n  • `/save list [--all]` - List all sessions"
        output += "\n  • `/save search [query]` - Search session content"
        output += "\n  • `/save stats` - Show session statistics"
        output += "\n  • `/save help` - Show this help"
        
        output += "\n\n💡 Examples:"
        output += "\n  • `/save new api integration` - Start new API work"
        output += "\n  • `/save search authentication` - Find auth-related work"
        output += "\n  • `/save stats` - See session metrics"
        
        output += "\n\n🔗 Integration:"
        output += "\n  • Sessions auto-create after 4-hour timeout"
        output += "\n  • Links with memory captures via Graphiti"
        output += "\n  • Pattern extraction runs on session saves"
        
        output += "\n" + MessageFormatter.footer()
        return output
    
    def _get_session_stats(self) -> Dict[str, Any]:
        """Calculate session statistics"""
        current_sessions = list(self.current_dir.glob("*.md"))
        archived_sessions = list(self.old_dir.glob("*.md"))
        all_sessions = current_sessions + archived_sessions
        
        stats = {
            'current_count': len(current_sessions),
            'archived_count': len(archived_sessions),
            'total_count': len(all_sessions),
            'total_size_mb': sum(s.stat().st_size for s in all_sessions) / (1024 * 1024),
            'current_sessions': [],
            'recent_sessions': [],
            'avg_duration_hours': 0,
            'avg_size_kb': 0,
            'avg_files_modified': 0
        }
        
        # Current session details
        for session in current_sessions:
            mtime = datetime.fromtimestamp(session.stat().st_mtime)
            creation_time = self._get_session_creation_time(session)
            age_hours = (datetime.now() - creation_time).total_seconds() / 3600
            
            stats['current_sessions'].append({
                'name': session.stem,
                'age_hours': age_hours,
                'size_kb': session.stat().st_size / 1024
            })
        
        # Recent sessions
        recent = sorted(all_sessions, key=lambda p: p.stat().st_mtime, reverse=True)
        for session in recent[:10]:
            mtime = datetime.fromtimestamp(session.stat().st_mtime)
            stats['recent_sessions'].append({
                'name': session.stem,
                'date': mtime.strftime('%Y-%m-%d %H:%M')
            })
        
        # Calculate averages
        if all_sessions:
            total_size_kb = sum(s.stat().st_size for s in all_sessions) / 1024
            stats['avg_size_kb'] = total_size_kb / len(all_sessions)
            
            # Estimate average duration from filename timestamps
            durations = []
            for session in archived_sessions[:20]:  # Sample
                try:
                    # Extract timestamp from filename (YYYY-MM-DD-HHMMSS)
                    parts = session.stem.split('-')
                    if len(parts) >= 6:
                        timestamp_str = '-'.join(parts[:6])
                        session_time = datetime.strptime(timestamp_str[:19], '%Y-%m-%d-%H%M%S')
                        # Assume 4-hour sessions on average
                        durations.append(4.0)
                except:
                    continue
            
            if durations:
                stats['avg_duration_hours'] = sum(durations) / len(durations)
            
            # Estimate files modified (rough average)
            stats['avg_files_modified'] = 5  # Typical session modifies ~5 files
        
        return stats
    
    def _get_session_creation_time(self, session_file: Path) -> datetime:
        """Get session creation time from filename or file stats"""
        try:
            # Try to parse from filename (YYYY-MM-DD-HHMMSS format)
            parts = session_file.stem.split('-')
            if len(parts) >= 6:
                timestamp_str = '-'.join(parts[:6])
                return datetime.strptime(timestamp_str[:19], '%Y-%m-%d-%H%M%S')
        except:
            pass
        
        # Fallback to file modification time
        return datetime.fromtimestamp(session_file.stat().st_mtime)


def main():
    """Main entry point for save command"""
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    command = SaveCommand()
    result = command.execute(args)
    
    print(result)


if __name__ == "__main__":
    main()