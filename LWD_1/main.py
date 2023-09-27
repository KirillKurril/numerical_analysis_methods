import initial_data as init
import gaussian_elimination_classic as gec
import gaussian_elimination_col_mod as gecm
import gaussian_elimination_full_matrix_mod as gefm
import numpy as np

#M = init.test1()

#M = init.test2()

M = init.test3()
M = gec.forward_move(M, (lambda x, y, z: None))
c_solution = gec.backward_move(M)

print(np.round(c_solution.astype(float), 4))

M = init.get_initial_matrix()
M = gec.forward_move(M, (lambda x, y, z: None))
c_solution = gec.backward_move(M)

print(c_solution.astype(float))
print(np.round(c_solution.astype(float), 4))

M = init.get_initial_matrix()
M = gec.forward_move(M, gecm.col_mod)
c_solution = gec.backward_move(M)

print(c_solution.astype(float))
print(np.round(c_solution.astype(float), 4))


M = init.get_initial_matrix()
arr = [i for i in range(M.shape[1] - 1)]
M = gec.forward_move(M, gefm.full_mod, arr)
c_solution = gec.backward_move(M, arr)

print(c_solution.astype(float))
print(np.round(c_solution.astype(float), 4))

