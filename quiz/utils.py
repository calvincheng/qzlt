import random
from typing import List, Any


def sample(n: int, array: List[Any]) -> List[Any]:
    array_ = [*array]
    random.shuffle(array_)
    return [*array_[0:n]]
