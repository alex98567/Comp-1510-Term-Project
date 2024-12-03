from unittest import TestCase
from game import is_level_3


class Test(TestCase):
    def test_is_level_3_false_125(self):
        actual = is_level_3({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 125, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = False
        self.assertEqual(actual, expected)

    def test_is_level_3_false_399(self):
        actual = is_level_3({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 399, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = False
        self.assertEqual(actual, expected)

    def test_is_level_3_True_400(self):
        actual = is_level_3({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 400, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = True
        self.assertEqual(actual, expected)

    def test_is_level_3_True_401(self):
        actual = is_level_3({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 401, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = True
        self.assertEqual(actual, expected)
