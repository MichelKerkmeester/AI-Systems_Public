#!/bin/bash
#
# Run Integration Tests for Command System Refactoring
#

echo "==================================="
echo "Running Hook Integration Tests"
echo "==================================="
echo ""

# Set up Python path
export PYTHONPATH="/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude:$PYTHONPATH"

# Run the integration tests
python3 test_hooks_integration.py

# Capture exit code
EXIT_CODE=$?

echo ""
echo "==================================="
echo "Test run complete"
echo "==================================="

exit $EXIT_CODE