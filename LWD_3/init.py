from fractions import Fraction as fr
from sympy import Poly, symbols


x = symbols('x')

PRECISION = 1e-05 
interval = (fr(-10), fr(10))

a = fr(9.57496)
b = fr(-243.672)
c = fr(773.65)

def validity_check(y):
    if(y.degree() < 2):
        raise ValueError("Equation is not nonlinear")

    coefficients = y.all_coeffs()
    if dalambert_criterion(coefficients):
        print("\n\nWarning! The polynomial can have complex roots!\n\n")

def dalambert_criterion(coefficients):
    ratio1 = coefficients[-2] / coefficients[-1]
    ratio2 = coefficients[-3] / coefficients[-2]
    
    if ratio1 > 0 or ratio2 > 0:
        return False  # Полином не удовлетворяет критерию Даламбера
    else:
        return True  # Полином может иметь комплексные корни

def get_initial_values():
    y = x ** 3 + a * x ** 2 + b * x + c
   
    validity_check(Poly(y))

    return (y, interval)


#x^3 + 9.57496*x^2 + -243.672*x + 773.65