#!/usr/bin/env python3
"""Test archive and backup functionality"""

import os
import subprocess
import time

def create_test_sessions():
    """Create test sessions in the old directory to exceed limit"""
    old_dir = ".claude/project/sessions/old"
    
    # Create additional test sessions to exceed 10
    for i in range(1, 6):
        filename = f"2025-07-18-1100{i:02d}-test-archive-{i}.md"
        filepath = os.path.join(old_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(f"# Test Archive Session {i}\n")
            f.write(f"**Date**: 2025-07-18\n")
            f.write(f"**Time**: 11:00:{i:02d}\n")
            f.write(f"Test content for archive testing\n")
        
        print(f"✅ Created: {filename}")
    
    print(f"\nTotal sessions in old/: {len(os.listdir(old_dir))}")

def check_backups():
    """Check if backups were created"""
    backup_dir = ".claude/project/sessions/backups"
    if os.path.exists(backup_dir):
        backups = [f for f in os.listdir(backup_dir) if f.startswith("backup-")]
        print(f"\n💾 Backups found: {len(backups)}")
        for backup in sorted(backups):
            size = os.path.getsize(os.path.join(backup_dir, backup))
            print(f"   • {backup} ({size} bytes)")
    else:
        print("\n❌ No backup directory found")

def run_session_manager():
    """Run session manager to trigger archival"""
    print("\n📦 Running session manager to archive current sessions...")
    
    result = subprocess.run(
        [".claude/project/sessions/session-manager.sh", "archive"],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print(f"Errors: {result.stderr}")

def check_old_sessions():
    """Check sessions after cleanup"""
    old_dir = ".claude/project/sessions/old"
    sessions = sorted(os.listdir(old_dir))
    
    print(f"\n📂 Sessions in old/ after cleanup: {len(sessions)}")
    for session in sessions[-10:]:  # Show last 10
        print(f"   • {session}")

if __name__ == "__main__":
    print("🧪 Testing Archive and Backup Functionality")
    print("=" * 50)
    
    # Step 1: Create test sessions
    print("\n1️⃣ Creating test sessions to exceed limit of 10...")
    create_test_sessions()
    
    # Step 2: Check current backups
    print("\n2️⃣ Checking existing backups...")
    check_backups()
    
    # Step 3: Run session manager to trigger archival
    print("\n3️⃣ Triggering archival process...")
    run_session_manager()
    
    # Step 4: Check backups again
    print("\n4️⃣ Checking backups after archival...")
    check_backups()
    
    # Step 5: Check remaining sessions
    print("\n5️⃣ Verifying session cleanup...")
    check_old_sessions()
    
    print("\n✅ Test complete!")