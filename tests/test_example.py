# tests/test_example.py
import unittest
from src.example_module import add  # Corrected import path

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    # Add more tests for other functions or edge cases

if __name__ == '__main__':
    unittest.main()
