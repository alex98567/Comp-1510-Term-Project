from unittest import TestCase
from game import get_opponent_1
from unittest.mock import patch
from colorama import Style, Fore, init


init(autoreset=True)


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_get_opponent_1_water(self, _):
        actual = get_opponent_1()
        expected = {"Name": Fore.LIGHTBLUE_EX + "Magicarp" + Style.RESET_ALL, "Current HP": 25, "First move": "Splash"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_get_opponent_2_fire(self, _):
        actual = get_opponent_1()
        expected = {"Name": Fore.LIGHTRED_EX + "Growlithe" + Style.RESET_ALL, "Current HP": 25, "First move": "Roar"}
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_get_opponent_3_grass(self, _):
        actual = get_opponent_1()
        expected = {"Name": Fore.LIGHTGREEN_EX + "Caterpie" + Style.RESET_ALL, "Current HP": 25,
                    "First move": "String shot"}
        self.assertEqual(actual, expected)
