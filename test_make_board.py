from unittest import TestCase
from game import make_board
from unittest.mock import patch


class Test(TestCase):
    @patch('random.choice', side_effect=[])
    def test_make_board_0_0(self, _):
        rows = 0
        columns = 0
        actual = make_board(rows, columns)
        expected = {}
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['Safe area'])
    def test_make_board_1_1(self, _):
        rows = 1
        columns = 1
        actual = make_board(rows, columns)
        expected = {(0, 0): 'Safe area'}
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['Safe area', 'Wild grass', 'Safe area', 'Wild grass'])
    def test_make_board_2_2(self, _):
        rows = 2
        columns = 2
        actual = make_board(rows, columns)
        expected = {(0, 0): 'Safe area', (0, 1): 'Wild grass', (1, 0): 'Safe area', (1, 1): 'Wild grass'}
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['Safe area', 'Wild grass', 'Safe area', 'Wild grass', 'Safe area',
                                         'Wild grass'])
    def test_make_board_2_3(self, _):
        rows = 2
        columns = 3
        actual = make_board(rows, columns)
        expected = {(0, 0): 'Safe area', (0, 1): 'Wild grass', (0, 2): 'Safe area',
                    (1, 0): 'Wild grass', (1, 1): 'Safe area', (1, 2): 'Wild grass'}
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['Safe area', 'Wild grass', 'Safe area', 'Wild grass', 'Safe area',
                                         'Wild grass'])
    def test_make_board_3_2(self, _):
        rows = 3
        columns = 2
        actual = make_board(rows, columns)
        expected = {(0, 0): 'Safe area', (0, 1): 'Wild grass', (1, 0): 'Safe area',
                    (1, 1): 'Wild grass', (2, 0): 'Safe area', (2, 1): 'Wild grass', }
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=['Safe area', 'Wild grass', 'Safe area', 'Wild grass', 'Safe area',
                                         'Wild grass', 'Wild grass', 'Safe area', 'Wild grass', 'Safe area',
                                         'Safe area', 'Wild grass', 'Pokecenter', 'Safe area', 'Safe area',
                                         'Wild grass', 'Safe area', 'Safe area', 'Wild grass', 'Safe area',
                                         'Safe area', 'Wild grass', 'Safe area', 'Wild grass', 'Safe area'])
    def test_make_board_5_5(self, _):
        rows = 5
        columns = 5
        actual = make_board(rows, columns)
        expected = {(0, 0): 'Safe area', (0, 1): 'Wild grass', (0, 2): 'Safe area', (0, 3): 'Wild grass',
                    (0, 4): 'Safe area', (1, 0): 'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area',
                    (1, 3): 'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                    (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area', (3, 0): 'Wild grass',
                    (3, 1): 'Safe area', (3, 2): 'Safe area', (3, 3): 'Wild grass', (3, 4): 'Safe area',
                    (4, 0): 'Safe area', (4, 1): 'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass',
                    (4, 4): 'Safe area'}
        self.assertEqual(actual, expected)
