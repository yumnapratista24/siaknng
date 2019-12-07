#!/bin/sh

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migration..."
python manage.py migrate

echo "Starting gunicorn server..."
/usr/local/bin/gunicorn siaknngauth.wsgi:application -w 2 -b :80
