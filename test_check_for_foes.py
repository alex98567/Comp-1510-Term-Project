from unittest import TestCase
from game import check_for_foes
from unittest.mock import patch


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_check_for_foes_1(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_check_for_foes_2(self, _):
        actual = check_for_foes()
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_check_for_foes_3(self, _):
        actual = check_for_foes()
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=4)
    def test_check_for_foes_4(self, _):
        actual = check_for_foes()
        expected = True
        self.assertEqual(actual, expected)
