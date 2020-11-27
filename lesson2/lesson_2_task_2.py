first = input('Введите данные для списка:')
first_list = list(first)
print(first_list)
new_list = [i for i in first_list]
for i in range(1, len(new_list), 2):
    new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]
print(new_list)

