# Magapp 

A system for manage my personal recipes.

## Tools, libs, etc. Sometimes the related files.

Versions is on Poetry.

- [Python](https://www.python.org/) Programming language
- [django-environ](https://django-environ.readthedocs.io) Manage .envs in Django
- [Poetry](https://python-poetry.org/) Python packaging and dependency management
  - poetry.lock
  - pyproject.toml
- [Django](https://www.djangoproject.com/) Web framework written in Python
- [Docker](https://www.docker.com/) Manage containers for development and production environment
  - compose.yaml
  - compose/dev/Dockerfile
  - compose/dev/start
  - compose/prod/Dockerfile
  - compose/prod/start
  - .env(Not in repo, but it's needed)
  - .env.template
  - .dockerignore
- [Just](https://just.systems/) Encapsulate commands for easier use.
  - justfile
- [psycopg](https://www.psycopg.org/) Python adapter for Postgres.
- [AlpineJS](https://alpinejs.dev/) JavaScript Framework based on Vue engine.
- [TailwindCSS](https://tailwindcss.com/) CSS Framework.
  - package.json
  - package-lock.json
  - tailwind.config.js
- [HTMX](https://htmx.org/) HTMX give access to AJAX, CSS Transitions, WebSockets and Server Sent Events directly from HTML.
- [django-htmx](https://django-htmx.readthedocs.io/en/latest/) Django extension for HTMX.
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) Add manage commands to the django and more.
- [gunicorn](https://gunicorn.org/) WSGI HTTP Server for Python web applications.
- [sentry-sdk](https://docs.sentry.io/platforms/python/) Used for error report. 
- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html) Used for serving static files.
- [django-allauth](https://docs.allauth.org/en/latest/) Add a more complete auth. 
- [django-environ](https://django-environ.readthedocs.io/en/latest/) Manage env vars.
- [Flowbite](https://flowbite.com/) Componentes created on top of Tailwind.
  - package.json
  - package-lock.json
- [AlpineJS](https://alpinejs.dev/) JavaScript Framework.
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) Add manage commands to the django and more. 

### ...and development

- [django-browser-reload](https://github.com/adamchainz/django-browser-reload) Auto reload the browser when change a template. Usefull for TailwindCSS. 
- [ruff](https://docs.astral.sh/ruff/) Linter and code formater. 
- [model_bakery](https://model-bakery.readthedocs.io/en/latest/) Used for fixtures in tests. 
- [Pytest](https://docs.pytest.org/en/8.0.x/) Tools for testing.
- [Pytest-django](https://pytest-django.readthedocs.io/en/latest/) Pytest Plugin for Django
- [Marimo](https://marimo.io/) Notebook for test, prototype, inspections, etc.
  - extras/local - It's on .gitignore, for personal notebooks.
  - local/template.py - Template for a new notebook.

## Dev environment setup

1. Install Just, Docker and Poetry(optional).
2. Copy .env.example to .env, no need for edition.
3. `$ just build`

## Run the server for development

1. Certified that docker is up and running
2. `$ just runserver`
3. Create a superuser so you can login and/or create a User. 

You can run `$ just` to see the available commands.

You can access the Django app on http://0.0.0.0:8000/ and Marimo notebook on http://0.0.0.0:2718/


