from module2 import multiply_numbers
import unittest

# Asegúrate de que haya exactamente dos líneas en blanco aquí


class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

# Asegúrate de que haya exactamente dos líneas en blanco aquí también


if __name__ == '__main__':
    unittest.main()
