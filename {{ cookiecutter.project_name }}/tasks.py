{{ cookiecutter.header }}
"""Invoke tasks."""
from invoke import task


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
def build(ctx, conda=True):
    """Build a source and wheel distribution."""
    ctx.run("python setup.py build sdist bdist_wheel")
    ctx.run("conda build .")
