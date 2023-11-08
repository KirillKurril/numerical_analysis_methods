from sympy import lambdify, diff
from init import x, PRECISION
import random

def get_initial_x(y, y_0, interval):
    dy_2 = lambdify(x, diff(diff(y, x), x))
    rand_val = random.uniform(interval[0], interval[1])
    counter = 5000
    while(counter):
        if(y_0(rand_val)*dy_2(rand_val) > 0):
            break
        rand_val = random.uniform(interval[0], interval[1])
        counter -= 1
    return rand_val
    

def newton(y, interval):
    a, b = interval[0], interval[1]
    f = lambdify(x, y)
    f_diff = lambdify(x, diff(y))

    if f(a) * f(b) > 0:
        raise Exception("An incorrect interval to be solved by newton method was passed"
                        "The boundaries of the interval to be solved by bisection must have different signs") 

    x_start = get_initial_x(y, f, interval)
    previous_value = abs(x_start) + PRECISION * 2
    x_newton = x_start - f(x_start) / f_diff(x_start)
    
    iteration = 1
    while abs(x_newton - previous_value) >= PRECISION:
        if f(x_newton) == 0:
            return x_newton, iteration

        previous_value = x_newton
        x_newton = x_newton - f(x_newton) / f_diff(x_newton)
        iteration += 1

    return x_newton, iteration