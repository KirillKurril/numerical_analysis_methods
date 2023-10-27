import sturm_algorithm
import init

equation, interval = init.get_condition_init()
print(sturm_algorithm.sturm(equation, interval))