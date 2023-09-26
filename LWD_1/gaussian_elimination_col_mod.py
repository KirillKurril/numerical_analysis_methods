from fractions import Fraction as fr
import numpy as np

def col_mod(M, cur_col, arr):
    pivot = np.argmax(np.abs(M[cur_col:, cur_col])) + cur_col
    M[pivot], M[cur_col] = M[cur_col].copy(), M[pivot].copy()
    