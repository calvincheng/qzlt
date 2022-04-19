import argparse
import sets
from sessions import Session

parser = argparse.ArgumentParser(description="Quizlet CLI")
subparsers = parser.add_subparsers(dest="command", help="Commands")

study_parser = subparsers.add_parser("study")
sets_parser = subparsers.add_parser("sets")
sets_parser.add_argument("subcommand", type=str, choices=["create", "list"])

args = parser.parse_args()


if args.command == "study":
    deck = sets.load("demo")
    session = Session(deck)
    session.write()
elif args.command == "sets":
    if args.subcommand == "create":
        sets.create() 
    elif args.subcommand == "list":
        sets.list()
else:
    parser.print_help()
