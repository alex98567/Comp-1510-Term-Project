"""
Alex Howe
A01309729
"""

import random
import copy


def is_fire_1():
    return "Charmander"


def is_fire_2():
    return "Charmeleon"


def is_fire_3():
    return "Charizard"


def is_water_1():
    return "Squirtle"


def is_water_2():
    return "Warturtle"


def is_water_3():
    return "Blastoise"


def is_grass_1():
    return "Bulbasaur"


def is_grass_2():
    return "Ivysaur"


def is_grass_3():
    return "Venasaur"


def get_list_of_wild_grass(board, rows, columns):
    spaces_to_check_for_foe = []
    for row in range(rows):
        for column in range(columns):
            coordinates = (row, column)
            if "W" in board[coordinates]:
                spaces_to_check_for_foe.append(coordinates)
    return spaces_to_check_for_foe


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

            board[0, 0] = "Safe area"
            board[2, 2] = "Pokecenter"
            board[4, 4] = "Safe area"

    return board


def make_character():
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
        print(f"Congratulations! You selected {is_fire_1()}, the fire type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "First move": "Scratch",
                     "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_fire_1()}
        return character
    elif choice == "2":
        print(f"Congratulations! You selected {is_water_1()}, the water type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "First move": "Bite",
                     "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_water_1()}
        return character
    elif choice == "3":
        print(f"Congratulations! You selected {is_grass_1()}, the grass type Pokemon.")
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0,  "First move": "Tackle",
                     "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_grass_1()}
        return character


def describe_current_location(rows, columns, board, character):
    board_copy = copy.deepcopy(board)
    character_location = (character["X-coordinate"], character["Y-coordinate"])
    print("\nMap:")
    for row in range(rows):
        grid = []
        for column in range(columns):
            coordinates = (column, row)
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
        return (str(character["Pokemon"]) + " is currently located at space " + str(character_location) + "\nCurrent "
                "HP is " + str(character["Current HP"]) + "\nCurrent level is " + str(character["Level"]) + "\nCurrent "
                "XP is " + str(character["Current XP"]) + "\nFirst move is " + str(character["First move"]))
    if character["Level"] == 2:
        return (str(character["Pokemon"]) + " is currently at space " + str(character_location) + "\nCurrent "
                "HP is " + str(character["Current HP"]) + "\nCurrent level is " + str(character["Level"]) + "\nCurrent "
                "XP is " + str(character["Current XP"]) + "\nFirst move is " + str(character["First move"]) +
                "\nSecond move is " + str(character["Second move"]))
    if character["Level"] == 3:
        return ((str(character["Pokemon"]) + " is currently located at space " + str(character_location) + "\nCurrent "
                "HP is " + str(character["Current HP"]) + "\nCurrent level is " + str(character["Level"]) + "\nCurrent "
                 "XP is " + str(character["Current XP"]) + "\nFirst move is " + str(character["First move"]) +
                 "\nSecond move is " + str(character["Second move"])) + "\nThird move is "
                + str(character["Third move"]))


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


def check_if_ready_for_final_boss(character, rows, columns):
    time_for_boss = False

    if (character["X-coordinate"] == (columns - 1) and character["Y-coordinate"] == (rows - 1) and
            character["Level"] == 3):
        time_for_boss = True

    return time_for_boss


def check_for_foes():
    is_foe = True

    chance = random.randint(1, 4)

    if chance == 1:
        is_foe = False

    return is_foe


def get_opponent_1():
    chance = random.randint(1, 3)
    if chance == 1:
        print("A wild Magicarp has appeared, a water type!")
        magicarp = {"Name": "Magicarp", "Current HP": 25, "First move": "Splash"}
        return magicarp
    if chance == 2:
        print("A wild Growlithe has appeared, a fire type!")
        growlithe = {"Name": "Growlithe", "Current HP": 25, "First move": "Roar"}
        return growlithe
    if chance == 3:
        print("A wild Caterpie has appeared, a grass type!")
        caterpie = {"Name": "Caterpie", "Current HP": 25, "First move": "String shot"}
        return caterpie


def choose_attack_1(character):
    attack = input("Press 1 to use " + str(character["First move"]) + ". An incorrent entry will cause your attack to "
                   "miss ")
    return attack


def validate_attack_1(attack):
    return attack == "1"


def opponent_is_alive(opponent):
    return opponent["Current HP"] > 0


def battle_1(character):
    opponent = get_opponent_1()
    while is_alive(character) and opponent_is_alive(opponent):
        if is_alive(character):
            attack = choose_attack_1(character)
            valid_attack = validate_attack_1(attack)
            if valid_attack:
                print("You used " + str(character["First move"]) + " and it did 5 damage!")
                opponent["Current HP"] -= 5
                print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            else:
                print("Oh no! Your attack has missed!")
            if opponent_is_alive(opponent):
                print("Opponent uses " + str(opponent["First move"]) + " and it did 3 damage!")
                character["Current HP"] -= 3
                print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
            else:
                print("Congratulations! You defeated the " + opponent["Name"] + " and gained 10 XP points")
                character["Current XP"] += 10
                return character


def is_alive(character):
    return character["Current HP"] >= 0


def is_pokecenter(character):
    if character["Level"] == 1 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 50
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again! ")
        return character
    if character["Level"] == 2 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 75
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again! ")
        return character
    if character["Level"] == 3 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 100
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again! ")
        return character


def game():
    print("Welcome to the world of Pokemon! You are a brand new Pokemon trainer who finds themself in Pallet Town.\n"
          "Your task is to defeat the local Pokemon master to become the best trainer in town.\nTo do this, you must "
          "select the Pokemon that you want to control.\nYour Pokemon will start at level 1 and will evolve when you "
          "reach levels 2 and 3.\nOnce you reach level 3, you can challenge the Pokemon master by progressing to the "
          "bottom right of the board.\nEach space on the board has been randomly designated as a safe area or contains "
          "wild grass.\nWild grass may contain wild Pokemon that can be defeated for experience, which helps you level "
          "up.\nIn the center of the board is a PokeCenter. Stepping on this space will replenish your Pokemon to full "
          "health.\nYou will learn more in time. For now, it's time to select your Pokemon!\n")
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    wild_grass_spaces = get_list_of_wild_grass(board, rows, columns)
    character = make_character()
    time_for_boss = False
    while is_alive(character) and not time_for_boss:
        print("\nLegend\nX represents user location\nS represents a safe area where you will not encounter enemies\n"
              "W represents wild grass where you will encounter enemies\nP represents Pokecenter where you can heal")
        print(describe_current_location(rows, columns, board, character))
        print("\n")
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            is_pokecenter(character)
            character_location = (character["X-coordinate"], character["Y-coordinate"])
            if character_location in wild_grass_spaces:
                there_is_a_foe = check_for_foes()
                if there_is_a_foe:
                    if character["Level"] == 1:
                        battle_1(character)
            time_for_boss = check_if_ready_for_final_boss(character, rows, columns)
        else:
            print("Invalid move. This would put you out of bounds. Please try again.")
    if not is_alive(character):
        print("Sorry but your Pokemon has fainted. Game Over!")


def main():
    game()


if __name__ == "__main__":
    main()
