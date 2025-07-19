#!/usr/bin/env python3
"""Test hook to verify hooks are working"""

import sys
from datetime import datetime

# Write to a log file to verify the hook was called
log_path = "/tmp/claude_hook_test.log"

with open(log_path, "a") as f:
    f.write(f"{datetime.now().isoformat()} - Test hook called with args: {sys.argv}\n")

# Don't print anything - hooks should be silent unless they have important messages
# print("🔍 Test hook executed successfully!")