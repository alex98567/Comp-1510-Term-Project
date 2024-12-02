from unittest import TestCase
from game import is_pokecenter


class Test(TestCase):
    def test_is_pokecenter_false(self):
        actual = is_pokecenter({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 94, 'Current XP': 500, 'First move':
                                'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3,
                                'Pokemon': 'Charizard'})
        expected = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 94, 'Current XP': 500, 'First move': 'Scratch',
                    'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'}
        self.assertEqual(actual, expected)

    def test_is_pokecenter_true_94(self):
        actual = is_pokecenter({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 94, 'Current XP': 500, 'First move':
                                'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3,
                                'Pokemon': 'Charizard'})
        expected = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 150, 'Current XP': 500, 'First move': 'Scratch',
                    'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'}
        self.assertEqual(actual, expected)

    def test_is_pokecenter_true_1(self):
        actual = is_pokecenter({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 1, 'Current XP': 500, 'First move':
                                'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3,
                                'Pokemon': 'Charizard'})
        expected = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 150, 'Current XP': 500, 'First move': 'Scratch',
                    'Second move': 'Flamethrower', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'}
        self.assertEqual(actual, expected)
