subjects = {}
with open('file6.txt', 'r') as my_obj:
    my_list = my_obj.readlines()
    for line in my_list:
        splitted_line = line.split()
        subject = splitted_line[0]
        for x in splitted_line[1:]:
            if '(' in x:
                hours = sum(map(int, (x[:x.find('(') in splitted_line])))
        subjects[subject[:-1]] = hours
print(subjects)
# Задача для меня оказалась тяжелой. Самостоятельно решить ее не смог.
# Посмотрев ваше решение, постарался написать свой код по аналогии.
# Нужный результат программа не дает. Сейчас ошибку найти не могу, постараюсь позже разобраться.
