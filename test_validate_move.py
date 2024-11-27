from unittest import TestCase
from game import validate_move


class Test(TestCase):
    def test_validate_move_invalid_north(self):
        expected = False
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "1")
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_west(self):
        expected = False
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "4")
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_south(self):
        expected = False
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}, "2")
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_east(self):
        expected = False
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}, "3")
        self.assertEqual(expected, actual)

    def test_validate_move_valid_north(self):
        expected = True
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, "1")
        self.assertEqual(expected, actual)

    def test_validate_move_valid_west(self):
        expected = True
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, "4")
        self.assertEqual(expected, actual)

    def test_validate_move_valid_south(self):
        expected = True
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, "2")
        self.assertEqual(expected, actual)

    def test_validate_move_valid_east(self):
        expected = True
        actual = validate_move({(0, 0): "Empty space", (0, 1): "Empty space", (0, 2): "Empty space",
                                (1, 0): "Empty space", (1, 1): "Empty space", (1, 2): "Empty space"},
                               {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}, "3")
        self.assertEqual(expected, actual)
