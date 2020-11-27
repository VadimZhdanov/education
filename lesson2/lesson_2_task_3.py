# вариант через list
# my_month = int(input('Введите номер месяца:'))
# year_list = ['winter', 'spring', 'summer', 'fall']
# a = 0
# if my_month == 12 or my_month == 1 or my_month == 2:
#     a = year_list[0]
# elif 2 < my_month < 6:
#     a = year_list[1]
# elif 5 < my_month < 9:
#     a = year_list[2]
# elif 8 < my_month < 12:
#     a = year_list[3]
# else:
#     print('Ошибка при вводе')
# print(a)

# вариант через dict
my_dict = {'Winter': (12, 1, 2), 'Spring': (3, 4, 5), "Summer": (6, 7, 8), "Fall": (9, 10, 11)}
month = int(input('Введите номер месяца:'))
while 0 < month < 13:
    for el in my_dict:
        if month in my_dict[el]:
            print(el)
else:
    print('Ошибка при вводе')






