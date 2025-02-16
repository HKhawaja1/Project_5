#!/bin/bash

# Exit on error
set -e

# Install dependencies
echo "Installing dependencies..."
pip install -r science_quiz/requirements.txt

# Collect static files
echo "Collecting static files..."
python science_quiz/manage.py collectstatic --noinput

# Run database migrations
echo "Running database migrations..."
python science_quiz/manage.py migrate

echo "Build completed!"