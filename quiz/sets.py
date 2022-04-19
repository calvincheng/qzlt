import os
import json
from cards import Card
from utils import style

""" Where all quiz files are stored """
BASE_PATH = "quizlet"


def create():
    """Prompts user to create a new set"""
    title = input(style("Title: ", color="bold"))
    description = input(style("Description (optional): ", color="bold"))
    new_set = Set(title, description)
    save(new_set)
    print(style("Set successfully created", color="green"))


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
    if os.path.exists(f"{BASE_PATH}/{title}"):
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
    else:
        raise FileNotFoundError(f"Set `{title}`not found")


def list():
    """Lists all cards saved in disk"""
    size = os.get_terminal_size()
    terminal_width = min(size.columns, 120)

    title_width = terminal_width // 4
    description_width = terminal_width // 4 * 3

    print(f"{'TITLE': <{title_width}}{'DESCRIPTION': <{description_width}}")

    for title in os.listdir(f"{BASE_PATH}"):
        with open(f"{BASE_PATH}/{title}/info.json", "r") as info_file:
            info = json.load(info_file)
            title, description = info["title"], info["description"]
            title_str = f"{title: <{title_width}}"
            description_str = f"{description: <{description_width}}"
            print(f"{title_str}{description_str}")


def add(name):
    """Prompts user to add cards to set"""
    s = load(name)
    try:
        while True:
            print(style("Adding new card (press ctrl+c to exit)", color="header"))
            term = input(style("Term: ", color="bold"))
            definition = input(style("Definition: ", color="bold"))
            new_card = Card(term, definition)
            s.add(new_card)
            save(s)
            print(style("Card added", color="green"))
            print()
    except KeyboardInterrupt:
        print(style("\n\nEXITED", color="bold"))
        pass


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

    def list(self):
        size = os.get_terminal_size()
        terminal_width = min(size.columns, 120)

        term_width = terminal_width // 4
        definition_width = terminal_width // 4 * 3

        print(f"{'TERM': <{term_width}}{'DEFINITION': <{definition_width}}")
        for card in self._cards:
            term, definition = card.term, card.definition
            term_str = f"{term: <{term_width}}"
            definition_str = f"{definition: <{definition_width}}"
            print(f"{term_str}{definition_str}")
