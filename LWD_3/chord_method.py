from sympy import lambdify
from init import x, PRECISION

def chord(y, interval: tuple):
    a, b = interval[0], interval[1]
    f = lambdify(x, y)

    if f(a) * f(b) > 0:
        raise Exception("An incorrect interval to be solved by chord method was passed"
                        "The boundaries of the interval to be solved by bisection must have different signs") 

    x_sec = a - (f(a) * (b - a)) / (f(b) - f(a))

    previous_value = abs(x_sec) + PRECISION * 2
    iteration = 1
    while abs(x_sec - previous_value) > PRECISION:
        if f(a) == 0:
            return a, iteration
        elif f(b) == 0:
            return b, iteration
        elif f(x_sec) == 0:
            return x_sec, iteration

        if f(a) * f(x_sec) < 0:
            b = x_sec
        elif f(x_sec) * f(b) < 0:
            a = x_sec

        previous_value = x_sec
        x_sec = a - (f(a) * (b - a)) / (f(b) - f(a))
        iteration += 1

    return x_sec, iteration

