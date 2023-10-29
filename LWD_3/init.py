from fractions import Fraction as fr
from sympy import Poly, symbols


x = symbols('x')

PRECISION = 1e-05 
interval = (fr(-10), fr(10))

a = fr(9.57496)
b = fr(-243.672)
c = fr(773.65)

test1 = x**2 + 4
test2 = 2*x
given = x ** 3 + a * x ** 2 + b * x + c

def validity_check(y):
    if(y.degree() < 2):
        raise Exception("Equation is not nonlinear")

    coefficients = y.all_coeffs()
    if dalambert_criterion(coefficients):
        print("\n\nWarning! The polynomial can have complex roots!\n\n")

def dalambert_criterion(coefficients):
    for i in range(len(coefficients) - 1):
        if coefficients[i] == 0 or coefficients[i + 1] == 0:
            return True  
        ratio = coefficients[i + 1] / coefficients[i]
        if ratio > 0:
            return True  
    return False
    
def get_initial_values():
    y = given
   
    validity_check(Poly(y))

    return (y, interval)


#x^3 + 9.57496*x^2 + -243.672*x + 773.65