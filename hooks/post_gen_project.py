# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Rich Lewis
# License: MIT

import pathlib
import shutil
import subprocess
from subprocess import DEVNULL


if __name__ == "__main__":
    proj = pathlib.Path.cwd()

    # create the .gitattributes (required for versioneer) now
    attrpath = proj.joinpath(".gitattributes")
    attrpath.write_text("src/{{ cookiecutter.project_slug }}/_version.py export-subst")

    # dont include a license if no license provided
    if "{{ cookiecutter.license }}" != "No license":
        shutil.move(
            proj.joinpath("licenses", "{{ cookiecutter.license }}"),
            proj.joinpath("LICENSE"),
        )

    shutil.rmtree(proj.joinpath("licenses"))

    # remove config for other vcs type
    if "{{ cookiecutter.vcs_remote_type}}" == "github":
        shutil.rmtree(proj.joinpath(".gitlab"))
        proj.joinpath(".gitlab-ci.yml").unlink()
    elif "{{ cookiecutter.vcs_remote_type}}" == "gitlab":
        shutil.rmtree(proj.joinpath(".github"))

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
    
    Used https://github.com/lewisacidic/cookiecutter-rich-pyproject
    to scaffold the project.
    """

    if subprocess.call(["git", "commit", f"-m{msg}"]):
        print("Failed to create initial commit.")
    if subprocess.call(["git", "tag", "v0.0.0", "-m", "0.0.0: initial release"]):
        print("Failed to create tag.")
