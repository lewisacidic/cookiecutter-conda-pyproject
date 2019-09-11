{{ cookiecutter.header }}
"""Tests for metadata loading."""

import pytest
import importlib
try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata


root = importlib.import_module("{{ cookiecutter.project_slug }}")


@pytest.parametrize("field", ["distname", "name", "copyright", "license", "name", "url", "version"])
def test_metadata(field):
    """Test metadata is available on base package"""
    importlib.reload(root)
    assert getattr(root, f"__{field}__") is not None


