import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, 2), 1)
        self.assertEqual(self.calc.add(1, -2), -1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, -1), 2)
    
    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(-1, 0), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    
    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 5), 4)
        self.assertEqual(self.calc.divide(2, 5), 0)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(20, -5), -4)
        self.assertEqual(self.calc.divide(-20, 5), -4)
        self.assertEqual(self.calc.divide(-20, -5), 4)

    def test_divide_zero(self):
        self.assertEqual(self.calc.divide(0, 0), "Cannot divide by zero")
        self.assertEqual(self.calc.divide(5, 0), "Cannot divide by zero")
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(17, 5), 2)

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(17, -5), 2)
        self.assertEqual(self.calc.modulo(5, -17), 5)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(0, 0),"Cannot mod by zero")
        self.assertEqual(self.calc.modulo(5, 0),"Cannot mod by zero")
        self.assertEqual(self.calc.modulo(-5, 0),"Cannot mod by zero") 

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()