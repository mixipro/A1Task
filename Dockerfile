FROM python:3.10-slim

RUN apt-get update; apt-get install -y curl gcc
# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false && pip install --upgrade pip

COPY alembic.ini /alembic.ini

# here we are using dephell to split package versioning from it's dependencies
# since in most cases package version will change far more often than its dependencies
COPY poetry.lock /

COPY pyproject.toml /
COPY ./src/a1task/__init__.py /src/a1task/__init__.py
RUN poetry install --only main

COPY migrations /migrations
COPY ./src/cute_be /src/cute_be
ENV PYTHONPATH=/src

EXPOSE 80
CMD alembic upgrade head && uvicorn a1task.api.main:app --host 0.0.0.0 --port 80 --no-access-log
