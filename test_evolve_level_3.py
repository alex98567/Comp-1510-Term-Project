from unittest import TestCase
from game import evolve_level_3, is_grass_2, is_fire_2, is_water_2, is_grass_3, is_fire_3, is_water_3
from unittest.mock import patch


class Test(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_evolve_level_3_fire(self, _):
        actual = evolve_level_3({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 400,
                                 'First move': 'Scratch', 'Second move': 'Ember', 'Third move': 'none', 'Level': 2,
                                 'Pokemon': is_fire_2()})
        expected = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 150, 'Current XP': 400, 'First move': 'Scratch',
                    'Second move': 'Ember', 'Third move': 'Fire blast', 'Level': 3, 'Pokemon': is_fire_3()}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_evolve_level_3_water(self, _):
        actual = evolve_level_3({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 400,
                                 'First move': 'Bite', 'Second move': 'Water gun', 'Third move': 'none', 'Level': 2,
                                 'Pokemon': is_water_2()})
        expected = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 150, 'Current XP': 400, 'First move': 'Bite',
                    'Second move': 'Water gun', 'Third move': 'Hydro pump', 'Level': 3, 'Pokemon': is_water_3()}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_evolve_level_3_grass(self, _):
        actual = evolve_level_3({'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 33, 'Current XP': 400,
                                 'First move': 'Tackle', 'Second move': 'Vine whip', 'Third move': 'none', 'Level': 1,
                                 'Pokemon': is_grass_2()})
        expected = {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 150, 'Current XP': 400, 'First move': 'Tackle',
                    'Second move': 'Vine whip', 'Third move': 'Solarbeam', 'Level': 3, 'Pokemon': is_grass_3()}
        self.assertEqual(actual, expected)
