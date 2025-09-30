#!/usr/bin/env bash
# Build script for Render deployment

# Set Django settings module
export DJANGO_SETTINGS_MODULE=RealEstateGenie.settings

# Install Python dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create/update admin user with new password
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
user, created = User.objects.get_or_create(username='admin', defaults={'is_staff': True, 'is_superuser': True})
user.set_password('Sales@2025')
user.is_staff = True
user.is_superuser = True
user.save()
print('Admin password updated to Sales@2025')
"

# Collect static files
python manage.py collectstatic --noinput
