#!/usr/bin/env python

import pathlib
import subprocess


def initialize_git_repo():
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "*"])
    msg = """feat(*): scaffold using cookiecutter.
    
    Use https://github.com/lewisacidic/cookiecutter-rich-pyproject
    to scaffold the project.
    """
    subprocess.call(["git", "commit", "-m", msg])


def add_git_hooks():
    proj_dir = pathlib.Path.cwd().resolve()
    for hook in "pre-commit", "commit-msg":
        proj_dir.joinpath(hook).rename(proj_dir.joinpath(".git", "hooks"))


if __name__ == "__main__":
    initialize_git_repo()
    add_git_hooks()
