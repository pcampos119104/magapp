# Magapp 

Sistema de alimentacao familiar

## Ferramentas utilizadas e seus arquivos, se tiver.

As versoes utilizadas estao no Poetry.

- [Python](https://www.python.org/) Linguagem de programç�o
- [django-environ](https://django-environ.readthedocs.io) Gerencia .envs no Django
- [Poetry](https://python-poetry.org/) Python packaging and dependency management
  - poetry.lock
  - pyproject.toml
- [Django](https://www.djangoproject.com/) Framework web escrito em Python
- [Docker](https://www.docker.com/) Criar e gerenciar containers para ambiente dev
  - compose.yaml
  - compose/Dockerfile
  - compose/start
- [gunicorn](https://gunicorn.org/) Servidor WSGI HTTP Python para UNIX
- [sentry-sdk](https://docs.sentry.io/platforms/python/) Usado para reportar erros no sistema
- [psycopg](https://www.psycopg.org/) Adaptador python para o Postgres
- [Just](https://just.systems/) Usado para encapsular comandos
  - justfile
- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html) Usado para gerenciar arquivos estaticos, neste caso, somente servir pelo django 
- [HTMX](https://htmx.org/) htmx da acesso a AJAX, CSS Transitions, WebSockets e Server Sent Events direto no HTML   
- [django-htmx](https://django-htmx.readthedocs.io/en/latest/) Extensao para usar o Django com HTMX
- [django-allauth](https://docs.allauth.org/en/latest/) Add Django para autenticacao e autorizacao. 
- [django-environ](https://django-environ.readthedocs.io/en/latest/) Gerencia variaveis de ambiente 
- [TailwindCSS](https://tailwindcss.com/) Framework CSS
- [Flowbite](https://flowbite.com/) Componentes construido em cima do Tailwind
- [AlpineJS](https://alpinejs.dev/) Framework JavaScript

### ...de desenvolvimento

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) Contem commandos e ferramentas para auxiliar no desenvolvimento
- [django-browser-reload](https://github.com/adamchainz/django-browser-reload) Atualiza a pagina no navegador quando salva um arquivo, util quando desenvolvento com tailwind 
- [ruff](https://docs.astral.sh/ruff/) Linter e formatacao de codigo  
- [model_bakery](https://model-bakery.readthedocs.io/en/latest/) Usado para criar fixtures para testes 
- [Pytest](https://docs.pytest.org/en/8.0.x/) Conjunto de ferramentas para testes.
- [Pytest-django](https://pytest-django.readthedocs.io/en/latest/) Plugin do Pytest para o Django 
- [Marimo](https://marimo.io/) Notebook utilizado para desenvolver algoritmos, testar, debugar e etc.
  - extras/local - Esta no .gitignore, para notebooks pessoais
  - extras/template_marimo.py - Template a se usar para criar um novo notebook.

## Instalacao do ambiente de desenvolvimento

1. Instale o Just, Docker e Poetry(opcional).
2. Copie o .env.example para .env, nao precisa alterar
3. `$ just build`

## Subir o servidor

1. Certifique-se de que o dockerd esteja rodando
2. `$ just runserver`

O servidor ja sobe o runserver do Django na porta 8000 e o Marimo na porta 2718
