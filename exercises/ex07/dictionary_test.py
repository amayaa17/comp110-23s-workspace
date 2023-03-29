"""EX07 - Dictionary Functions Tests."""

__author__ = "730311817"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_empty_dict() -> None:
    """Tests that when given an empty dictionary, it returns an empty dictionary."""
    assert invert({}) == {}


def test_correct_invert_multiple_items() -> None:
    """Tests to insure that the given dictionary with multiple keys is in fact inverted completely."""
    dictionary_a: dict[str, str] = {'COMP': '110', 'MCRO': '251', 'ARMY': '102', 'BIOL': '291', 'ASTR': '103'}
    dictionary_b: dict[str, str] = {'110': 'COMP', '251': 'MCRO', '102': 'ARMY', '291': 'BIOL', '103': 'ASTR'}
    assert invert(dictionary_a) == dictionary_b


def test_correct_invert_one_item() -> None:
    """Tests to insure that when given only one key in a dictionary, it inverts it correctly."""
    dictionary_a: dict[str, str] = {'first_name': 'last_name'}
    assert invert(dictionary_a) == {'last_name': 'first_name'}


def test_empty() -> None:
    """Tests that when given an empty dictionary, it returns an empty string."""
    assert favorite_color({}) == ""


def test_most_common() -> None:
    """Tests that the function is giving the most common favorite color."""
    dictionary_a: dict[str, str] = {'john': 'blue', 'sammy': 'red', 'steve': 'yellow', 'martin': 'red'}
    assert favorite_color(dictionary_a) == 'red'


def test_tie() -> None:
    """Tests that when there is a tie for most common color, the color that was first is returned."""
    dictionary_a: dict[str, str] = {'john': 'blue', 'sammy': 'blue', 'steve': 'red', 'martin': 'red'}
    assert favorite_color(dictionary_a) == 'blue'


def test_empty_string() -> None:
    """Tests that when given an empty string, function returns an empty dictionary."""
    assert count([]) == {}


def test_homogenous_occurences() -> None:
    """Tests that when given a string of the same value, the occurences equal the length of the list."""
    list_a: list[str] = ["chocolate", "chocolate", "chocolate", "chocolate", "chocolate", "chocolate"]
    assert count(list_a) == {"chocolate": 6}


def test_multiple_occurences() -> None:
    """Tests that when given a string with different values, it counts the occurences correctly."""
    list_a: list[str] = ["chocolate", "vanilla", "strawberry", "vanilla", "strawberry", "mint", "chocolate", "strawberry", "vanilla", "vanilla"]
    assert count(list_a) == {"chocolate": 2, "vanilla": 4, "strawberry": 3, "mint": 1}