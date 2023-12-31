from sympy import symbols, sin, cos, sqrt
import numpy as np

k = 4
m = 0.2
a = 0.9

approx = (0.6, 0.6)
approx_2 = (0.05, -0.7)

x = symbols('x:2')
y_1 = sin(x[0]*x[1])
y_2 = cos(x[0] + x[1]) - (1/3)


def get_system():
    return np.array([
        [
            y_1,
            y_2
        ],
        [
            sin(x[0]*x[1]),
            cos(x[0] + x[1]) - (1/3)
        ]
    ])
