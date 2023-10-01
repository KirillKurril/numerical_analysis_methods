import numpy
from initial_data import Accuracy as ac 
import secondary_functions as sf
from initial_data import Limit_number_of_iterations as il


def simple_iteration(A, b):

    print("\n---------------------------Метод простых итераций---------------------------\n")

    n = A.shape[0]

    for i in range(n):
        if A[i, i] == 0.0:
            print("\nВозникла ошибка:\n"
                  + "Обнаружен нулевой диагональный элемент!\n")
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

    print("\nПромежуточные результаты метода простого итерирования:\n")
    
    while deltax + deltaf >= ac:

        oldx = x
        x = initial_solution  + transition_matrix.dot(x)
        deltax = numpy.absolute((x - oldx)).max()
        deltaf = numpy.absolute((A.dot(x) - b)).max()
        
        if not numpy.isfinite(deltax + deltaf) or count > il:
            print("\nВозникла ошибка:\n"
                  + f"Последовательность расходится\n")
            return sf.err(n)
        
        for cur in range(len(x)):
            print("%.4f" % x[cur, 0], end=", ")
        print()
        
        count += 1
    print("Количество итераций:", count)

    return x