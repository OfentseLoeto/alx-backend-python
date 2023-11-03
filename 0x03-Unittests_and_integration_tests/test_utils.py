#!/usr/bin/env python3
"""
Unit test for the access_nested_map function.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test for the access_nested_map function.

    This test class is designed to varify the correctness of
    the access_nested_map function by using parameterized test
    case. The function should return the expected results when
    given specific inputs.

    Test Cases:
        1. Test when the nested_map is a simple dictoionary
           with a single key.
        2. Test when the nested_map is a dictionary with nested
           dictionaries.
        3. Test when the path leads to a nested value within
           the dictionary
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map."),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map.")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)


if __name__ == '__main__':
    unittest.main()
