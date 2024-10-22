from module1 import add_numbers
import unittest

class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
