.DEFAULT_GOAL: all

# Setup githooks and git commit template
.PHONY: init
init:
	git config commit.template .github/commit_template
	git config core.hooksPath .github/.githooks

# Install poetry
.PHONY: install
install:
	poetry config virtualenvs.in-project true
	poetry install

# Run tests
.PHONY: test
test:
	poetry run pytest tests

# Run lint checking
.PHONY: check
check:
	poetry run flake8 titanic tests
	poetry run pylama -l pylint,mccabe,pep257,pydocstyle,pep8,pycodestyle,pyflakes,mypy titanic tests
	poetry run bandit -r titanic
	poetry run black --check titanic tests
