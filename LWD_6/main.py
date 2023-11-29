from min_squares import get_polynomial
from lagrange_interpolation import lagrange_poly
from newton_interpolation import newton_poly
import task
import numpy as np
from sympy import symbols, Poly
from scipy.interpolate import interp1d
from test import estimate_interpolation_error

x = task.x
y = task.y
point = task.point

x_var = symbols('x')

newton = newton_poly(x, y)
lagrange = lagrange_poly(x, y)

print(f'\tLagrange:\nL(x) = {lagrange}')
print(f'Interpolation point: x = {point}\n')
print(f'Lagrange poly result on x = {point}:\n{float(lagrange.subs(x_var, point))}')
print(f'\tNewton interpolation polynomial:\nN(x) = {newton}')
print(f'Interpolation point: x = {point}')
print(f'Newton poly result on x = {point}:\n{float(newton.subs(x_var, point))}')

lsm = get_polynomial(x, y)
print(lsm)
print(f'Polynomial of best approximation(least squares poly) result on x = {point}')
print(float(lsm.subs(x_var, point)))


# error = estimate_interpolation_error(Poly(lagrange, x_var), x, y)
# print(error)

# error = estimate_interpolation_error(Poly(newton, x_var), x, y)
# print(error)

# error = estimate_interpolation_error(Poly(lsm, x_var), x, y)
# print(error)
#print(np.interp(point, x, y))


