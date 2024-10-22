from module2 import multiply_numbers
import unittest

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
