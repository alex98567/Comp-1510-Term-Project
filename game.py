"""
Alex Howe
A01309729
"""

import random
import copy
from colorama import Fore, init, Style


init(autoreset=True)


def is_fire_1():
    """
    Provide an easy way to access the name of the first evolution of the fire starter

    :postcondition: the string Charmander is returned
    :return: the string Charmander

    >>> is_fire_1() #doctest: +SKIP
    'Charmander'
    """
    charmander = Fore.RED + "Charmander" + Style.RESET_ALL
    return charmander


def is_fire_2():
    """
    Provide an easy way to access the name of the second evolution of the fire starter

    :postcondition: the string Charmeleon is returned
    :return: the string Charmeleon

    >>> is_fire_2() #doctest: +SKIP
    'Charmeleon'
    """
    charmeleon = Fore.RED + "Charmeleon" + Style.RESET_ALL
    return charmeleon


def is_fire_3():
    """
    Provide an easy way to access the name of the third evolution of the fire starter

    :postcondition: the string Charizard is returned
    :return: the string Charizard

    >>> is_fire_3() #doctest: +SKIP
    'Charizard'
    """
    charizard = Fore.RED + "Charizard" + Style.RESET_ALL
    return charizard


def is_water_1():
    """
    Provide an easy way to access the name of the first evolution of the water starter

    :postcondition: the string Squirtle is returned
    :return: the string Squirtle

    >>> is_water_1() #doctest: +SKIP
    'Squirtle'
    """
    squirtle = Fore.BLUE + "Squirtle" + Style.RESET_ALL
    return squirtle


def is_water_2():
    """
    Provide an easy way to access the name of the second evolution of the water starter

    :postcondition: the string Warturtle is returned
    :return: the string Warturtle

    >>> is_water_2() #doctest: +SKIP
    'Warturtle'
    """
    warturtle = Fore.BLUE + "Warturtle" + Style.RESET_ALL
    return warturtle


def is_water_3():
    """
    Provide an easy way to access the name of the third evolution of the water starter

    :postcondition: the string Blastoise is returned
    :return: the string Blastoise

    >>> is_water_3() #doctest: +SKIP
    'Blastoise'
    """
    blastoise = Fore.BLUE + "Blastoise" + Style.RESET_ALL
    return blastoise


def is_grass_1():
    """
    Provide an easy way to access the name of the first evolution of the grass starter

    :postcondition: the string Bulbasaur is returned
    :return: the string Bulbasaur

    >>> is_grass_1() #doctest: +SKIP
    'Bulbasaur'
    """
    bulbasaur = Fore.GREEN + "Bulbasaur" + Style.RESET_ALL
    return bulbasaur


def is_grass_2():
    """
    Provide an easy way to access the name of the second evolution of the grass starter

    :postcondition: the string Ivysaur is returned
    :return: the string Ivysaur

    >>> is_grass_2() #doctest: +SKIP
    'Ivysaur'
    """
    ivysaur = Fore.GREEN + "Ivysaur" + Style.RESET_ALL
    return ivysaur


def is_grass_3():
    """
    Provide an easy way to access the name of the third evolution of the grass starter

    :postcondition: the string Venasaur is returned
    :return: the string Venasaur

    >>> is_grass_3() #doctest: +SKIP
    'Venasaur'
    """
    venasaur = Fore.GREEN + "Venasaur" + Style.RESET_ALL
    return venasaur


def get_list_of_wild_grass(board, rows, columns):
    """
    Create a list of the coordinates that may contain enemies

    :param board: a dictionary
    :param rows: a non negative integer
    :param columns: a non negative integer
    :precondition board: board must be a dictionary
    :precondition rows: rows must be a non negative integer, ideally a 5
    :precondition columns: columns must be a non negative integer, ideally a 5
    :precondition board: board must be a dictionary, ideally containing 25 key-value pairs
    :postcondition: A list will be generated that contains the key value pairs, which represent coordinates on the
                    board, where an enemy may be encountered
    :return: a list called spaces_to_check_for_foe

    >>> get_list_of_wild_grass({(0, 0): 'S', (0, 1): 'W', (1, 0): 'S', (1, 1): 'W'}, 2, 2)
    [(0, 1), (1, 1)]
    >>> get_list_of_wild_grass({(0, 0): 'S', (0, 1): 'W', (0, 2): 'W', (1, 0): 'S', (1, 1): 'W', (1, 2): 'S', \
    (2, 0): 'S', (2, 1): 'W', (2, 2): 'S'}, 3, 3)
    [(0, 1), (0, 2), (1, 1), (2, 1)]
    """
    spaces_to_check_for_foe = []
    for row in range(rows):
        for column in range(columns):
            coordinates = (row, column)
            if "W" in board[coordinates]:
                spaces_to_check_for_foe.append(coordinates)
    return spaces_to_check_for_foe


def make_board(rows, columns):
    """
    Create a board of given number of rows and columns.

    :param rows: a positive non-zero integer
    :param columns: a positive non-zero integer
    :precondition rows: rows must be a positive non-zero integer
    :precondition columns: columns must be a positive non-zero integer
    :postcondition: create a dictionary of given number of rows and columns stored as keys in board_dictionary
                    and either "Safe area", "Wild grass", or "Pokecenter" stored as the value for each key
    :return: a dictionary of given number of rows and columns that serves as a board

    >>> make_board(3, 3) #doctest: +SKIP
    {(0, 0): 'Safe area', (0, 1): 'Safe area', (0, 2): 'Wild grass', (1, 0): 'Safe area', (1, 1): 'Wild grass', \
(1, 2): 'Wild grass', (2, 0): 'Safe area', (2, 1): 'Wild grass', (2, 2): 'Pokecenter'}
    >>> make_board(2, 2) #doctest: +SKIP
    {(0, 0): 'Safe area', (0, 1): 'Wild grass', (1, 0): 'Safe area', (1, 1): 'Wild grass'}
    """
    board = {}
    spaces = ["Safe area", "Wild grass"]
    for row in range(rows):
        for column in range(columns):
            coordinates = (row, column)
            board[coordinates] = random.choice(spaces)

            if rows > 0 and columns > 0:
                board[0, 0] = "Safe area"
            if rows > 2 and columns > 2:
                board[2, 2] = "Pokecenter"
            if rows > 4 and columns > 4:
                board[4, 4] = "Safe area"

    return board


def make_character():
    """
    Create a character

    Choose between 3 characters and a dictionary will be created that stores character stats

    :postcondition: A dictionary will be created that contains the names of stat categories as keys and the values of
                    those stats as values
    :return: A dictionary storing character stats

    >>> make_character() #doctest: +SKIP
    {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0,  "First move": "Tackle",
    "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_grass_1()}
    >>> make_character() #doctest: +SKIP
    {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "First move": "Scratch",
    "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_fire_1()}
    """
    choice = (input("\nEnter 1 to choose " + is_fire_1() + ", 2 to choose " + is_water_1() + ", or 3 to choose "
                    + is_grass_1() + ". "))
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
    """
    Describe the current location of the character and display stats

    Describe the current location of the character on the board with a grid, legend to understand the grid, and also
    show the current stats of the character including name, location, current HP, current XP. and move-set

    :param rows: a positive integer
    :param columns: a positive integer
    :param board: a dictionary of coordinates on the board and what those spaces contain
    :param character: a dictionary containing key-value pairs showing attributes
    :precondition rows: rows must be a positive integer
    :precondition columns: columns must be a positive integer
    :precondition board: board must be a dictionary with a tuple of integers as keys and with values of 'Safe area',
                         'Wild grass', or 'Pokecenter'
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: a grid is generated showing the visual location with a legend for comprehension, as well as a
                    dictionary containing the names of stats categories as keys and values of those categories as values
    :return: a string summarizing the character dictionary
    """
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
    :param character: a dictionary containing key-value pairs showing attributes
    :param direction: A string of the proposed direction to move the character
    :precondition board: Dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", and have valid
                         values for all keys
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
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

    :param character: a dictionary containing key-value pairs showing attributes
    :param direction: A string of the direction the character will be moved
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :precondition direction: String must be one of "1", "2", "3", "4"
    :postcondition: Your character is moved on the board according to the direction entered
    :return: Character is returned with updated dictionary values to reflect the move

    >>> move_character({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "First move": \
    "Scratch", "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": "Charmander"}, "2")
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move': 'Scratch', 'Second move': \
'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
    >>> move_character({"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 50, "Current XP": 0, "First move": \
    "Scratch", "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": "Charmander"}, "1")
    {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move': 'Scratch', 'Second move': \
'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
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
    """
    Check if the final boss battle should be triggered

    :param character: a dictionary containing key-value pairs showing attributes
    :param rows: a positive integer
    :param columns: a positive integer
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :precondition rows: rows must be a positive integer
    :precondition columns: columns must be a positive integer
    :postcondition: A False boolean will be generated and changed to True if the user is level 3, has 500 XP, and is at
                    the bottom right square on the board
    :return: A True or False boolean

    >>> check_if_ready_for_final_boss({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, \
    'First move': 'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}, 5, 5)
    False
    >>> check_if_ready_for_final_boss({'X-coordinate': 4, 'Y-coordinate': 4, 'Current HP': 150, 'Current XP': 500, \
    'First move': 'Scratch', 'Second move': 'Ember', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'}, \
    5, 5)
    True
    """
    time_for_boss = False

    if (character["X-coordinate"] == (columns - 1) and character["Y-coordinate"] == (rows - 1) and
            character["Level"] == 3) and character["Current XP"] >= 500:
        time_for_boss = True

    return time_for_boss


def check_for_foes():
    """
    Check if there is a foe

    Check if the current location on the board occupied by the character contains a foe. There is a 75% chance of
    encountering an enemy to battle

    :postcondition: A random integer is generated in range 1 to 4. A True boolean, indicating that there is a foe to
                    battle, is generated and changed to False if the random integer generated is a 1, signifying that
                    there is no foe in this location.
    :return: A boolean indicating whether the current location has a foe or not

    >>> check_for_foes() #doctest: +SKIP
    True
    >>> check_for_foes() #doctest: +SKIP
    False
    """
    is_foe = True

    chance = random.randint(1, 4)

    if chance == 1:
        is_foe = False

    return is_foe


def get_opponent_1():
    """
    Determine which type of enemy Pokemon to fight if user is level 1

    :postcondition: A random integer is determined in range 1 to 3. If integer is a 1, user will battle Magicarp, a
                    water type. If integer is a 2, user will battle Growlithe, a fire type. If integer is a 3, user will
                    battle Caterpie, a grass type.
    :return: A dictionary containing key-value pairs with the names and values of the attributes of the selected Pokemon

    >>> get_opponent_1() #doctest: +SKIP
    {"Name": "Magicarp", "Current HP": 25, "First move": "Splash"}

    >>> get_opponent_1() #doctest: +SKIP
    {"Name": "Growlithe", "Current HP": 25, "First move": "Roar"}

    >>> get_opponent_1() #doctest: +SKIP
    {"Name": "Caterpie", "Current HP": 25, "First move": "String shot"}
    """
    chance = random.randint(1, 3)
    if chance == 1:
        print("A wild " + Fore.LIGHTBLUE_EX + "Magicarp" + Style.RESET_ALL + " has appeared, a water type!")
        magicarp = {"Name": Fore.LIGHTBLUE_EX + "Magicarp" + Style.RESET_ALL, "Current HP": 25, "First move": "Splash"}
        return magicarp
    if chance == 2:
        print("A wild " + Fore.LIGHTRED_EX + "Growlithe" + Style.RESET_ALL + " has appeared, a fire type!")
        growlithe = {"Name": Fore.LIGHTRED_EX + "Growlithe" + Style.RESET_ALL, "Current HP": 25, "First move": "Roar"}
        return growlithe
    if chance == 3:
        print("A wild " + Fore.LIGHTGREEN_EX + "Caterpie" + Style.RESET_ALL + " has appeared, a grass type!")
        caterpie = {"Name": Fore.LIGHTGREEN_EX + "Caterpie" + Style.RESET_ALL, "Current HP": 25, "First move":
                    "String shot"}
        return caterpie


def choose_attack_1(character):
    """
    Choose what attack to use when level 1

    :param character: a dictionary containing key-value pairs showing attributes for a level 1 Pokemon
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: user will enter a string that indicates which move they choose to attack with
    :return: a string

    >>> choose_attack_1({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}) # doctest: +SKIP
    '1'
    >>> choose_attack_1({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}) # doctest: +SKIP
    '2'
    """
    attack = input("Press 1 to use " + str(character["First move"]) + ". An incorrect entry will cause your attack to "
                   "miss ")
    return attack


def validate_attack_1(attack):
    """
    Validate that the user has chosen the First move attack

    :param attack: a string
    :precondition attack: attack must be a string
    :postcondition: a True boolean will be returned if the string is '1'. Otherwise, it will return False
    :return: a boolean indicating if the First move was chosen as an attack

    >>> validate_attack_1('1')
    True
    >>> validate_attack_1('2')
    False
    """
    return attack == "1"


def opponent_is_alive(opponent):
    """
    Check if the opponent still has HP

    :param opponent: a dictionary of the opponents attributes
    :precondition opponent: opponent must be a dictionary of the opponents attributes
    :postcondition: a True boolean will be returned if the opponent has a "Current HP" attribute that is greater than
                    zero. Otherwise, it will return False
    :return: a boolean indicating whether the opponent still has HP

    >>> opponent_is_alive({'Name': 'Caterpie', 'Current HP': 25, 'First move': 'String shot'})
    True
    >>> opponent_is_alive({'Name': 'Caterpie', 'Current HP': 0, 'First move': 'String shot'})
    False
    """
    return opponent["Current HP"] > 0


def battle_1(character):
    """
    Drive the battle
    """
    opponent = get_opponent_1()
    while is_alive(character) and opponent_is_alive(opponent):
        if is_alive(character):
            attack = choose_attack_1(character)
            valid_attack = validate_attack_1(attack)
            if valid_attack:
                print(str(character["Pokemon"]) + " used " + str(character["First move"]) + " and it did 5 damage!")
                opponent["Current HP"] -= 5
                if opponent["Current HP"] < 0:
                    opponent["Current HP"] = 0
                print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            else:
                print("Oh no! Your attack has missed!")
            if opponent_is_alive(opponent):
                print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it did 3 damage!")
                character["Current HP"] -= 3
                if character["Current HP"] < 0:
                    character["Current HP"] = 0
                print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
            else:
                print("Congratulations! You defeated the " + opponent["Name"] + " and gained 10 XP points")
                character["Current XP"] += 10
    return character


def get_opponent_2():
    """
    Determine which type of enemy Pokemon to fight if user is level 2

    :postcondition: A random integer is determined in range 1 to 3. If integer is a 1, user will battle Vaporeon, a
                    water type. If integer is a 2, user will battle Flareon, a fire type. If integer is a 3, user will
                    battle Leafeon, a grass type.
    :return: A dictionary containing key-value pairs with the names and values of the attributes of the selected Pokemon

    >>> get_opponent_2() # doctest: +SKIP
    {"Name": "Vaporeon", "Current HP": 60, "First move": "Bubble"}
    >>> get_opponent_2() # doctest: +SKIP
    {"Name": "Flareon", "Current HP": 60, "First move": "Blast burn"}
    >>> get_opponent_2() # doctest: +SKIP
    {"Name": "Leafeon", "Current HP": 60, "First move": "Razor leaf"}
    """
    chance = random.randint(1, 3)
    if chance == 1:
        print("A wild " + Fore.LIGHTBLUE_EX + "Vaporeon" + Style.RESET_ALL + " has appeared, a water type! Be careful, "
                                                                             "this pokemon uses a water move.")
        vaporeon = {"Name": Fore.LIGHTBLUE_EX + "Vaporeon" + Style.RESET_ALL, "Current HP": 60, "First move": "Bubble"}
        return vaporeon
    if chance == 2:
        print("A wild " + Fore.LIGHTRED_EX + "Flareon" + Style.RESET_ALL + " has appeared, a fire type! Be careful, "
                                                                           "this pokemon uses a fire move.")
        flareon = {"Name": Fore.LIGHTRED_EX + "Flareon" + Style.RESET_ALL, "Current HP": 60, "First move":
                   "Blast burn"}
        return flareon
    if chance == 3:
        print("A wild " + Fore.LIGHTGREEN_EX + "Leafeon" + Style.RESET_ALL + " has appeared, a grass type! Be careful, "
                                                                             "this pokemon uses a grass move")
        leafeon = {"Name": Fore.LIGHTGREEN_EX + "Leafeon" + Style.RESET_ALL, "Current HP": 60, "First move":
                   "Razor leaf"}
        return leafeon


def choose_attack_2(character):
    """
    Choose what attack to use when level 2

    :param character: a dictionary containing key-value pairs showing attributes for a level 2 Pokemon
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: user will enter a string that indicates which move they choose to attack with
    :return: a string

    >>> choose_attack_2({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 100, 'Current XP': 200, 'First move': \
    'Scratch', 'Second move': 'Flamethrower', 'Third move': 'none', 'Level': 2, 'Pokemon': 'Charmeleon'}) \
    # doctest: +SKIP
    '1'
    >>> choose_attack_2({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 100, 'Current XP': 200, 'First move': \
    'Scratch', 'Second move': 'Flamethrower', 'Third move': 'none', 'Level': 2, 'Pokemon': 'Charmeleon'}) \
    # doctest: +SKIP
    '2'
    """
    attack = input("Press 1 to use " + str(character["First move"]) + " or 2 to use " + str(character["Second move"]) +
                   ". An incorrect entry will cause your attack to miss ")
    return attack


def validate_attack_2(attack):
    """
    Validate that the user has chosen the Second move attack

    :param attack: a string
    :precondition attack: attack must be a string
    :postcondition: a True boolean will be returned if the string is '2'. Otherwise, it will return False
    :return: a boolean indicating if the Second move was chosen as an attack

    >>> validate_attack_2('1')
    False
    >>> validate_attack_2('2')
    True
    """
    return attack == "2"


def get_opponent_3():
    """
    Determine which type of enemy Pokemon to fight if user is level 3

    :postcondition: A random integer is determined in range 1 to 3. If integer is a 1, user will battle Kyogre, a
                    water type. If integer is a 2, user will battle Entei, a fire type. If integer is a 3, user will
                    battle Groudon, a grass type.
    :return: A dictionary containing key-value pairs with the names and values of the attributes of the selected Pokemon

    >>> get_opponent_3() # doctest: +SKIP
    {"Name": "Kyogre", "Current HP": 100, "First move": "Surf"}
    >>> get_opponent_3() # doctest: +SKIP
    {"Name": "Entei", "Current HP": 100, "First move": "Flamethrower"}
    >>> get_opponent_3() # doctest: +SKIP
    {"Name": "Groudon", "Current HP": 100, "First move": "Frenzy plant"}
    """
    chance = random.randint(1, 3)
    if chance == 1:
        print("A wild " + Fore.LIGHTBLUE_EX + "Kyogre" + Style.RESET_ALL + " has appeared, a water type! Be careful, "
                                                                           "this high level pokemon uses a water move.")
        kyogre = {"Name": Fore.LIGHTBLUE_EX + "Kyogre" + Style.RESET_ALL, "Current HP": 100, "First move": "Surf"}
        return kyogre
    if chance == 2:
        print("A wild " + Fore.LIGHTRED_EX + "Entei" + Style.RESET_ALL + " has appeared, a fire type! Be careful, "
                                                                         "this high level pokemon uses a fire move.")
        entei = {"Name": Fore.LIGHTRED_EX + "Entei" + Style.RESET_ALL, "Current HP": 100, "First move": "Flamethrower"}
        return entei
    if chance == 3:
        print("A wild " + Fore.LIGHTGREEN_EX + "Groudon" + Style.RESET_ALL + " has appeared, a grass type! Be careful, "
              "this high level pokemon uses a grass move")
        groudon = {"Name": Fore.LIGHTGREEN_EX + "Groudon" + Style.RESET_ALL, "Current HP": 100, "First move":
                   "Frenzy plant"}
        return groudon


def choose_attack_3(character):
    """
    Choose what attack to use when level 3

    :param character: a dictionary containing key-value pairs showing attributes for a level 3 Pokemon
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: user will enter a string that indicates which move they choose to attack with
    :return: a string

    >>> choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500, 'First move': \
    'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'}) \
    # doctest: +SKIP
    '1'
    >>> choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500, 'First move': \
    'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'}) \
    # doctest: +SKIP
    '3'
    """
    attack = input("Press 1 to use " + str(character["First move"]) + ", 2 to use " + str(character["Second move"]) +
                   ", or 3 to use " + str(character["Third move"]) + ". An incorrect entry will cause your attack to "
                   "miss.")
    return attack


def validate_attack_3(attack):
    """
    Validate that the user has chosen the Third move attack

    :param attack: a string
    :precondition attack: attack must be a string
    :postcondition: a True boolean will be returned if the string is '3'. Otherwise, it will return False
    :return: a boolean indicating if the Third move was chosen as an attack

    >>> validate_attack_3('3')
    True
    >>> validate_attack_3('2')
    False
    """
    return attack == "3"


def battle_2(character):
    """
    Drive the battle
    """
    opponent = get_opponent_2()
    while is_alive(character) and opponent_is_alive(opponent):
        if is_alive(character):
            attack = choose_attack_2(character)
            use_attack_1 = validate_attack_1(attack)
            use_attack_2 = validate_attack_2(attack)
            if use_attack_1:
                print(str(character["Pokemon"]) + " used " + str(character["First move"]) + " and it did 8 damage!")
                opponent["Current HP"] -= 8
                if opponent["Current HP"] < 0:
                    opponent["Current HP"] = 0
                print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            elif use_attack_2:
                if (character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == Fore.LIGHTBLUE_EX + "Vaporeon" +
                        Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your fire move "
                          "is not very effective. It did 7 damage!")
                    opponent["Current HP"] -= 7
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == Fore.LIGHTGREEN_EX + "Leafeon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your fire move "
                          "is super effective! It did 13 damage!")
                    opponent["Current HP"] -= 13
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_2() and str(opponent["Name"]) == Fore.LIGHTRED_EX + "Flareon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your grass move "
                          "is not very effective. It did 7 damage!")
                    opponent["Current HP"] -= 7
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_2() and opponent["Name"] == Fore.LIGHTBLUE_EX + "Vaporeon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your grass move "
                          "is super effective! It did 13 damage!")
                    opponent["Current HP"] -= 13
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_2() and opponent["Name"] == Fore.LIGHTGREEN_EX + "Leafeon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your water move "
                          "is not very effective. It did 7 damage!")
                    opponent["Current HP"] -= 7
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_2() and opponent["Name"] == Fore.LIGHTRED_EX + "Flareon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your water move "
                          "is super effective! It did 13 damage!")
                    opponent["Current HP"] -= 13
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                else:
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and it did 10 "
                          "damage!")
                    opponent["Current HP"] -= 10
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            else:
                print("Oh no! Your attack has missed!")
            if opponent_is_alive(opponent):
                if (character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == Fore.LIGHTBLUE_EX + "Vaporeon" +
                        Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", it's super effective! "
                          "It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == Fore.LIGHTGREEN_EX + "Leafeon" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " used " + str(opponent["First move"]) + " but it's not very "
                          "effective! It did 6 damage!")
                    character["Current HP"] -= 6
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_2() and str(opponent["Name"]) == Fore.LIGHTGREEN_EX + "Leafeon" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " has used " + str(opponent["First move"]) + " and it's super "
                          "effective! It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_2() and str(opponent["Name"]) == Fore.LIGHTRED_EX + "Flareon" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", but it's not very "
                          "effective! It did 6 damage!")
                    character["Current HP"] -= 6
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_2() and str(opponent["Name"]) == Fore.LIGHTRED_EX + "Flareon" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it's super effective! "
                          "It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_2() and str(opponent["Name"]) == Fore.LIGHTBLUE_EX + "Vaporeon" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " but it's not very "
                          "effective! It did 6 damage!")
                    character["Current HP"] -= 6
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                else:
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it did 8 damage!")
                    character["Current HP"] -= 8
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
            else:
                print("Congratulations! You defeated the " + opponent["Name"] + " and gained 20 XP points")
                character["Current XP"] += 20
    return character


def battle_3(character):
    """
    Drive the battle
    """
    opponent = get_opponent_3()
    while is_alive(character) and opponent_is_alive(opponent):
        if is_alive(character):
            attack = choose_attack_3(character)
            use_attack_1 = validate_attack_1(attack)
            use_attack_2 = validate_attack_2(attack)
            use_attack_3 = validate_attack_3(attack)
            if use_attack_1:
                print(str(character["Pokemon"]) + " used " + str(character["First move"]) + " and it did 12 damage!")
                opponent["Current HP"] -= 12
                if opponent["Current HP"] < 0:
                    opponent["Current HP"] = 0
                print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            elif use_attack_2:
                if (character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == Fore.LIGHTBLUE_EX + "Kyogre" +
                        Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your fire move "
                          "is not very effective. It did 10 damage!")
                    opponent["Current HP"] -= 10
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == Fore.LIGHTGREEN_EX + "Groudon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your fire move "
                          "is super effective! It did 16 damage!")
                    opponent["Current HP"] -= 16
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == Fore.LIGHTRED_EX + "Entei" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your grass move "
                          "is not very effective. It did 10 damage!")
                    opponent["Current HP"] -= 10
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_3() and opponent["Name"] == Fore.LIGHTBLUE_EX + "Kyogre" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your grass move "
                          "is super effective! It did 16 damage!")
                    opponent["Current HP"] -= 16
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_3() and opponent["Name"] == Fore.LIGHTGREEN_EX + "Groudon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your water move "
                          "is not very effective. It did 10 damage!")
                    opponent["Current HP"] -= 10
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_3() and opponent["Name"] == Fore.LIGHTRED_EX + "Entei" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your water move "
                          "is super effective! It did 16 damage!")
                    opponent["Current HP"] -= 16
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                else:
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and it did 13 "
                          "damage!")
                    opponent["Current HP"] -= 13
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            elif use_attack_3:
                if (character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == Fore.LIGHTBLUE_EX + "Kyogre" +
                        Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " but your fire move "
                          "is not very effective. It did 5 damage!")
                    opponent["Current HP"] -= 5
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == Fore.LIGHTGREEN_EX + "Groudon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " and your fire move "
                          "is super effective! It did 25 damage!")
                    opponent["Current HP"] -= 25
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == Fore.LIGHTRED_EX + "Entei" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " but your grass move "
                          "is not very effective. It did 5 damage!")
                    opponent["Current HP"] -= 5
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_3() and opponent["Name"] == Fore.LIGHTBLUE_EX + "Kyogre" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " and your grass move "
                          "is super effective! It did 25 damage!")
                    opponent["Current HP"] -= 25
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_3() and opponent["Name"] == Fore.LIGHTGREEN_EX + "Groudon" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " but your water move "
                          "is not very effective. It did 5 damage!")
                    opponent["Current HP"] -= 5
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_3() and opponent["Name"] == Fore.LIGHTRED_EX + "Entei" +
                      Style.RESET_ALL):
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " and your water move "
                          "is super effective! It did 25 damage!")
                    opponent["Current HP"] -= 25
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                else:
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " and it did 15 "
                          "damage!")
                    opponent["Current HP"] -= 15
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            else:
                print("Oh no! Your attack has missed!")
            if opponent_is_alive(opponent):
                if (character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == Fore.LIGHTBLUE_EX + "Kyogre" +
                        Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", it's super effective! "
                          "It did 16 damage!")
                    character["Current HP"] -= 16
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == Fore.LIGHTGREEN_EX + "Groudon" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " used " + str(opponent["First move"]) + " but it's not very "
                          "effective! It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_3() and str(opponent["Name"]) == Fore.LIGHTGREEN_EX + "Groudon" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " has used " + str(opponent["First move"]) + " and it's super "
                          "effective! It did 16 damage!")
                    character["Current HP"] -= 16
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_water_3() and str(opponent["Name"]) == Fore.LIGHTRED_EX + "Entei" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", but it's not very "
                          "effective! It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == Fore.LIGHTRED_EX + "Entei" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it's super effective! "
                          "It did 16 damage!")
                    character["Current HP"] -= 16
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif (character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == Fore.LIGHTBLUE_EX + "Kyogre" +
                      Style.RESET_ALL):
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " but it's not very "
                          "effective! It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                else:
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it did 13 damage!")
                    character["Current HP"] -= 13
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
            else:
                print("Congratulations! You defeated the " + opponent["Name"] + " and gained 50 XP points")
                character["Current XP"] += 50
    return character


def is_alive(character):
    """
    Check if the user Pokemon still has HP

    :param character: a dictionary containing key-value pairs showing attributes
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: a True boolean will be returned if the user Pokemon has a "Current HP" attribute that is greater
                    than zero. Otherwise, it will return False
    :return: a boolean indicating whether the user has HP or not

    >>> is_alive({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500, 'First move': \
    'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'})
    True
    >>> is_alive({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 0, 'Current XP': 500, 'First move': \
    'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'})
    False
    """
    return character["Current HP"] > 0


def is_pokecenter(character):
    """
    Check if the user Pokemon is located at the Pokecenter and restore health to max if they are

    :param character: a dictionary containing key-value pairs showing attributes
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: if the user Pokemon is located at the Pokecenter, their "Current HP" will be restored to full
    :return: Either a character with full "Current HP" or with their current HP

    >>> is_pokecenter({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 6, 'Current XP': 10, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'})
    {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 6, 'Current XP': 10, 'First move': 'Scratch', 'Second move': \
'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
    >>> is_pokecenter({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 10, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'})
    You have reached the Pokecenter and your Charmander has full health again!
    {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 50, 'Current XP': 10, 'First move': 'Scratch', 'Second move': \
'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
    """
    if character["Level"] == 1 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 50
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again!")
        return character
    if character["Level"] == 2 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 100
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again!")
        return character
    if character["Level"] == 3 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 150
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again!")
        return character
    else:
        return character


def is_level_2(character):
    """
    Check if the user has enough experience to level up to level 2

    :param character: a dictionary containing key-value pairs showing attributes
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: A boolean is generated indicating if the user has enough XP to level up to level 2
    :return: A boolean indicating if the user has enough experience to level up to level 2

    >>> is_level_2({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 10, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'})
    False
    >>> is_level_2({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 100, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'})
    True
    """
    return character["Current XP"] in range(100, 400)


def is_level_3(character):
    """
    Check if the user has enough experience to level up to level 3

    :param character: a dictionary containing key-value pairs showing attributes
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: A boolean is generated indicating if the user has enough XP to level up to level 3
    :return: A boolean indicating if the user has enough experience to level up to level 3

    >>> is_level_3({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 100, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmeleon'})
    False
    >>> is_level_3({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 400, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmeleon'})
    True
    """
    return character["Current XP"] >= 400


def evolve_level_2(character):
    """
    Level up to level 2 and evolve your starting Pokemon to the second evolution

    :param character: a dictionary containing key-value pairs showing attributes
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: user Pokemon has new values for "Current HP", "Second move", and "Pokemon" to reflect the level up
                    and evolution
    :return: an updated character dictionary

    >>> evolve_level_2({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 100, 'First move': \
    'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}) #doctest: +SKIP
    {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 100, 'Current XP': 100, 'First move': 'Scratch', \
'Second move': 'Ember', 'Third move': 'none', 'Level': 2, 'Pokemon': 'Charmeleon'}

    >>> evolve_level_2({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 100, 'First move': \
    'Bite', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Squirtle'}) #doctest: +SKIP
    {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 100, 'Current XP': 100, 'First move': 'Bite', 'Second move': \
'Water gun', 'Third move': 'none', 'Level': 2, 'Pokemon': 'Warturtle'}
    """
    if character["Pokemon"] == is_fire_1():
        character["Pokemon"] = is_fire_2()
        character["Second move"] = "Ember"
        character["Current HP"] = 100
        character["Level"] = 2
        print("\n" + Fore.YELLOW + "Wow! You reached level 2 " + Style.RESET_ALL + " and your " + str(is_fire_1()) +
              " has evolved into a " + str(is_fire_2()) + "!")
        print(str(is_fire_2()) + " learned ember, a fire type move! Remember what you have learned about move types.")
        print(str(is_fire_2()) + " now has 100 HP instead of 50.")
    elif character["Pokemon"] == is_grass_1():
        character["Pokemon"] = is_grass_2()
        character["Second move"] = "Vine whip"
        character["Current HP"] = 100
        character["Level"] = 2
        print("\n" + Fore.YELLOW + "Wow! You reached level 2 " + Style.RESET_ALL + " and your " + str(is_grass_1()) +
              " has evolved into an " + str(is_grass_2()) + "!")
        print(str(is_grass_2()) + " learned vine whip, a grass type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_grass_2()) + " now has 100 HP instead of 50.")
    elif character["Pokemon"] == is_water_1():
        character["Pokemon"] = is_water_2()
        character["Second move"] = "Water gun"
        character["Current HP"] = 100
        character["Level"] = 2
        print("\n" + Fore.YELLOW + "Wow! You reached level 2 " + Style.RESET_ALL + " and your " + str(is_water_1()) +
              " has evolved into a " + str(is_water_2()) + "!")
        print(str(is_water_2()) + " learned water gun, a water type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_water_2()) + " now has 100 HP instead of 50.")
    print(str(character["First move"]) + " now does 8 damage while " + str(character["Second move"]) + " naturally "
          "does 10 damage. It will do 13 damage when super effective and only 7 damage when not very effective.")
    input("Enter any input to continue to level 2...")
    return character


def evolve_level_3(character):
    """
    Level up to level 3 and evolve your starting Pokemon to the third and final evolution

    :param character: a dictionary containing key-value pairs showing attributes
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate", "Current HP", "Current XP",
                             "First move", "Second move", "Third move", "Level", and "Pokemon" with valid values for all
    :postcondition: user Pokemon has new values for "Current HP", "Third move", and "Pokemon" to reflect the level up
                    and evolution
    :return: an updated character dictionary

    >>> evolve_level_3({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 400, 'First move': \
    'Scratch', 'Second move': 'Ember', 'Third move': 'none', 'Level': 2, 'Pokemon': 'Charmeleon'}) #doctest: +SKIP
    {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 150, 'Current XP': 400, 'First move': 'Scratch', \
'Second move': 'Ember', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'}

    >>> evolve_level_2({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 400, 'First move': \
    'Bite', 'Second move': 'Water gun', 'Third move': 'none', 'Level': 2, 'Pokemon': 'Squirtle'}) #doctest: +SKIP
    {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 150, 'Current XP': 400, 'First move': 'Bite', 'Second move': \
'Water gun', 'Third move': 'Hydro cannon', 'Level': 3, 'Pokemon': 'Blastoise'}
    """
    if character["Pokemon"] == is_fire_2():
        character["Pokemon"] = is_fire_3()
        character["Third move"] = "Fire blast"
        character["Current HP"] = 150
        character["Level"] = 3
        print("\n" + Fore.YELLOW + "Wow! You reached level 3 " + Style.RESET_ALL + " and your " + str(is_fire_2()) +
              " has evolved into a " + str(is_fire_3()) + "!")
        print(str(is_fire_3()) + " learned Fire blast, a fire type move! Remember what you have learned about move "
                                 "types.")
        print(str(is_fire_3()) + " now has 150 HP instead of 10.")
    elif character["Pokemon"] == is_grass_2():
        character["Pokemon"] = is_grass_3()
        character["Third move"] = "Solarbeam"
        character["Current HP"] = 150
        character["Level"] = 3
        print("\n" + Fore.YELLOW + "Wow! You reached level 3 " + Style.RESET_ALL + " and your " + str(is_grass_2()) +
              " has evolved into a " + str(is_grass_3()) + "!")
        print(str(is_grass_3()) + " learned Solarbeam, a grass type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_grass_3()) + " now has 150 HP instead of 100.")
    elif character["Pokemon"] == is_water_2():
        character["Pokemon"] = is_water_3()
        character["Third move"] = "Hydro pump"
        character["Current HP"] = 150
        character["Level"] = 3
        print("\n" + Fore.YELLOW + "Wow! You reached level 3 " + Style.RESET_ALL + " and your " + str(is_water_2()) +
              " has evolved into a " + str(is_water_3()) + "!")
        print(str(is_water_3()) + " learned Hydro pump, a water type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_water_3()) + " now has 150 HP instead of 100.")
    print(str(character["First move"]) + " now does 12 damage. " + str(character["Second move"]) + " naturally "
          "does 13 damage, but will do 16 damage when super effective and only 10 damage when not very effective.\n"
          + str(character["Third move"]) + " naturally does 15 damage.\nIt will do 25 damage when super "
          "effective, but will only do 5 damage when not very effective so use this move wisely!")
    input("Enter any input to continue to level 3...")
    return character


def battle_boss(character):
    """
    Drive the final boss battle
    """
    print("Your final test awaits! You have done well to get this far and are now challenging the Pokemon master. "
          "\nHe sends out the legendary " + Fore.LIGHTMAGENTA_EX + "Mewtwo" + Style.RESET_ALL + "! " +
          Fore.LIGHTMAGENTA_EX + "Mewtwo" + Style.RESET_ALL + " has 150 HP and is a Psychic type. Psychic types "
          "have no type advantage and all of your moves will do their natural damage. \nOne incorrect move will likely "
          "mean defeat. Good luck!")
    mewtwo = {"Name": Fore.LIGHTMAGENTA_EX + "Mewtwo" + Style.RESET_ALL, "Current HP": 150, "First move": "Psybeam"}
    opponent = mewtwo
    character["Current HP"] = 150
    while is_alive(character) and opponent_is_alive(opponent):
        if is_alive(character):
            attack = choose_attack_3(character)
            use_attack_1 = validate_attack_1(attack)
            use_attack_2 = validate_attack_2(attack)
            use_attack_3 = validate_attack_3(attack)
            if use_attack_1:
                print(
                    str(character["Pokemon"]) + " attacks with " + str(character["First move"]) + " and it did 12 "
                    "damage!")
                opponent["Current HP"] -= 12
                if opponent["Current HP"] < 0:
                    opponent["Current HP"] = 0
                print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            elif use_attack_2:
                print(
                    str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and it did 13 damage!")
                opponent["Current HP"] -= 13
                if opponent["Current HP"] < 0:
                    opponent["Current HP"] = 0
                print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            elif use_attack_3:
                print(
                    str(character["Pokemon"]) + " used " + str(character["Third move"]) + " and it did 15 damage!")
                opponent["Current HP"] -= 15
                if opponent["Current HP"] < 0:
                    opponent["Current HP"] = 0
                print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
            else:
                print("Oh no! Your attack has missed!")
            if opponent_is_alive(opponent):
                print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it did 15 damage!")
                character["Current HP"] -= 15
                if character["Current HP"] < 0:
                    character["Current HP"] = 0
                print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
            else:
                print("\n" + Fore.YELLOW + "Congratulations!" + Style.RESET_ALL + " You defeated the " +
                      opponent["Name"] + "!!! You are the new Pokemon master and have completed the game!!")
    return character


def game():
    """
    Drive the game
    """
    print("\nWelcome to the world of Pokemon! You are a brand new Pokemon trainer who finds themself in Pallet Town.\n"
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
    print("You have a choice between 3 unique Pokemon on your journey.\nThere is " + Fore.RED + "Charmander" +
          Style.RESET_ALL + ", the " + Fore.RED + "fire" + Style.RESET_ALL + " type Pokemon, " + Fore.BLUE + "Squirtle"
          + Style.RESET_ALL + ", the " + Fore.BLUE + "water" + Style.RESET_ALL + " type Pokemon, and " + Fore.GREEN +
          "Bulbasaur" + Style.RESET_ALL + ", the " + Fore.GREEN + "grass" + Style.RESET_ALL + " type Pokemon.\n\nYou "
          "will now learn about type effectiveness, which is one of the keys to winning this game so read the "
          "following " + Fore.YELLOW + "CAREFULLY" + Style.RESET_ALL + "!\n" + Fore.RED + "Fire" + Style.RESET_ALL +
          " is weak to " + Fore.BLUE + "water" + Style.RESET_ALL + " and strong against " + Fore.GREEN + "grass" +
          Style.RESET_ALL + ". " + Fore.GREEN + "Grass" + Style.RESET_ALL + " is weak to " + Fore.RED + "fire" +
          Style.RESET_ALL + " and strong against " + Fore.BLUE + "water" + Style.RESET_ALL + ". " + Fore.BLUE + "Water"
          + Style.RESET_ALL + " is weak to " + Fore.GREEN + "grass" + Style.RESET_ALL + " and strong against " +
          Fore.RED + "fire" + Style.RESET_ALL + ".\n\nFor example, water attacks will do less damage to grass Pokemon, "
          "but more damage to fire Pokemon.\nYou will not be able to change your Pokemon once you make your selection. "
          "You will start with 50 HP and the game will end if your Pokemon loses all of their health.")
    character = make_character()
    time_for_boss = False
    while is_alive(character) and not time_for_boss and not is_level_2(character):
        print("\nLegend\nX represents user location\nS represents a safe area where you will not encounter enemies\n"
              "W represents wild grass where you MIGHT encounter enemies\nP represents Pokecenter where you can heal. "
              "\n100 XP is needed for level 2.")
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
                    battle_1(character)
            time_for_boss = check_if_ready_for_final_boss(character, rows, columns)
        else:
            print("Invalid move. This would put you out of bounds. Please try again.")
    if is_level_2(character):
        evolve_level_2(character)
    while is_alive(character) and not time_for_boss and is_level_2(character):
        print("\nLegend\nX represents user location\nS represents a safe area where you will not encounter enemies\n"
              "W represents wild grass where you MIGHT encounter enemies\nP represents Pokecenter where you can heal. "
              "\n400 XP is needed for level 3.")
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
                    battle_2(character)
            time_for_boss = check_if_ready_for_final_boss(character, rows, columns)
        else:
            print("Invalid move. This would put you out of bounds. Please try again.")
        if is_level_3(character):
            evolve_level_3(character)
    while is_alive(character) and not time_for_boss and is_level_3(character):
        print("\nLegend\nX represents user location\nS represents a safe area where you will not encounter enemies\n"
              "W represents wild grass where you MIGHT encounter enemies\nP represents Pokecenter where you can heal. "
              "\n500 XP is needed to challenge the Pokemon master. You're so close! Reach the bottom right hand corner "
              "of the board with 500 XP to challenge the Pokemon master. \nYour health will be replenished when this "
              "fight begins.")
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
                    battle_3(character)
            time_for_boss = check_if_ready_for_final_boss(character, rows, columns)
        else:
            print("Invalid move. This would put you out of bounds. Please try again.")
    if time_for_boss and is_alive(character):
        battle_boss(character)
    if not is_alive(character):
        print("Sorry but your Pokemon has fainted. Game Over!")


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    main()
