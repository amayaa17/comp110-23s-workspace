"""EX04 - List Utilities"""

__author__ = "730311817"

def all(list: list[int], number: int) -> bool:
    """Tests to see if all integers in the list match number"""
    index = 0
    while index < len(list):
        if int(number) is int(list[index]):
            index += 1
        else:
            return False
    
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    index = 0
    current_high_number = 0
    while index < len(input):
        if input[index] >= current_high_number:
            current_high_number = input[index]
            index += 1
        else:
            index += 1
    
    return current_high_number

def is_equal(List1: list[int], List2: list[int]) -> bool:
    """Checks if the two given lists are equal at each index"""
    index = 0
    while index < len(List1) and index < len(List2):
        if List1[index] == List2[index]:
            index += 1
        else:
            return False
    
    return True