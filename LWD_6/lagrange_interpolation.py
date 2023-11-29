from sympy import symbols


def lagrange_l(x_list: list, x_cur):
    x = symbols('x')
    lg = 1
    n = len(x_list)
    for i in range(n):
        if x_cur == x_list[i]:
            continue
        lg *= (x - x_list[i]) / (x_cur - x_list[i])
    return lg


def lagrange_poly(x, y):
    if len(x) != len(y):
        raise ValueError("x and y are not same length")
    n = len(x)

    L = 0
    for i in range(n):
        L += y[i] * lagrange_l(x, x[i])
    return L


#https://www.youtube.com/watch?v=wHFqvpzCb-c