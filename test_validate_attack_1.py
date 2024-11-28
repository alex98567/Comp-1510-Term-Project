from unittest import TestCase
from game import validate_attack_1


class Test(TestCase):
    def test_validate_attack_1_true(self):
        actual = validate_attack_1('1')
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_attack_1_false_2(self):
        actual = validate_attack_1('2')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_1_false_3(self):
        actual = validate_attack_1('3')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_1_false_4(self):
        actual = validate_attack_1('4')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_1_false_word(self):
        actual = validate_attack_1('string')
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_attack_1_false_mix(self):
        actual = validate_attack_1('1! 2, 1')
        expected = False
        self.assertEqual(expected, actual)
