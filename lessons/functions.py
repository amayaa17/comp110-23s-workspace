"""Defining functions"""

def mimic(my_words: str) -> str:
    """Given the str m_words, outputs the same string"""
    return my_words

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
   
    if letter_idx >= len(my_words):
        return ("Index too high")
    #If we made it here, that means the letter_idx is valid
    return my_words[letter_idx]
