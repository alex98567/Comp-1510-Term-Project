from unittest import TestCase
from game import validate_attack_2


class Test(TestCase):
    def test_validate_attack_2_false_1(self):
        actual = validate_attack_2('1')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_2_true(self):
        actual = validate_attack_2('2')
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_attack_2_false_3(self):
        actual = validate_attack_2('3')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_2_false_4(self):
        actual = validate_attack_2('4')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_2_false_word(self):
        actual = validate_attack_2('string')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_2_false_mix(self):
        actual = validate_attack_2('1! 2, 1')
        expected = False
        self.assertEqual(expected, actual)
