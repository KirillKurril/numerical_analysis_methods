from sympy import lambdify
from init import x, PRECISION

def bisection(y, interval: tuple):
    f = lambdify(x, y)
    a, b = interval[0], interval[1]
    mid = (a + b) / 2

    if f(a) * f(b) > 0:
        raise Exception("An incorrect interval to be solved by bisection was passed"
                        "The boundaries of the interval to be solved by bisection must have different signs") 
    
    iteration = 1
    previous_value = abs(mid) + PRECISION * 2

    while abs(mid - previous_value) > PRECISION:
        if f(a) == 0:
            return a, iteration
        elif f(b) == 0:
            return b, iteration
        elif f(mid) == 0:
            return mid, iteration

        if f(a) * f(mid) < 0:
            b = mid
        elif f(b) * f(mid) < 0:
            a = mid

        previous_value = mid
        mid = (a + b) / 2
        iteration += 1

    return mid, iteration

