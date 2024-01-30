#!/usr/bin/python3
"""Unnittest for max_integer(list = []):
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer function"""
    
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_integer_in_a_list(self)
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 10)

    def test_max_at_mid(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_big_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 20)
    
    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_zero_in_list(self):
        self.assertEqual([0, 0], 0]

    def test_character_in_list(self):
        with self_assertRaise(TypeError):
            max_integer([0, '8'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (70, 50)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key8': 8, 'key9': 9})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(3)
