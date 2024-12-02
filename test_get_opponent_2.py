from unittest import TestCase
from game import get_opponent_2
from unittest.mock import patch
from colorama import Style, init, Fore


init(autoreset=True)


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_get_opponent_2_water(self, _):
        actual = get_opponent_2()
        expected = {"Name": Fore.LIGHTBLUE_EX + "Vaporeon" + Style.RESET_ALL, "Current HP": 60, "First move": "Bubble"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_get_opponent_2_fire(self, _):
        actual = get_opponent_2()
        expected = {"Name": Fore.LIGHTRED_EX + "Flareon" + Style.RESET_ALL, "Current HP": 60, "First move":
                    "Blast burn"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_get_opponent_2_grass(self, _):
        actual = get_opponent_2()
        expected = {"Name": Fore.LIGHTGREEN_EX + "Leafeon" + Style.RESET_ALL, "Current HP": 60, "First move":
                    "Razor leaf"}
        self.assertEqual(actual, expected)
