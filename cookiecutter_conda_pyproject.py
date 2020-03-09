# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Rich Lewis
# License: MIT
"""Run the cookiecutter."""

import pathlib

from cookiecutter.main import cookiecutter


if __name__ == "__main__":
    cookiecutter(str(pathlib.Path(__file__).parent))
