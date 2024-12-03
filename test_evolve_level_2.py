from unittest import TestCase
from game import evolve_level_2, is_grass_2, is_fire_2, is_water_2, is_grass_1, is_fire_1, is_water_1
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_evolve_level_2_fire(self, _):
        actual = evolve_level_2({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 100,
                                 'First move': 'Scratch', 'Second move': 'none', 'Third move': 'none', 'Level': 1,
                                 'Pokemon': is_fire_1()})
        expected = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 100, 'Current XP': 100, 'First move': 'Scratch',
                    'Second move': 'Ember', 'Third move': 'none', 'Level': 2, 'Pokemon': is_fire_2()}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_evolve_level_2_water(self, _):
        actual = evolve_level_2({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 100,
                                 'First move': 'Bite', 'Second move': 'none', 'Third move': 'none', 'Level': 1,
                                 'Pokemon': is_water_1()})
        expected = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 100, 'Current XP': 100, 'First move': 'Bite',
                    'Second move': 'Water gun', 'Third move': 'none', 'Level': 2, 'Pokemon': is_water_2()}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_evolve_level_2_grass(self, _):
        actual = evolve_level_2({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 100,
                                 'First move': 'Tackle', 'Second move': 'none', 'Third move': 'none', 'Level': 1,
                                 'Pokemon': is_grass_1()})
        expected = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 100, 'Current XP': 100, 'First move': 'Tackle',
                    'Second move': 'Vine whip', 'Third move': 'none', 'Level': 2, 'Pokemon': is_grass_2()}
        self.assertEqual(actual, expected)
