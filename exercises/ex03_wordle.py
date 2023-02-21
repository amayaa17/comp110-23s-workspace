"""EX03 - Structured Wordle - The final step towards Wordle."""

__author__ = "730311817"

def contains_char(correct_word: str, character: str) -> bool:
    """Searches for character within guess."""
    assert len(character) == 1
    index = 0
    exist: bool = False

    while not exist and index < len(correct_word):
        if correct_word[index] == character:
            exist = True
        else:
            index += 1
        # Checks for character at specified index
    if exist:
        return True
    if not exist:
        return False
    # Returns the result of the while loop, ending the function
    
def emojified(guess: str, correct_word: str) -> str:
    """Adds emojis to the corresponding indicies of the guess."""
    assert len(guess) == len(correct_word)
    index = 0
    wordle_boxes: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while index < len(correct_word):
        if guess[index] == correct_word[index]:
            wordle_boxes = (wordle_boxes + GREEN_BOX)
            index += 1
        # Concatenates GREEN_BOX when the character is the same at specified index
        else:
            if contains_char(correct_word, guess[index]):
                wordle_boxes = (wordle_boxes + YELLOW_BOX)
                index += 1
            else:
                wordle_boxes = (wordle_boxes + WHITE_BOX)
                index += 1
            # Uses the contains_char function, which determines whether or not the character is present in the word at all
            # Concatenates YELLOW_BOX if the character is present elsewhere in the guess, and WHITE_BOX if it is not present
    return wordle_boxes
    
def input_guess(character_amount: int) -> str:
    """Prompts the user to give a word of a specific length."""
    guess: str = input(f"Enter a {character_amount} character word: ")

    while len(guess) != character_amount:
        guess = input(f"That wasn't {character_amount} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    correct_word: str = "codes"
    turns: int = 1
    playing: bool = True
    guessed_yet: bool = False
    game_guess: str = ""

    while turns <= 6 and playing:
        print(f"=== Turn {turns}/6 ===")
        if guessed_yet == False:
            game_guess = input_guess(len(correct_word))
            guessed_yet == True
        # Assigns the variable guess with the returned value of input_guess (str), and makes guessed_yet True, so that input_guess is not called again
        print(emojified(game_guess, correct_word))

        if correct_word == game_guess:
            playing = False
            print(f"You won in {turns}/6 turns!")
        # If correct word is guessed, it turns playing False, which makes the while loop false
        turns += 1
        # Adds to the variable turn
        
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == '__main__':
    main()