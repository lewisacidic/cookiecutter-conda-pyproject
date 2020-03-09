{{ cookiecutter.header }}
"""Tests for metadata loading."""

import pathlib
import importlib
import runpy

import pytest


BASEDIR = pathlib.Path(__file__).parents[1]


@pytest.fixture
def base_pkg():
    """Provide a reloaded base package as a fixture."""
    pkg = importlib.import_module("{{ cookiecutter.project_slug }}")
    return importlib.reload(pkg)


@pytest.mark.parametrize(["field", "value"], [
    ("distname", "{{ cookiecutter.project_name }}"),
    ("name", "{{ cookiecutter.project_slug }}"),
    ("copyright", "{{ cookiecutter.copyright }}"),
    ("license", "{{ cookiecutter.license }}"),
    ("url", "{{ cookiecutter.project_url }}"),
])
def test_metadata(base_pkg, field, value):
    """Test metadata is available on base package."""
    assert getattr(base_pkg, f"__{field}__") is not None


@pytest.mark.srconly
def test_version(base_pkg):
    """Test the version is correctly detected with versioneer."""
    # get version using versioneer.py script 
    versioneer_path = str(BASEDIR.joinpath("versioneer.py"))
    versioneer = runpy.run_path(versioneer_path)
    version = versioneer["get_version"]()
    assert base_pkg.__version__ == version  # noqa: WPS609


@pytest.mark.srconly
def test_import_fails():
    """Test behaviour if import fails."""
    # if we run __about__ as a script with runpy, imports will fail
    about_path = str(BASEDIR.joinpath("src", "{{ cookiecutter.project_slug }}", "__about__.py"))
    about = runpy.run_path(about_path)
    assert about["__version__"] is None

