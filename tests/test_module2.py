from module2 import multiply_numbers
import unittest

# Dos líneas en blanco antes de la definición de clase
class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply_numbers(2, 3), 6)

# Dos líneas en blanco después de la definición de clase
if __name__ == '__main__':
    unittest.main()
