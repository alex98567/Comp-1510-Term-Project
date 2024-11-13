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


def game():
    rows = 5
    columns = 5
    board = make_board(rows, columns)


def main():
    game()


if __name__ == "__main__":
    main()
