#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_normal_list(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -2, -8]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_string_list(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_mixed_type_list(self):
        """Test with a list of mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3])


if __name__ == '__main__':
    unittest.main()
