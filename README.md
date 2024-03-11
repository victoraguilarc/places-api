## Places API

API to enrich places with weather forecasts.

![styleguide](https://img.shields.io/badge/styleguide-flake8-blue)
![Coverage](web/badges/coverage.svg)

### Stack

* [Django](https://www.djangoproject.com/) as main web Framework
* [Django Rest Framework](http://www.django-rest-framework.org/) as API development tooling
* [Postgres](http://www.django-rest-framework.org/) for SQL Database
* [Redis](http://redis.io/) for caching and memoizations.
* [Docker/docke-compose](http://www.django-rest-framework.org/) for development and standalone deployments.

### Features

- [x] Registration
- [x] Autthentication (JWT Token)
- [x] Accounts (Users)
- [x] Places

## Getting started

### Development

You need to have installed `git`, `docker`, `ssh` and a decent `terminal`.

1. `make build` build the images for development.
2. `make fixtures` load initial data (optional).
3. `make up` start development server.
4. Open `localhost:8000` in your browser.

### Useful commands

* `make debug` to enable `debug` mode for development.
* `make migrations` run django makemigrations command
* `make migrate` run django migrate command
* `make superuser` make a superuserfor develoment

#### Code Quality

* `make test` run pytest over all test files in the project
* `make test ARG=path_to_file` run pytest of a single test file.
* `make coverage` run pytest and generate the coverage report.
* `make isort` Fix posible import issues
* `make lint` run flake8 and generate linting report.
* `make report_coverage` serves the coverage report as html at `localhost:3000`
* `make report_lint` serves the lint report as html at `localhost:3001`
* `make code_review` run formatting linting and tests in just one command.

#### Translation

* `make locales` harverst translate string and generate .po files.
* `make compile_locales` compile translation strings.

### Code Quality

Firstly we need to configure pre-commit hooks, we need to do this just one time.

* `brew install pre-commit` installs pre-commit
* `pre-commit install` install hooks in the current repo.
* `pre-commit autoupdate` enables the pre-commit autoupdate.

## Tools

- Postman Collection


