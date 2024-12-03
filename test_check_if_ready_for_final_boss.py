from unittest import TestCase
from game import check_if_ready_for_final_boss


class Test(TestCase):
    def test_check_if_ready_for_final_boss_False_2_2(self):
        actual = check_if_ready_for_final_boss({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 50,
                                                'Current XP': 0, 'First move': 'Scratch', 'Second move': 'none',
                                                'Third move': 'none', 'Level': 1, 'Pokemon': 'Charmander'},
                                               5, 5)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_ready_for_final_boss_True_2_2(self):
        actual = check_if_ready_for_final_boss({'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 150,
                                                'Current XP': 500, 'First move': 'Scratch', 'Second move': 'Ember',
                                                'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'},
                                               2, 2)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_if_ready_for_final_boss_False_4_3(self):
        actual = check_if_ready_for_final_boss({'X-coordinate': 4, 'Y-coordinate': 3, 'Current HP': 100,
                                                'Current XP': 0, 'First move': 'Scratch', 'Second move': 'Ember',
                                                'Third move': 'none', 'Level': 2, 'Pokemon': 'Charmeleon'},
                                               5, 5)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_ready_for_final_boss_False_4_4_499(self):
        actual = check_if_ready_for_final_boss({'X-coordinate': 4, 'Y-coordinate': 4, 'Current HP': 150,
                                                'Current XP': 499, 'First move': 'Scratch', 'Second move': 'Ember',
                                                'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'},
                                               5, 5)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_ready_for_final_boss_True_5_5_500(self):
        actual = check_if_ready_for_final_boss({'X-coordinate': 4, 'Y-coordinate': 4, 'Current HP': 150,
                                                'Current XP': 500, 'First move': 'Scratch', 'Second move': 'Ember',
                                                'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'},
                                               5, 5)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_if_ready_for_final_boss_True_5_5_501(self):
        actual = check_if_ready_for_final_boss({'X-coordinate': 4, 'Y-coordinate': 4, 'Current HP': 150,
                                                'Current XP': 501, 'First move': 'Scratch', 'Second move': 'Ember',
                                                'Third move': 'Fire blast', 'Level': 3, 'Pokemon': 'Charizard'},
                                               5, 5)
        expected = True
        self.assertEqual(actual, expected)
