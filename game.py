"""
Alex Howe
A01309729
"""

import random


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

    return board


def make_character():
    pass


def game():
    print("Welcome to the world of Pokemon! You are a brand new pokemon trainer who finds himself in Pallet Town.\n"
          "Your task is to defeat the local Pokemon master to become the best trainer in town.\nTo do this, you must "
          "select the Pokemon that you want to control.\nYour Pokemon will start at level 1 and will evolve when you "
          "reach levels 2 and 3.\nOnce you reach level 3, you can challenge the Pokemon master by progressing to the "
          "bottom right of the board.\nEach space on the board has been randomly designated as a Safe area or contains "
          "Wild grass.\nWild grass contains wild Pokemon that can be defeated for experience, which helps you level.\n"
          "In the center of the board is a PokeCenter. Stepping on this space will replenish your Pokemon to full "
          "health.\nYou will learn more in time. For now, it's time to select your Pokemon!\n\n")
    rows = 5
    columns = 5
    board = make_board(rows, columns)


def main():
    game()


if __name__ == "__main__":
    main()
