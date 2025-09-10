import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, -1), 1)
        self.assertEqual(calculator.multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calculator.divide(10, 0)


    def test_power(self):
        self.assertEqual(calculator.power(5, 2), 25)
        self.assertEqual(calculator.power(-5, 3), -125)
        self.assertEqual(calculator.power(-5, 2), 25)

    def test_squareroot(self):
        self.assertEqual(calculator.squareroot(25), 5)
        self.assertEqual(calculator.squareroot(100), 10)
        self.assertEqual(calculator.squareroot(81), 9)



if __name__ == "__main__":
    unittest.main()