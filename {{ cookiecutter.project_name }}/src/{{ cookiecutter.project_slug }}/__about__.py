{{ cookiecutter.header }}
"""Metadata for {{ cookiecutter.project_name}}."""
import warnings

try:
    from importlib.metadata import distribution
    from importlib.metadata import PackageNotFoundError
except ImportError:
    from importlib_metadata import distribution
    from importlib_metadata import PackageNotFoundError

dist_name = __name__.split(".")[0]

try:
    dist = distribution(dist_name)
    metadata = dist.metadata
except PackageNotFoundError:
    msg = f"{dist_name} does not appear to be installed correctly."
    warnings.warn(msg, UserWarning)
    metadata = {}

__title__ = metadata.get("Name", dist_name)
__description__ = metadata.get("Summary", None)
__url__ = metadata.get("Home-page", None)
__version__ = metadata.get("Version", None)
__author__ = metadata.get("Author", None)
__author_email__ = metadata.get("Author-email", None)
__license__ = metadata.get("License", None)

__all__ = [
    "__title__",
    "__description__",
    "__url__",
    "__version__",
    "__author__",
    "__author_email__",
    "__license__",
]
