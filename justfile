# Lista os comandos quando executar sem argumentos
default:
  just --list

# Cria a imagem docker
build:
  docker compose build

# Sobe o servidor em desenvolvimento com hot reload
runserver:
  docker compose up --build

# Roda o comando manage.py dentro do container
mng command:
  docker compose run --rm web python manage.py {{command}}

# Entra no console do container web
sh:
  docker compose run --rm web sh

# Ruff format
ruff:
  docker compose run --rm web ruff check --fix
  docker compose run --rm web ruff format

# Ruff check
check:
  docker compose run --rm web ruff check