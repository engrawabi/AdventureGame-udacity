import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def field(item, creatures):
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to knock on the door of the house."
                "\nEnter 2 to peer into the cave."
                "\nWhat would you like to do?")
    choice = input("(Please enter 1 or 2.)\n")
    if choice == "1":
        house(item, creatures)
    elif choice == "2":
        cave(item, creatures)
    else:
        field(item, creatures)


def house(item, creatures):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when"
                " the door opens and out steps a " + creatures + ".")
    print_pause("Eep! This is the " + creatures + "'s house!")
    print_pause("The " + creatures + " attacks you!")
    if "Sward" not in item:
        print_pause("You feel a bit under - prepared for this,"
                    "what with only having a tiny dagger.")
    while True:
        choice1 = input("Would you like to (1) fight or (2) run away?")
        if choice1 == "1":
            fight(item, creatures)
            break
        elif choice1 == "2":
            print_pause("You run back into the field. Luckily,"
                        "you don't seem to have been followed.\n")
            field(item, creatures)
            break


def cave(item, creatures):
    # Things that happen to the player goes in the cave
    if "Sward" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        field(item, creatures)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        item.append("Sward")
        field(item, creatures)


def fight(item, creatures):
    # Things that happen when the player fights
    if "Sward" in item:
        print_pause("As the" + creatures + " moves to attack,"
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your"
                    " hand as you brace yourself for the attack.")
        print_pause("But the " + creatures + " takes one look at your"
                    " shiny new toy and runs away!")
        print_pause("You have rid the town of the " + creatures + "."
                    "You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + creatures + ".")
        print_pause("You have been defeated!")
        play_again()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def play_again():
    again = valid_input("Would you like to play again? ( y / n )", ['y', 'n'])
    if again == 'y':  # option 1 (y)
        print_pause("Excellent! Restarting the game ...")
        main()
    else:  # option 2 (n)
        print("Thanks for playing! See you next time.\n")
        exit(0)


def main():
    item = []
    creatures = random.randint(1, 5)
    if creatures == 1:
        creatures = "wicked fairie"
    elif creatures == 2:
        creatures = "pirate"
    elif creatures == 3:
        creatures = "dragon"
    elif creatures == 4:
        creatures = "troll"
    elif creatures == 5:
        creatures = "gorgon"
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a is " + creatures + " somewhere "
                "around here, and has been"
                " terrifying the nearby village.")
    print_pause("In front of you is a house.\nTo your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.\n")
    field(item, creatures)


main()
