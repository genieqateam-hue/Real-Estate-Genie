# Real Estate Genie

A Django-based real estate application for property listings, events, and more.

## Deployment on Render

This project is configured for deployment on Render.com with the following files:

- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `Procfile` - Application startup command
- `build.sh` - Build script for deployment

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Production Settings

The application is configured for production with:
- DEBUG = False
- WhiteNoise for static file serving
- Gunicorn as WSGI server
- SQLite database (can be changed to PostgreSQL for production)
