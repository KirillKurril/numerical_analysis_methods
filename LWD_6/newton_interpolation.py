import numpy as np
from sympy import *


def get_a(x: list, y: list):
    a_table = np.zeros(shape=(len(y) - 1, len(y) - 1))
    n = a_table.shape[0]

    for i in range(n):
        a_table[0, i] = (y[i + 1] - y[i]) / (x[i+1] - x[i])     #разделенная разность

    for i in range(1, n):
        for j in range(n - i):
            a_table[i, j] = (a_table[i - 1, j + 1] - a_table[i - 1, j]) / (x[i+1+j] - x[j])

    return a_table


def newton_poly(x_list: list, y_list: list):
    if len(x_list) != len(y_list):
        raise TypeError("x and y must be same size")

    n = len(x_list)

    x = symbols('x')
    N = 0
    a_table = get_a(x_list, y_list)
    for i in range(n):
        if i == 0:
            N += y_list[0]
            continue
        x_poly = 1
        for j in range(i):
            x_poly *= (x-x_list[j])

        N += a_table[i-1, 0] * x_poly

    return N


#https://www.youtube.com/watch?v=B3p19JHfzQU