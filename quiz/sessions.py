from utils import sample
import random
import typer


class Session:
    def __init__(self, deck, shuffle=False):
        self._deck = deck
        if shuffle:
            random.shuffle(self._deck.cards)

    def write(self):
        for i, card in enumerate(self._deck.cards):
            typer.secho(f"Card {i+1}/{len(self._deck)}", fg="magenta")
            typer.secho(card.term, fg="bright_white", bold=True)
            answer = typer.prompt(typer.style("Answer", fg="bright_black"))
            if answer == card.definition:
                typer.secho("Correct!", fg="green")
            else:
                typer.secho(f"Incorrect", fg="red")
                typer.secho(
                    f"The correct answer was '{card.definition}'", fg="bright_black"
                )
            typer.echo()

    def learn(self):
        for i, card in enumerate(self._deck.cards):
            typer.secho(f"Card {i+1}/{len(self._deck)}", fg="magenta")
            typer.secho(card.term, fg="bright_white", bold=True)

            num_choices = 4
            choices = list(
                map(lambda x: x.definition, sample(num_choices - 1, self._deck.cards))
            )
            while card.definition in choices:
                choices = list(
                    map(
                        lambda x: x.definition,
                        sample(num_choices - 1, self._deck.cards),
                    )
                )
            choices.append(card.definition)
            random.shuffle(choices)

            for i, choice in enumerate(choices):
                typer.echo(f"{i + 1}. {choice}")

            answer = typer.prompt(typer.style("Select the correct term", bold=True))
            if choices[int(answer) - 1] == card.definition:
                typer.secho("Correct!", fg="green")
            else:
                typer.secho("Incorrect", fg="red")
                typer.secho(
                    f"The correct answer was '{card.definition}'", fg="bright_black"
                )
            typer.echo()
