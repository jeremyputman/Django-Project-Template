# Makefile
.PHONY: install run migrate test lint clean

install_dev:
 uv add -r requirements/development.txt

install_prod:
 uv add -r requirements/production.txt

run:
 uv run manage.py runserver_plus 0.0.0.0:8080

run_ssl:
 uv run manage.py runserver_plus 0.0.0.0:8443 --cert-file certs/fullchain.pem --key-file certs/privkey.pem"

migrate:
 python manage.py makemigrations
 python manage.py migrate

test:
 pytest --cov=apps --cov-report=html

lint:
 ruff check apps/
 ruff format apps/

shell:
 python manage.py shell_plus

clean:
 find . -type f -name '*.pyc' -delete
 find . -type d -name '__pycache__' -delete