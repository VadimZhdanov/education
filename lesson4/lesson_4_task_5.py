from functools import reduce
def func(first_el, second_el):
    return first_el * second_el
my_list = [el for el in range(99, 1001) if el % 2 == 0]
new_list = reduce(func, my_list)
print(new_list)
