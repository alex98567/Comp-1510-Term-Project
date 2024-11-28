from unittest import TestCase
from game import choose_attack_3
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_attack_3_1(self, _):
        actual = choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast',
                                  'Level': 3, 'Pokemon': 'Charizard'})
        expected = '1'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_attack_3_2(self, _):
        actual = choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast',
                                  'Level': 3, 'Pokemon': 'Charizard'})
        expected = '2'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_choose_attack_3_3(self, _):
        actual = choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast',
                                  'Level': 3, 'Pokemon': 'Charizard'})
        expected = '3'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['4'])
    def test_choose_attack_3_4(self, _):
        actual = choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast',
                                  'Level': 3, 'Pokemon': 'Charizard'})
        expected = '4'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['string'])
    def test_choose_attack_3_string(self, _):
        actual = choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast',
                                  'Level': 3, 'Pokemon': 'Charizard'})
        expected = 'string'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['.12! $%'])
    def test_choose_attack_3_mix(self, _):
        actual = choose_attack_3({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 150, 'Current XP': 500,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'Fire blast',
                                  'Level': 3, 'Pokemon': 'Charizard'})
        expected = '.12! $%'
        self.assertEqual(actual, expected)
