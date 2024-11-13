"""
Alex Howe
A01309729
"""

import random
from locale import format_string


def make_board(rows, columns):
    board = {}
    for row in range(rows):
        for column in range(columns):
            coordinates = (row, column)
            space_selector = random.randint(1, 2)
            if space_selector == 1:
                board[coordinates] = "Safe area"
            else:
                board[coordinates] = "Wild grass"
            board[2, 2] = "Pokecenter"

    return board


def make_character():
    fire = "Charmander"
    water = "Squirtle"
    grass = "Bulbasaur"
    choice = (input("You get a choice between 3 unique Pokemon on your journey.\nThere is Charmander: the fire type "
                    "Pokemon, Squirtle: the water type Pokemon, and Bulbasaur: the grass type Pokemon.\nFire is weak "
                    "to water and strong against grass. Grass is weak to fire and strong against water. Water is weak "
                    "to grass and strong against fire.\nFor example, water attacks will do less damage to grass "
                    "Pokemon, but more damage to fire Pokemon.\nYou will not be able to change your selection. You "
                    "will start with 50 HP and the game will end if your Pokemon loses all of their health.\nEnter 1 "
                    "to choose Charmander, 2 to choose Squirtle, or 3 to choose Bulbasaur. "))
    while choice not in ["1", "2", "3"]:
        print("This is not a valid selection.\n")
        choice = (input("Enter 1 to choose Charmander, 2 to choose Squirtle, or 3 to choose Bulbasaur. "))
    if choice == "1":
        print(f"Congratulations! You selected {fire}, the fire type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "First move": "Scratch", "Second move":
                     "none", "Third move": "none"}
        return character
    elif choice == "2":
        print(f"Congratulations! You selected {water}, the water type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "First move": "Bite", "Second move":
                     "none", "Third move": "none"}
        return character
    elif choice == "3":
        print(f"Congratulations! You selected {grass}, the grass type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "First move": "Tackle", "Second move":
                     "none", "Third move": "none"}
        return character


def get_user_choice():
    """
    Decide which direction to move character

    User is prompted to enter a direction to move their character on the board

    :postcondition: User enters input that decides the direction to move the character
    :return: The direction that the user decided to move the character

    >>> get_user_choice() #doctest: +SKIP
    '1'
    >>> get_user_choice() #doctest: +SKIP
    '2'
    """
    choice = (input("Which direction would you like to go to? "
                    "(Enter 1 for North, 2 for South, 3 for East, 4 for West) "))
    while choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        choice = (
            input("Which direction would you like to go to? (Enter 1 for North, 2 for South, 3 for East, 4 for West) "))
    return choice


def game():
    print("Welcome to the world of Pokemon! You are a brand new Pokemon trainer who finds themself in Pallet Town.\n"
          "Your task is to defeat the local Pokemon master to become the best trainer in town.\nTo do this, you must "
          "select the Pokemon that you want to control.\nYour Pokemon will start at level 1 and will evolve when you "
          "reach levels 2 and 3.\nOnce you reach level 3, you can challenge the Pokemon master by progressing to the "
          "bottom right of the board.\nEach space on the board has been randomly designated as a safe area or contains "
          "wild grass.\nWild grass contains wild Pokemon that can be defeated for experience, which helps you level "
          "up.\nIn the center of the board is a PokeCenter. Stepping on this space will replenish your Pokemon to full "
          "health.\nYou will learn more in time. For now, it's time to select your Pokemon!\n")
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()


def main():
    game()


if __name__ == "__main__":
    main()
