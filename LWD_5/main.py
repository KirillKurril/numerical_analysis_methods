import numpy as np
from jacobi_eigen_method import find_eigen
from staff import print_array, is_matrix_symmetric
from jacobi_staff import check_equal_dim
import task
import test

E = task.E
A = task.A

if not check_equal_dim(A):
        raise ValueError("Matrix isn't square")

if not is_matrix_symmetric(A, 0.000001):
    raise ValueError("Matrix isn't symmetrice")

if np.linalg.det(A) == 0: #вырожденные
    raise ValueError("Matrix is degenerate")

eig_val, eig_vec, steps = find_eigen(A, E, 0)

print(f'Default Matrix:\n{A}')

print(f'\nMatrix of Eigenvalues:\n{eig_val}')
print(f'Eigenvalues:\n{eig_val @ np.ones(shape=(eig_val.shape[0], ))}') 
print(f'Eigenvectors:\n{eig_vec}')


print("\nVerification:")

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)


