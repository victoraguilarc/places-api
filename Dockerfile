FROM python:3.11-slim-buster as image_base

ENV NODE_VERSION 18.17.0
ENV POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_CREATE=false

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDEBUG 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential libssl-dev libffi-dev \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext bash xz-utils curl \
  # Install node
  && curl "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-arm64.tar.xz" -O \
  && tar -xf "node-v$NODE_VERSION-linux-arm64.tar.xz" \
  && ln -s "/node-v$NODE_VERSION-linux-arm64/bin/node" /usr/local/bin/node \
  && ln -s "/node-v$NODE_VERSION-linux-arm64/bin/npm" /usr/local/bin/npm \
  && ln -s "/node-v$NODE_VERSION-linux-arm64/bin/npx" /usr/local/bin/npx \
  # Timezone
  && apt-get install -y tzdata \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


ENV TZ UTC

RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml /app/

RUN poetry config --local installer.no-binary psycopg2
RUN poetry install --no-interaction --no-ansi --with dev

COPY compose/post-build /post-build
RUN sed -i 's/\r//' /post-build
RUN chmod +x /post-build

EXPOSE 8000

#
#  D E V E L O P M E N T
#
FROM image_base as development

COPY compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY compose/start-dev /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT ["/entrypoint"]

