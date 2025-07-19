#!/usr/bin/env python3
"""
Output formatting utilities for Claude hooks
Provides consistent message formatting across all hooks
"""

from typing import List, Optional, Dict, Any
from datetime import datetime


class MessageFormatter:
    """Formats messages with consistent styling"""
    
    # Standard separators
    SEPARATOR_SINGLE = "=" * 50
    SEPARATOR_DOUBLE = "=" * 70
    SEPARATOR_DASHED = "-" * 50
    
    # Common emoji mappings
    EMOJIS = {
        # Status
        "success": "✅",
        "warning": "⚠️",
        "error": "🚨",
        "info": "ℹ️",
        "progress": "⏳",
        "complete": "✅",
        "failed": "❌",
        
        # Categories
        "security": "🔐",
        "test": "🧪",
        "memory": "🧠",
        "commit": "📝",
        "code": "📜",
        "css": "🎨",
        "file": "📁",
        "search": "🔍",
        "stats": "📊",
        "todo": "📋",
        "settings": "⚙️",
        "session": "📂",
        "mode": "🎯",
        "quality": "📋",
        
        # Actions
        "save": "💾",
        "load": "📥",
        "delete": "🗑️",
        "update": "🔄",
        "create": "➕",
        "check": "✔️",
        "fix": "🔧",
        "suggest": "💡",
        "remind": "💭"
    }
    
    @classmethod
    def header(cls, title: str, emoji: Optional[str] = None, 
               separator: str = None) -> str:
        """
        Create a formatted header
        
        Args:
            title: Header title
            emoji: Optional emoji key or literal emoji
            separator: Type of separator (uses SEPARATOR_SINGLE by default)
        """
        if separator is None:
            separator = cls.SEPARATOR_SINGLE
            
        # Get emoji if key provided
        if emoji and emoji in cls.EMOJIS:
            emoji = cls.EMOJIS[emoji]
        
        # Build header
        lines = [separator]
        if emoji:
            lines.append(f"{emoji} {title}")
        else:
            lines.append(title)
        lines.append(separator)
        
        return "\n".join(lines)
    
    @classmethod
    def footer(cls, separator: str = None) -> str:
        """Create a footer separator"""
        return separator or cls.SEPARATOR_SINGLE
    
    @classmethod
    def section(cls, title: str, content: List[str], 
                emoji: Optional[str] = None, indent: int = 2) -> str:
        """
        Format a section with title and bullet points
        
        Args:
            title: Section title
            content: List of content items
            emoji: Optional emoji for title
            indent: Number of spaces to indent items
        """
        # Get emoji if key provided
        if emoji and emoji in cls.EMOJIS:
            emoji = cls.EMOJIS[emoji]
        
        lines = []
        
        # Add title
        if emoji:
            lines.append(f"\n{emoji} {title}:")
        else:
            lines.append(f"\n{title}:")
        
        # Add content items
        indent_str = " " * indent
        for item in content:
            lines.append(f"{indent_str}• {item}")
        
        return "\n".join(lines)
    
    @classmethod
    def box(cls, title: str, content: str, width: int = 50) -> str:
        """
        Create a box around content
        
        Args:
            title: Box title
            content: Box content
            width: Box width
        """
        border = "─" * (width - 2)
        lines = [
            f"┌{border}┐",
            f"│ {title.center(width - 4)} │",
            f"├{border}┤"
        ]
        
        # Add content lines
        for line in content.split('\n'):
            padded = line.ljust(width - 4)
            lines.append(f"│ {padded} │")
        
        lines.append(f"└{border}┘")
        
        return "\n".join(lines)
    
    @classmethod
    def timestamp(cls, dt: datetime = None, format: str = "%Y-%m-%d %H:%M:%S") -> str:
        """Format a timestamp"""
        if dt is None:
            dt = datetime.now()
        return dt.strftime(format)
    
    @classmethod
    def status_line(cls, label: str, value: str, 
                    emoji: Optional[str] = None) -> str:
        """
        Format a status line
        
        Args:
            label: Status label
            value: Status value
            emoji: Optional emoji key
        """
        if emoji and emoji in cls.EMOJIS:
            emoji = cls.EMOJIS[emoji]
            return f"{emoji} {label}: {value}"
        return f"{label}: {value}"
    
    @classmethod
    def progress(cls, current: int, total: int, label: str = "Progress") -> str:
        """Format a progress indicator"""
        percentage = (current / total * 100) if total > 0 else 0
        return f"{cls.EMOJIS['progress']} {label}: {current}/{total} ({percentage:.0f}%)"
    
    @classmethod
    def warning_box(cls, message: str) -> str:
        """Create a warning box"""
        lines = [
            cls.SEPARATOR_SINGLE,
            f"{cls.EMOJIS['warning']} WARNING",
            cls.SEPARATOR_DASHED,
            message,
            cls.SEPARATOR_SINGLE
        ]
        return "\n".join(lines)
    
    @classmethod
    def error_box(cls, message: str) -> str:
        """Create an error box"""
        lines = [
            cls.SEPARATOR_DOUBLE,
            f"{cls.EMOJIS['error']} ERROR",
            cls.SEPARATOR_DASHED,
            message,
            cls.SEPARATOR_DOUBLE
        ]
        return "\n".join(lines)
    
    @classmethod
    def success_box(cls, message: str) -> str:
        """Create a success box"""
        lines = [
            cls.SEPARATOR_SINGLE,
            f"{cls.EMOJIS['success']} SUCCESS",
            cls.SEPARATOR_DASHED,
            message,
            cls.SEPARATOR_SINGLE
        ]
        return "\n".join(lines)
    
    @classmethod
    def table(cls, headers: List[str], rows: List[List[str]], 
              align: str = "left") -> str:
        """
        Create a simple text table
        
        Args:
            headers: Column headers
            rows: Table rows
            align: Text alignment (left, right, center)
        """
        # Calculate column widths
        widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(widths):
                    widths[i] = max(widths[i], len(str(cell)))
        
        # Build table
        lines = []
        
        # Headers
        header_cells = []
        for i, header in enumerate(headers):
            if align == "right":
                header_cells.append(header.rjust(widths[i]))
            elif align == "center":
                header_cells.append(header.center(widths[i]))
            else:
                header_cells.append(header.ljust(widths[i]))
        lines.append(" | ".join(header_cells))
        
        # Separator
        lines.append("-|-".join(["-" * w for w in widths]))
        
        # Rows
        for row in rows:
            cells = []
            for i, cell in enumerate(row):
                cell_str = str(cell)
                if i < len(widths):
                    if align == "right":
                        cells.append(cell_str.rjust(widths[i]))
                    elif align == "center":
                        cells.append(cell_str.center(widths[i]))
                    else:
                        cells.append(cell_str.ljust(widths[i]))
            lines.append(" | ".join(cells))
        
        return "\n".join(lines)