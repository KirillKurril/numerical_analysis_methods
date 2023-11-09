import numpy as np
from jacobi_eigen_method import find_eigen
from staff import print_array, is_matrix_symmetric
import task
import test

E = task.E
A = test.A_1

if not is_matrix_symmetric(A, 0.000001):
    print("Matrix not symmetric")
    exit(0)

if np.linalg.det(A) == 0:
    print("Matrix is degenerate")
    exit(0)

eig_val, eig_vec, steps = find_eigen(A, E, 0)

print_array(A, 'Default Matrix:')
print_array(eig_val, '\nMatrix of Eigenvalues:')
print_array(eig_val @ np.ones(shape=(eig_val.shape[0], )), 'Eigenvalues:') 
print_array(eig_vec, 'Eigenvectors:')


print("\nVerification:")

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)


