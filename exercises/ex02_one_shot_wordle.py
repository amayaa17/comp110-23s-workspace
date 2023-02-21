"""EX02 - One Shot Wordle - Another step towards Wordle."""

__author__ = "730311817"

SECRET_WORD: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word_length = len(SECRET_WORD)

index = 0
wordle_boxes: str = ""

guess: str = input(f"What is your {word_length}-letter guess? ")

while len(guess) != word_length:
    guess = input(f"That was not {word_length} letters! Try again: ")
# Allows player to continue guessing until the guess is of the same length as SECRET_WORD

while index < word_length:
    if guess[index] == SECRET_WORD[index]:
        wordle_boxes = (wordle_boxes + GREEN_BOX)
        index += 1
    # Concatenates green box to wordle_boxes if the character at guess[index] is equal to the character at SECRET_WORD[index]
    else:
        alt_index = 0
        exist: bool = False
        # Sets variables for the while loop checking each character of the SECRET_WORD to see if it equals character at guess[index]
        while not exist and alt_index < word_length:
            if SECRET_WORD[alt_index] == guess[index]:
                exist = True
            else:
                alt_index += 1
            # Checks to see if the character at the specified index of the guessed word is equal at any index in the secret word

        if exist is True:
            wordle_boxes = (wordle_boxes + YELLOW_BOX)
            index += 1
            # If character at guess[index] is located at another loaction of SECRET_WORD, a yellow box is concatenated
        else:
            wordle_boxes = (wordle_boxes + WHITE_BOX)
            index += 1
            # If character at guess[index] is not located anywhere else in SECRET_WORD, a white box is concatenated

print(wordle_boxes)

if len(guess) == word_length:
    # The given messages after guessing either correct, or incorrectly (with the same number of characters)
    if guess == SECRET_WORD:
        print("Woo! You got it!")

    else:
        print("Not quite. Play again soon!")