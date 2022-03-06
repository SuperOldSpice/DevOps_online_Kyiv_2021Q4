import math

class square_equation:
    def discriminant( a, b, c):
        d = pow(b, 2) - 4 * a * c 
        return d 

    def roots(a, b, c):
        x1 = (-1 * b - square_equation.solv_square(a, b, c)) / 2 / a
        x2 = (-1 * b + square_equation.solv_square(a, b, c)) / 2 / a
        return x1, x2

    def solv_square(a, b, c):
        return math.sqrt(square_equation.discriminant(a, b, c))

    def square_print(a, b, c , roots):
        x1, x2 = roots(a, b, c)
        return (f'{a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0 \nx1 = {x1} and x2 = {x2}')