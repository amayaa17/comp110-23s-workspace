"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730311817"


word: str = input("Enter a 5-character word: ")
if (len(word) != int(5)):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if (len(character) != int(1)):
    print("Error: Character must be a single character")
    exit()

print("Searching for " + character + " in " + word)


instances: int = 0

if (word[0] == character):
    print(character + " found at index 0")
    instances += 1

if (word[1] == character):
    print(character + " found at index 1")
    instances += 1

if (word[2] == character):
    print(character + " found at index 2")
    instances += 1

if (word[3] == character):
    print(character + " found at index 3")
    instances += 1

if (word[4] == character):
    print(character + " found at index 4")
    instances += 1


if (instances == 0):

    print("No instances of " + character + " found in " + word)

if (instances == 1):

    print("1 instance of " + character + " found in " + word)

if (instances > 1):

    print(str(instances) + " instances of " + character + " found in " + word)