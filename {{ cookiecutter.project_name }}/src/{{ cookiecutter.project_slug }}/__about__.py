{% set _trove_lookup = {
    "MIT": "License :: OSI Approved :: MIT License",
    "BSD-2-Clause": "License :: OSI Approved :: BSD License",
    "BSD-3-Clause": "License :: OSI Approved :: BSD License",
    "Apache-2.0": "License :: OSI Approved :: Apache Software License",
    "GPL-2.0": "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    "GPL-3.0": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "LGPL-2.1": "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "LGPL-3.0": "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "ISC": "License :: OSI Approved :: ISC License (ISCL)",
    "GNU General Public License v3": "GNU General Public License v3 (GPLv3)",
    "No license": "License :: Other/Proprietary License"
}%}{{ cookiecutter.header }}
"""Metadata for {{ cookiecutter.project_name}}."""

# guard import as this is exec'd with runpy in setup.py so import will fail
try:
    from ._version import get_versions  # noqa: WPS433,WPS436

    __version__ = get_versions()["version"]
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
    "Natural Language :: English",{% if cookiecutter.license != "No license" %}
    "{{ _trove_lookup[cookiecutter.license] }}"{% endif %}
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
