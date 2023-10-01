import numpy as np

Accuracy = 1e-4

Limit_number_of_iterations = 50

C = np.array([
        [0.01, 0, -0.02, 0, 0],
        [0.01, 0.01, -0.02, 0, 0],
        [0, 0.01, 0.01, 0, -0.02],
        [0, 0, 0.01, 0.01, 0],
        [0, 0, 0, 0.01, 0.01]
    ])

D = np.array([
       
        [1.33, 0.21, 0.17, 0.12, -0.13],
        [-0.13, -1.33, 0.11, 0.17, 0.12],
        [0.12, -0.13, -1.33, 0.11, 0.17],
        [0.17, 0.12, -0.13, -1.33, 0.11],
        [0.11, 0.67, 0.12, -0.13, -1.33]
    ])

b = np.array([
        [1.2],
        [2.2],
        [4.0],
        [0.0],
        [-1.2]
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
