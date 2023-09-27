from fractions import Fraction as fr
import numpy as np

C = np.array([
        [fr(0.2), 0, fr(0.2), 0, 0],
        [0, fr(0.2), 0, fr(0.2), 0],
        [fr(0.2), 0, fr(0.2), 0, fr(0.2)],
        [0, fr(0.2), 0, fr(0.2), 0],
        [fr(0.2), 0, fr(0.2), 0, fr(0.2)]
    ])

D = np.array([
        [fr(2.33), fr(0.81), fr(0.67), fr(0.92), fr(-0.53)],
        [fr(-0.53), fr(2.33), fr(0.81), fr(0.67), fr(0.92)],
        [fr(0.92), fr(-0.53), fr(2.33), fr(0.81), fr(0.67)],
        [fr(0.67), fr(0.92), fr(-0.53), fr(2.33), fr(0.81)],
        [fr(0.81), fr(0.67), fr(0.92), fr(-0.53), fr(2.33)]
    ])

b = np.array([
        [fr(4.2)], 
        [fr(4.2)], 
        [fr(4.2)], 
        [fr(4.2)], 
        [fr(4.2)]
    ])

k = 5


def test1():
    M = np.array([
        [fr(2),fr(3)],
        [fr(4),fr(6)]
    ]) 

    B = np.array([
        [fr(7)], 
        [fr(14)]
    ])

    col = M.shape[0]
    M = np.transpose(M)
    for c in range(col):
        if all(i == 0 for i in M[c]):
            M = np.delete(M, c, axis = 0)
    M = np.transpose(M)

    M_ex = np.hstack((M,B))

    print(np.round(M_ex.astype(float), 4))

    if np.linalg.matrix_rank(M.astype(float)) != np.linalg.matrix_rank(M_ex.astype(float)):
        print("the matrix is inconsistent")
        exit(0)
    if np.linalg.matrix_rank(M.astype(float)) != len(M[0]):
        print("the matrix has an infinite number of solutions")
        exit(0)
    return M_ex



def test2():
    M = np.array([
        [2,3],
        [4,6]
    ]) 

    B = np.array([
        [7], 
        [12]
    ])

    col = M.shape[0]
    M = np.transpose(M)
    for c in range(col):
        if all(i == 0 for i in M[c]):
            M = np.delete(M, c, axis = 0)
    M = np.transpose(M)

    M_ex = np.hstack((M,B))

    print(np.round(M_ex.astype(float), 4))

    if np.linalg.matrix_rank(M.astype(float)) != np.linalg.matrix_rank(M_ex.astype(float)):
        print("the matrix is inconsistent")
        exit(0)
    if np.linalg.matrix_rank(M.astype(float)) != len(M[0]):
        print("the matrix has an infinite number of solutions")
        exit(0)
    return M_ex



def test3():
    M = np.array([
        [2.0,3.0],
        [4.0,-5.0]
    ]) 

    B = np.array([
        [7.0], 
        [-6.0]
    ])

    col = M.shape[0]
    M = np.transpose(M)
    for c in range(col):
        if all(i == 0 for i in M[c]):
            M = np.delete(M, c, axis = 0)
    M = np.transpose(M)

    M_ex = np.hstack((M,B))

    print(np.round(M_ex.astype(float), 4))

    if np.linalg.matrix_rank(M.astype(float)) != np.linalg.matrix_rank(M_ex.astype(float)):
        print("the matrix is inconsistent")
        exit(0)
    if np.linalg.matrix_rank(M.astype(float)) != len(M[0]):
        print("the matrix has an infinite number of solutions")
        exit(0)
    return M_ex

def get_initial_matrix():
    M = k*C + D 

    col = M.shape[0]
    M = np.transpose(M)
    for c in range(col):
        if all(i == 0 for i in M[c]):
            M = np.delete(M, c, axis = 0)
    M = np.transpose(M)

    M_ex = np.hstack((M,b))

    #print(np.round(M_ex.astype(float), 4))

    if np.linalg.matrix_rank(M.astype(float)) != np.linalg.matrix_rank(M_ex.astype(float)):
        print("the matrix is inconsistent")
        exit(0)
    if np.linalg.matrix_rank(M.astype(float)) != len(M[0]):
        print("the matrix has an infinite number of solutions")
        exit(0)
    return M_ex


