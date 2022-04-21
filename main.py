# Hawthorne Manor Video Game by Bastian Barthel
# Art by ascii.co.uk


# Modules
from art import logo, credits
from data import ROOM, ITEM, VERB


# Functions
def does_include(to_check):
    """Takes a list of commands, returns True if they are all included in the 'user_input' string."""
    for word in to_check:
        if word not in user_input:
            return False
    return True


def check_room(to_check):
    """Takes a string and checks if the player is in that room and returns True."""
    return current_room == to_check


def get_input():
    """Prints the prompt and returns the user input as a string."""
    return input(">").lower()


def get_verbs():
    """Prints a list of verbs that are in the game"""
    print(f"Verbs I know: {VERB}")


def show_items():
    """Prints out all the items the player is carrying."""
    if not inventory:
        print("You don't carry any items.")
    else:
        for item in inventory:
            print(item.replace("_", " "))


def add_item(new_item):
    """Takes an item as a string and adds it to the 'inventory' list."""
    if new_item not in inventory:
        inventory.append(new_item)
        print("You got it.")
    else:
        print("No need to get another.")


def remove_item(item_to_remove):
    """Takes an item as a string and removes it from the 'inventory' list."""
    inventory.remove(item_to_remove)


def change_room(new_room):
    """Takes the new room as an integer and returns it to the variable."""
    if new_room == 9 and "candlelight" not in inventory:
        print(ROOM[new_room]["intro_dark"])
    else:
        print(ROOM[new_room]["intro"])
    return new_room


def examine_room():
    """Examines the current room."""
    if current_room == 9 and "candlelight" not in inventory:
        print(ROOM[current_room]["look_dark"])
    else:
        print(ROOM[current_room]["look"])


def examine_item(item):
    """Takes a string and examines the item."""
    if current_room == 9 and "candlelight" not in inventory:
        print("It is too dark to see anything.")
    else:
        print(ITEM[item])


def get_help():
    """Prints the Help Screen"""
    print("If you see '>' before the prompt, you can enter a command like 'open window' or 'read letter'")
    print("Use commands like 'enter library', 'north' or 'upstairs' to move around the house")
    print("Type 'look around' to inspect your surroundings")
    print("Type 'inventory' or 'items' to check your belongings")
    print("Type 'commands' or 'verbs' to see a list of verbs the computer recognizes")
    print("Type 'help' or '?' for this list")
    print("Type 'exit game' to leave")


# Variables
error = "You can't do that."
user_input = ""
inventory = []
current_room = 0
played_piano = False


# Start
print(logo)


# Game Loop
while user_input != "exit game":
    user_input = get_input()

    # General Game Logic
    if user_input == "help" or user_input == "?":
        get_help()
    elif user_input == "commands" or user_input == "verbs":
        get_verbs()
    elif user_input == "inventory" or user_input == "items":
        show_items()
    elif user_input == "look around" or user_input == "look":
        examine_room()
    elif does_include(["lighter", "candle"]):
        add_item("candlelight")
        remove_item("candle")
    elif does_include(["examine", "candlelight"]) or does_include(["look", "candlelight"]):
        examine_item("candlelight")
    elif does_include(["examine", "lighter"]) or does_include(["look", "lighter"]):
        examine_item("lighter")
    elif does_include(["examine", "regular", "key"]) or does_include(["look", "regular", "key"]):
        examine_item("regular_key")
    elif does_include(["examine", "small", "key"]) or does_include(["look", "small", "key"]):
        examine_item("small_key")
    elif does_include(["examine", "big", "key"]) or does_include(["look", "big", "key"]):
        examine_item("big_key")
    elif does_include(["examine", "candle"]) or does_include(["look", "candle"]):
        examine_item("candle")
    elif does_include(["examine", "ring"]) or does_include(["look", "ring"]):
        examine_item("diamond_ring")
    elif does_include(["examine", "small", "note"]) or does_include(["read", "small", "note"]):
        examine_item("small_note")
    elif does_include(["examine", "1948"]) or does_include(["look", "1948"]):
        examine_item("1948_merlot")
    elif does_include(["open", "1948"]) or does_include(["open", "1948"]):
        print("There is a note inside...")
        add_item("small_note")
    elif does_include(["examine", "diary"]) or does_include(["read", "diary"]):
        examine_item("diary")

    # Entrance Hall
    elif current_room == 0:
        if does_include(["go", "upstairs"]) or user_input == "upstairs":
            current_room = change_room(1)
        elif user_input == "enter salon" or user_input == "west":
            current_room = change_room(2)
        elif user_input == "enter billiard" or user_input == "east":
            current_room = change_room(3)
        elif user_input == "enter kitchen" or user_input == "south":
            current_room = change_room(5)
        elif does_include(["outside"]) or user_input == "north" or user_input == "leave":

            # Player wins
            if "big_key" in inventory:
                user_input = "exit game"
                print("Congratulations, you've escaped Hawthorne Manor!")
                print("After leaving the house you decide to head straight home and take a nice long bath.")
                print(credits)

            else:
                print("The door is locked and you don't have the right key to open it.")

        elif does_include(["examine", "portrait"]) or does_include(["look", "portrait"]):
            examine_item("portrait_hall")
        elif does_include(["take", "portrait"]):
            print(error)
        elif does_include(["examine", "door"]) or does_include(["look", "door"]):
            examine_item("front_door")
        elif does_include(["open", "door"]):
            if "big_key" in inventory:
                print("It is open now.")
            else:
                print("The front door is locked. You don't have the right key to open it.")

    # Hallway
    elif current_room == 1:
        if does_include(["go", "downstairs"]) or user_input == "downstairs":
            current_room = change_room(0)
        elif user_input == "enter bedroom" or user_input == "west":
            current_room = change_room(6)
        elif user_input == "enter bathroom" or user_input == "east":
            current_room = change_room(7)
        elif does_include(["go", "upstairs"]) or user_input == "upstairs":
            if "regular_key" in inventory:
                current_room = change_room(8)
            else:
                print("The door to the attic is locked. You don't have the right key to open it.")

        elif does_include(["examine", "door"]) or does_include(["look", "door"]):
            examine_item("attic_door")
        elif does_include(["open", "door"]):
            if "regular_key" in inventory:
                print("It is open now.")
            else:
                print("The door to the attic is locked. You don't have the right key to open it.")

    # Salon
    elif current_room == 2:
        if user_input == "enter hall" or user_input == "east":
            current_room = change_room(0)
        elif does_include(["examine", "portrait"]) or does_include(["look", "portrait"]):
            examine_item("portrait_salon")
        elif does_include(["examine", "piano"]) or does_include(["look", "piano"]):
            examine_item("piano")
        elif does_include(["examine", "notes"]) or does_include(["read", "notes"]):
            examine_item("notes")
        elif does_include(["play", "piano"]) or does_include(["use", "piano"]):
            print("You start playing the notes in front of you...")
            if played_piano:
                print("Nothing happens.")
            else:
                played_piano = True
                print("After a while, an unusual sound comes from inside the piano.")
        elif does_include(["open", "piano"]):
            if played_piano:
                print("You find a key inside the piano.")
                add_item("regular_key")
            else:
                print("It doesn't seem to open.")

    # Billiard Room
    elif current_room == 3:
        if user_input == "enter hall" or user_input == "west":
            current_room = change_room(0)
        elif user_input == "enter library" or user_input == "south":
            current_room = change_room(4)

        elif does_include(["examine", "pool"]) or does_include(["look", "pool"]):
            examine_item("pool_table")
        elif does_include(["play", "pool"]) or does_include(["use", "pool"]):
            print("You don't see any pool equipment.")
        elif does_include(["examine", "clock"]) or does_include(["look", "clock"]):
            examine_item("clock")
        elif does_include(["use", "clock"]) or does_include(["set", "clock"]):
            if input("Which time do you want to set (hh:mm)?:> ") == "11:59":
                print("A secret compartment in the clock opens up and you find a small key in there!")
                add_item("small_key")
            else:
                print("Nothing happens.")

    # Library
    elif current_room == 4:
        if user_input == "enter billiard" or user_input == "north":
            current_room = change_room(3)

        elif does_include(["examine", "books"]) or does_include(["look", "books"]) or does_include(["read", "books"]):
            examine_item("books")
        elif does_include(["examine", "desk"]) or does_include(["look", "desk"]):
            examine_item("desk")
        elif does_include(["open", "desk"]) or does_include(["open", "drawer"]):
            if "small_key" in inventory:
                print("You find a lighter inside the drawer...")
                add_item("lighter")
            else:
                print("You don't have the right key with you.")

    # Kitchen
    elif current_room == 5:
        if does_include(["go", "downstairs"]) or user_input == "downstairs":
            current_room = change_room(9)
        elif user_input == "enter hall" or user_input == "north":
            current_room = change_room(0)

    # Bedroom
    elif current_room == 6:
        if user_input == "enter hall" or user_input == "east":
            current_room = change_room(1)

        elif does_include(["move", "picture"]) or does_include(["put", "picture"]) or does_include(["pull", "picture"]):
            print("There is a safe hidden behind the picture.")
        elif does_include(["take", "picture"]) or does_include(["get", "picture"]):
            print("The picture is too big to take it with you, maybe try to move it instead.")
        elif does_include(["examine", "picture"]) or does_include(["look", "picture"]):
            examine_item("picture")
        elif does_include(["examine", "bed"]) or does_include(["look", "bed"]):
            examine_item("bed")
        elif does_include(["take", "diary"]) or does_include(["get", "diary"]):
            add_item("diary")
        elif does_include(["examine", "safe"]) or does_include(["look", "safe"]):
            examine_item("safe")
        elif does_include(["open", "safe"]) or does_include(["unlock", "safe"]):
            if "big_key" not in inventory:
                if input("Enter the four digit code:> ") == "0729":
                    print("It is open. You find a big metal key.")
                    add_item("big_key")
                else:
                    print("Nothing happens.")
            else:
                print("The safe is empty.")

    # Bathroom
    elif current_room == 7:
        if user_input == "enter hall" or user_input == "west":
            current_room = change_room(1)
        elif does_include(["take", "ring"]) or does_include(["get", "ring"]):
            add_item("diamond_ring")
        elif does_include(["examine", "sink"]) or does_include(["look", "sink"]):
            examine_item("sink")

    # Attic
    elif current_room == 8:
        if does_include(["go", "downstairs"]) or user_input == "downstairs":
            current_room = change_room(1)

        elif does_include(["take", "candle"]) or does_include(["get", "candle"]):
            add_item("candle")
        elif does_include(["examine", "stuff"]) or does_include(["look", "stuff"]):
            print("Nothing really useful except the candles.")

    # Wine Cellar
    elif current_room == 9 and "candlelight" in inventory:

        # if room is not dark
        if does_include(["go", "upstairs"]) or user_input == "upstairs":
            current_room = change_room(5)
        elif does_include(["take", "1948"]) or does_include(["get", "1948"]):
            add_item("1948_merlot")
        elif does_include(["take", "1926"]) or does_include(["get", "1926"]):
            print("You can't find a wine from that year.")
        elif does_include(["take", "1987"]) or does_include(["get", "1987"]):
            print("There are several bottles from that year, but nothing from interest.")
        elif does_include(["take", "bottle"]) or does_include(["get", "bottle"]):
            print("There are hundreds of bottles, you need to be more specific. Maybe pick a year?")
        elif does_include(["examine", "bottles"]) or does_include(["look", "bottles"]):
            examine_item("bottles")

    elif current_room == 9:

        # if room is dark
        if does_include(["go", "upstairs"]) or user_input == "upstairs":
            current_room = change_room(5)

        elif does_include(["examine"]) or does_include(["look"]):
            print("It is too dark to see anything.")
        elif does_include(["use", "lighter"]):
            print("The lighter alone doesn't do anything, you need a candle.")
        elif does_include(["take"]) or does_include(["use"]):
            print("It is too dark to see anything.")

    # User input isn't recognized
    else:
        print("Nothing happens.")

print("Thank you for playing the Hawthorne Manor Video Game! Good bye.")
