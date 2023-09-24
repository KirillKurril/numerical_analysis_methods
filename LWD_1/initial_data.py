from fractions import Fraction as fr
import numpy as np

C = np.array([
        [fr(0.2), 0, fr(0.2), 0, 0, 0],
        [0, fr(0.2), 0, fr(0.2), 0, 0],
        [fr(0.2), 0, fr(0.2), 0, fr(0.2), 0],
        [0, fr(0.2), 0, fr(0.2), 0, 0],
        [fr(0.2), 0, fr(0.2), 0, fr(0.2), 0]
    ])

D = np.array([
        [fr(2.33), fr(0.81), fr(0.67), fr(0.92), fr(-0.53), 0],
        [fr(-0.53), fr(2.33), fr(0.81), fr(0.67), fr(0.92), 0],
        [fr(0.92), fr(-0.53), fr(2.33), fr(0.81), fr(0.67), 0],
        [fr(0.67), fr(0.92), fr(-0.53), fr(2.33), fr(0.81), 0],
        [fr(0.81), fr(0.67), fr(0.92), fr(-0.53), fr(2.33), 0]
    ])

b = np.array([
        [fr(4.2)], 
        [fr(4.2)], 
        [fr(4.2)], 
        [fr(4.2)], 
        [fr(4.2)]
    ])

k = 5

def initialization_data_check(M):
    if np.linalg.det(M) == 0:
        return False
    


def get_initial_matrix():
    M = k*C + D 
    M_ex = np.hstack(M,b)
    if np.linalg.matrix_rank(M) != np.linalg.matrix_rank(M_ex):
        print("the matrix is inconsistent")
        exit(0)
    if np.linalg.matrix_rank(M) != len(M[0]):
        print("the matrix has an infinite number of solutions")
        exit(0)
    return M


