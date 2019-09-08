#!/usr/bin/env python

import subprocess


if __name__ == "__main__":
    # initialize git repo
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "*"])

    # add pre-commit hooks
    for hook in "pre-commit", "commit-msg":
        subprocess.call(["pre-commit" "install", "--hook-type", hook])

    # initial commit
    msg = """feat(*): scaffold using cookiecutter
    
    Use https://github.com/lewisacidic/cookiecutter-rich-pyproject
    to scaffold the project.
    """
    subprocess.call(["git", "commit", "-m", msg, "--no-verify"])
