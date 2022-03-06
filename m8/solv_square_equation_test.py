import unittest
import square_equation_lib

class square_equation_test(unittest.TestCase):
    
    def test_discriminant(self):
        a, b, c = 4, 5, 1
        result = square_equation_lib.square_equation.discriminant(a, b, c)
        self.assertEqual(result, 9)

    def test_solv_square(self):
        a, b, c = 4, 5, 1
        result = square_equation_lib.square_equation.solv_square(a, b, c)
        self.assertEqual(result, 3)

    def test_roots(self):
        a, b, c = 4, 5, 1
        result = square_equation_lib.square_equation.roots(a, b, c)
        self.assertEqual(result, (-1, -0.25))

    def test_dividebyzero(self):
        a, b, c = 0, 5, 1
        try:
            result = square_equation_lib.square_equation.roots(a, b, c)
        except ZeroDivisionError:
            result = "ZeroDivisionError"
        self.assertEqual(result, "ZeroDivisionError")

if __name__ == '__main__':
    unittest.main()


