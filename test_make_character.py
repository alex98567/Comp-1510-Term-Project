from unittest import TestCase
from game import make_character
from unittest.mock import patch
from game import is_fire_1
from game import is_water_1
from game import is_grass_1


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_make_character_fire(self, _):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "First move": "Scratch",
                    "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_fire_1()}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_make_character_water(self, _):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "First move": "Bite",
                    "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_water_1()}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_make_character_grass(self, _):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "First move": "Tackle",
                    "Second move": "none", "Third move": "none", "Level": 1, "Pokemon": is_grass_1()}
        self.assertEqual(actual, expected)
