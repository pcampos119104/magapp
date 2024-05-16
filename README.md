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
- [Just](https://just.systems/) Usado para encapsular comandos
  - justfile
- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html) Usado para gerenciar arquivos estaticos, neste caso, somente servir pelo django 
- [HTMX](https://htmx.org/) htmx da acesso a AJAX, CSS Transitions, WebSockets e Server Sent Events direto no HTML   
- [TailwindCSS](https://tailwindcss.com/) Framework CSS
- [Flowbite](https://flowbite.com/) Componentes construido em cima do Tailwind
- [AlpineJS](https://alpinejs.dev/) Framework JavaScript

### ...de desenvolvimento

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) Contem commandos e ferramentas para auxiliar no desenvolvimento
- [Pytest](https://docs.pytest.org/en/8.0.x/) Conjunto de ferramentas para testes.
- [Pytest-django](https://pytest-django.readthedocs.io/en/latest/) Plugin do Pytest para o Django 
- [Marimo](https://marimo.io/) Notebook utilizado para desenvolver algoritmos, testar, debugar e etc.
  - extras/local - Esta no .gitignore, para notebooks pessoais
  - extras/template_marimo.py - Template para criar um novo notebook.

## Instalacao do ambiente de desenvolvimento

1. Instale o Just, Docker e Poetry(opcional).
2. Copie o .env.example para .env, nao precisa alterar
3. `$ just build`

## Subir o servidor

1. Certifique-se de que o dockerd esteja rodando
2. `$ just runserver`

O servidor ja sobe o runserver do Django na porta 8000 e o Marimo na porta 2718
