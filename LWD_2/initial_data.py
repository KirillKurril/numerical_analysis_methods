import numpy as np
from fractions import Fraction as fr

Accuracy = 1e-5

Limit_number_of_iterations = 50

C = np.array([
        [(0.2), 0, (0.2), 0, 0],
        [0, (0.2), 0, (0.2), 0],
        [(0.2), 0, (0.2), 0, (0.2)],
        [0, (0.2), 0, (0.2), 0],
        [(0.2), 0, (0.2), 0, (0.2)]
    ])

D = np.array([
        [(2.33), (0.81), (0.67), (0.92), (-0.53)],
        [(-0.53), (2.33), (0.81), (0.67), (0.92)],
        [(0.92), (-0.53), (2.33), (0.81), (0.67)],
        [(0.67), (0.92), (-0.53), (2.33), (0.81)],
        [(0.81), (0.67), (0.92), (-0.53), (2.33)]
    ])

b = np.array([
        [(4.2)], 
        [(4.2)], 
        [(4.2)], 
        [(4.2)], 
        [(4.2)]
    ])

k = 5

def test1(): #Ошибка из-за нулевого диагонального элемента
    M = np.array([
        [0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8]
    ]) 

    B = np.array([
        [1], 
        [2],
        [3]
    ])

    return (M, B)


def test2(): #Потенциальная расходимость итерационного процесса
    M = np.array([
        [2, 1, 1], 
        [1, 2, 1], 
        [1, 1, 2]
    ]) 

    B = np.array([
        [1], 
        [2],
        [3]
    ])

    return (M, B)

def test3(): #Ошибка из-за расходимости последовательности
    M = np.array([
        [1, 2, 3],
        [4, 5, 6], 
        [7, 8, 9]
    ]) 

    B = np.array([
        [1], 
        [2],
        [3]
    ])

    return (M, B)

def test4():
    M = np.array([
        [(2),(3)],
        [(4),(6)]
    ]) 

    B = np.array([
        [(7)], 
        [(14)]
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



def test5():
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



def test6():
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

    if np.linalg.matrix_rank(M) != np.linalg.matrix_rank(M_ex):
        print("the matrix is inconsistent")
        exit(0)
    if np.linalg.matrix_rank(M) != len(M[0]):
        print("the matrix has an infinite number of solutions")
        exit(0)
    return (M, b)
