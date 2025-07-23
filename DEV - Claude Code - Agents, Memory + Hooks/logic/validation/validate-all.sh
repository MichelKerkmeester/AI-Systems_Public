#!/bin/bash
# Run all validation scripts

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/../.." &> /dev/null && pwd )"

echo -e "${YELLOW}Running all validation checks...${NC}\n"

# Default path to validate
VALIDATE_PATH="${1:-src}"

# Run comment validation
echo -e "${YELLOW}1. Running comment pattern validation...${NC}"
python3 "$SCRIPT_DIR/validate-comments.py" "$VALIDATE_PATH"
COMMENT_RESULT=$?

echo -e "\n${YELLOW}2. Running Slater compliance check...${NC}"
python3 "$SCRIPT_DIR/check-slater-compliance.py" "$VALIDATE_PATH"
SLATER_RESULT=$?

# Summary
echo -e "\n${YELLOW}===================================================${NC}"
echo -e "${YELLOW}Validation Summary${NC}"
echo -e "${YELLOW}===================================================${NC}"

if [ $COMMENT_RESULT -eq 0 ]; then
    echo -e "Comment Patterns: ${GREEN}✅ PASSED${NC}"
else
    echo -e "Comment Patterns: ${RED}❌ FAILED${NC}"
fi

if [ $SLATER_RESULT -eq 0 ]; then
    echo -e "Slater Compliance: ${GREEN}✅ PASSED${NC}"
else
    echo -e "Slater Compliance: ${RED}❌ FAILED${NC}"
fi

# Exit with failure if any check failed
if [ $COMMENT_RESULT -ne 0 ] || [ $SLATER_RESULT -ne 0 ]; then
    echo -e "\n${RED}Some validation checks failed. Please fix the issues above.${NC}"
    exit 1
else
    echo -e "\n${GREEN}All validation checks passed!${NC}"
    exit 0
fi