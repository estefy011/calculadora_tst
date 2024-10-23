from module1 import add_numbers
import unittest

# Debe haber exactamente dos líneas en blanco aquí


class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(1, 2), 3)

# Debe haber exactamente dos líneas en blanco aquí también


if __name__ == '__main__':
    unittest.main()
