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
