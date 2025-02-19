#!/bin/bash

# Install only the backend requirements
pip install -r backend/vercel_requirements.txt

# Create the output directory
mkdir -p /vercel/output

# Copy the backend files
cp -r backend/* /vercel/output/

# Create the public directory
mkdir -p /vercel/output/public

echo "Build completed!"
