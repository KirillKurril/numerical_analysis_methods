from init import x
import init

def get_sturm_row(y):
    sturm_row = []
    sturm_row.append(y)
    sturm_row.append(y.diff(x))
    n = 2
    while(sturm_row[n - 1].degree() != 0):
        reminder = - sturm_row[n - 2] % sturm_row[n - 1]
        sturm_row.append(reminder)
    return sturm_row

def get_number_of_sign_changes(sturm_row, border):
    x = border

    boundary_values = []
    for polynomial in sturm_row:
        boundary_values.append(eval(polynomial))
    counter = 0

    is_positiv = boundary_values[0] >= 0
    for i in range(1, len(boundary_values)):
        is_positiv_current = boundary_values[i] >= 0
        if is_positiv_current != is_positiv:
            counter += 1
            is_positiv = is_positiv_current
    
    return counter



def sturm(init):
    sturm_row = get_sturm_row(init[0])
    right_changes = get_number_of_sign_changes(sturm_row, init[1][0])
    left_changes = get_number_of_sign_changes(sturm_row, init[1][1])
    root_count = abs(right_changes - left_changes)
    return root_count




