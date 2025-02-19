#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p .vercel/cache
mkdir -p .vercel/output/static

# Copy static files if any
cp -r backend/static/* .vercel/output/static/ 2>/dev/null || true

echo "Setup completed!"
