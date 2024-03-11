#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


echo "Running migrations..."
python manage.py migrate

echo "Starting server"
exec gunicorn --bind :8000 --workers 2 magapp.wsgi
