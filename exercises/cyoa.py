"""EX06 - Choose Your Own Adventure."""

__author__ = "730311817"

from random import randint

points: int = 0
hearts: int = 3
player: str
key_lw: bool = False
key_ttm: bool = False
key_lh: bool = False

MASTER_SWORD: str = "\U0001F5E1"
HEART: str = "\U00002764"
KEY: str = "\U0001F5DD"
CHOICES: str = "\U000025AB"
OCTOROK: str = "\U0001F419"
BOKOBLIN: str = "\U0001F479"
KEESE: str = "\U0001F987"
PRINCESS: str = "\U0001F478"


def main() -> None:
    """Entry point of the program."""
    global player
    global hearts
    global points
    greet()


def greet() -> None:
    """Greets the player, asks for their name, and describes the game."""
    global player
    welcome_message: str = "Welcome to The Legend of Zelda: Python Adventure!"
    print(welcome_message)
    print("\n")
    print(f"In order to save Princess Zelda {PRINCESS}, you must venture through Hyrule and collect all three keys {KEY} to the castle.")
    player = input("What is your name? ")
    print(f"\n{player}. It's dangerous to go alone! Take this. {MASTER_SWORD}\n")
    move_on: str = input("Are you ready to journey through Hyrule? Type 'yes' or 'no': ")
    if move_on == "yes":
        main_fork()
    if move_on == "no":
        print(f"{player}, please return when you are ready.")
    


def main_fork() -> None:
    """Makes the player choose between places in the game."""
    global player
    global hearts
    global points
    global turns
    global key_lw
    global key_ttm
    global key_lh
    print("----------------------------------\n")
    while points < 3 and hearts > 0:
        print("----------------------------------\n")
        if points != 1:
            print(f"{player}, you have currently have {points} keys.")
        else:
            print(f"{player}, you have currently have {points} key.")
        if hearts == 3:
            print(f"This is your current health: {HEART}{HEART}{HEART}")
        elif hearts == 2:
            print(f"This is your current health: {HEART}{HEART}")
        elif hearts == 1:
            print(f"This is your current health: {HEART}")
        print("\n")
        print(f"{CHOICES} Lost Woods\n{CHOICES} Tal Tal Mountains\n{CHOICES} Lake Hylia\n{CHOICES} Hyrule Castle")
        place: str = input("Which part of Hyrule would you like to explore? ")
        while place != "Lost Woods" and place != "Tal Tal Mountains" and place != "Lake Hylia" and place != "Hyrule Castle":
            place = input("Sorry, that's not an option. Try again: ")
        if place == "Lost Woods":
            lost_woods()
        if place == "Tal Tal Mountains":
            tal_tal_mountains()
        if place == "Lake Hylia":
            lake_hylia(points)
        if place == "Hyrule Castle":
            hyrule_castle()
    hyrule_castle()
    


def lost_woods() -> None:
    """The Lost Woods location."""
    global player
    global hearts
    global points
    global key_lw
    print("----------------------------------\n")
    if key_lw == True:
        print(f"{player}, you already have the key from the Lost Woods. Please visit another destination.")
    else:
        print(f"{player}, you are now in the Lost Woods. A bokoblin {BOKOBLIN} approaches you.")
        print("\n")
        decision: str = input(f"Do you 'a' - dodge its attack or 'b' - charge at it? ")
        while decision != 'a' and decision != 'b':
            decision = input("Sorry, that's not an option. Try again: ")
        if decision == 'a':
            print(f"Great move {player}! You dodged the attack of the bokoblin {BOKOBLIN}, but got lost in the woods after running away.")
            continued: str = input("Do you continue left or right? ")
            while continued != "left" and continued != "right":
                continued = input("Sorry, that's not an option. Try again: ")
            if continued == "left":
                print(f"You approach a chest with a key inside of it! {KEY}\nYou pick up the key and move forward in your journey.")
                key_lw = True
                points += 1
            elif continued == "right":
                print(f"{player}, you get even more lost. The mysterious forest brings you back to the beginning, where the bokoblin {BOKOBLIN} awaits you.\nIt strikes you immediately.")
                hearts -= 1
        if decision == 'b':
            print("\n")
            print(f"You manage to defeat the bokoblin {BOKOBLIN}, but he doesn't go down without a fight. You have lost some health.")
            print(f"As you continue your travels through the Lost Woods, you come across a chest with a key {KEY} in it.")
            key_lw = True
            points += 1
            hearts -= 1


def tal_tal_mountains() -> None:
    """The Tal Tal Mountain location."""
    global player
    global hearts
    global points
    global key_ttm
    print("----------------------------------\n")
    if key_ttm == True:
        print(f"{player}, you already have the key from the Tal Tal Mountains. Please visit another destination.")
    else:
        choice: str = input(f"{player}, you are now in the Tal Tal Mountains. You have an option of a - entering the cave, or b - continuing towards the summit.\nPlease input 'a' or 'b': ")
        while choice == 'a':
            print(f"You enter the cave, and are suprised by a keese! {KEESE}\nYou can attack either 3 or 4 times.")
            attack: int = input("How many times do you attack? ")
            if attack == randint(3, 4):
                print(f"You defeat the keese {KEESE} without damage and move along.")
                print("\nThough, you don't find anything in the cave and decide to climb the summit.")
                choice = 'b'
            else:
                print(f"The keese {KEESE} dodges your attacks and charges at you.")
                print(f"\nAfter eventually getting back at the keese {KEESE}, you don't find anything in the cave and decide to climb the summit.")
                hearts -= 1
                choice = 'b'
                
        if choice == 'b':
            print("You find your way to the summit of Tal Tal Mountain and come across a pot.")
            breaking: str = input("Do you chose to smash the pot? Type 'yes' or 'no': ")
            if breaking == 'yes':
                print(f"Congratulations {player}! Upon breaking the pot, you found the key! {KEY}")
                points += 1
                key_ttm = True
            else:
                print("You climb back down the mountain, with no key. Maybe you can come back and break the pot another time.")


def lake_hylia(keys: int) -> int:
    """Lake Hylia location."""
    global player
    global hearts
    global points
    global key_lh
    print("----------------------------------\n")
    if key_lh == True:
         print(f"{player}, you already have the key from Lake Hylia. Please visit another destination.")
    else:
        print(f"{player}, welcome to Lake Hylia. As you approach the lake, you should see a shiny object propped up on the bottom, but the lake is infested with octorok {OCTOROK}.\n")
        choice: str = input("Do you a - cannonball into the lake or b - swiftly dive into the lake: ")
        while choice == "a":
            print(f"Doing a cannonball into the lake was a mistake. You are attacked by octorok {OCTOROK}.\n")
            print("You make it back to shore and decide to dive in the water instead.")
            choice = "b"
            hearts -= 1
        if choice == "b":
            if keys == 0:
                print(f"\n{player}, you currently have 0 keys, making it much harder to sink down to the bottom of the lake and grab the key. Return once you have more keys.")
                return points
            if keys == 1:
                print(f"{player}, you currently have 1 key, and start sinking slowly to the bottom of the lake when an octorok {OCTOROK} begins attacking.\nYou lose health and quickly swim back to surface without the key.")
                print(f"Maybe it would be better to return when you have both of the other keys.")
                hearts -= 1
                return points
            if keys == 2:
                print(f"You dive down to the lake with ease, and grab the key! {KEY}")
                points += 1
                key_lh = True
                return points

def hyrule_castle() -> None:
    """The end of the game, arrival at the castle."""
    global player
    global hearts
    global points
    print("----------------------------------\n")
    print(f"{player}, you have made it to Hyrule Castle with {points} keys.")
    if points < 3 and hearts > 0:
        print(f"At this time, you do not have enough keys to save Princess Zelda {PRINCESS}. Go back and find all of the keys.")
    if hearts == 0:
        print("THE END. You have no health left, please try this adventure again.")
    if points == 3 and hearts > 0:
        print(f"Congratulations on saving Princess Zelda! {PRINCESS}")
        if {hearts} == 1:
            print(f"Your final health: {HEART}")
        if {hearts} == 2:
            print(f"Your final health: {HEART}{HEART}")
        if {hearts} == 3:
            print(f"Your final health: {HEART}{HEART}{HEART}\nCongrats! You saved Princess Zelda {PRINCESS} with full health!")
    options: str = input("Type 'restart' to restart the game, or 'stop' to stop playing: ")
    if options == "restart":
        main()
    else: 
        if options == "stop":
            print(f"Thanks for playing Legend of Zelda: Python Adventure!")

if __name__ == "__main__":
    main()