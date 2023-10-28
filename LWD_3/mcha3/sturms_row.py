from sympy import div, degree, diff

BDC = 1e-05    #boundary difference constant

def get_number_of_sign_changes(sturm_row, value):
    sturm_row_values = []
    for polynomial in sturm_row:
        sturm_row_values.append(polynomial.subs('x', value))

    counter = 0
    for i, current_value in enumerate(sturm_row_values[1:], start=1):
        if sturm_row_values[i-1] * current_value < 0:
            counter += 1
    
    return counter


def get_sturm_row(equation):
    sturm_row = list()
    y = equation
    sturm_row.append(y)

    y_2 = diff(y)
    sturm_row.append(y_2)

    r = y_2
    while degree(r) > 0:
        r = div(y, y_2)[1] * (-1) 
        sturm_row.append(r)
        y = y_2
        y_2 = r
    return sturm_row


def get_intervals(sturm_row, interval: tuple):
    intervals = []
    get_elementary_intervals(sturm_row, interval, intervals)

    if len(intervals) > 1:
        for i in range(1, len(intervals)):
            if intervals[i][0] == intervals[i - 1][1]:
                intervals[i][0] += BDC
    return intervals
    

def get_elementary_intervals(sturm_row, interval: tuple, intervals : list):                                
    left_sign_change_number = get_number_of_sign_changes(sturm_row, interval[0])
    right_sign_change_number = get_number_of_sign_changes(sturm_row, interval[1])

    if left_sign_change_number == right_sign_change_number:         
        return         

    if abs(left_sign_change_number - right_sign_change_number) == 1:
        intervals.append(list(interval)) 

    else:
        middle = float(interval[1] - interval[0]) / 2 
        get_elementary_intervals(sturm_row, (interval[0], interval[0] + middle), intervals)
        get_elementary_intervals(sturm_row, (interval[0] + middle, interval[1]), intervals)

