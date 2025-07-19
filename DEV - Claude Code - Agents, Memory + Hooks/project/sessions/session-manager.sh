#!/bin/bash

# Session Manager for Claude Sessions
# Automatically moves current sessions to old when creating new ones
# Features: Auto-backup, confirmation prompts, timestamp-based naming

SESSIONS_DIR="/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/project/sessions"
CURRENT_DIR="$SESSIONS_DIR/current"
OLD_DIR="$SESSIONS_DIR/old"
BACKUP_DIR="$SESSIONS_DIR/backups"

# Create directories if they don't exist
mkdir -p "$CURRENT_DIR"
mkdir -p "$OLD_DIR"
mkdir -p "$BACKUP_DIR"

# Function to create backup before deletion
create_backup() {
    local backup_timestamp=$(date +%Y%m%d-%H%M%S)
    local backup_file="$BACKUP_DIR/backup-${backup_timestamp}.tar.gz"
    
    echo "  💾 Creating backup before deletion..."
    
    # Get files that will be deleted (oldest ones)
    cd "$OLD_DIR"
    local files_to_backup=$(ls -t *.md 2>/dev/null | tail -n +11)
    
    if [ -n "$files_to_backup" ]; then
        # Create tar.gz of files to be deleted
        tar -czf "$backup_file" $files_to_backup 2>/dev/null
        echo "  ✓ Backup created: $(basename "$backup_file")"
        
        # Rotate backups (keep only 5)
        cd "$BACKUP_DIR"
        local backup_count=$(ls -1 backup-*.tar.gz 2>/dev/null | wc -l)
        if [ $backup_count -gt 5 ]; then
            ls -t backup-*.tar.gz | tail -n +6 | xargs rm
            echo "  ✓ Rotated old backups (keeping last 5)"
        fi
    fi
    
    cd - > /dev/null
}

# Function to setup AI exclusion for backups
setup_backup_exclusion() {
    # Create .claudeignore if it doesn't exist
    if [ ! -f "$BACKUP_DIR/.claudeignore" ]; then
        echo "*" > "$BACKUP_DIR/.claudeignore"
    fi
    
    # Create README if it doesn't exist
    if [ ! -f "$BACKUP_DIR/README.md" ]; then
        cat > "$BACKUP_DIR/README.md" << EOF
# DO NOT CRAWL THIS DIRECTORY

This directory contains compressed backup archives of deleted sessions.
These files should NOT be indexed or read by Claude, Gemini, or any other AI tools.

The backups are automatically created before sessions are deleted when the limit of 10 is exceeded.
Only the 5 most recent backups are kept.

Format: backup-YYYYMMDD-HHMMSS.tar.gz
EOF
    fi
}

# Function to archive current sessions
archive_current_sessions() {
    echo "📦 Archiving current sessions..."
    
    # Check if there are any files to move
    if [ "$(ls -A "$CURRENT_DIR"/*.md 2>/dev/null)" ]; then
        # Move all markdown files from current to old
        for file in "$CURRENT_DIR"/*.md; do
            if [ -f "$file" ]; then
                filename=$(basename "$file")
                mv "$file" "$OLD_DIR/"
                echo "  ✓ Moved $filename → old/"
            fi
        done
        
        # Auto-clean: Keep only the 10 most recent sessions
        echo "  🧹 Auto-cleaning old sessions..."
        cd "$OLD_DIR"
        session_count=$(ls -1 *.md 2>/dev/null | wc -l)
        if [ $session_count -gt 10 ]; then
            # Create backup before deletion
            create_backup
            
            # Delete oldest files (keep newest 10)
            ls -t *.md 2>/dev/null | tail -n +11 | xargs -I {} rm "{}"
            deleted=$((session_count - 10))
            echo "  ✓ Removed $deleted old sessions (keeping last 10)"
        fi
        cd - > /dev/null
    else
        echo "  ℹ️  No sessions to archive"
    fi
}

# Function to create new session with timestamp naming
create_new_session() {
    local description="$1"
    local timestamp=$(date +%Y-%m-%d-%H%M%S)
    
    # If no description provided, prompt for it
    if [ -z "$description" ]; then
        echo "Enter 2-word description (or press Enter for 'general-session'):"
        read -r description
        description=${description:-general-session}
    fi
    
    # Clean description: lowercase, replace spaces with hyphens, limit length
    description=$(echo "$description" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | cut -d'-' -f1-3)
    
    local session_name="${timestamp}-${description}"
    local session_file="$CURRENT_DIR/${session_name}.md"
    
    echo "📝 Creating new session: $session_name"
    
    # Create session template
    cat > "$session_file" << EOF
# ${description}
**Date**: $(date +%Y-%m-%d)  
**Time**: $(date +%H:%M:%S)  
**Filename**: ${session_name}.md

## 🎯 Session Goals
- [ ] Goal 1
- [ ] Goal 2

## 📋 Tasks Completed

## 🔧 Changes Made

## 📝 Notes

## 📋 Next Steps

## 🔗 Related Files
EOF
    
    echo "  ✓ Created $session_file"
}

# Function to list sessions
list_sessions() {
    echo "📂 Current Sessions:"
    if [ "$(ls -A "$CURRENT_DIR"/*.md 2>/dev/null)" ]; then
        for file in "$CURRENT_DIR"/*.md; do
            if [ -f "$file" ]; then
                local filename=$(basename "$file")
                local size=$(du -h "$file" | cut -f1)
                echo "  • $filename ($size)"
            fi
        done
    else
        echo "  (none)"
    fi
    
    echo -e "\n📦 Archived Sessions:"
    if [ "$(ls -A "$OLD_DIR"/*.md 2>/dev/null)" ]; then
        local count=0
        for file in $(ls -t "$OLD_DIR"/*.md 2>/dev/null); do
            if [ -f "$file" ]; then
                local filename=$(basename "$file")
                local size=$(du -h "$file" | cut -f1)
                echo "  • $filename ($size)"
                count=$((count + 1))
                [ $count -eq 10 ] && break
            fi
        done
        total=$(ls "$OLD_DIR"/*.md 2>/dev/null | wc -l)
        if [ $total -gt 10 ]; then
            echo "  ... and $((total - 10)) more"
        fi
    else
        echo "  (none)"
    fi
    
    # Show backup info
    if [ -d "$BACKUP_DIR" ] && [ "$(ls -A "$BACKUP_DIR"/backup-*.tar.gz 2>/dev/null)" ]; then
        echo -e "\n💾 Backups:"
        local backup_count=$(ls "$BACKUP_DIR"/backup-*.tar.gz 2>/dev/null | wc -l)
        local backup_size=$(du -sh "$BACKUP_DIR" 2>/dev/null | cut -f1)
        echo "  $backup_count backups ($backup_size total)"
    fi
}

# Function to clean with confirmation
clean_sessions() {
    local force_flag="$1"
    
    cd "$OLD_DIR"
    session_count=$(ls -1 *.md 2>/dev/null | wc -l)
    
    if [ $session_count -gt 10 ]; then
        local files_to_delete=$(ls -t *.md 2>/dev/null | tail -n +11)
        local delete_count=$(echo "$files_to_delete" | wc -l)
        
        echo "🧹 Cleaning old sessions (keeping last 10)..."
        echo ""
        echo "Files to be deleted:"
        for file in $files_to_delete; do
            local size=$(du -h "$file" 2>/dev/null | cut -f1)
            local date=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$file" 2>/dev/null || echo "unknown")
            echo "  • $file ($size, modified: $date)"
        done
        echo ""
        
        # Check for force flag
        if [ "$force_flag" != "--force" ]; then
            echo "⚠️  This will permanently delete $delete_count files!"
            echo -n "Continue? [y/N] "
            read -r response
            if [[ ! "$response" =~ ^[Yy]$ ]]; then
                echo "❌ Cleanup cancelled"
                return
            fi
        fi
        
        # Create backup before deletion
        create_backup
        
        # Delete files
        echo "$files_to_delete" | xargs rm
        echo "  ✓ Removed $delete_count old sessions"
    else
        echo "  ℹ️  No cleanup needed ($session_count sessions)"
    fi
    
    cd - > /dev/null
}

# Initialize backup exclusion on first run
setup_backup_exclusion

# Main script logic
case "${1:-help}" in
    new)
        archive_current_sessions
        shift # Remove 'new' from arguments
        create_new_session "$*"
        ;;
    
    archive)
        archive_current_sessions
        ;;
    
    list)
        list_sessions
        ;;
    
    clean)
        clean_sessions "$2"
        ;;
    
    help|*)
        echo "📚 Claude Session Manager"
        echo "========================"
        echo "Commands:"
        echo "  new [description]  - Archive current & create new (timestamp-based naming)"
        echo "  archive           - Move current sessions to old/ (auto-cleans after 10)"
        echo "  list              - List all sessions with sizes"
        echo "  clean [--force]   - Remove old sessions with confirmation (keeps last 10)"
        echo "  help              - Show this help"
        echo ""
        echo "Features:"
        echo "  • Automatic timestamp-based naming (YYYY-MM-DD-HHMMSS-description)"
        echo "  • Backups created before deletion (kept in backups/ directory)"
        echo "  • Confirmation prompts for safety"
        echo "  • AI-excluded backup directory"
        echo ""
        echo "Examples:"
        echo "  $0 new memory testing     → Creates: 2025-01-17-143052-memory-testing.md"
        echo "  $0 new                    → Prompts for description"
        echo "  $0 clean                  → Shows files and asks confirmation"
        echo "  $0 clean --force          → Skips confirmation"
        ;;
esac