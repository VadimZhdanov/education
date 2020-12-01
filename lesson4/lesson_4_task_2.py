my_list = [43, 6, 346, 14, 14, 796, 999, 1, 5, 71]
new_list = [el for x, el in enumerate(my_list) if my_list[x - 1] < my_list[x]]
print(f'Исходный список: {my_list}')
print(f'Отредактированный список: {new_list}')
