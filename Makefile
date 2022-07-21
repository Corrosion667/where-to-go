MANAGE := poetry run python manage.py

install:
	poetry install

lint:
	poetry run flake8 where_to_go

db-clean:
	@rm db.sqlite3 || true

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

run:
	$(MANAGE) runserver