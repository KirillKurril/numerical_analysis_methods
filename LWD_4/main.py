from iteration_method import *
import task
from newton_method import *
import numpy as np


def print_list(ls, ):
    output = [el for el in ls]
    return output


system = task.get_system()
approx = task.approx

#print(np.linalg.solve(system[0], system[1]))
print(f"\n\nInitial approximation: {approx}")
iteration_ans = iteration_solve(system, approx, verbose=1)
print("Simple iteration:")
print(f"Roots: {print_list(iteration_ans[0])}")
print(f"Number of iterations: {iteration_ans[1]}")

print("\n\n\n")

print(f"Initial approximation: {approx}")
newton_ans = newton_solve(system[0], approx)
print("Newton method")
print(f"Roots: {print_list(newton_ans[0])}")
print(f"Number of iterations: {newton_ans[1]}")