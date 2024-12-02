from unittest import TestCase
from game import describe_current_location


class Test(TestCase):
    def test_describe_current_location_0_0_fire_1(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 0, "Y-coordinate": 0,
                                           "Current HP": 50, "Current XP": 0, "First move": "Scratch",
                                                          "Second move": "none", "Third move": "none", "Level": 1,
                                                          "Pokemon": "Charmander"})
        expected = ('Charmander is currently located at space (0, 0)\nCurrent HP is 50\nCurrent level is 1\nCurrent XP '
                    'is 0\nFirst move is Scratch')
        self.assertEqual(actual, expected)

    def test_describe_current_location_3_2_fire_2(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 3, "Y-coordinate": 2,
                                           "Current HP": 100, "Current XP": 100, "First move": "Scratch",
                                                          "Second move": "Ember", "Third move": "none", "Level": 2,
                                                          "Pokemon": "Charmeleon"})
        expected = ('Charmeleon is currently at space (3, 2)\nCurrent HP is 100\nCurrent level is 2\nCurrent XP is '
                    '100\nFirst move is Scratch\nSecond move is Ember')
        self.assertEqual(actual, expected)

    def test_describe_current_location_2_3_fire_3(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 2, "Y-coordinate": 3,
                                           "Current HP": 150, "Current XP": 500, "First move": "Scratch",
                                                          "Second move": "Ember", "Third move": "Fire Blast", "Level":
                                                          3, "Pokemon": "Charizard"})
        expected = ('Charizard is currently located at space (2, 3)\nCurrent HP is 150\nCurrent level is 3\nCurrent XP '
                    'is 500\nFirst move is Scratch\nSecond move is Ember\nThird move is Fire Blast')
        self.assertEqual(actual, expected)

    def test_describe_current_location_2_2_grass_1(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 2, "Y-coordinate": 2,
                                           "Current HP": 50, "Current XP": 0, "First move": "Tackle",
                                                          "Second move": "none", "Third move": "none", "Level": 1,
                                                          "Pokemon": "Bulbasaur"})
        expected = ('Bulbasaur is currently located at space (2, 2)\nCurrent HP is 50\nCurrent level is 1\nCurrent XP '
                    'is 0\nFirst move is Tackle')
        self.assertEqual(actual, expected)

    def test_describe_current_location_1_4_grass_2(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 1, "Y-coordinate": 4,
                                           "Current HP": 100, "Current XP": 100, "First move": "Tackle",
                                                          "Second move": "Vine whip", "Third move": "none", "Level": 2,
                                                          "Pokemon": "Ivysaur"})
        expected = ('Ivysaur is currently at space (1, 4)\nCurrent HP is 100\nCurrent level is 2\nCurrent XP '
                    'is 100\nFirst move is Tackle\nSecond move is Vine whip')
        self.assertEqual(actual, expected)

    def test_describe_current_location_4_1_grass_3(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 4, "Y-coordinate": 1,
                                           "Current HP": 150, "Current XP": 500, "First move": "Tackle",
                                                          "Second move": "Vine whip", "Third move": "Solarbeam",
                                                          "Level": 3, "Pokemon": "Venasaur"})
        expected = ('Venasaur is currently located at space (4, 1)\nCurrent HP is 150\nCurrent level is 3\nCurrent XP '
                    'is 500\nFirst move is Tackle\nSecond move is Vine whip\nThird move is Solarbeam')
        self.assertEqual(actual, expected)

    def test_describe_current_location_4_4_water_1(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 4, "Y-coordinate": 4,
                                           "Current HP": 50, "Current XP": 0, "First move": "Bite",
                                                          "Second move": "none", "Third move": "none", "Level": 1,
                                                          "Pokemon": "Squirtle"})
        expected = ('Squirtle is currently located at space (4, 4)\nCurrent HP is 50\nCurrent level is 1\nCurrent XP '
                    'is 0\nFirst move is Bite')
        self.assertEqual(actual, expected)

    def test_describe_current_location_0_3_water_2(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 0, "Y-coordinate": 3,
                                           "Current HP": 100, "Current XP": 100, "First move": "Bite",
                                                          "Second move": "Water gun", "Third move": "none", "Level": 2,
                                                          "Pokemon": "Warturtle"})
        expected = ('Warturtle is currently at space (0, 3)\nCurrent HP is 100\nCurrent level is 2\nCurrent XP '
                    'is 100\nFirst move is Bite\nSecond move is Water gun')
        self.assertEqual(actual, expected)

    def test_describe_current_location_3_0_water_3(self):
        actual = describe_current_location(5, 5, {(0, 0): 'Safe area', (0, 1): 'Wild grass',
                                           (0, 2): 'Safe area', (0, 3): 'Wild grass', (0, 4): 'Safe area', (1, 0):
                                           'Wild grass', (1, 1): 'Wild grass', (1, 2): 'Safe area', (1, 3):
                                           'Wild grass', (1, 4): 'Safe area', (2, 0): 'Safe area', (2, 1): 'Wild grass',
                                           (2, 2): 'Pokecenter', (2, 3): 'Safe area', (2, 4): 'Safe area',
                                           (3, 0): 'Wild grass', (3, 1): 'Safe area', (3, 2): 'Safe area',
                                           (3, 3): 'Wild grass', (3, 4): 'Safe area', (4, 0): 'Safe area', (4, 1):
                                           'Wild grass', (4, 2): 'Safe area', (4, 3): 'Wild grass', (4, 4):
                                           'Safe area'}, {"X-coordinate": 3, "Y-coordinate": 0,
                                           "Current HP": 150, "Current XP": 500, "First move": "Bite",
                                                          "Second move": "Water gun", "Third move": "Hydro cannon",
                                                          "Level": 3, "Pokemon": "Blastoise"})
        expected = ('Blastoise is currently located at space (3, 0)\nCurrent HP is 150\nCurrent level is 3\nCurrent XP '
                    'is 500\nFirst move is Bite\nSecond move is Water gun\nThird move is Hydro cannon')
        self.assertEqual(actual, expected)
