from unittest import TestCase
from game import is_alive


class Test(TestCase):
    def test_is_alive_150(self):
        actual = is_alive({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500, 'First move':
                           'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon':
                           'Charizard'})
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_1(self):
        actual = is_alive({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 1, 'Current XP': 500, 'First move':
                           'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon':
                           'Charizard'})
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_false_0(self):
        actual = is_alive({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 0, 'Current XP': 500, 'First move':
                           'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon':
                           'Charizard'})
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_negative(self):
        actual = is_alive({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': -1, 'Current XP': 500, 'First move':
                           'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon':
                           'Charizard'})
        expected = False
        self.assertEqual(actual, expected)
