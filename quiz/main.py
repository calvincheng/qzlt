import typer
import sets
from sessions import Session

app = typer.Typer()

sets_app = typer.Typer()
app.add_typer(sets_app, name="sets")

set_app = typer.Typer()
app.add_typer(set_app, name="set")

@app.command()
def study(set_title: str, study_mode: str = "write"):
    deck = sets.load(set_title)
    session = Session(deck)
    if study_mode == "write":
        session.write()
    elif study_mode == "learn":
        session.learn()

@sets_app.command("create")
def sets_create():
    sets.create() 

@sets_app.command("list")
def sets_list():
    sets.list() 

@set_app.command("add")
def set_add(set_title: str):
    sets.add(set_title)

if __name__ == "__main__":
    app()
