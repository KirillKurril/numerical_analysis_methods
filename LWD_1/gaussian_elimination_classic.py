from fractions import Fraction as fr
import numpy as np

def forward_move(M):
    row, col = M.shape

    for i in range(row):
        if M[i][i] == 0:
            

    for j in range(5):
        for i in range(j + 1, 5):
            koef = matrix[i][j] / matrix[j][j]
            for q in range(j, 6):
                matrix[i][q] -= (matrix[j][q] * koef)

    for i in range(5):
        for j in range(6):
            print(f"{matrix[i][j]:10.5f}", end=' ')
        print()

    print()

    for i in range(4, -1, -1):
        total = matrix[i][5]

        for j in range(i + 1, 5):
            total -= matrix[i][j] * solutions[j]

        solutions[i] = total / matrix[i][i]

    for i in range(5):
        print(f"x[{i}] = {solutions[i]:10.5f}")
