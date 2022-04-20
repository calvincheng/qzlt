import typer
import sets
import cards
from sessions import Session

app = typer.Typer()

sets_app = typer.Typer()
app.add_typer(sets_app, name="sets")

set_app = typer.Typer()
app.add_typer(set_app, name="set")


@app.command()
def study(
    set_title: str = typer.Option(None, prompt=typer.style("Set title", bold=True)),
    mode: str = "write",
    shuffle: bool = False,
):
    deck = sets.load(set_title)
    session = Session(deck, shuffle)
    if mode == "write":
        session.write()
    elif mode == "learn":
        session.learn()


@sets_app.callback(invoke_without_command=True)
def sets_default(ctx: typer.Context):
    if ctx.invoked_subcommand is not None:
        return
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
    deck.list()


if __name__ == "__main__":
    app()
