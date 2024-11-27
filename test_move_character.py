from unittest import TestCase
from game import move_character, is_fire_1


class Test(TestCase):
    def test_move_character_south(self):
        actual = move_character({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0,
                                 "First move": "Scratch", "Second move": "none", "Third move": "none", "Level": 1,
                                 "Pokemon": is_fire_1()}, "2")
        expected = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move': 'Scratch',
                    'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
        self.assertEqual(actual, expected)

    def test_move_character_north(self):
        actual = move_character({"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 50, "Current XP": 0,
                                 "First move": "Scratch", "Second move": "none", "Third move": "none", "Level": 1,
                                 "Pokemon": is_fire_1()}, "1")
        expected = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move': 'Scratch',
                    'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
        self.assertEqual(actual, expected)

    def test_move_character_east(self):
        actual = move_character({"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 50, "Current XP": 0,
                                 "First move": "Scratch", "Second move": "none", "Third move": "none", "Level": 1,
                                 "Pokemon": is_fire_1()}, "3")
        expected = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 50, 'Current XP': 0, 'First move': 'Scratch',
                    'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
        self.assertEqual(actual, expected)

    def test_move_character_west(self):
        actual = move_character({"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 50, "Current XP": 0,
                                 "First move": "Scratch", "Second move": "none", "Third move": "none", "Level": 1,
                                 "Pokemon": is_fire_1()}, "4")
        expected = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 50, 'Current XP': 0, 'First move': 'Scratch',
                    'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'}
        self.assertEqual(actual, expected)
