.PHONY: docs coverage fixtures
.SILENT: clean
.PRECIOUS: lint

COMPOSE := @docker compose -f docker-compose.yml
COMPOSE_PROD := @docker compose -f docker-compose.prod.yml
COMPOSE_TEST := @docker compose -f docker-compose.yml

ARG=

lock:
	$(COMPOSE) run --rm django poetry lock

build:
	$(COMPOSE) build

up:
	@echo "Server up..."
	$(COMPOSE) up

watch_logs:
	$(COMPOSE) logs -t -f django

frontend_start:
	$(COMPOSE) run --rm django python manage.py tailwind start

frontend_build:
	$(COMPOSE) run --rm django python manage.py tailwind build

down:
	@echo "Server up..."
	$(COMPOSE) down

run:
	$(COMPOSE) run --rm django $(ARG)

tunnel:
	cloudflared tunnel --config tunnel.yml run

command:
	$(COMPOSE) run --rm django python manage.py $(ARG)

debug:
	@echo "Launchings Server for debbugging..."
	$(COMPOSE) run --service-ports django

loaddata:
	@echo "Loading fixtures..."
	$(COMPOSE) run --rm django python manage.py loaddata $(ARG)

fixtures:
	@echo "Loading fixtures..."
	$(COMPOSE) run --rm django python manage.py loaddata api_keys phone_numbers email_addresses users linked_sites tenants tenant_customers tenant_users tenant_classes tenant_class_schedules payment_products payment_prices payment_accounts payment_methods

dumpdata:
	@echo "Getting fixtures..."
	$(COMPOSE) run --rm django python manage.py dumpdata $(ARG)

superuser:
	@echo "Creating superuser..."
	$(COMPOSE) run --rm django python manage.py createsuperuser

migrate:
	@echo "Applying migrations ..."
	$(COMPOSE) run --rm django python manage.py migrate $(ARG)

migrations:
	@echo "Creating migrations ..."
	$(COMPOSE) run --rm django python manage.py makemigrations $(ARG)

squashmigrations:
	@echo "Creating migrations ..."
	$(COMPOSE) run --rm django python manage.py squashmigrations $(APP)

settings:
	@echo "Opening django compiled settings ..."
	$(COMPOSE) run --rm django python manage.py diffsettings

flushdb:
	@echo "Flushing database ..."
	$(COMPOSE) run --rm django python manage.py flush

# Window version: docker ps -aq |  %{docker stop $_}
clean:
	@echo "Cleaning containers ..."
	docker ps -aq | xargs docker stop
	docker ps -aq | xargs docker rm

clean_volumes:
	@echo "Cleaning volumes ..."
	docker volume ls -q | grep places-api | xargs docker volume rm
	docker images | grep "^<none>" | awk '{print $3}' | xargs docker rmi

console:
	@echo "Opening django shell for testing and debbugging"
	$(COMPOSE) run --rm django python manage.py shell_plus

shell:
	@echo "Opening container bash session"
	$(COMPOSE) run --rm django bash

dbshell:
	@echo "Opening database shell"
	$(COMPOSE) run --rm django python manage.py dbshell

stop:
	@echo "Stopping containers"
	docker ps -qa | xargs docker stop

restart: stop up
	@echo "Containers restarted"

show_urls:
	@echo "Show api routes"
	$(COMPOSE) run --rm django python manage.py show_urls

printenv:
	$(COMPOSE) run --rm django python merge_envs.py
	@echo "New [.env] file generated"

test:
	$(COMPOSE_TEST) run --rm django bash -c "DJANGO_ENV=testing pytest --pyargs $(ARG)"

single_test:
	$(COMPOSE_TEST) run --rm django bash -c "DJANGO_ENV=testing pytest --pyargs -m single"

clear_tests_cache:
	$(COMPOSE_TEST) run --rm django pytest -n auto --pyargs --cache-clear

coverage:
	$(COMPOSE_TEST) run django coverage run -m pytest
	$(COMPOSE_TEST) run --rm django coverage report

coverage_tests:
	$(COMPOSE_TEST) run django coverage run -m pytest
	$(COMPOSE_TEST) run --rm django coverage html
	$(COMPOSE_TEST) run --rm django coverage json
	$(COMPOSE_TEST) run --rm django rm -f web/badges/coverage.svg
	$(COMPOSE_TEST) run --rm django coverage-badge -o web/badges/coverage.svg

bash:
	@echo "Opening a shell session"
	$(COMPOSE) run --rm django bash

isort:
	@echo "Sorting imports..."
	@$(COMPOSE) run --rm --no-deps django isort .


lint:
	@echo "Linting..."
	@$(COMPOSE) run --rm --no-deps django ruff check .
#	@$(COMPOSE) run --rm --no-deps django mypy .
#	@$(COMPOSE) run --rm django refurb .
#	@$(COMPOSE) run --rm django vulture .

format:
	@echo "Formatting..."
	@$(COMPOSE) run --rm --no-deps django isort .
	@$(COMPOSE) run --rm --no-deps django black --config=pyproject.toml .

#review: isort typing vulture refurb lint test
code_review: format lint test
	@echo "Review Finished"

locales:
	@echo "Generate traslations"
	$(COMPOSE) run --rm django python manage.py makemessages -l en
	$(COMPOSE) run --rm django python manage.py makemessages -l es

serve_coverage_report:
	@echo "Running coverage report"
	$(COMPOSE_TEST) run --rm django coverage run -m pytest
	$(COMPOSE_TEST) run --rm django coverage html
	cd reports/coverage && python3 -m http.server 3000

compile_locales:
	@echo "Compile traslations"
	$(COMPOSE) run --rm django python manage.py compilemessages

prod_build:
	$(COMPOSE_PROD) build

prod_up:
	@echo "Server up..."
	$(COMPOSE_PROD) up

prod_shell:
	@echo "Opening container bash session"
	$(COMPOSE_PROD) run --rm django bash

