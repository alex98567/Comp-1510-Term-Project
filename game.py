"""
Alex Howe
A01309729
"""

import random
import copy


def is_fire_1():
    """
    Provide an easy way to access the name of the first evolution of the fire starter

    :postcondition: the string Charmander is returned
    :return: the string Charmander

    >>> is_fire_1()
    'Charmander'
    """
    return "Charmander"


def is_fire_2():
    """
    Provide an easy way to access the name of the second evolution of the fire starter

    :postcondition: the string Charmeleon is returned
    :return: the string Charmeleon

    >>> is_fire_2()
    'Charmeleon'
    """
    return "Charmeleon"


def is_fire_3():
    """
    Provide an easy way to access the name of the third evolution of the fire starter

    :postcondition: the string Charizard is returned
    :return: the string Charizard

    >>> is_fire_3()
    'Charizard'
    """
    return "Charizard"


def is_water_1():
    """
    Provide an easy way to access the name of the first evolution of the water starter

    :postcondition: the string Squirtle is returned
    :return: the string Squirtle

    >>> is_water_1()
    'Squirtle'
    """
    return "Squirtle"


def is_water_2():
    """
    Provide an easy way to access the name of the second evolution of the water starter

    :postcondition: the string Warturtle is returned
    :return: the string Warturtle

    >>> is_water_2()
    'Warturtle'
    """
    return "Warturtle"


def is_water_3():
    """
    Provide an easy way to access the name of the third evolution of the water starter

    :postcondition: the string Blastoise is returned
    :return: the string Blastoise

    >>> is_water_3()
    'Blastoise'
    """
    return "Blastoise"


def is_grass_1():
    """
    Provide an easy way to access the name of the first evolution of the grass starter

    :postcondition: the string Bulbasaur is returned
    :return: the string Bulbasaur
    >>> is_grass_1()
    'Bulbasaur'
    """
    return "Bulbasaur"


def is_grass_2():
    """
    Provide an easy way to access the name of the second evolution of the grass starter

    :postcondition: the string Ivysaur is returned
    :return: the string Ivysaur

    >>> is_grass_2()
    'Ivysaur'
    """
    return "Ivysaur"


def is_grass_3():
    """
    Provide an easy way to access the name of the third evolution of the grass starter

    :postcondition: the string Venasaur is returned
    :return: the string Venasaur

    >>> is_grass_3()
    'Venasaur'
    """
    return "Venasaur"


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
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0,  "First move": "f",
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
    :param character: a dictionary containing keys of "X-coordinate", "Y-coordinate", "Current HP"
    :precondition rows: rows must be a positive integer
    :precondition columns: columns must be a positive integer
    :precondition board: board must be a dictionary with a tuple of integers as keys and with values of 'Safe area',
                         'Wild grass', or 'Pokecenter'
    :precondition character: dictionary must contain keys of "X-coordinate", "Y-coordinate",
                             "Current HP" with valid values
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
            character["Level"] == 3) and character["Current XP"] >= 100:
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
    attack = input("Press 1 to use " + str(character["First move"]) + ". An incorrect entry will cause your attack to "
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
    chance = random.randint(1, 3)
    if chance == 1:
        print("A wild Vaporeon has appeared, a water type! Be careful, this pokemon uses a water move.")
        vaporeon = {"Name": "Vaporeon", "Current HP": 60, "First move": "Bubble"}
        return vaporeon
    if chance == 2:
        print("A wild Flareon has appeared, a fire type! Be careful, this pokemon uses a fire move.")
        flareon = {"Name": "Flareon", "Current HP": 60, "First move": "Blast burn"}
        return flareon
    if chance == 3:
        print("A wild Leafeon has appeared, a grass type! Be careful, this pokemon uses a grass move")
        leafeon = {"Name": "Leafeon", "Current HP": 60, "First move": "Razor leaf"}
        return leafeon


def choose_attack_2(character):
    attack = input("Press 1 to use " + str(character["First move"]) + " or 2 to use " + str(character["Second move"]) +
                   ". An incorrect entry will cause your attack to miss ")
    return attack


def validate_attack_2(attack):
    return attack == "2"


def get_opponent_3():
    chance = random.randint(1, 3)
    if chance == 1:
        print("A wild Kyogre has appeared, a water type! Be careful, this high level pokemon uses a water move.")
        kyogre = {"Name": "Kyogre", "Current HP": 100, "First move": "Surf"}
        return kyogre
    if chance == 2:
        print("A wild Entei has appeared, a fire type! Be careful, this high level pokemon uses a fire move.")
        entei = {"Name": "Entei", "Current HP": 100, "First move": "Flamethrower"}
        return entei
    if chance == 3:
        print("A wild Groudon has appeared, a grass type! Be careful, this high level pokemon uses a grass move")
        groudon = {"Name": "Groudon", "Current HP": 100, "First move": "Frenzy plant"}
        return groudon


def choose_attack_3(character):
    attack = input("Press 1 to use " + str(character["First move"]) + ", 2 to use " + str(character["Second move"]) +
                   ", or 3 to use " + str(character["Third move"]) + ". An incorrect entry will cause your attack to "
                   "miss.")
    return attack


def validate_attack_3(attack):
    return attack == "3"


def battle_2(character):
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
                if character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == "Vaporeon":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your fire move "
                          "is not very effective. It did 7 damage!")
                    opponent["Current HP"] -= 7
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == "Leafeon":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your fire move "
                          "is super effective! It did 13 damage!")
                    opponent["Current HP"] -= 13
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_2() and str(opponent["Name"]) == "Flareon":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your grass move "
                          "is not very effective. It did 7 damage!")
                    opponent["Current HP"] -= 7
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_2() and opponent["Name"] == "Vaporeon":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your grass move "
                          "is super effective! It did 13 damage!")
                    opponent["Current HP"] -= 13
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_2() and opponent["Name"] == "Leafeon":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your water move "
                          "is not very effective. It did 7 damage!")
                    opponent["Current HP"] -= 7
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_2() and opponent["Name"] == "Flareon":
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
                if character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == "Vaporeon":
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", it's super effective! "
                          "It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_fire_2() and str(opponent["Name"]) == "Leafeon":
                    print(str(opponent["Name"]) + " used " + str(opponent["First move"]) + " but it's not very "
                          "effective! It did 6 damage!")
                    character["Current HP"] -= 6
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_2() and str(opponent["Name"]) == "Leafeon":
                    print(str(opponent["Name"]) + " has used " + str(opponent["First move"]) + " and it's super "
                          "effective! It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_2() and str(opponent["Name"]) == "Flareon":
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", but it's not very "
                          "effective! It did 6 damage!")
                    character["Current HP"] -= 6
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_2() and str(opponent["Name"]) == "Flareon":
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it's super effective! "
                          "It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_2() and str(opponent["Name"]) == "Vaporeon":
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
                if character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == "Kyogre":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your fire move "
                          "is not very effective. It did 10 damage!")
                    opponent["Current HP"] -= 10
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == "Groudon":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your fire move "
                          "is super effective! It did 16 damage!")
                    opponent["Current HP"] -= 16
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == "Entei":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your grass move "
                          "is not very effective. It did 10 damage!")
                    opponent["Current HP"] -= 10
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_3() and opponent["Name"] == "Kyogre":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " and your grass move "
                          "is super effective! It did 16 damage!")
                    opponent["Current HP"] -= 16
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_3() and opponent["Name"] == "Groudon":
                    print(str(character["Pokemon"]) + " used " + str(character["Second move"]) + " but your water move "
                          "is not very effective. It did 10 damage!")
                    opponent["Current HP"] -= 10
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_3() and opponent["Name"] == "Entei":
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
                if character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == "Kyogre":
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " but your fire move "
                          "is not very effective. It did 5 damage!")
                    opponent["Current HP"] -= 5
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == "Groudon":
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " and your fire move "
                          "is super effective! It did 25 damage!")
                    opponent["Current HP"] -= 25
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == "Entei":
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " but your grass move "
                          "is not very effective. It did 5 damage!")
                    opponent["Current HP"] -= 5
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_3() and opponent["Name"] == "Kyogre":
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " and your grass move "
                          "is super effective! It did 25 damage!")
                    opponent["Current HP"] -= 25
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_3() and opponent["Name"] == "Groudon":
                    print(str(character["Pokemon"]) + " used " + str(character["Third move"]) + " but your water move "
                          "is not very effective. It did 5 damage!")
                    opponent["Current HP"] -= 5
                    if opponent["Current HP"] < 0:
                        opponent["Current HP"] = 0
                    print(str(opponent["Name"]) + " has " + str(opponent["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_3() and opponent["Name"] == "Entei":
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
                if character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == "Kyogre":
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", it's super effective! "
                          "It did 16 damage!")
                    character["Current HP"] -= 16
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_fire_3() and str(opponent["Name"]) == "Leafeon":
                    print(str(opponent["Name"]) + " used " + str(opponent["First move"]) + " but it's not very "
                          "effective! It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_3() and str(opponent["Name"]) == "Groudon":
                    print(str(opponent["Name"]) + " has used " + str(opponent["First move"]) + " and it's super "
                          "effective! It did 16 damage!")
                    character["Current HP"] -= 16
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_water_3() and str(opponent["Name"]) == "Entei":
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + ", but it's not very "
                          "effective! It did 10 damage!")
                    character["Current HP"] -= 10
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == "Entei":
                    print(str(opponent["Name"]) + " uses " + str(opponent["First move"]) + " and it's super effective! "
                          "It did 16 damage!")
                    character["Current HP"] -= 16
                    if character["Current HP"] < 0:
                        character["Current HP"] = 0
                    print(str(character["Pokemon"]) + " has " + str(character["Current HP"]) + " HP")
                elif character["Pokemon"] == is_grass_3() and str(opponent["Name"]) == "Kyogre":
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
    return character["Current HP"] > 0


def is_pokecenter(character):
    if character["Level"] == 1 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 50
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again! ")
        return character
    if character["Level"] == 2 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 100
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again! ")
        return character
    if character["Level"] == 3 and character["X-coordinate"] == 2 and character["Y-coordinate"] == 2:
        character["Current HP"] = 150
        print("You have reached the Pokecenter and your " + character["Pokemon"] + " has full health again! ")
        return character


def is_level_2(character):
    return character["Current XP"] in range(20, 59)


def is_level_3(character):
    return character["Current XP"] >= 60


def evolve_level_2(character):
    if character["Pokemon"] == is_fire_1():
        character["Pokemon"] = is_fire_2()
        character["Second move"] = "Ember"
        character["Current HP"] = 100
        character["Level"] = 2
        print("\nWow! You reached level 2 and your " + str(is_fire_1()) + " has evolved into a " + str(is_fire_2()) +
              "!")
        print(str(is_fire_2()) + " learned ember, a fire type move! Remember what you have learned about move types.")
        print(str(is_fire_2()) + " now has 100 HP instead of 50.")
    elif character["Pokemon"] == is_grass_1():
        character["Pokemon"] = is_grass_2()
        character["Second move"] = "Vine whip"
        character["Current HP"] = 100
        character["Level"] = 2
        print("\nWow! You reached level 2 and your " + str(is_grass_1()) + " has evolved into an " + str(is_grass_2()) +
              "!")
        print(str(is_grass_2()) + " learned vine whip, a grass type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_grass_2()) + " now has 100 HP instead of 50.")
    elif character["Pokemon"] == is_water_1():
        character["Pokemon"] = is_water_2()
        character["Second move"] = "Water gun"
        character["Current HP"] = 100
        character["Level"] = 2
        print("\nWow! You reached level 2 and your " + str(is_water_1()) + " has evolved into a " + str(is_water_2()) +
              "!")
        print(str(is_water_2()) + " learned water gun, a water type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_water_2()) + " now has 100 HP instead of 50.")
    print(str(character["First move"]) + " now does 8 damage while " + str(character["Second move"]) + " naturally "
          "does 10 damage. It will do 13 damage when super effective and only 7 damage when not very effective.")
    return character


def evolve_level_3(character):
    if character["Pokemon"] == is_fire_2():
        character["Pokemon"] = is_fire_3()
        character["Third move"] = "Fire blast"
        character["Current HP"] = 150
        character["Level"] = 3
        print("\nWow! You reached level 3 and your " + str(is_fire_2()) + " has evolved into a " + str(is_fire_3()) +
              "!")
        print(str(is_fire_3()) + " learned Fire blast, a fire type move! Remember what you have learned about move "
                                 "types.")
        print(str(is_fire_3()) + " now has 150 HP instead of 10.")
    elif character["Pokemon"] == is_grass_2():
        character["Pokemon"] = is_grass_3()
        character["Second move"] = "Solarbeam"
        character["Current HP"] = 150
        character["Level"] = 3
        print("\nWow! You reached level 3 and your " + str(is_grass_2()) + " has evolved into a " + str(is_grass_3()) +
              "!")
        print(str(is_grass_2()) + " learned Solarbeam, a grass type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_grass_2()) + " now has 150 HP instead of 100.")
    elif character["Pokemon"] == is_water_2():
        character["Pokemon"] = is_water_3()
        character["Second move"] = "Hydro pump"
        character["Current HP"] = 150
        character["Level"] = 3
        print("\nWow! You reached level 3 and your " + str(is_water_2()) + " has evolved into a " + str(is_water_3()) +
              "!")
        print(str(is_water_2()) + " learned Hydro pump, a water type move! Remember what you have learned about move "
                                  "types.")
        print(str(is_water_2()) + " now has 150 HP instead of 100.")
    print(str(character["First move"]) + " now does 12 damage. " + str(character["Second move"]) + " naturally "
          "does 13 damage, but will do 16 damage when super effective and only 10 damage when not very effective.\n"
          + str(character["Third move"]) + " naturally does 15 damage.\nIt will do 25 damage when super very "
          "effective, but will only do 5 damage when not very effective so use this move wisely!")
    return character


def battle_boss(character):
    print("Your final test awaits! You have done well to get this far and are now challenging the Pokemon master. "
          "\nHe sends out the legendary Mewtwo! Mewtwo has 150 HP and is a Psychic type. Psychic types have no "
          "type advantage and all of your moves will do their natural damage. \nOne incorrect move will likely mean "
          "defeat. Good luck!")
    mewtwo = {"Name": "Mewtwo", "Current HP": 150, "First move": "Psybeam"}
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
                print("Congratulations! You defeated the " + opponent["Name"] + "!!! You are the new Pokemon master "
                      "and have completed the game!!")
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
    game()


if __name__ == "__main__":
    main()
