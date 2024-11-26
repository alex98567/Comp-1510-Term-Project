from unittest import TestCase
from game import get_list_of_wild_grass


class Test(TestCase):
    def test_get_list_of_wild_grass_empty_0_0(self):
        actual = get_list_of_wild_grass({}, 0, 0)
        expected = []
        self.assertEqual(actual, expected)

    def test_get_list_of_wild_grass_none_2_2(self):
        actual = get_list_of_wild_grass({(0, 0): 'S', (0, 1): 'S', (1, 0): 'S', (1, 1): 'S'}, 2, 2)
        expected = []
        self.assertEqual(actual, expected)

    def test_get_list_of_wild_grass_2_2(self):
        actual = get_list_of_wild_grass({(0, 0): 'S', (0, 1): 'W', (1, 0): 'S', (1, 1): 'W'}, 2, 2)
        expected = [(0, 1), (1, 1)]
        self.assertEqual(actual, expected)

    def test_get_list_of_wild_grass_5_5(self):
        actual = get_list_of_wild_grass({(0, 0): 'S', (0, 1): 'W', (0, 2): 'S', (0, 3): 'W', (0, 4): 'W',
                                        (1, 0): 'S', (1, 1): 'W', (1, 2): 'S', (1, 3): 'S', (1, 4): 'S',
                                        (2, 0): 'W', (2, 1): 'S', (2, 2): 'P', (2, 3): 'W', (2, 4): 'S',
                                        (3, 0): 'S', (3, 1): 'S', (3, 2): 'W', (3, 3): 'S', (3, 4): 'W',
                                        (4, 0): 'W', (4, 1): 'W', (4, 2): 'S', (4, 3): 'W', (4, 4): 'S'},
                                        5, 5)
        expected = [(0, 1), (0, 3), (0, 4), (1, 1), (2, 0), (2, 3), (3, 2), (3, 4), (4, 0), (4, 1), (4, 3),]
        self.assertEqual(actual, expected)
