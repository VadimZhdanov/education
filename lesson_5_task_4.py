my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_obj = []
my_obj = open('file4.txt', 'r')
for i in my_obj:
    i = i.split(' - ', )
    new_obj.append(my_dict[i[0]] + ' - ' + i[1])
my_obj.close()
print(new_obj)
with open('file4_1.txt', 'w') as new_file:
    new_file.writelines(new_obj)
