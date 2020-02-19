{{ cookiecutter.header }}
"""Invoke tasks."""
import sys

from invoke import task
import semver
import versioneer


@task(help={"python": "whether to lint `.py` files", "all": "run on all files"})
def lint(ctx, python=True, all=False):  # noqa: A002
    """Lint the codebase."""
    if python:
        ctx.run("flake8 .")


@task(name="format", help={"python": "whether to format `.py` files", "all": "run on all files"})
def format_(ctx, python=True, all=False):  # noqa: A002
    """Autoformat the codebase."""
    if python or all:
        ctx.run("reorder-python-imports {,**/}*.py")
        ctx.run("black .")


@task(
    help={
        "build": "whether to delete `build/` directory",
        "dist": "whether to delete `dist/` directory",
        "bytecode": "whether to delete python bytecode",
        "reports": "whether to delete reports",
        "coverage": "whether to remove the .coverage file",
        "pytest": "whether to remove the .pytest_cache",
        "all": "clean all temporary files",
    }
)
def clean(
    ctx,
    build=True,
    dist=False,
    bytecode=False,
    reports=False,
    coverage=True,
    pytest=True,
    all=False,  # noqa: A002
):
    """Clean temporary files from the project."""
    patterns = []
    if build or all:
        patterns.append("build")
    if dist or all:
        patterns.append("dist")
    if bytecode or all:
        patterns.append("**/*.pyc")
        patterns.append("{,**/}__pycache__")
    if reports or all:
        patterns.append("reports")
    if coverage or all:
        patterns.append(".coverage")
    if pytest or all:
        patterns.append(".pytest_cache")
    for pattern in patterns:
        ctx.run(f"rm -rf {pattern}")


@task
def test(ctx):
    """Run the project tests."""
    ctx.run("pytest")


@task
def new(ctx, path, module=True, package=False):
    """Create new source files."""
    if module:
        ctx.run(f"jinja2 templates/module.py.tmpl {path}.py")
    if package:
        ctx.run(f"mkdir -p {path}")
        ctx.run(f"jinja2 templates/module.py.tmpl {path}/__init__.py")


@task
def version(ctx, kind):
    """Bump the project version."""

    version_info = versioneer.get_versions()

    if version_info["dirty"]:
        print("Git working directory not clean.\n")
        ctx.run("git status -s")
        print("\nPlease commit changes or stash them before creating a release.")
        sys.exit(1)
    v = version_info["version"].lstrip("v").split("+")[0]
    v = semver.parse_version_info(v)
    try:
        new_v = getattr(v, f"bump_{kind}")()
    except AttributeError:
        print(f"{kind} is not a valid semver versioning level.")
        sys.exit(1)

    ctx.run(
        f'git commit --no-verify --allow-empty -m"chore: bump version {v} → {new_v}"'
    )
    ctx.run(f'git tag -as -m"Release {new_v}" v{new_v}')

