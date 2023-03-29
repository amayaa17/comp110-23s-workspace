"""EX07 - Dictionary Functions."""

__author__ = "730311817"


def invert(jisho: dict[str, str]) -> dict[str, str]:
    "Inverts the keys and values of given dictionary."
    counter_of_keys: dict[str, int] = {}
    inverted_dictionary: dict = {}
    for tango in jisho:
        if jisho[tango] in counter_of_keys:
            counter_of_keys[jisho[tango]] += 1
        else:
            inverted_dictionary[jisho[tango]] = tango
            counter_of_keys[jisho[tango]] = 1

    for keys in counter_of_keys:
        if counter_of_keys[keys] > 1:
            raise KeyError("Keys in the new inverted dictionary must be unique! Make sure all of your values in the original dictionary are unique and ready for inversion!")
    return inverted_dictionary


def favorite_color(iro: dict[str, str]) -> str:
    """Returns the most popular color."""
    suki_iro: dict[str, int] = {}
    ichiban_suki_iro: str = ""
    for name in iro:
        if iro[name] in suki_iro:
            suki_iro[iro[name]] += 1
        else:
            suki_iro[iro[name]] = 1
    
    current_high = 0
    for color in suki_iro:
        if suki_iro[color] > current_high:
            current_high = suki_iro[color]

    for color in suki_iro:
        if suki_iro[color] == current_high:
            ichiban_suki_iro += color

    return ichiban_suki_iro


def count(tango: list[str]) -> dict[str, int]:
    """Counts the number of times each value appears in the given list."""
    occurences: dict[str, int] = {}
    for word in tango:
        if word not in occurences:
            occurences[word] = 1
        else:
            occurences[word] += 1
    
    return occurences
