ARG PYTHON_VERSION="3.11"

FROM python:${PYTHON_VERSION}-slim-bullseye

ARG POETRY_VERSION="1.4.2"

RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
    build-essential \
    git \
    && pip install "poetry==$POETRY_VERSION" poetry-dynamic-versioning \
    && rm -rf /var/lib/apt/lists/*
