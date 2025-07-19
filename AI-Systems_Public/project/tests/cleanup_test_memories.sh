#!/bin/bash
# Cleanup script to remove test memories from Graphiti

echo "🧹 Cleaning up test memories from Graphiti..."

# Define test memory names to delete
TEST_MEMORIES=(
    "TEST-MEMORY-2025-01-18-CLAUDE"
    "Direct Test - Object"
    "Direct Test - String"
    "Test Memory from Claude Code"
    "Graphiti MCP Test Episode"
)

# Delete each test memory
for memory in "${TEST_MEMORIES[@]}"; do
    echo "Deleting: $memory"
    docker exec -i graphiti-neo4j cypher-shell -u neo4j -p password -d neo4j --format plain <<EOF
MATCH (e:Episodic {name: "$memory"})
DETACH DELETE e
RETURN "Deleted: $memory" as result;
EOF
done

# Show remaining memories
echo -e "\n📚 Remaining memories:"
docker exec -i graphiti-neo4j cypher-shell -u neo4j -p password -d neo4j --format plain <<EOF
MATCH (e:Episodic)
RETURN e.name as Memory, e.group_id as Category
ORDER BY e.created_at DESC;
EOF

# Count stats
echo -e "\n📊 Updated stats:"
docker exec -i graphiti-neo4j cypher-shell -u neo4j -p password -d neo4j --format plain <<EOF
MATCH (e:Episodic) WITH count(e) as episodes
MATCH (n:Entity) WITH episodes, count(n) as entities
RETURN "Episodes: " + episodes + ", Entities: " + entities as Summary;
EOF