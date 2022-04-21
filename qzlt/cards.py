import typer
from qzlt import sets


def add(set_title):
    """Prompts user to add cards to set"""
    s = sets.load(set_title)
    if s is None:
        typer.secho(f"Could not find deck titled `{set_title}`", fg="red")
        return

    while True:
        typer.secho("Adding new card (press ctrl+c to exit)", fg="magenta")
        term = typer.prompt(typer.style("Term", fg="bright_black")).strip()
        definition = typer.prompt(typer.style("Definition", fg="bright_black")).strip()
        new_card = Card(term, definition)
        s.add(new_card)
        sets.save(s)
        typer.secho("Card added", fg="green")
        typer.echo()


def delete(set_title, idx):
    """Deletes card `idx` from a set"""
    s = sets.load(set_title)
    if s is None:
        typer.secho(f"Could not find set `{set_title}`", fg="red")
        return

    if idx < len(s):
        s.delete(idx)
        sets.save(s)
        typer.echo(f"Deleted card {idx}")
    else:
        reason = None
        if idx < 0:
            reason = "cannot be less than 0"
        elif idx >= len(s):
            reason = "greater than set size"
        typer.secho(f"Invalid index: {idx} ({reason})", fg="red", err=True)


class Card:
    """
    Contains a term and definition.
    """

    def __init__(self, term, definition):
        """
        Constructs a new Card

        :param term: The term to learn (e.g. mitochondria)
        :param definition: The term's definition (e.g. powerhouse of the cell)
        """
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
