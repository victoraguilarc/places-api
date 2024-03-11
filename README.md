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
3. Copy the `.env.local` to `.env` and fill the required variables.
4. `make up` start development server.
   5Open `localhost:8000` in your browser.

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

- [Postman Collection Link](https://collectives-pro.postman.co/workspace/collectives-api~8fee08f2-f4e0-43f9-a60d-6dbffe3f54f0/collection/7561664-6eb706a0-83d1-43f5-ac6c-a85ce2c00210?action=share&creator=7561664&active-environment=7561664-af6ab1ce-cf25-4f93-8144-9871781b7ee1)
- [Postmand Docs](https://documenter.getpostman.com/view/7561664/2sA2xh4Dnw)

## Deployment

This project was deployed in Digital Ocean using docker-compose and a nginx reverse proxy in
a Ubuntu 22.04 droplet in the domain https://places.codemia.dev.

