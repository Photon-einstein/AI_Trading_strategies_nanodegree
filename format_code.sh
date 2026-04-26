#!/bin/bash
# Format all Python files and Jupyter notebooks using black

set -e

WORKSPACE_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing black with Jupyter support..."
pip install "black[jupyter]" --quiet

echo ""
echo "Formatting Python files (.py)..."
find "$WORKSPACE_DIR" -name "*.py" -not -path "*/.git/*" | while read -r file; do
    echo "  $file"
    black "$file"
done

echo ""
echo "Formatting Jupyter notebooks (.ipynb)..."
find "$WORKSPACE_DIR" -name "*.ipynb" -not -path "*/.git/*" -not -path "*/.ipynb_checkpoints/*" | while read -r file; do
    echo "  $file"
    black "$file"
done

echo ""
echo "Done! All files formatted."
