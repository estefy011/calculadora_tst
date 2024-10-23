from module1 import add_numbers
import unittest

# Dos líneas en blanco antes de la definición de clase


class TestAddNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(1, 2), 3)

# Dos líneas en blanco después de la definición de clase


if __name__ == '__main__':
    unittest.main()
