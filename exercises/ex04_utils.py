"""EX04 - List Utilities."""

__author__ = "730311817"


def all(list: list[int], number: int) -> bool:
    """Tests to see if all integers in the list match number."""
    if len(list) == 0:
        return False
    
    index = 0
    while index < len(list):
        if int(number) == int(list[index]):
            index += 1
        else:
            return False
    
    return True


def max(input: list[int]) -> int:
    """Gives the max number in a given list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    index = 0
    current_high_number = input[0]
    while index < len(input):
        if input[index] >= current_high_number:
            current_high_number = input[index]
            index += 1
        else:
            index += 1
    
    return current_high_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if the two given lists are equal at each index, regardless of length of either."""
    if len(list1) == 0 or len(list2) == 0:
        return False
    index = 0
    if len(list1) >= len(list2):
        while index < len(list1) and index < len(list2):
            if list1[index] == list2[index]:
                index += 1
            else:
                return False
        return True