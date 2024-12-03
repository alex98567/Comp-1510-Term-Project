from unittest import TestCase
from game import is_level_2


class Test(TestCase):
    def test_is_level_2_false_6(self):
        actual = is_level_2({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 10, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = False
        self.assertEqual(actual, expected)

    def test_is_level_2_false_99(self):
        actual = is_level_2({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 99, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = False
        self.assertEqual(actual, expected)

    def test_is_level_2_True_100(self):
        actual = is_level_2({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 100, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = True
        self.assertEqual(actual, expected)

    def test_is_level_2_True_101(self):
        actual = is_level_2({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 101, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = True
        self.assertEqual(actual, expected)

    def test_is_level_2_True_399(self):
        actual = is_level_2({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 6, 'Current XP': 399, 'First move':
                             'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                             'Charmander'})
        expected = True
        self.assertEqual(actual, expected)
