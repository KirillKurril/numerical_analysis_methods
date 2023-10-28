from sympy import div, degree, diff

def get_number_of_sign_changes(sturm_row, current_value):

    sturm_row_values = []
    for polynomial in sturm_row:
        sturm_row_values.append(polynomial.subs('x', current_value))

    counter = 0
    for i, current_value in enumerate(sturm_row[1:]):
        if sturm_row[i - 1] * current_value < 0:
            counter += 1
    
    return counter


def traverse_list(ls, a):
    if type(ls) == tuple:
        if ls[0] != 0 or ls[1] != 0:
            a.append(ls)
        return
    for i in range(len(ls)):
        traverse_list(ls[i], a)


def get_clean_intervals(ls, a):
    traverse_list(ls, a)
    return a


def get_sturm_row(equation):
    sturm_row = list()
    y = equation
    sturm_row.append(y)

    y_2 = diff(y)
    sturm_row.append(y_2)

    r = y_2
    while degree(r) > 0:
        r = div(y, y_2)[1] * (-1)  # get remain
        sturm_row.append(r)
        y = y_2
        y_2 = r
    return sturm_row


def get_root_local_interval(sturm_row, interval: tuple): #в этом методе рассматривается локальный интервал
    local_output_intervals = []                                #он разбивает переданный интервал на   
                                                                 #подинтервалы, содержащие каждый только по одному корню
    left_sign_change_number = get_number_of_sign_changes(sturm_row, interval[0])
    right_sign_change_number = get_number_of_sign_changes(sturm_row, interval[1])

    if abs(left_sign_change_number - right_sign_change_number) == 1: #если обнаружен только один корень
        return left_sign_change_number, right_sign_change_number  #возвращается текущий интервал

    if left_sign_change_number == right_sign_change_number:          #если оказалось, что переданный интервал корней не   
        return 0, 0                                   #содержит, возвращается нулевой интервал

                      
    else:
        middle = float(interval[1] - interval[0]) / 2 #в противном случае интервал бинарно разбивается на подинтервалы
        left_subinterval = get_root_local_interval(sturm_row, (interval[0], interval[0] + middle))
        right_subinterval = get_root_local_interval(sturm_row, (interval[0], interval[0] + middle))

        if not all(value == 0 for value in left_subinterval):
            local_output_intervals.append(left_subinterval)
        if not all(value == 0 for value in right_subinterval):
            local_output_intervals.append(right_subinterval)

    return local_output_intervals


def get_elementary_intervals(sturm_row, interval: tuple):
    elementary_intervals = list()
    sign_change_times = dict()
    for i in range(interval[0], interval[1] + 1): #цикл проходится по всем натуральным числам ряда и для каждого 
        func_values = list()                      #вычисляет количество изменений знака в ряды штурма
        sign_changes_count = 0
        for num, func in enumerate(sturm_row):
            func_values.append(func.subs('x', i))
            if num == 0:
                continue
            if func_values[num] * func_values[num - 1] < 0:
                sign_changes_count += 1

        sign_change_times[i] = sign_changes_count

    for i in range(interval[0] + 1, interval[1] + 1): #опять проходится по всем натуральным числам и если оказывается 

        if sign_change_times[i - 1] - sign_change_times[i] > 1:   #что число изменений знака между предыдущим и текущим
            local_output_intervals = get_root_local_interval(sturm_row, (i - 1, i)) #больше единицы, то выполняется разбиение его на
            clean_upped_intervals = []                              #более мелкие интервалы при помощи функции get_root_local_interval
            clean_upped_intervals = get_clean_intervals(local_output_intervals, clean_upped_intervals)
                                                                    #в результате работы которой возвращаются не только
            for inter in clean_upped_intervals:                     #значимые интервалы, но и нулевые
                elementary_intervals.append(list(inter))                  #избавление от них происходит в get_clean_intervals

        elif sign_change_times[i - 1] != sign_change_times[i]:    #в противном случае оно равно единице, а значит
            elementary_intervals.append([i - 1, i])                       #интервал уже готовый

    for i in range(1, len(elementary_intervals)):
        if elementary_intervals[i][0] == elementary_intervals[i - 1][1]:
            elementary_intervals[i][0] = elementary_intervals[i][0] + 0.00001
            # если начало интервала elementary_intervals[i]
            # совпадает с концом предыдущего интервала elementary_intervals[i - 1],
            # то он увеличивает начало текущего интервала 
            # elementary_intervals[i] на небольшую величину 0.00001.

    return elementary_intervals
