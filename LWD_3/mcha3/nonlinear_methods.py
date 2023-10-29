from sympy import symbols, lambdify, diff
import random

x = symbols('x')
PRECISION = 1e-05



def bisection(y, interval: tuple):
   
    f = lambdify(x, y)
    a, b = interval[0], interval[1]
    mid = (a + b) / 2

    if f(a) * f(b) > 0:
        raise Exception("An incorrect interval to be solved by bisection was passed"
                        "The boundaries of the interval to be solved by bisection must have different signs") 
    
    iteration = 1
    previous_value = mid + PRECISION * 2

    while abs(mid - previous_value) >= PRECISION:
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

def chord(y, interval: tuple):
    a, b = interval[0], interval[1]
    f = lambdify(x, y)

    if f(a) * f(b) > 0:
        raise Exception("An incorrect interval to be solved by chord method was passed"
                        "The boundaries of the interval to be solved by bisection must have different signs") 

    x_sec = a - (f(a) * (b - a)) / (f(b) - f(a))

    previous_value = abs(x_sec) + PRECISION * 2
    iteration = 1
    while abs(x_sec - previous_value) >= PRECISION:
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




def get_initial_x(y, y_0, interval):
    dy_2 = lambdify(x, diff(y, x, 2))
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
    while abs(x_newton - previous_value) > PRECISION:
        if f(x_newton) == 0:
            return x_newton, iteration

        previous_value = x_newton
        x_newton = x_newton - f(x_newton) / f_diff(x_newton)
        iteration += 1

    return x_newton, iteration
