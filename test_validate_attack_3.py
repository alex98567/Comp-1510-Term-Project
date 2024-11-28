from unittest import TestCase
from game import validate_attack_3


class Test(TestCase):
    def test_validate_attack_3_false_1(self):
        actual = validate_attack_3('1')
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_attack_3_false_2(self):
        actual = validate_attack_3('2')
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_attack_3_true(self):
        actual = validate_attack_3('3')
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_attack_3_false_4(self):
        actual = validate_attack_3('4')
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_attack_3_false_string(self):
        actual = validate_attack_3('string')
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_attack_3_false_mix(self):
        actual = validate_attack_3('2112. yyz$%^')
        expected = False
        self.assertEqual(actual, expected)
