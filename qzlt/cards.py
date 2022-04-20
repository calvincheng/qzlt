import typer
from qzlt import sets


def add(set_title):
    """Prompts user to add cards to set"""
    s = sets.load(set_title)
    while True:
        typer.secho("Adding new card (press ctrl+c to exit)", fg="magenta")
        term = typer.prompt(typer.style("Term", fg="bright_black"))
        definition = typer.prompt(typer.style("Definition", fg="bright_black"))
        new_card = Card(term, definition)
        s.add(new_card)
        sets.save(s)
        typer.secho("Card added", fg="green")
        typer.echo()


def delete(set_title, idx):
    """Deletes card `idx` from a set"""
    s = sets.load(set_title)
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
