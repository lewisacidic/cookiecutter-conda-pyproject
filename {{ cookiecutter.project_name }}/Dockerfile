FROM {{ cookiecutter.docker_base_image }} AS base

LABEL maintainer="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>"

RUN mkdir /app
WORKDIR /app

COPY env.yml .
RUN conda env update -n base -f env.yml && conda clean --all -f -y

COPY . .
RUN python -m pip install -e. --no-deps --ignore-installed

CMD ["bash"]
