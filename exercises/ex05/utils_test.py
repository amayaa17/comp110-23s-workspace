"""Creating a unit test to test defined functions."""

__author__ = "730311817"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub

"""Tests for only_evens function."""
def test_empty_list() -> None:
    assert only_evens([]) == []

def test_evens_returned() -> None:
    given_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(given_list) == [2, 4, 6, 8, 10]

def test_with_negatives() -> None:
    given_list: list[int] = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert only_evens(given_list) == [-4, -2, 0, 2, 4]

"""Tests for sub function."""
def test_one_empty() -> None:
    list1: list[int] = [1, 3, 5]
    list2: list[int] = []
    assert concat(list1, list2) == [1, 3, 5]

def test_same() -> None:
    list1: list[int] = [20, 30, 0, 40]
    assert concat(list1, list1) == [20, 30, 0, 40, 20, 30, 0, 40]

def test_invert_with_negatives() -> None:
    list1: list[int] = [-1, -2, -3]
    list2: list[int] = [-3, -2, -1]
    assert concat(list1, list2) == [-1, -2, -3, -3, -2, -1]

"""Tests for sub function."""
def test_empty() -> None:
    assert sub([], 0, 3) == []

def test_negative_start_index() -> None:
    list_of_ints: list[int] = [10, 20, 30, 40, 50]
    assert sub(list_of_ints, -2, 3) == [10, 20, 30]

def test_larger_end_index() -> None:
    list_of_ints: list[int] = [10, 20, 30, 40, 50]
    assert sub(list_of_ints, 3, 7) == [40, 50]