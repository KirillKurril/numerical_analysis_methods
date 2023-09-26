from fractions import Fraction as fr
import numpy as np

def forward_move(M, mod_func, arr = None):
    row, col = M.shape

    for cur_col in range(col - 1):

        #print(f"\n\nstep{cur_col}\n")
        #print(M.astype(float))
        
        mod_func(M, cur_col, arr)
        #print(M.astype(float))

        if M[cur_col][cur_col] == 0:
            for r in range(cur_col, row):
                if M[r][cur_col] != 0:
                    M[r], M[cur_col] = M[cur_col].copy(), M[r].copy()
                    break
            
        deviser = M[cur_col][cur_col]

        for r in range(cur_col + 1, row):
            M[r] -= M[cur_col]*M[r][cur_col] / deviser
        # print(M.astype(float))
    
    return M

def backward_move(M, arr = None):
    row, col = M.shape

    solutions = np.zeros(col)

    for r in range(row - 1, -1, -1):
        obtained = np.dot(M[r, r + 1:], solutions[r + 1:])
        solutions[r] = (M[r][col - 1] - obtained) / M[r][r]

    if arr:
        resort(solutions, arr)

    return solutions[:col - 1]



def resort(solutions, arr):
    for i in range(len(solutions) - 1):
        swap = arr.index(i)
        a, b, c, d = solutions[swap], solutions[i], arr[swap], arr[i]
        solutions[i], solutions[swap], arr[i], arr[swap] = a, b, c, d


    