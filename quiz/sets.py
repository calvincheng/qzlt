import os
import json
from cards import Card
from utils import style

""" Where all quiz files are stored """
BASE_PATH = "quizlet"

def create():
    """ Prompts user to create a new set """
    title = input(style("Title: ", color="bold"))
    description = input(style("Description (optional): ", color="bold"))
    new_set = Set(title, description)
    save(new_set)
    print(style("Set successfully created", color="green"))

def save(s):
    SET_PATH = f"{BASE_PATH}/{s.title}"
    os.makedirs(SET_PATH)
    with open(f"{SET_PATH}/info.json", "w") as info_file:
        info = { "title": s.title, "description": s.description }
        info = json.dump(info, info_file)
    with open(f"{SET_PATH}/terms.txt", "w") as terms_file:
        for card in s:
            terms_file.writelines(f"{card.term}\n")
            terms_file.writelines(f"{card.definition}\n")

def load(title):
    """ Loads an exisiting set """
    if os.path.exists(f"{BASE_PATH}/{title}"):
        title, description = None, None
        cards = []

        # Populate title and description
        with open(f"{BASE_PATH}/{title}/info.json", "r") as info_file:
            info = json.load(info_file)
            title = info["title"]
            description = info["description"]

        # Populate cards
        with open(f"{BASE_PATH}/{title}/terms.txt", "r") as file:
            lines = file.read().splitlines()
            for i in range(len(lines) // 2):
                term, definition = lines[2 * i], lines[2 * i + 1]
                card = Card(term, definition)
                cards.append(card)

        return Set(title, description, cards)
    else:
        raise FileNotFoundError(f"Set `{title}`not found")


def list():
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


class Set:
    def __init__(self, title, description, cards = []):
        self._title = title
        self._description = description
        self._cards = cards

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, n):
        return self._cards[n]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self):
            result = self._cards[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

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
