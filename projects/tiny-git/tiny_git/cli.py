from tiny_git.commands import init_repo
import argparse

def build_parser() -> argparse.ArgumentParser:
    """Each subcommand gets added to the parser here."""

    # Tells argparse that this is the main parser for the `tg` command
    parser = argparse.ArgumentParser(prog="tg")
    # Tells argparse that a subcommand must be provided after `tg`
    sub = parser.add_subparsers(dest="command", required=True)

    # Add the `init` as a subcommand
    p_init = sub.add_parser("init")
    # Connect the `init` subcommand to the `init_repo` function
    p_init.set_defaults(func=init_repo)
    
    
    
    return parser

def main() -> None:
    args = build_parser().parse_args()
    args.func(args)
