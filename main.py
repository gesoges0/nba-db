import argparse

from src.initialize import initialize

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers(help="sub-commands")
    subparsers.required = True
    subparsers.dest = "SUB_COMMAND"

    # initialize tables
    parser_initialize = subparsers.add_parser("initialize", help="initialize tables")
    parser_initialize.set_defaults(func=initialize)

    args = parser.parse_args()
    args.func(args)
