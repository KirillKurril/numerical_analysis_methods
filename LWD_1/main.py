import initial_data as init
import gaussian_elimination_classic as gec
import gaussian_elimination_col_mod as gecm
import gaussian_elimination_full_matrix_mod as gefm

#M = init.test1()

#M = init.test2()

M = init.test3()
M = gec.forward_move(M, (lambda x, z: None))
c_solution = gec.backward_move(M)

print(c_solution)

M = init.get_initial_matrix()
M = gec.forward_move(M, (lambda x, z: None))
c_solution = gec.backward_move(M)

print(c_solution)

M = init.get_initial_matrix()
M = gec.forward_move(M, gecm.col_mod)
c_solution = gec.backward_move(M)


print(c_solution)


M = init.get_initial_matrix()
M = gec.forward_move(M, gefm.full_mod)
c_solution = gec.backward_move(M)


print(c_solution)
