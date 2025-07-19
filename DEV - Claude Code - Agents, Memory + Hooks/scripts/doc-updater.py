#!/usr/bin/env python3
"""
Documentation Auto-Update System
Maintains README files, TOCs, and cross-references
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple

class DocUpdater:
    """Automated documentation maintenance system"""
    
    def __init__(self, base_path: Path = None):
        if base_path is None:
            self.base_path = Path(__file__).parent.parent
        else:
            self.base_path = base_path
        
        self.docs_path = self.base_path / "y__docs"
        self.broken_links = []
        self.updated_files = []
        
    def scan_directory_structure(self, path: Path, level: int = 0) -> List[str]:
        """Scan directory and generate structure lines"""
        lines = []
        indent = "│   " * level
        
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
        
        for i, item in enumerate(items):
            if item.name.startswith('.'):
                continue
                
            is_last = i == len(items) - 1
            prefix = "└── " if is_last else "├── "
            
            if item.is_dir():
                lines.append(f"{indent}{prefix}{item.name}/")
                # Recursively scan subdirectories
                if level < 3:  # Limit depth
                    sub_lines = self.scan_directory_structure(item, level + 1)
                    lines.extend(sub_lines)
            else:
                # Add description for key files
                desc = self._get_file_description(item)
                lines.append(f"{indent}{prefix}{item.name}{desc}")
        
        return lines
    
    def _get_file_description(self, file_path: Path) -> str:
        """Get description for documentation files"""
        descriptions = {
            "README.md": " # Overview and navigation",
            "practical-examples.md": " # Real-world usage examples",
            "memory-verifcation-guide.md": " # Testing and verification",
            "troubleshooting.md": " # Common issues and solutions",
            "migration.md": " # Migration guide",
            "commands.md": " # Command reference",
            "hooks.md": " # Hook system docs",
            "automation.md": " # Automation patterns"
        }
        return descriptions.get(file_path.name, "")
    
    def update_directory_readme(self, dir_path: Path):
        """Update or create README with current directory structure"""
        readme_path = dir_path / "README.md"
        
        # Read existing README
        existing_content = ""
        if readme_path.exists():
            existing_content = readme_path.read_text()
        
        # Generate directory structure
        structure_lines = ["```"]
        structure_lines.append(f"{dir_path.name}/")
        structure_lines.extend(self.scan_directory_structure(dir_path))
        structure_lines.append("```")
        structure = "\n".join(structure_lines)
        
        # Update or insert structure section
        structure_section = f"## Directory Structure\n\n{structure}"
        
        if "## Directory Structure" in existing_content:
            # Replace existing structure section
            pattern = r'## Directory Structure\s*\n.*?(?=\n## |\Z)'
            updated_content = re.sub(pattern, structure_section, existing_content, flags=re.DOTALL)
        else:
            # Add structure section after TOC or at beginning
            if "## Table of Contents" in existing_content:
                # Insert after TOC
                toc_end = existing_content.find("\n## ", existing_content.find("## Table of Contents") + 1)
                if toc_end == -1:
                    toc_end = len(existing_content)
                updated_content = (
                    existing_content[:toc_end] + 
                    f"\n{structure_section}\n" + 
                    existing_content[toc_end:]
                )
            else:
                # Insert at beginning after title
                lines = existing_content.split('\n')
                insert_pos = 1 if lines and lines[0].startswith('#') else 0
                lines.insert(insert_pos + 1, f"\n{structure_section}")
                updated_content = '\n'.join(lines)
        
        # Write updated content
        readme_path.write_text(updated_content)
        self.updated_files.append(str(readme_path.relative_to(self.base_path)))
    
    def validate_internal_links(self):
        """Check all markdown files for broken internal links"""
        md_files = list(self.docs_path.rglob("*.md"))
        
        for md_file in md_files:
            content = md_file.read_text()
            
            # Find all markdown links
            link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
            links = re.findall(link_pattern, content)
            
            for link_text, link_url in links:
                # Skip external links
                if link_url.startswith(('http://', 'https://', '#')):
                    continue
                
                # Resolve relative path
                if link_url.startswith('/'):
                    target_path = self.base_path / link_url[1:]
                else:
                    target_path = md_file.parent / link_url
                    # Handle anchor links
                    if '#' in link_url:
                        target_path = Path(str(target_path).split('#')[0])
                
                # Check if target exists
                if not target_path.exists():
                    self.broken_links.append({
                        'file': str(md_file.relative_to(self.base_path)),
                        'line': self._find_line_number(content, f"[{link_text}]({link_url})"),
                        'link': link_url,
                        'text': link_text
                    })
    
    def _find_line_number(self, content: str, search_text: str) -> int:
        """Find line number of text in content"""
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if search_text in line:
                return i
        return 0
    
    def generate_index_files(self):
        """Generate index files for documentation directories"""
        # Main docs index
        self._generate_docs_index()
        
        # Subdirectory indices
        for subdir in self.docs_path.iterdir():
            if subdir.is_dir() and not subdir.name.startswith('.'):
                self._generate_subdir_index(subdir)
    
    def _generate_docs_index(self):
        """Generate main documentation index"""
        index_path = self.docs_path / "INDEX.md"
        
        content = ["# Documentation Index", ""]
        content.append("## Quick Links")
        content.append("")
        
        # Collect all documentation files
        categories = {
            "Getting Started": [],
            "System Documentation": [],
            "MCP Servers": [],
            "Guides": [],
            "Reference": []
        }
        
        for md_file in sorted(self.docs_path.rglob("*.md")):
            if md_file.name == "INDEX.md":
                continue
                
            rel_path = md_file.relative_to(self.docs_path)
            
            # Categorize files
            if "README" in md_file.name:
                categories["Getting Started"].append(rel_path)
            elif "mcp" in str(rel_path) and "mcp/" in str(rel_path):
                categories["MCP Servers"].append(rel_path)
            elif any(x in str(rel_path) for x in ["guide", "tutorial", "examples"]):
                categories["Guides"].append(rel_path)
            elif any(x in str(rel_path) for x in ["command", "reference", "api"]):
                categories["Reference"].append(rel_path)
            else:
                categories["System Documentation"].append(rel_path)
        
        # Generate index content
        for category, files in categories.items():
            if files:
                content.append(f"### {category}")
                for file_path in sorted(files):
                    title = self._get_document_title(self.docs_path / file_path)
                    content.append(f"- [{title}](./{file_path})")
                content.append("")
        
        # Add statistics
        total_docs = sum(len(files) for files in categories.values())
        content.append("## Documentation Statistics")
        content.append(f"- Total documents: {total_docs}")
        content.append(f"- Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        content.append(f"- Categories: {len([c for c in categories.values() if c])}")
        
        index_path.write_text('\n'.join(content))
        self.updated_files.append(str(index_path.relative_to(self.base_path)))
    
    def _generate_subdir_index(self, subdir: Path):
        """Generate index for a subdirectory"""
        index_path = subdir / "INDEX.md"
        
        content = [f"# {subdir.name.title()} Documentation Index", ""]
        
        # List all files in the directory
        md_files = sorted(subdir.glob("*.md"))
        if md_files:
            content.append("## Documents")
            for md_file in md_files:
                if md_file.name != "INDEX.md":
                    title = self._get_document_title(md_file)
                    content.append(f"- [{title}](./{md_file.name})")
        
        # List subdirectories
        subdirs = sorted([d for d in subdir.iterdir() if d.is_dir()])
        if subdirs:
            content.append("")
            content.append("## Subdirectories")
            for sub in subdirs:
                content.append(f"- [{sub.name}/](./{sub.name}/)")
        
        index_path.write_text('\n'.join(content))
        self.updated_files.append(str(index_path.relative_to(self.base_path)))
    
    def _get_document_title(self, file_path: Path) -> str:
        """Extract title from markdown file"""
        try:
            content = file_path.read_text()
            lines = content.split('\n')
            for line in lines:
                if line.startswith('# '):
                    return line[2:].strip()
        except:
            pass
        
        # Fallback to filename
        return file_path.stem.replace('-', ' ').replace('_', ' ').title()
    
    def generate_report(self) -> str:
        """Generate update report"""
        report = ["# Documentation Update Report", ""]
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        report.append("")
        
        # Updated files
        if self.updated_files:
            report.append(f"## Updated Files ({len(self.updated_files)})")
            for file in sorted(self.updated_files):
                report.append(f"- {file}")
            report.append("")
        
        # Broken links
        if self.broken_links:
            report.append(f"## Broken Links ({len(self.broken_links)})")
            for link in self.broken_links:
                report.append(f"- {link['file']}:{link['line']} - [{link['text']}]({link['link']})")
            report.append("")
        
        # Summary
        report.append("## Summary")
        report.append(f"- Files updated: {len(self.updated_files)}")
        report.append(f"- Broken links found: {len(self.broken_links)}")
        report.append(f"- Status: {'✅ Success' if not self.broken_links else '⚠️ Needs attention'}")
        
        return '\n'.join(report)
    
    def run(self):
        """Run complete documentation update"""
        print("Starting documentation update...")
        
        # Update directory READMEs
        print("Updating directory structures...")
        self.update_directory_readme(self.docs_path)
        for subdir in self.docs_path.iterdir():
            if subdir.is_dir() and not subdir.name.startswith('.'):
                self.update_directory_readme(subdir)
        
        # Validate links
        print("Validating internal links...")
        self.validate_internal_links()
        
        # Generate indices
        print("Generating index files...")
        self.generate_index_files()
        
        # Generate report
        report = self.generate_report()
        report_path = self.base_path / "y__docs" / "UPDATE_REPORT.md"
        report_path.write_text(report)
        
        print(f"\nUpdate complete!")
        print(f"Files updated: {len(self.updated_files)}")
        print(f"Broken links found: {len(self.broken_links)}")
        print(f"Report saved to: {report_path.relative_to(self.base_path)}")

def main():
    """Run documentation updater"""
    updater = DocUpdater()
    updater.run()

if __name__ == "__main__":
    main()