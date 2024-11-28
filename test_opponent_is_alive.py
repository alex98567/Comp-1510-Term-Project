from unittest import TestCase
from game import opponent_is_alive


class Test(TestCase):
    def test_opponent_is_alive_True_25(self):
        actual = opponent_is_alive({'Name': 'Caterpie', 'Current HP': 25, 'First move': 'String shot'})
        expected = True
        self.assertEqual(actual, expected)

    def test_opponent_is_alive_True_12(self):
        actual = opponent_is_alive({'Name': 'Magicarp', 'Current HP': 12, 'First move': 'Splash'})
        expected = True
        self.assertEqual(actual, expected)

    def test_opponent_is_alive_True_1(self):
        actual = opponent_is_alive({'Name': 'Growlithe', 'Current HP': 12, 'First move': 'Roar'})
        expected = True
        self.assertEqual(actual, expected)

    def test_opponent_is_alive_False_0(self):
        actual = opponent_is_alive({'Name': 'Growlithe', 'Current HP': 0, 'First move': 'Roar'})
        expected = False
        self.assertEqual(actual, expected)

    def test_opponent_is_alive_False_negative(self):
        actual = opponent_is_alive({'Name': 'Growlithe', 'Current HP': -1, 'First move': 'Roar'})
        expected = False
        self.assertEqual(actual, expected)
