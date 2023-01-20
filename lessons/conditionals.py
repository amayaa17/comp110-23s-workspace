"""Conditionals lesson"""

result: str = input("Did UNC win the natty? ")

if (result == "Yes"):
    print("Hell yeah!")
    print("Go Heels! Rush Franklin!!")

else:
    if (result != "No"):
        print("Was it a tie?")
    else:
        print("Dang what a shame...")
        print("You should stay at home and cry.")