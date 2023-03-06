"""Defining functions to test with unit tests."""

__author__ = "730311817"


def only_evens(numbers: list[int]) -> list[int]:
    """Given a list of integers, returns only the even numebrs of that list."""
    even_list: list[int] = []
    for digit in numbers:
        if digit % 2 == 0:
            even_list.append(digit)

    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists of integers, concatenates both of the lists together."""
    concatenation: list[int] = []
    concatenation += list1
    concatenation += list2

    return concatenation


def sub(list_of_ints: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list of integers, returns the integers within the given indicies."""
    returned_list: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(list_of_ints):
        end_index = len(list_of_ints)
    for number in range(start_index, end_index):
        returned_list.append(list_of_ints[number])
    
    return returned_list