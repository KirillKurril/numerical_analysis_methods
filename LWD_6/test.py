from math import factorial
from sympy import symbols, Poly, diff

def estimate_interpolation_error(poly, x, y):
    x_var = symbols('x')
    n = len(x) - 1
    M = max(abs(diff(poly, x_var).subs(x_var, x_i)) for x_i in x)  # Максимальное значение производной

    product_term = 1.0
    for x_i in x:
        product_term *= abs(poly - x_i)

    error_estimate = M / factorial(n + 1) * product_term
    return float(error_estimate)




