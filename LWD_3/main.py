import numpy as np
from init import get_initial_values, PRECISION, a, b, c
from sturm_algorithm import get_intervals
from bisection_method import bisection
from chord_method import chord
from newton_method import newton


def check_accuracy(interval, my_roots, numpy_roots):
    numpy_roots = sorted(list(filter(lambda x: interval[0] <= x <= interval[1], numpy_roots)))
    my_roots =  sorted(my_roots)
    for i in range(len(my_roots)):
        for j in range(3):
            if (abs(numpy_roots[i] - my_roots[i][j])) >= PRECISION:
                return False
            else:
                print(f"|{numpy_roots[i]} - {my_roots[i][j]}| < {PRECISION}")
        print('\n')
    return True

def main():
    y, full_interval = get_initial_values()

    print(f'Given equation:\ny = {y}\n')
    intervals = get_intervals(y, full_interval)
    print(f"\nElementary intervals: {[x for x in intervals]}\n")
    my_roots = []
    for interval in intervals:
        root_variations = []
        print(f'\nInterval: {interval}\n')

        bisection_root = bisection(y, interval)
        print(f'\t\tBisection method\n'
              f'Root:\n  {bisection_root[0]}\n'
              f'Iterations:\n  {bisection_root[1]}\n')
        root_variations.append(bisection_root[0])

        chord_root = chord(y, interval)
        print(f'\t\tSecant method\n'
              f'Root:\n  {chord_root[0]}\n'
              f'Iterations:\n  {chord_root[1]}\n')
        root_variations.append(chord_root[0])

        newton_root = newton(y, interval)
        print(f'\t\tNewton method\n'
              f'Root:\n  {newton_root[0]}\n'
              f'Iterations:\n  {newton_root[1]}\n')
        root_variations.append(newton_root[0])

        my_roots.append(root_variations)

    correct_roots = np.roots([1, a, b, c])
    print(f'\n\nLibrary method (Jacobi )\n'
          f'Roots: {correct_roots}\n')

    print(check_accuracy(full_interval, my_roots, correct_roots))

if __name__ == '__main__':
    main()
