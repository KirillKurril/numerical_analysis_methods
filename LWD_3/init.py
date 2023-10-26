from fractions import Fraction as fr
from sympy import symbols

interval = (-10, 10)

a = fr(9.57496)
b = fr(-243.672)
c = fr(773.65)

x = symbols('x')
y = x ** 3 + a * x ** 2 + b * x + c
