"""Example function for unit tests."""

def sum_old(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    index: int = 0
    while index <= len(xs) - 1:
        sum_total += xs[index]
        index += 1
    return sum_total

def sum_old2(xs: list[float]) -> float:
    """Returns sum of all elements in xs."""
    sum_total: float = 0.0
    for items in xs:
        sum_total += items
    return sum_total

def sum(xs: list[float]) -> float:
    """Returns sum of all elements in xs."""
    sum_total: float = 0.0
    for numbers in range(0, len(xs)):
        sum_total += xs[numbers]
    return sum_total