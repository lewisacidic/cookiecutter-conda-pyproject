{{ cookiecutter.header }}
"""Tests for metadata loading."""

import pytest
import importlib
try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata


root = importlib.import_module("{{ cookiecutter.project_slug }}")


@pytest.parametrize("field", ["distname", "name", "author", "author_email", "copyright", "license", "name", "url", "version"])
def test_metadata(field):
    importlib.reload(root)
    assert getattr(root, field) is not None


