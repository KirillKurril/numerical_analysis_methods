from fractions import Fraction as fr
import numpy as np
import copy

def full_mod(M, cur_col, arr = None):
    row, col = M.shape
    mr, mc = cur_col, cur_col

    print(arr)

    max = np.abs(M[cur_col][cur_col])
    for r in range(cur_col, row):
        for c in range(cur_col, col - 1):
            if np.abs(M[r][c]) > max:
                max = np.abs(M[r][c])
                mr, mc = r,c
    
    arr[cur_col], arr[mc] = arr[mc], arr[cur_col]

    M[mr], M[cur_col] = M[cur_col].copy(), M[mr].copy()

    M[:, [cur_col, mc]] = M[:, [mc, cur_col]]



                
