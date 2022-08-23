import argparse

from src.initialize import initialize

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers(help="sub-commands")
    subparsers.required = True
    subparsers.dest = "SUB_COMMAND"

    # initialize players, teams tables
    # python3 main.py initialize
    parser_initialize = subparsers.add_parser("initialize", help="initialize tables")
    parser_initialize.set_defaults(func=initialize)

    # initialize stats table
    # parser_initialize_stats = subparsers.add_parser("init-stats", help="initialize stats tables")
    # parser_initialize_stats.set_defaults(func=initialize_stats)

    args = parser.parse_args()
    args.func(args)
