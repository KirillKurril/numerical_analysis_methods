from init import PRECISION

def check_accuracy(interval, my_roots, numpy_roots):
    numpy_roots = list(filter(lambda x: interval[0] <= x <= interval[1], numpy_roots))
    my_roots =  sorted(my_roots)
    for i in range(len(my_roots)):
        if (abs(numpy_roots[i] - my_roots[i])) >= PRECISION:
            return False
        else:
            print(f"|{numpy_roots[i]} - {my_roots[i]}| < {PRECISION}")
    return True
