import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map(self):
        nested_map = {"a": {"b": {"c": 1}}}
                            
        # Test a valid path
        result = access_nested_map(nested_map, ["a", "b", "c"])
        self.assertEqual(result, 1)

        # Test an invalid path
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, ["x", "y", "z"])

if __name__ == '__main__':
    unittest.main()

