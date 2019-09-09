#!/usr/bin/env python

import os
import subprocess
from subprocess import DEVNULL


if __name__ == "__main__":
    subprocess.call(["git", "init"])

    # add pre-commit hooks
    for hook in "pre-commit", "commit-msg":
        subprocess.call(["pre-commit", "install", "--hook-type", hook])
    
    # run the precommit hooks to fix anything broken
    subprocess.call(["git", "add", "*"])
    subprocess.call(["pre-commit", "run", "--all"], stdout=DEVNULL)
    subprocess.call(["git", "add", "*"])

    # initial commit
    msg = """feat(*): scaffold using cookiecutter
    
    Use https://github.com/lewisacidic/cookiecutter-rich-pyproject
    to scaffold the project.
    """
    subprocess.call(["git", "commit", "-m", msg])
    subprocess.call(["git", "tag", "-s", "0.0.0" "-m" "Initial release"])
