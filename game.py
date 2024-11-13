"""
Alex Howe
A01309729
"""

import random
import copy


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
                     "none", "Third move": "none", "Level": 1}
        return character
    elif choice == "2":
        print(f"Congratulations! You selected {water}, the water type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "First move": "Bite", "Second move":
                     "none", "Third move": "none", "Level": 1}
        return character
    elif choice == "3":
        print(f"Congratulations! You selected {grass}, the grass type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "First move": "Tackle", "Second move":
                     "none", "Third move": "none", "Level": 1}
        return character


def describe_current_location(rows, columns, board, character):
    board_copy = copy.deepcopy(board)
    character_location = (character["X-coordinate"], character["Y-coordinate"])
    print("\nMap:")
    for row in range(rows):
        grid = []
        for column in range(columns):
            coordinates = (row, column)
            if board_copy[coordinates] == "Wild grass":
                board_copy[coordinates] = "W"
            elif board_copy[coordinates] == "Safe area":
                board_copy[coordinates] = "S"
            elif board_copy[coordinates] == "Pokecenter":
                board_copy[coordinates] = "P"
            if character_location == coordinates:
                board_copy[coordinates] = "X"
            grid.append(board_copy[coordinates])
        print(grid)
    print("\n")
    if character["Level"] == 1:
        return ("Character is currently located at space " + str(character_location) + "\nCurrent HP is "
                + str(character["Current HP"]) + "\nCurrent level is " + str(character["Level"]) + "First move is "
                + str(character["First move"]))


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


def validate_move(board, character, direction):
    """
    Validate if proposed move keeps the character on the board

    :param board: A dictionary of the board's layout
    :param character: A dictionary of the character's attributes
    :param direction: A string of the proposed direction to move the character
    :precondition board: Dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", and have valid
                         values for all keys
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate",
                             "Current HP" with valid values
    :precondition direction: String must be one of "1", "2", "3", "4"
    :postcondition: A False boolean is generated and then changed to true if the character remains on the board
    :return: A boolean indicating if the move is valid

    >>> validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (1, 0): "Empty space", (1, 1): "Empty space"}, \
    {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "1")
    False
    >>> validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (1, 0): "Empty space", (1, 1): "Empty space"}, \
    {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "2")
    True
    """
    valid = False

    character_copy = copy.deepcopy(character)

    if direction == "1":
        character_copy["Y-coordinate"] -= 1
    elif direction == "2":
        character_copy["Y-coordinate"] += 1
    elif direction == "3":
        character_copy["X-coordinate"] += 1
    else:
        character_copy["X-coordinate"] -= 1

    move_tuple = (character_copy["X-coordinate"], character_copy["Y-coordinate"])

    if move_tuple in board.keys():
        valid = True

    return valid


def move_character(character, direction):
    """
    Move your character on the board

    :param character: A dictionary of the character's attributes
    :param direction: A string of the direction the character will be moved
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate",
                             "Current HP" with valid values
    :precondition direction: String must be one of "1", "2", "3", "4"
    :postcondition: Your character is moved on the board according to the direction entered
    :return: Character is returned with updated dictionary values to reflect the move

    >>> move_character({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "2")
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    >>> move_character({"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 5}, "1")
    {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}
    """
    if direction == "1":
        character["Y-coordinate"] -= 1
    elif direction == "2":
        character["Y-coordinate"] += 1
    elif direction == "3":
        character["X-coordinate"] += 1
    else:
        character["X-coordinate"] -= 1

    return character


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
    print("\nLegend\nX represents user location\nS represents a safe area where you will not encounter enemies\n"
          "W represents wild grass where you will encounter enemies\nP represents Pokecenter where you can heal")
    print(describe_current_location(rows, columns, board, character))


def main():
    game()


if __name__ == "__main__":
    main()
