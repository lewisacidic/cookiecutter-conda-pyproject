FROM {{ cookiecutter.docker_base_image }} AS base

LABEL maintainer="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>"

RUN mkdir /app
WORKDIR /app

COPY envs /app/envs
RUN conda env update -n base -f envs/prod.yml && conda clean --all -f -y

# ====== DEVELOPMENT ======

FROM base AS development

RUN conda env update -n base -f envs/dev.yml -f envs/test.yml && conda clean --all -f -y
COPY . /app
RUN python -m pip install -e. --no-deps --ignore-installed

ENTRYPOINT bash
CMD []

# ====== PRODUCTION ======

FROM base as production

COPY . /app
RUN python -m pip install . --no-deps --ignore-installed

CMD ["python" "-m", "{{ cookiecutter.project_slug }}"]

