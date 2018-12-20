from sys import exit 
def gold_room():
    print("This room is full of gold.")
    print("Take how as mush as you want (0-100)")
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man,learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("Bear here")
    bear_moved = False
    while True:
        choice = input(">")
        if choice == "take honey":
            dead("Die")
        elif choice == "taunt"and not(bear_moved):
            print("Go now")
            bear_moved = True
        elif choice == "taunt" and bear_moved:
            dead("You die")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("No idea")

def cthulhu_room():
    print("Cthulhu room")
    choice = input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("Choose a room")
    choice = input(">")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You starved!")

start()