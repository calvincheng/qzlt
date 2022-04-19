import argparse
import sets
from sessions import Session

parser = argparse.ArgumentParser(description="Quizlet CLI")
subparsers = parser.add_subparsers(dest="command", help="Commands")

study_parser = subparsers.add_parser("study")
args = parser.parse_args()

if args.command == "study":
    deck = sets.load("demo")
    session = Session(deck)
    session.write()
else:
    parser.print_help()
