def my_calc():
    try:
        var_1 = int(input('Введите число 1:'))
        var_2 = int(input('Введите число 2:'))
        my_div = var_1 / var_2
        return my_div
    except ZeroDivisionError:
        return 'деление на 0!'
print(my_calc())


