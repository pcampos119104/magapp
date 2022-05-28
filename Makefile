build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

test:
	pre-commit run --all
	docker-compose run --rm django python manage.py pytest

migrate:
	docker-compose run --rm django python manage.py migrate

migrations:
	docker-compose run --rm django python manage.py makemigrations

notebook:
	docker-compose run --rm -p 8888:8888 django python manage.py shell_plus --notebook

rebuild:
	echo "TODO"