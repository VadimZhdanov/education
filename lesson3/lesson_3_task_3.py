def my_calc():
    var_1 = int(input('Введите число 1:'))
    var_2 = int(input('Введите число 2:'))
    var_3 = int(input('Введите число 3:'))
    my_nums = [var_1, var_2, var_3]
    my_nums.sort()
    my_sum = my_nums[1] + my_nums[2]
    return my_sum
print(my_calc())


