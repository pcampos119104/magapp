#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


echo "Running migrations..."
python manage.py migrate

echo "Starting marimo"
exec marimo edit --host 0.0.0.0 -p 2718 --no-token --headless &> /dev/null &

echo "Starting tailwindcss watcher"
exec npx tailwindcss -i ./magapp/static/input.css -o ./magapp/static/output.css --watch=always &

echo "Starting runserver"
exec python manage.py runserver_plus 0.0.0.0:8000 --nostatic