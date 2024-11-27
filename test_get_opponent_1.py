from unittest import TestCase
from game import get_opponent_1
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_get_opponent_1_water(self, _):
        actual = get_opponent_1()
        expected = {"Name": "Magicarp", "Current HP": 25, "First move": "Splash"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_get_opponent_2_fire(self, _):
        actual = get_opponent_1()
        expected = {"Name": "Growlithe", "Current HP": 25, "First move": "Roar"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_get_opponent_3_grass(self, _):
        actual = get_opponent_1()
        expected = {"Name": "Caterpie", "Current HP": 25, "First move": "String shot"}
        self.assertEqual(actual, expected)
