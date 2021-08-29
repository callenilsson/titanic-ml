# Titanic ML

This repository provides a solution to the Kaggle exercise [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic), where the task is to predict which passengers survived the Titanic shipwreck. The goal of this solution is not to achieve the best model accuracy, but rather demonstrate the thinking process of how a typical machine learning problem should be approached.

## Experimental solution
The initial solution is provided in the Jupyter Notebook [experiment.ipynb](experiment.ipynb), and was completed in roughly 6-7 hours. It goes through the following steps:
 1) Understanding the data (histograms, bar plots, etc)
 2) Data cleaning
 3) Feature engineering
 4) Data encoding
 5) Model training
 6) Model tuning
 7) Feature importance

## Backend solution
An additional backend solution in the folder `titanic/` was also written over an extra 7-8 hours based on the findings in the Jupyter Notebook. This is to demonstrate the skill set that a typical notebook does not provide when working as a Data Analyst/Engineer. The backend treats the dataset as if it was a designated product for a client, with data and model versioning hypothetically running in the cloud.

The backend has functions to parse the raw data according to the schemas in `titanic/data/`, provide data cleanup, feature engineering, and data encoding. A hypothetical scheduled cloud job `titanic/ml/scheduled_train.py` then trains a model (SVC - Support Vector Classifier), and saves the model and the encoder by versioning on date in the folder `titanic/ml/models/` (should be cloud storage). An API exposes the model to an endpoint by loading the latest model and encoder version, and given a set of input parameters, predicts the survival probability of a passenger, to be used by a hypothetical frontend.

For demonstration purposes, the next following parts of the README have been written as if this was a real project for a client.

## WoW - Git

For maintainability and overview it's better if everyone follows the following guidelines while using git.

### Single purpose commits / branches

The scope of a commit should be a single change.
If you have to write an `&` in your commit message, you should split the changes into multiple commits.
The scope of a branch should follow the same logic but at a larger scale.

### Commit messages

Commit messages should be concise and should summarize the content of the commit so it fits in the commit header in github (72 chars).
If needed you can also write a longer description of why the solution was shaped the way it was.
This context allows future development to understand / adapt easier if the scenario changes.
As a general rule, you should write the intent of the commit rather than what was changed (if this is not the same).
This allows for easier identification of errors and allows developers to understand changes in the project simply from reading the commit messages rather than understanding the code.

Commits should be written according to the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) practice, which is is used to provide context for all commits. It makes them a lot more readable, allows for easier debugging, and assists in maintaining a good overview of the project, as those messages can be interpreted by machines. A few example types are:

- `fix`: used for functional fixes
- `feat`: new functionality
- `test`: test added
- `refactor`: changes that are not intended to change behaviour in any way
- `revert`: for reverts of commits
- `other`: remaining commits

In addition to this, use the `!` flag on a conventional commit to signal that this will be a breaking commit. E.g `feat!: <commit message>`.

#### Commit template

To get a commit template on your local machine, run the following command.

```bash
make init
```

### Branching

In general, all changes should be done on individual feature branches.
This allows the project to use PR's which improve knowledge sharing, quality maintenance and allows for parallel work.
Feature branches should be named using kebab-case and should describe context of the changes included in the branch.
Whenever you realize that a branch is no longer required, you are responsible for removing it.
E.g. after an accepted and merged PR.

### Pull requests

In general, it should be okay for the reviewer to merge your changes if they approve the review request.
PR's is to be accepted by another developer.
Minor fixes and chores can be performed by reviewer.
The reviewer should update the story/task progress after accepting a pull request.

`Squash and merge` is the preferred way of merging to the main development branch, whilst `Merge commit` is blocked.

## Setting up
### 1. pyenv & poetry
This repository expects you to have [`poetry`](https://python-poetry.org/) installed, a tool for managing your python library dependencies for each project using virtual python environments. It also expects you to have python `>= 3.7.1, < 3.9` installed.
It is recommended to use [`pyenv`](https://github.com/pyenv/pyenv) to manage your local python versions.
[This blog post](https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/) explains how to setup both `pyenv` and `poetry`on your computer.

```bash
# Activate the poetry virtual python environment. Possible to run python commands as normally after this.
poetry shell

# Exit the poetry virtual python environment
exit
```

### 2. direnv
For easily managing environment variables, it is recommended to have [`direnv`](https://direnv.net/) installed. It is an extension to the terminal that automatically loads/unloads environment variables depending on the current directory. This makes it very easy to switch between multiple projects, each with their own environment variables.

Placeholder environment variable secrets are defined in the file `.envrc.example`, but should be filled in with the correct values, and placed in a new file `.envrc`. However, if possible, it is a lot more convenient to use a cloud keystore instead to avoid passing around `.envrc` files across different people all the time.

## Install

Before installing, make sure that you have the tools installed specified in the [Setting up](#setting-up).
After that, it is possible to install the project dependencies by running the following commands:

```bash
make init
make install
```

## Development

When developing, you should do this on a separate branch.
Make sure to check that the code conforms to the linter, formatter, complexity analyzer and security analyzer before making a pull request. Also, make sure that the tests succeed. This can be done by running the following commands:

```bash
make check
make test
```

If you have run the `make init` command, you will have the `pre-push` [hook](.github/.githooks/pre-push) enabled that will check and test the code before pushing to remote. A [Github Actions Workflow](.github/workflows/check-and-test.yaml) event will be triggered on `push` and `pull_request` and check & test the code also. This is to lower the risk of pushing broken code master.


### Writing and running tests
To make sure that your changes doesn't break anything, don't forget to run the tests.
```bash
# Run all the tests in the tests/ directory
make test
```

When developing a new feature, be sure to write relevant tests in the `tests` directory.
Relevant tests are:
 * Unit tests that ensure that the basics of a function work as expected.
 * Integration tests across multiple functions.

If relevant and applicable, use [`pytest markers`](https://docs.pytest.org/en/stable/mark.html). By marking tests, it is possible to specify which kinds of test you wish to run.
To see the available markers, run the following command:

```bash
# Get a list of the available pytest markers
poetry run pytest --markers
```

### Develop Github Action Workflows

To be able to test your new/updated Github Actions workflows locally, you can use the framework [`act`](https://github.com/nektos/act#installation).

Once you have [`act`](https://github.com/nektos/act#installation) installed, you can for example run a specific job locally by running the following commands.

```bash
# List the actions
act -l

# Download the same environment that github action workflow uses
docker pull nektos/act-environments-ubuntu:18.04

# Run the job check-and-test, specify docker environment, and secrets file (.envrc)
act -j check-and-test -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 --secret-file=.envrc
```

## Titanic ML API
The Titanic ML API is built using [FastAPI](https://fastapi.tiangolo.com/), and with its usage of [pydantic](https://pydantic-docs.helpmanual.io/) allows runtime type checking of all data. This ensures that all API users can trust the data 100%, while also making it impossible for users to provide incorrect data back to the API as well. Data in and out is **always** clean, all in line with the Data as a Product mindset. However, the data could still pass while being logically incorrect, despite having correct types. This is ignored for now. The schemas that the data parser uses is also built using pydantic, to ensure that the training/test data is always correct as well.

The added benefit of using FastAPI is that it uses the Documentation as Code principle. Meaning it automatically generates documentation from the code, and exposes a Swagger/OpenAPI endpoint to be used by its users.

To expose the Titanic API, run the following command:
```bash
# Expose the Titanic API on:
# - Swagger: localhost:8000/docs
# - OpenAPI: localhost:8000/redoc
uvicorn titanic.api.provider.api:app --reload
```