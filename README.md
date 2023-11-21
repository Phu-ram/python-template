# Python Boilerplate

The Python Boilerplate is the external layer of a development project implementing most up-to-date best practices.

This project aims to define, build and maintain the Python Boilerplate with ease and no pain.

With clear and concise commands, any developer can create and start to deploy a project in an optimized manner.

<!-- TOC depthFrom:2 depthTo:3 -->

- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Contribution](#how-to-contribute-to-this-repository)
- [Resources](#resources)

<!-- /TOC -->

## Installation

### Install cookiecutter

```bash
$ pip install cookiecutter
```

### Generate the boilerplate

```bash
$ python -m cookiecutter git@github.com.com:Phu-ram/...
```

You will be prompted to enter project configuration values:

```bash
project_name [My Awesome Project]: Hello World
project_slug [hello-world]: 
version [0.1.0]: 
python_version [3.8]: 3.9
```

Then, Cookiecutter will generate a ready-to-use Python Boilerplate using the values that you entered. It will be placed in your current directory.

### Upload to Gitlab

First, create a new blank repository on Github.

Then, push your new boilerplate to the remote repository:

```bash
cd hello-world
git init --initial-branch=main
git remote add origin git@github.com:Phu-ram/hello-world.git
git add .
git commit -a -m "Initial Commit"
git push -u origin main
```

## Environment variables
Key | Comment | Default |
--- | --- | --- |
GITLAB_PYPI_USER | PyPI username | ``
GITLAB_PYPI_PASS | PyPI password | ``

The environment variable can be found on [Keeper](https://keepersecurity.com/).

## How to contribute to this repository

If you want to contribute to this repository you have two ways to do it:

- Open a Merge request to suggest or propose a new change using clear commit messages and MR description about why you would like to change something.
- Open an Issue for anything else.

## Resources

- [black](https://github.com/ambv/black/)
- [isort](https://github.com/timothycrosley/isort/)
- [poetry](https://python-poetry.org/docs/)
- [pylint](https://www.pylint.org/)
- [pytest](https://docs.pytest.org/en/stable/)
- [mypy](https://mypy.readthedocs.io/en/stable/)
