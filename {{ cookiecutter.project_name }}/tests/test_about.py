{{ cookiecutter.header }}
"""Tests for metadata loading."""

import pathlib
import importlib
import runpy

import pytest


@pytest.fixture
def base_pkg():
    """Provide a reloaded base package as a fixture."""
    base_pkg = importlib.import_module("{{ cookiecutter.project_slug }}")
    return importlib.reload(base_pkg)


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


def test_version(base_pkg):
    """Test the version is correctly detected with versioneer."""
    versioneer_path = pathlib.Path(__file__).parents[1].joinpath("versioneer.py")
    versioneer = runpy.run_path(versioneer_path)
    version = versioneer["get_version"]()
    assert base_pkg.__version__ == version
