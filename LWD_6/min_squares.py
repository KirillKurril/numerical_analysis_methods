import numpy as np
import sympy as sp

def sum_of_pow(x_list, pow):
    n = x_list.shape[0]
    sum = 0
    for i in range(n):
        sum += np.power(x_list[i], pow)
    return sum


def sum_x_y_pows(x_list, y_list, pow):
    n = x_list.shape[0]
    sum = 0

    for i in range(n):
        sum += y_list[i] * np.power(x_list[i], pow)
    return sum


def min_square(x_list, y_list, m):
  
    
    n = x_list.shape[0]

    A = np.zeros(shape=(m+1, m+1))
    for i in range(m+1):
        for j in range(m+1):
            A[i, j] = sum_of_pow(x_list, i+j)

    b = np.zeros(shape=m + 1)
    for i in range(m+1):
        b[i] = sum_x_y_pows(x_list, y_list, i)

    a_vec = np.linalg.solve(A, b)
    return a_vec

def get_polynomial(x_list, y_list):
    a_vec = min_square(x_list, y_list, y_list.shape[0])
    x = sp.symbols('x')
    polynomial = 0
    for i in range(len(a_vec)):
        polynomial += a_vec[i] * x**i
    return polynomial

#https://www.youtube.com/watch?v=yBiM750v4Hk