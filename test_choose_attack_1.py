from unittest import TestCase
from game import choose_attack_1
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_attack_1(self, _):
        actual = choose_attack_1({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move':
                                 'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                                  'Charmander'})
        expected = '1'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_attack_2(self, _):
        actual = choose_attack_1({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move':
                                 'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                                  'Charmander'})
        expected = '2'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_choose_attack_3(self, _):
        actual = choose_attack_1({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move':
                                 'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                                  'Charmander'})
        expected = '3'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['string'])
    def test_choose_attack_string(self, _):
        actual = choose_attack_1({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move':
                                 'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                                  'Charmander'})
        expected = 'string'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['13a b!?'])
    def test_choose_attack_mix(self, _):
        actual = choose_attack_1({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 50, 'Current XP': 0, 'First move':
                                 'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1, 'Pokemon':
                                  'Charmander'})
        expected = '13a b!?'
        self.assertEqual(actual, expected)
