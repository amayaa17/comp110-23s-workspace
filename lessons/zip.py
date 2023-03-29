"""Challenge question 4."""

def zip(a_list: list[str], b_list: list[int]) -> dict[str, int]:
    """Produces a dictionary where the keys are the strings of the first list, and the values are the integers of the second list."""
    zipped: dict[str, int] = {}
    index = 0
    if len(a_list) != len(b_list):
        return zipped
    else:
        while index < len(a_list) and index < len(b_list):
            zipped[a_list[index]] = b_list[index]
            index += 1
    return zipped