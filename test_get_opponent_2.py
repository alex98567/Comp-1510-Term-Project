from unittest import TestCase
from game import get_opponent_2
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_get_opponent_2_water(self, _):
        actual = get_opponent_2()
        expected = {"Name": "Vaporeon", "Current HP": 60, "First move": "Bubble"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_get_opponent_2_fire(self, _):
        actual = get_opponent_2()
        expected = {"Name": "Flareon", "Current HP": 60, "First move": "Blast burn"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_get_opponent_2_grass(self, _):
        actual = get_opponent_2()
        expected = {"Name": "Leafeon", "Current HP": 60, "First move": "Razor leaf"}
        self.assertEqual(actual, expected)
