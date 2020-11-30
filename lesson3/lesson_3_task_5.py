def my_sum ():
    sum_result = 0
    exit_calc = False
    while exit_calc == False:
        numbers = input('Введите числа через пробел, Q для завершения:').split()
        my_result = 0
        for el in range(len(numbers)):
            if numbers[el] == 'q' or numbers[el] == 'Q':
                exit_calc = True
                break
            else:
                my_result = my_result + int(numbers[el])
        sum_result = sum_result + my_result
        print(f'Текущая сумма: {sum_result}')
    print(f'Окончательная сумма: {sum_result}')
my_sum()
