import random
from typing import List, Any


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def style(text, color = None):
    """ Style text for terminal output """

    if color == "header":
        return f"{bcolors.HEADER}{text}{bcolors.ENDC}"
    elif color == "fail":
        return f"{bcolors.FAIL}{text}{bcolors.ENDC}"
    elif color == "green":
        return f"{bcolors.OKGREEN}{text}{bcolors.ENDC}"
    elif color == "bold":
        return f"{bcolors.BOLD}{text}{bcolors.ENDC}"
    elif color == "warning":
        return f"{bcolors.WARNING}{text}{bcolors.ENDC}"
    else:
        return text


def sample(n: int, array: List[Any]) -> List[Any]:
    array_ = [*array]
    random.shuffle(array_)
    return [*array_[0:n]]


