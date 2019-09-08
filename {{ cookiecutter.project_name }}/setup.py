{{ cookiecutter.header }}
"""Set up {{ cookiecutter.project_name }}."""

from setuptools import find_packages
from setuptools import setup

name = "{{ cookiecutter.project_name }}"
description = "{{ cookiecutter.project_description }}"
license_ = "{{ cookiecutter.license }}"

author = "{{ cookiecutter.author_name }}"
author_email = "{{ cookiecutter.author_email }}"

home_url = "{{ cookiecutter.project_url }}"
docs_url = "{{ cookiecutter.docs_url }}"
source_url = "{{ cookiecutter.source_url }}"
bugtracker_url = "{{ cookiecutter.bugtracker_url }}"
download_url = "{{ cookiecutter.download_url }}"

classifiers = [
    "Development Status :: 2 - Pre-Apha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only"
    "Programming Language :: Python :: 3.7",
    "Natural Language :: English",
]

keywords = [{% for kw in cookiecutter.keywords.split(",") %}
    "{{ kw.strip() }}"{% endfor %}
]


def read_readme():
    """Load the project README."""
    with open("README.md") as readme:
        return readme.read()


setup_requirements = [
    "setuptools_scm"
]

install_requirements = [
    "importlib_metadata; python_version<'3.8'"
]

dev_requirements = [
    "ipython",
    "black",
    "rope",
    "flake8",
    "flake8-bandit",
    "flake8-bugbear",
    "flake8-builtins",
    "flake8-mutable",
    "flake8-print",
    "pep8-naming",
    "pre-commit"
]

test_requirements = [
    "pytest",
    "pytest-cov"
]


if __name__ == "__main__":
    setup(
        author=author,
        author_email=author_email,
        classifiers=classifiers,
        description=description,
        download_url=download_url,
        extras_require={
            "dev": dev_requirements,
            "test": test_requirements
        },
        install_requires=install_requirements,
        keywords=keywords,
        license=license_,
        long_description=read_readme(),
        name="{{ cookiecutter.project_slug }}",
        packages=find_packages(include="src"),
        package_dir={"": "src"},
        project_urls={
            "Trackers": bugtracker_url,
            "Source": source_url,
            "Documentation": docs_url
        },
        setup_requires=setup_requirements,
        tests_require=test_requirements,
        test_suite="tests",
        url=docs_url,
        use_scm_version=True,
        zip_safe=False
    )
