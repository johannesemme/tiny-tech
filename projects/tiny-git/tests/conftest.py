"""Shared test helpers.

Every test gets a fresh, empty temporary folder (pytest's built-in`tmp_path`) and runs
the real `tg` command in it. Where possible, the result is checked with real
`git`, pointed at our `.tg/` folder.
"""

import subprocess

import pytest


@pytest.fixture
def tg(tmp_path):
    """Run `tg <args>` in the test's temporary folder."""

    def run(*args):
        return subprocess.run(["tg", *args], cwd=tmp_path, capture_output=True, text=True)

    return run


@pytest.fixture
def git(tmp_path):
    """Run real `git <args>` against the .tg/ folder in the test's temporary folder."""

    def run(*args):
        return subprocess.run(
            ["git", "--git-dir=.tg", "--work-tree=.", *args],
            cwd=tmp_path,
            capture_output=True,
            text=True,
        )

    return run
