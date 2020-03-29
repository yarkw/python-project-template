# python-project-template

## Prerequisites

Install pyenv and pipenv globally.

```
pip install pyenv pipenv
```

## Setup

```
git clone git@github.com:space0x20/python-project-template.git
pipenv shell
pipenv check
pipenv install
```

## Python version and package management

* Use [pyenv](https://github.com/pyenv/pyenv) for python version management.
* Use [pipenv](https://github.com/pypa/pipenv) for package management.

## Linting

* Use [pycodestyle](https://github.com/PyCQA/pycodestyle) to check code style conventions from PEP8.
* Use [pydocstyle](https://github.com/PyCQA/pydocstyle/) to check docstring style conventions from PEP257.
* Use [flake8](https://www.pylint.org/) to check source files for errors.
* Use [yapf](https://github.com/google/yapf) to format source code.
* Use [isort](https://github.com/timothycrosley/isort) for sorting imports.
* Use [MyPy](http://mypy-lang.org/) for static type checking.

## Testing

* Use [pytest](https://docs.pytest.org/en/latest/)
