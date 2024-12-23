#!/bin/bash

set -e

echo "Building shared library and Python package..."
python setup.py sdist bdist_wheel

echo "Cleaning up build artifacts..."
rm -rf build/ src/*.egg-info 

echo "Cleaning up Python cache files..."
find . -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete

echo "Cleaning up temporary files..."
find . -name "*.tmp" -delete
find . -name "*.swp" -delete
rm -f .DS_Store

echo "Cleanup complete!"
