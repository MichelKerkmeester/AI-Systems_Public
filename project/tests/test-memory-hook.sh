#!/bin/bash
# Test the memory context hook

echo "Testing memory context hook..."

# Create test input for UserPromptSubmit event
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook.py
{
  "type": "UserPromptSubmit",
  "userPrompt": "How do I fix the Webflow CSS animation issues with security considerations?"
}
EOF

echo -e "\n\nTesting with different prompt:"

cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook.py
{
  "type": "UserPromptSubmit",
  "userPrompt": "Tell me about client preferences for performance optimization"
}
EOF

echo -e "\n\nTesting startup memory status:"
python3 .claude/scripts/startup-with-memory.py