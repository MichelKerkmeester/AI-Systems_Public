#!/usr/bin/env python3
"""
Add or update table of contents in markdown files
"""

import re
from pathlib import Path
from typing import List, Tuple

def extract_headers(content: str) -> List[Tuple[int, str]]:
    """Extract headers from markdown content"""
    headers = []
    lines = content.split('\n')
    in_code_block = False
    
    for line in lines:
        # Check for code block boundaries
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
            
        # Skip lines in code blocks
        if in_code_block:
            continue
            
        # Match markdown headers
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            # Skip if it's the main title (first H1) or TOC itself
            if not (level == 1 and len(headers) == 0) and 'table of contents' not in title.lower():
                headers.append((level, title))
    
    return headers

def generate_toc(headers: List[Tuple[int, str]]) -> str:
    """Generate table of contents from headers"""
    if not headers:
        return ""
    
    toc_lines = ["## Table of Contents\n"]
    
    for level, title in headers:
        # Create anchor link
        anchor = title.lower()
        # Remove special characters and replace spaces with hyphens
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        
        # Indent based on header level
        indent = "  " * (level - 2)
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    
    return "\n".join(toc_lines)

def add_toc_to_file(file_path: Path) -> bool:
    """Add or update table of contents in a markdown file"""
    try:
        content = file_path.read_text()
        
        # Check if TOC already exists
        toc_pattern = r'## Table of Contents\s*\n((?:.*\n)*?)(?=\n## |\n# |$)'
        existing_toc = re.search(toc_pattern, content, re.MULTILINE)
        
        # Extract headers
        headers = extract_headers(content)
        
        # Only add TOC if there are enough headers
        if len(headers) < 3:
            print(f"  Skipping {file_path.name} - not enough headers")
            return False
        
        # Generate new TOC
        new_toc = generate_toc(headers)
        
        if existing_toc:
            # Replace existing TOC
            content = content.replace(existing_toc.group(0), new_toc.rstrip())
            print(f"  Updated TOC in {file_path.name}")
        else:
            # Find the position after the main title and any initial description
            lines = content.split('\n')
            insert_pos = 0
            
            # Skip the main title
            for i, line in enumerate(lines):
                if line.startswith('# '):
                    insert_pos = i + 1
                    break
            
            # Skip any immediate description paragraphs
            while insert_pos < len(lines) and lines[insert_pos].strip() != '':
                insert_pos += 1
            
            # Insert TOC
            lines.insert(insert_pos + 1, new_toc)
            content = '\n'.join(lines)
            print(f"  Added TOC to {file_path.name}")
        
        # Write back to file
        file_path.write_text(content)
        return True
        
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return False

def main():
    """Process all markdown files in .claude/y__docs"""
    base_path = Path(__file__).parent.parent
    docs_path = base_path / "y__docs"
    
    if not docs_path.exists():
        print(f"Error: {docs_path} does not exist")
        return
    
    # Find all markdown files
    md_files = list(docs_path.rglob("*.md"))
    
    print(f"Found {len(md_files)} markdown files")
    print("Adding/updating table of contents...\n")
    
    success_count = 0
    for md_file in sorted(md_files):
        print(f"Processing {md_file.relative_to(base_path)}...")
        if add_toc_to_file(md_file):
            success_count += 1
    
    print(f"\nCompleted: {success_count}/{len(md_files)} files updated")

if __name__ == "__main__":
    main()