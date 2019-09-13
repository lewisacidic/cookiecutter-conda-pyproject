{{ cookiecutter.header }}
"""Metadata for {{ cookiecutter.project_name}}."""

# guard import as this is exec'd with runpy in setup.py so import will fail
try:
    from ._version import get_versions

    __version__ = get_versions()["version"]
    del get_versions
except ImportError:
    __version__ = None

__distname__ = "{{ cookiecutter.project_name }}"
__name__ = "{{ cookiecutter.project_slug }}"
__description__ = "{{ cookiecutter.project_description }}"
__license__ = "{{ cookiecutter.license }}"
__copyright__ = "{{ cookiecutter.copyright }}"

__author__ = "{{ cookiecutter.author_name }}"
__author_email__ = "{{ cookiecutter.author_email }}"

__url__ = "{{ cookiecutter.project_url }}"
__docs_url__ = "{{ cookiecutter.docs_url }}"
__source_url__ = "{{ cookiecutter.source_url }}"
__bugtracker_url__ = "{{ cookiecutter.bugtracker_url }}"
__download_url__ = "{{ cookiecutter.download_url }}"

__classifiers__ = [
    "Development Status :: 2 - Pre-Alpha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Natural Language :: English",
]

__keywords__ = [{% for kw in cookiecutter.keywords.split(",") %}
    "{{ kw.strip() }}",{% endfor %}
]

__all__ = [
    "__author__",
    "__author_email__",
    "__bugtracker_url__",
    "__classifiers__",
    "__copyright__",
    "__description__",
    "__distname__",
    "__docs_url__",
    "__download_url__",
    "__keywords__",
    "__license__",
    "__name__",
    "__source_url__",
    "__url__",
    "__version__",
]
