my_list = [9, 6, 6, 5, 4, 3]
my_rating = int(input('Введите свой рейтинг:'))
for el in range(len(my_list)):
    if my_list[el] == my_rating:
        my_list.insert(el + 1, my_rating)
        break
    elif my_list[0] < my_rating:
        my_list.insert(0, my_rating)
        break
    elif my_list[-1] > my_rating:
        my_list.append(my_rating)
        break
    elif my_list[el] > my_rating and my_list[el + 1] < my_rating:
        my_list.insert(el + 1, my_rating)
        break
print(f'Обновленный рейтинг: {my_list}')
