import os
import json
from cards import Card

""" Where all quiz files are stored """
BASE_PATH = "quizlet"

def load(path):
    """
    Creates a Set from a filepath
    """
    if os.path.exists(path):
        title, description = None, None
        cards = []

        # Populate title and description
        with open(f"{path}/info.json") as info_file:
            info = json.load(info_file)
            title = info["title"]
            description = info["description"]

        # Populate cards
        with open(f"{path}/terms.txt", "r") as file:
            lines = file.read().splitlines()
            for i in range(len(lines) // 2):
                term, definition = lines[2 * i], lines[2 * i + 1]
                card = Card(term, definition)
                cards.append(card)

        return Set(title, description, cards)
    else:
        raise FileNotFoundError("Set not found")


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
