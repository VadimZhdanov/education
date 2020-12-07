with open('file5.txt', 'w+') as my_obj:
    content = input('Введите числа через пробел:\n')
    my_obj.writelines(content)
    numbers = content.split()
    sum_num = sum(map(float, numbers))
    print(sum_num)

