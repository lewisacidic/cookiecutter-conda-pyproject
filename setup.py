# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Rich Lewis
# License: MIT

from setuptools import setup


def read_readme():
    """Load the project readme."""
    with open("README.md") as readme:
        return readme.read()

setup(
    author="Rich Lewis",
    author_email="opensource@richlew.is",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python : 3.8",
        "Natural Language :: English",
        "Framework :: Cookiecutter",
    ],
    description="Cookiecuter for a Conda-based Python project.",
    download_url="https://github.com/lewisacidic/cookiecutter-conda-pyproject",
    install_requirements=["cookiecutter", "license"],
    keywords=["cookiecutter", "conda"],
    license="MIT",
    long_description=read_readme(),
    name="cookiecutter-conda-pyproject",
    py_modules=["cookiecutter_conda_pyproject"],
    project_urls={
        "Trackers": "https://github.com/lewisacidic/cookiecutter-conda-pyproject/issues",
        "Source": "https://github.com/lewisacidic/cookiecutter-conda-pyproject/"
    },
    version="0.0.1",
    zip_safe=False,
)
