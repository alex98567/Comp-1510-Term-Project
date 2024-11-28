from unittest import TestCase
from game import choose_attack_2
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_choose_attack_2_1(self, _):
        actual = choose_attack_2({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 100, 'Current XP': 200,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'none',
                                  'Level': 2, 'Pokemon': 'Charmeleon'})
        expected = '1'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_attack_2_2(self, _):
        actual = choose_attack_2({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 100, 'Current XP': 200,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'none',
                                  'Level': 2, 'Pokemon': 'Charmeleon'})
        expected = '2'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_choose_attack_2_3(self, _):
        actual = choose_attack_2({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 100, 'Current XP': 200,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'none',
                                  'Level': 2, 'Pokemon': 'Charmeleon'})
        expected = '3'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['string'])
    def test_choose_attack_2_string(self, _):
        actual = choose_attack_2({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 100, 'Current XP': 200,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'none',
                                  'Level': 2, 'Pokemon': 'Charmeleon'})
        expected = 'string'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2112, yyz$%^'])
    def test_choose_attack_2_mix(self, _):
        actual = choose_attack_2({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 100, 'Current XP': 200,
                                  'First move': 'Scratch', 'Second move': 'Flamethrower', 'Third move': 'none',
                                  'Level': 2, 'Pokemon': 'Charmeleon'})
        expected = '2112, yyz$%^'
        self.assertEqual(actual, expected)
