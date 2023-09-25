from fractions import Fraction as fr
import numpy as np
import copy

def full_mod(m, cur_col):
    M = copy.deepcopy(m)
    n = M.shape[0]

    max_val = 0.0
    max_row = -1
    max_col = -1

    for i in range(cur_col, n):
        for j in range(n):
            if abs(M[i][j]) > max_val:
                max_val = abs(M[i][j])
                max_row = i
                max_col = j

        # Переставляем строки и столбцы, чтобы максимальный элемент был на диагонали
    M[[cur_col, max_row]] = M[[max_row, cur_col]]
    M[:, [cur_col, max_col]] = M[:, [max_col, cur_col]]
