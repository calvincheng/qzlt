import typer
from qzlt import sets
from qzlt import cards
from qzlt.sessions import Session

app = typer.Typer()

sets_app = typer.Typer()
app.add_typer(sets_app, name="sets")

set_app = typer.Typer()
app.add_typer(set_app, name="set")


@app.command()
def study(set_title: str, study_mode: str = "write", shuffle: bool = False):
    """
    Begin a study session

    :param set_title: Title of set
    :param study_mode: Study mode (default: "write")
    :param shuffle: Shuffles cards in set if True (default: False)
    """
    deck = sets.load(set_title)
    if deck is None:
        typer.secho(f"Could not find deck titled `{set_title}`", fg="red")
        return

    session = Session(deck, shuffle)
    if study_mode == "write":
        session.write()
    elif study_mode == "learn":
        session.learn()


@sets_app.callback(invoke_without_command=True)
def sets_default(ctx: typer.Context):
    """
    List all sets as the default action for `sets` command
    """
    if ctx.invoked_subcommand is None:
        sets.list()


@sets_app.command("list")
def sets_list():
    sets.list()


@sets_app.command("create")
def sets_create():
    sets.create()


@set_app.command("add")
def set_add(set_title: str):
    cards.add(set_title)


@set_app.command("delete")
def set_delete(set_title: str, card_id: int):
    cards.delete(set_title, card_id)


@set_app.command("list")
def set_list(set_title: str):
    deck = sets.load(set_title)
    if deck is None:
        typer.secho(f"Could not find deck titled `{set_title}`", fg="red")
        return
    deck.list()


if __name__ == "__main__":
    app()
