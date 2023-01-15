import argparse

from src.operation import initialize

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers(help="sub-commands")
    subparsers.required = True
    subparsers.dest = "SUB_COMMAND"

    # initialize tables
    # to execute: python3 main.py initialize
    parser_initialize = subparsers.add_parser("initialize", help="initialize tables")
    parser_initialize.set_defaults(func=initialize)

    # update tables
    # to execute: python3 main.py update
    # parser_update = subparsers.add_parser("update", help="update tables")
    # parser_update.set_defaults(func=update)

    args = parser.parse_args()
    args.func(args)
