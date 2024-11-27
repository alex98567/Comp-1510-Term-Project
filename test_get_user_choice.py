from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class Test(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_1(self, _):
        actual = get_user_choice()
        expected = "1"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_get_user_choice_2(self, _):
        actual = get_user_choice()
        expected = "2"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_choice_3(self, _):
        actual = get_user_choice()
        expected = "3"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_choice_4(self, _):
        actual = get_user_choice()
        expected = "4"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['5', '4'])
    def test_get_user_choice_5_4(self, _):
        actual = get_user_choice()
        expected = "4"
        self.assertEqual(actual, expected)
