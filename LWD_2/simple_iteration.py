import numpy
from initial_data import Accuracy as ac 
import secondary_functions as sf


def simple_iteration(A, b):

    n = A.shape[0]

    for i in range(n):
        if A[i, i] == 0.0:
            print("Возникла ошибка:\n"
                  + "Обнаружен нулевой диагональный элемент!")
            return sf.err(n)

    transition_matrix = sf.get_transition_matrix(A)

    if not (min(sf.Norms(transition_matrix)) < 1):
        print("Возникла потенциальная расходимость итерационного процесса:\n||B|| >= 1.")

    initial_solution  = numpy.zeros((n, 1))
    for i in range(n):
        initial_solution [i] = b[i] / A[i, i]

    x = numpy.zeros((n, 1))
    count = 0
    deltax = ac
    deltaf = ac

    print("\n---------------------------Метод простых итераций---------------------------\n")
    print("Промежуточные результаты метода простого итерирования:\n")
    
    while deltax + deltaf > ac:

        oldx = x
        x = initial_solution  + transition_matrix.dot(x)
        deltax = numpy.absolute((x - oldx)).max()
        deltaf = numpy.absolute((A.dot(x) - b)).max()
        
        if not numpy.isfinite(deltax + deltaf):
            print("Возникла ошибка:\n"
                  + f"Последовательность {x} расходится")
            return sf.err(n)
        
        for cur in range(len(x)):
            print("%.4f" % x[cur, 0], end=", ")
        print()
        
        count += 1
    print("Количество итераций:", count)

    return x