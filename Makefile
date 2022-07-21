MANAGE := poetry run python manage.py

install:
	poetry install

lint:
	poetry run flake8 where_to_go

db-clean:
	@rm db.sqlite3 || true

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

mmigrate: makemigrations migrate

run:
	$(MANAGE) runserver

compile:
	$(MANAGE) compilemessages --ignore=cache --ignore=.venv/*/locale

messages:
	$(MANAGE) makemessages -l ru