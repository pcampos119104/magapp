#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


echo "Running migrations..."
python manage.py migrate

echo "Running collectstatic..."
python manage.py collectstatic --noinput

echo "Starting server"
exec gunicorn --log-level debug --bind :80 --workers 3 magapp.wsgi:application
