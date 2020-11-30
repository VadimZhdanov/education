# Вариант 1
#def my_calc(x, y):
#    my_res = x ** y
#    return my_res
#print(my_calc(x = int(input('Введите действительное положительное число:')),
# y = int(input('Введите целое отрицательное число:'))))

#Вариант 2
def my_calc(x, y):
    my_res = 1 / (x ** abs(y))
    return my_res
print(my_calc(x = int(input('Введите действительное положительное число:')),
              y = int(input('Введите целое отрицательное число:'))))
