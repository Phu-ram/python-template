#!/usr/bin/env sh

pip install --user poetry
poetry install

git init
git checkout -b main
