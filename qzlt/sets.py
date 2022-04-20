import os
import json
import typer
from qzlt.cards import Card

""" Where all quiz files are stored """
BASE_PATH = "sets"


def create():
    """Prompts user to create a new set"""
    title = typer.prompt(typer.style("Title", fg="bright_black"))
    description = typer.prompt(typer.style("Description", fg="bright_black"))
    new_set = Set(title, description)
    save(new_set)
    typer.secho("Set successfully created", fg="green")


def save(s):
    """Save a set to disk"""
    SET_PATH = f"{BASE_PATH}/{s.title}"
    if not os.path.exists(SET_PATH):
        os.makedirs(SET_PATH)
    with open(f"{SET_PATH}/info.json", "w") as info_file:
        info = {"title": s.title, "description": s.description}
        info = json.dump(info, info_file)
    with open(f"{SET_PATH}/terms.txt", "w") as terms_file:
        for card in s:
            terms_file.writelines(f"{card.term}\n")
            terms_file.writelines(f"{card.definition}\n")


def load(title):
    """Loads an exisiting set from disk"""
    if not os.path.exists(f"{BASE_PATH}/{title}"):
        return None

    set_title, set_description = None, None
    cards = []

    # Populate title and description
    with open(f"{BASE_PATH}/{title}/info.json", "r") as info_file:
        info = json.load(info_file)
        set_title = info["title"]
        set_description = info["description"]

    # Populate cards
    with open(f"{BASE_PATH}/{title}/terms.txt", "r") as file:
        lines = file.read().splitlines()
        for i in range(len(lines) // 2):
            term, definition = lines[2 * i], lines[2 * i + 1]
            card = Card(term, definition)
            cards.append(card)

    return Set(set_title, set_description, cards)


def list():
    """Lists all cards saved in disk"""
    size = os.get_terminal_size()
    terminal_width = min(size.columns, 120)

    title_width = terminal_width // 4
    description_width = terminal_width // 4 * 3

    typer.echo(f"{'TITLE': <{title_width}}{'DESCRIPTION': <{description_width}}")

    for title in os.listdir(f"{BASE_PATH}"):
        with open(f"{BASE_PATH}/{title}/info.json", "r") as info_file:
            info = json.load(info_file)
            title, description = info["title"], info["description"]
            title_str = f"{title: <{title_width}}"
            description_str = f"{description: <{description_width}}"
            typer.echo(f"{title_str}{description_str}")


class Set:
    def __init__(self, title, description, cards=[]):
        self._title = title
        self._description = description
        self._cards = cards

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, n):
        return self._cards[n]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, new_cards):
        self._cards = new_cards

    def add(self, card):
        self._cards.append(card)

    def delete(self, idx):
        self._cards.pop(idx)

    def list(self):
        idx_width = 6
        term_width = 32
        definition_width = 32

        title_idx_str = f"{'ID': <{idx_width}}"
        title_term_str = f"{'TERM': <{term_width}}"
        title_definition_str = f"{'DEFINITION': <{definition_width}}"
        typer.echo(f"{title_idx_str}{title_term_str}{title_definition_str}")

        for i, card in enumerate(self._cards):
            term, definition = card.term, card.definition
            idx_str = f"{i: <{idx_width}}"
            term_str = f"{term: <{term_width}}"
            definition_str = f"{definition: <{definition_width}}"
            typer.echo(f"{idx_str}{term_str}{definition_str}")
