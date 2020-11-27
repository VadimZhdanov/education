my_str = input('Введите слова:')
word = []
x = 1
for el in range(my_str.count(' ') + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(f'{x} {word [el]}')
        x = x + 1
    else:
        print(f'{x} {word [el] [0:10]}')
        x = x + 1
        










