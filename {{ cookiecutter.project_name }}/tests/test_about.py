{{ cookiecutter.header }}
"""Tests for metadata loading."""
import importlib

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

import pytest

import {{ cookiecutter.project_slug }} as project
from {{ cookiecutter.project_slug }} import __about__ as about


fields = [
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__"
]


@pytest.mark.parametrize("field", fields)
def test_metadata(field):
    """Test metadata fields are importable and not `None`."""
    importlib.reload(about)
    importlib.reload(project)
    assert getattr(project, field) is not None


@pytest.fixture
def distribution_mock(monkeypatch):
    """Mock for `importlib.metadata.distribution`."""

    def inner(name):
        raise importlib_metadata.PackageNotFoundError

    monkeypatch.setattr(importlib_metadata, "distribution", inner)


@pytest.mark.parametrize("field", fields)
def test_with_no_pkg_info(distribution_mock, field):
    """Test metadata fields don't work without distribution info."""

    with pytest.warns(UserWarning):
        importlib.reload(about)
        importlib.reload(project)
        target = "{{ cookiecutter.project_slug }}" if field == "__title__" else None
        assert getattr(project, field) == target
