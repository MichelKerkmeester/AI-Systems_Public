#!/bin/bash
# Comprehensive test for memory context hook v2

echo "=== Testing Memory Context Hook v2 ==="
echo

# Test 1: Normal query
echo "1. Testing normal query (security):"
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py
{
  "type": "UserPromptSubmit",
  "userPrompt": "How do I implement security for API keys?"
}
EOF

echo -e "\n2. Testing query with special characters:"
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py
{
  "type": "UserPromptSubmit", 
  "userPrompt": "What's the pattern for O'Reilly's \"best practices\" guide?"
}
EOF

echo -e "\n3. Testing empty prompt:"
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py
{
  "type": "UserPromptSubmit",
  "userPrompt": ""
}
EOF

echo -e "\n4. Testing /memory command (should skip):"
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py
{
  "type": "UserPromptSubmit",
  "userPrompt": "/memory search security"
}
EOF

echo -e "\n5. Testing wrong event type (should skip):"
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py
{
  "type": "PreToolUse",
  "userPrompt": "test"
}
EOF

echo -e "\n6. Testing with debug mode:"
CLAUDE_DEBUG=true cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py 2>&1
{
  "type": "UserPromptSubmit",
  "userPrompt": "Debug test for webflow patterns"
}
EOF

echo -e "\n7. Testing Docker health check:"
# Stop Docker temporarily to test error handling
docker stop graphiti-neo4j 2>/dev/null || true
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py 2>&1
{
  "type": "UserPromptSubmit",
  "userPrompt": "Test when Docker is down"
}
EOF

# Restart Docker
echo -e "\nRestarting Docker container..."
docker start graphiti-neo4j 2>/dev/null || true
sleep 2

echo -e "\n8. Testing complex query:"
cat << 'EOF' | python3 .claude/logic/memory/hooks/memory-context-hook-v2.py
{
  "type": "UserPromptSubmit",
  "userPrompt": "I need to fix the webflow CSS animation performance issues while maintaining security best practices for our client's requirements"
}
EOF