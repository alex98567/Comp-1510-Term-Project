"""
Alex Howe
A01309729
"""


def make_board(rows, columns):
    """
    Create a board of given number of rows and columns.

    :param rows: a positive non-zero integer
    :param columns: a positive non-zero integer
    :precondition rows: rows must be a positive non-zero integer
    :precondition columns: columns must be a positive non-zero integer
    :postcondition: create a dictionary of given number of rows and columns stored as keys in board_dictionary
                    and "Empty Room" stored as the value for each key
    :return: a dictionary of given number of rows and columns that serves as a board

    >>> make_board(3, 3)
    {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room', \
(1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room', (2, 2): 'Empty room'}
    >>> make_board(2, 2)
    {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
    """
    board = {}
    for row in range(rows):
        for column in range(columns):
            coordinates = (row, column)
            board[coordinates] = "Empty room"

    return board


def game():
    rows = 5
    columns = 5
    board = make_board(rows, columns)


def main():
    game()


if __name__ == "__main__":
    main()
