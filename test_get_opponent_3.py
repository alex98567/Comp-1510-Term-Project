from unittest import TestCase
from game import get_opponent_3
from unittest.mock import patch
from colorama import Style, Fore, init


init(autoreset=True)


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_get_opponent_3_water(self, _):
        actual = get_opponent_3()
        expected = {"Name": Fore.LIGHTBLUE_EX + "Kyogre" + Style.RESET_ALL, "Current HP": 100, "First move": "Surf"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_get_opponent_3_fire(self, _):
        actual = get_opponent_3()
        expected = {"Name": Fore.LIGHTRED_EX + "Entei" + Style.RESET_ALL, "Current HP": 100, "First move":
                    "Flamethrower"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_get_opponent_3_grass(self, _):
        actual = get_opponent_3()
        expected = {"Name": Fore.LIGHTGREEN_EX + "Groudon" + Style.RESET_ALL, "Current HP": 100, "First move":
                    "Frenzy plant"}
        self.assertEqual(actual, expected)
