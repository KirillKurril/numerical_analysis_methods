from simple_iteration import simple_iteration as simp
from seidel import seidel as sd
import secondary_functions as sf
import numpy as np
import initial_data as init

np.seterr(over="ignore")

print("\nВходные данные варианта 5\n")
sf.test(simp, init.get_initial_matrix)
sf.test(sd, init.get_initial_matrix)

print("\nВходные данные теста 1\n")
sf.test(simp, init.test1)
sf.test(sd, init.test1)

print("\nВходные данные теста 2\n")
sf.test(simp, init.test2)
sf.test(sd, init.test2)

print("\nВходные данные теста 3\n")
sf.test(simp, init.test3)
sf.test(sd, init.test3)



