build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

test:
	pre-commit run --all
	docker-compose run --rm django pytest -v

migrate:
	docker-compose run --rm django python manage.py migrate

remove_draft:
	docker-compose run --rm django python manage.py remove_draft

makemigrations:
	docker-compose run --rm django python manage.py makemigrations

notebook:
	docker-compose run --rm -p 8888:8888 django python manage.py shell_plus --notebook

rebuild:
	echo "TODO"
