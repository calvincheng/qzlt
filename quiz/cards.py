from utils import style
import sets


def add(set_title):
    """Prompts user to add cards to set"""
    s = sets.load(set_title)
    while True:
        print(style("Adding new card (press ctrl+c to exit)", color="header"))
        term = input(style("Term: ", color="bold"))
        definition = input(style("Definition: ", color="bold"))
        new_card = Card(term, definition)
        s.add(new_card)
        sets.save(s)
        print(style("Card added", color="green"))
        print()


def delete(set_title, idx):
    """Deletes card `idx` from a set"""
    s = sets.load(set_title)
    if idx < len(s):
        s.delete(idx)
        sets.save(s)
        print(f"Deleted card {idx}")
    else:
        reason = None
        if idx < 0:
            reason = "cannot be less than 0"
        elif idx >= len(s):
            reason = "greater than set size"
        print(style(f"Invalid index: {idx} ({reason})", color="fail"))


class Card:
    def __init__(self, term, definition):
        self._term = term
        self._definition = definition

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, new_term):
        self._term = new_term

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, new_definition):
        self._definition = new_definition
