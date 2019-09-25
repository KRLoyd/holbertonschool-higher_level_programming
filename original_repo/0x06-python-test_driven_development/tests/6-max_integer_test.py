#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_int_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    @unittest.expectedFailure
    def test_mix_list(self):
        self.assertEqual(max_integer([a, 3, 4, 6]), "broken")

    @unittest.expectedFailure
    def test_mix_list2(self):
        self.assertEqual(max_integer(["b", 3, 4, 6]), "broken")

    def test_no_input(self):
        self.assertIsNone(max_integer())

    def test_empty_matrix(self):
        self.assertIsNone(max_integer([]))

    def test_list_is_only_none(self):
        self.assertIsNone(max_integer([None]))

    def test_boolean_matrix(self):
        self.assertEqual(max_integer([True, False, 1, 3, 2]), 3)

    @unittest.expectedFailure
    def test_str(self):
        self.assertEqual(max_integer("str"), "broken")

    @unittest.expectedFailure
    def test_str_in_list(self):
        self.assertEqual(max_integer([1, 'hi']), "broken")

    @unittest.expectedFailure
    def test_only_int(self):
        self.assertEqual(max_integer(100), "broken")

    @unittest.expectedFailure
    def test_only_float(self):
        self.assertEqual(max_integer(5.8), "broken")

    @unittest.expectedFailure
    def test_float_list(self):
        self.assertEqual(max_integer([5.8, 5.6, 3.4]), "broken")

    @unittest.expectedFailure
    def test_none_in_list(self):
        self.assertEqual(max_integer([-3, -87, None, -1]), "broken")

    def test_arge_number(self):
        self.assertEqual(max_integer([1000000000000000,
                         1, 3, 2]), 1000000000000000)

    @unittest.expectedFailure
    def test_list_is_neg(self):
        self.assertEqual(max_integer(-[-3, -87, 5, -1]), "broken")

    @unittest.expectedFailure
    def test_neg_boolean(self):
        self.assertEqual(max_integer([-True, -False, 5, -1]), "broken")

    @unittest.expectedFailure
    def test_just_boolean_f(self):
        self.assertEqual(max_integer(False))

    @unittest.expectedFailure
    def test_just_boolean_t(self):
        self.assertEqual(max_integer(True))

    @unittest.expectedFailure
    def test_list_of_nones(self):
        self.assertEqual(max_integer([None, None, None]))
