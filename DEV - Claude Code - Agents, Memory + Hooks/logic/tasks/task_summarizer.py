#!/usr/bin/env python3
"""
Task Summary Generator for Claude Code
Generates completion summaries when tasks are marked as complete
"""

import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
import json


class TaskSummarizer:
    """Generates summaries for completed tasks"""
    
    def __init__(self):
        """Initialize task summarizer"""
        self.summary_template = """

## 📋 Completion Summary

**Completed:** {completed_date}
**Duration:** {duration}
**Files Changed:** {files_changed}

### 🎯 What Was Done
{what_was_done}

### 🔧 Key Changes
{key_changes}

### 📊 Impact
{impact}

### 💡 Lessons Learned
{lessons_learned}

### 🔗 Related Resources
{related_resources}

---
*Summary generated automatically by Task Summarizer*
"""
    
    def generate_summary(self, task_file_path: Path, todo_data: Optional[Dict[str, Any]] = None) -> str:
        """Generate a summary for a completed task"""
        # Read task file content
        content = task_file_path.read_text()
        
        # Extract task metadata
        metadata = self._extract_metadata(content)
        
        # Calculate duration
        duration = self._calculate_duration(metadata)
        
        # Analyze content for key information
        analysis = self._analyze_task_content(content, todo_data)
        
        # Build summary data
        summary_data = {
            "completed_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "duration": duration,
            "files_changed": analysis.get("files_changed", "N/A"),
            "what_was_done": self._format_list(analysis.get("what_was_done", [])),
            "key_changes": self._format_list(analysis.get("key_changes", [])),
            "impact": self._format_list(analysis.get("impact", [])),
            "lessons_learned": self._format_list(analysis.get("lessons_learned", [])),
            "related_resources": self._format_list(analysis.get("related_resources", []))
        }
        
        # Generate summary
        summary = self.summary_template.format(**summary_data)
        
        return summary
    
    def _extract_metadata(self, content: str) -> Dict[str, str]:
        """Extract metadata from task content"""
        metadata = {}
        
        # Extract created date
        created_match = re.search(r'Created:\s*(\d{4}-\d{2}-\d{2})', content)
        if created_match:
            metadata['created'] = created_match.group(1)
        
        # Extract task name
        name_match = re.search(r'#\s*Task:\s*(.+)', content)
        if name_match:
            metadata['name'] = name_match.group(1).strip()
        
        # Extract priority
        priority_match = re.search(r'Priority:\s*(\w+)', content)
        if priority_match:
            metadata['priority'] = priority_match.group(1)
        
        # Extract effort estimates
        est_effort_match = re.search(r'Estimated Effort:\s*(.+)', content)
        if est_effort_match:
            metadata['estimated_effort'] = est_effort_match.group(1)
        
        actual_effort_match = re.search(r'Actual Effort:\s*(.+)', content)
        if actual_effort_match:
            metadata['actual_effort'] = actual_effort_match.group(1)
        
        return metadata
    
    def _calculate_duration(self, metadata: Dict[str, str]) -> str:
        """Calculate task duration"""
        if 'actual_effort' in metadata:
            return metadata['actual_effort']
        
        if 'created' in metadata:
            try:
                created = datetime.strptime(metadata['created'], '%Y-%m-%d')
                completed = datetime.now()
                days = (completed - created).days
                
                if days == 0:
                    return "< 1 day"
                elif days == 1:
                    return "1 day"
                else:
                    return f"{days} days"
            except:
                pass
        
        return "Unknown"
    
    def _analyze_task_content(self, content: str, todo_data: Optional[Dict[str, Any]] = None) -> Dict[str, List[str]]:
        """Analyze task content to extract key information"""
        analysis = {
            "what_was_done": [],
            "key_changes": [],
            "impact": [],
            "lessons_learned": [],
            "related_resources": [],
            "files_changed": "N/A"
        }
        
        # Extract completed items (checkboxes)
        completed_items = re.findall(r'- \[x\] (.+)', content, re.IGNORECASE)
        analysis["what_was_done"].extend(completed_items[:5])  # Top 5
        
        # Extract implementation details
        if "## Implementation" in content:
            impl_section = self._extract_section(content, "## Implementation")
            key_points = self._extract_key_points(impl_section)
            analysis["key_changes"].extend(key_points[:3])
        
        # Extract from solution/resolution sections
        for section_name in ["## Solution", "## Resolution", "## Changes Made"]:
            if section_name in content:
                section = self._extract_section(content, section_name)
                points = self._extract_key_points(section)
                analysis["key_changes"].extend(points[:2])
        
        # Analyze todo data if provided
        if todo_data and isinstance(todo_data, dict):
            todos = todo_data.get("todos", [])
            completed_todos = [t for t in todos if t.get("status") == "completed"]
            
            # Count unique file references
            files = set()
            for todo in completed_todos:
                content_lower = todo.get("content", "").lower()
                # Look for file paths
                file_matches = re.findall(r'[./\w-]+\.\w+', content_lower)
                files.update(file_matches)
            
            if files:
                analysis["files_changed"] = f"{len(files)} files"
        
        # Extract impact
        if "security" in content.lower():
            analysis["impact"].append("Security improvements")
        if "performance" in content.lower():
            analysis["impact"].append("Performance optimization")
        if "bug" in content.lower() or "fix" in content.lower():
            analysis["impact"].append("Bug fixes")
        if "feature" in content.lower():
            analysis["impact"].append("New features added")
        
        # Extract lessons learned from notes
        if "## Notes" in content:
            notes_section = self._extract_section(content, "## Notes")
            lessons = self._extract_lessons(notes_section)
            analysis["lessons_learned"].extend(lessons[:3])
        
        # Extract related resources
        # Look for file paths
        file_refs = re.findall(r'`([./\w-]+\.\w+)`', content)
        for ref in file_refs[:5]:
            analysis["related_resources"].append(f"File: `{ref}`")
        
        # Look for commands
        command_refs = re.findall(r'`/(\w+ \w+[^`]*)`', content)
        for cmd in command_refs[:3]:
            analysis["related_resources"].append(f"Command: `/{cmd}`")
        
        return analysis
    
    def _extract_section(self, content: str, section_header: str) -> str:
        """Extract content of a specific section"""
        pattern = rf'{re.escape(section_header)}\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1) if match else ""
    
    def _extract_key_points(self, section: str) -> List[str]:
        """Extract key points from a section"""
        points = []
        
        # Look for bullet points
        bullets = re.findall(r'[•\-*]\s+(.+)', section)
        points.extend(bullets)
        
        # Look for numbered items
        numbered = re.findall(r'\d+\.\s+(.+)', section)
        points.extend(numbered)
        
        # Clean and return unique points
        cleaned_points = []
        for point in points:
            # Remove markdown formatting
            clean = re.sub(r'[*_`]', '', point).strip()
            if clean and len(clean) > 10:  # Meaningful content
                cleaned_points.append(clean)
        
        return list(dict.fromkeys(cleaned_points))  # Remove duplicates while preserving order
    
    def _extract_lessons(self, notes: str) -> List[str]:
        """Extract lessons learned from notes"""
        lessons = []
        
        # Common patterns for lessons
        patterns = [
            r'learned that (.+)',
            r'discovered (.+)',
            r'found out (.+)',
            r'realized (.+)',
            r'important: (.+)',
            r'note: (.+)',
            r'tip: (.+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, notes, re.IGNORECASE)
            lessons.extend(matches)
        
        # Also look for emphasized text that might be lessons
        emphasized = re.findall(r'\*\*(.+?)\*\*', notes)
        for text in emphasized:
            if 10 < len(text) < 100:  # Reasonable length for a lesson
                lessons.append(text)
        
        return lessons[:5]  # Top 5 lessons
    
    def _format_list(self, items: List[str]) -> str:
        """Format a list of items for the summary"""
        if not items:
            return "- None captured"
        
        formatted = []
        for item in items:
            # Truncate long items
            if len(item) > 100:
                item = item[:97] + "..."
            formatted.append(f"- {item}")
        
        return "\n".join(formatted)
    
    def append_summary_to_file(self, task_file_path: Path, summary: str) -> bool:
        """Append summary to the task file"""
        try:
            # Read current content
            current_content = task_file_path.read_text()
            
            # Check if summary already exists
            if "## 📋 Completion Summary" in current_content:
                return False  # Summary already exists
            
            # Append summary
            updated_content = current_content.rstrip() + "\n" + summary
            task_file_path.write_text(updated_content)
            
            return True
        except Exception as e:
            print(f"Error appending summary: {e}")
            return False