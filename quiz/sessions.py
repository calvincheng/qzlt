from utils import style, sample, bcolors
import random


class Session:
    def __init__(self, deck, mode="study"):
        self._deck = deck
        self._mode = mode

    def write(self):
        for i, card in enumerate(self._deck.cards):
            print(style(f"Card {i+1}/{len(self._deck)}", color="header"))
            print(card.term)
            answer = input(style("Answer: ", color="bold"))
            if answer == card.definition:
                print(style("Correct!", color="green"))
            else:
                print(style("Incorrect", color="fail"))
            print()

    def learn(self):
        for i, card in enumerate(self._deck.cards):
            print(style(f"Card {i+1}/{len(self._deck)}", color="header"))
            print(style(card.term, color="bold"))

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
                print(f"{i + 1}. {choice}")

            answer = input(f"{bcolors.BOLD}Select the correct term: {bcolors.ENDC}")
            if choices[int(answer) - 1] == card.definition:
                print(f"{bcolors.OKGREEN}Correct!{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Incorrect{bcolors.ENDC}")
            print()
