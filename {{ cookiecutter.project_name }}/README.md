# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Starting up

Create the conda environment:

```shell
conda env create -f envs/dev.yml
conda activate {{ cookiecutter.project_name }}-dev
```

## Format code

Format code by running the pre-commit tasks:

```shell
pre-commit run --all
```

## Run tests

Run the tests with pytest:

```shell
pytest
```
