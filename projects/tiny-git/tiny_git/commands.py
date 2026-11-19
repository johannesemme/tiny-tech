

import argparse
import sys
from pathlib import Path

def init_repo(args: argparse.Namespace) -> None:
    # If .tg/ already exists, tg init refuses.
    if Path(".tg").exists():
        print("tg: repository already exists", file=sys.stderr)
        sys.exit(1)

    # Create the .tg folder 
    Path(".tg").mkdir()

    # Create the HEAD file
    head_path = Path(".tg") / "HEAD"
    with open(head_path, "w") as f:
        f.write("ref: refs/heads/main\n")

    # Create the refs/heads/ folder for future head references
    refs_heads_path = Path(".tg") / "refs" / "heads"
    refs_heads_path.mkdir(parents=True)

    # Create the objects/ folder
    objects_path = Path(".tg") / "objects"
    objects_path.mkdir(parents=True)

    # Print success message
    print("Initialized empty tiny-git repository in .tg")