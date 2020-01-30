# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}


## Installation

```shell
pip install {{ cookiecutter.project_name }}
```


## Usage

```python
import {{ cookiecutter.project_slug }}
```


## Development

Create the development conda environment:

```shell
conda env create -n {{ cookiecutter.project_name }}-dev -f envs/dev.yml -f envs/prod.yml envs/test.yml -f envs/self.yml
conda activate {{ cookiecutter.project_name }}-dev
```

Format code by running the pre-commit tasks:

```shell
pre-commit run --all
```

Run the tests with pytest:

```shell
pytest
```

Build the production testing environment:

```shell
conda env create -n {{ cookiecutter.project_name }}-prod -f envs/prod.yml -f envs/self.yml
conda activate {{ cookiecutter.project_name }}-prod
```

