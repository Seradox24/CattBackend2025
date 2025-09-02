# CattBackend2025

Backend Django project configured with PostgreSQL, static/media files, and Tailwind CSS.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Tailwind dependencies:
   ```bash
   python manage.py tailwind install
   ```
3. Apply migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Environment variables `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, and `POSTGRES_PORT` can override default PostgreSQL settings.

Static files are collected to `staticfiles/` and served at `/static/`, while uploaded media lives in `media/` and is served at `/media/`.
