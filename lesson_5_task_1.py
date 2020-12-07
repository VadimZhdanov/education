my_obj = open('my_text.txt', 'w')
my_line = input('Введите строку\n')
while my_line:
    my_obj.writelines(my_line)
    my_line = input('Введите строку\n')
    if my_line == '':
        break
my_obj.close()
my_obj = open('my_text.txt', 'r')
content = my_obj.readlines()
print(content)
my_obj.close()

