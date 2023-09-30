import numpy as np
from initial_data import Accuracy as ac 
import secondary_functions as sf

def seidel(A, b):
    n = A.shape[0]
    for i in range(n):

        if A[i, i] == 0.0:
            print("Возникла ошибка:\n"
                  + "Обнаружен нулевой диагональный элемент!")
            return sf.err(n)

    transition_matrix = sf.get_transition_matrix(A)

    if not (min(sf.Norms(transition_matrix)[:2]) < 1):
        print("Внимание: Метод Зейделя может расходится")

    x = np.zeros((n, 1))
    count = 0
    deltax = ac
    deltaf = ac

    print("\n---------------------------Метод Зейделя---------------------------\n")
    print("Промежуточные результаты метода Зейделя:\n")

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

        if not np.isfinite(deltax + deltaf):
            print("Возникла ошибка:\n"
                  + f"Последовательность {x} расходится")
            return sf.err(n)
        
        for cur in range(len(x)):
            print("%.4f" % x[cur, 0], end=", ")
        print()
        
        count += 1

    print("Количество итераций:", count)
    return x