import numpy as np
import initial_data as init
from fractions import Fraction as fr


def err(n):
    v = np.zeros((n, 1))
    v[:] = np.NaN
    return v

def Norms(A):
    n = A.shape[0]
    f = max(np.absolute(A[i]).sum() for i in range(n))
    s = max(np.absolute(A.T[j]).sum() for j in range(n))
    t = ((A**2).sum()) ** (1 / 2)
    return (f, s, t)

def get_transition_matrix(A):
    n = A.shape[0]
    alpha = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            alpha[i, j] = -A[i, j] / A[i, i]
        alpha[i, i] = 0
    return alpha

def output(A, x, b):
    np.set_printoptions(suppress=True, precision=6, floatmode="fixed")
    print(f"A = \n{A}\n"
         + f"b = \n{b.T}\n"
         + f"x = \n{x.T}\n")
    if not np.isnan(x).any():
            print(f"Проверка: b = \n{b.T}\n{A.dot(x).T}")




def test(method, initial):
    (A, b) = initial()
    x = method(A.copy(), b.copy())
    output(A, x, b)
