my_list = [2, 3, 3, 81, 14, 14, 5, 2, 23, 23, 7, 6, 6]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
