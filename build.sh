#!/usr/bin/env bash
# Build script for Render deployment

# Set Django settings module
export DJANGO_SETTINGS_MODULE=real_estate_genie.settings

# Install Python dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
