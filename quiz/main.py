import argparse
import sets
from sessions import Session

parser = argparse.ArgumentParser(description="Quizlet CLI")
subparsers = parser.add_subparsers(dest="command", help="Commands")

study_parser = subparsers.add_parser("study")
study_parser.add_argument("set_name", type=str)

sets_parser = subparsers.add_parser("sets")
sets_parser.add_argument("subcommand", type=str, choices=["create", "list"])

set_parser = subparsers.add_parser("add")
set_parser.add_argument("set_name", type=str)

args = parser.parse_args()


if args.command == "study":
    deck = sets.load(args.set_name)
    session = Session(deck)
    session.write()
elif args.command == "sets":
    if args.subcommand == "create":
        sets.create() 
    elif args.subcommand == "list":
        sets.list()
elif args.command == "add":
    sets.add(args.set_name)
else:
    parser.print_help()
