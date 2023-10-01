import numpy as np
from initial_data import Accuracy as ac 
from initial_data import Limit_number_of_iterations as il
import secondary_functions as sf

def seidel(A, b):

    print("\n---------------------------Метод Зейделя---------------------------\n")

    n = A.shape[0]

    for i in range(n):

        if A[i, i] == 0.0:
            print("\nВозникла ошибка:\n"
                  + "Обнаружен нулевой диагональный элемент!\n")
            return sf.err(n)

    transition_matrix = sf.get_transition_matrix(A)

    if not (min(sf.Norms(transition_matrix)[:2]) < 1):
        print("Внимание: Метод Зейделя может расходится")

    x = np.zeros((n, 1))
    count = 0
    deltax = ac
    deltaf = ac

    print("\nПромежуточные результаты метода Зейделя:\n")

    while deltax + deltaf > ac:
        oldx = x.copy()

        for i in range(n):
            s = 0
            for j in range(n):
                s += A[i, j] * x[j]
            s -= b[i]
            x[i] = x[i] - s / A[i, i]

        deltax = np.absolute((x - oldx)).max()
        deltaf = np.absolute((A.dot(x) - b)).max()

        if not np.isfinite(deltax + deltaf) or count > il:
            print("\nВозникла ошибка:\n"
                  + f"Последовательность расходится\n")
            return sf.err(n)
        
        for cur in range(len(x)):
            print("%.4f" % x[cur, 0], end=", ")
        print()
        
        count += 1

    print("Количество итераций:", count)
    return x