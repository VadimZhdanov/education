from itertools import cycle, count
#for el in count(int(input('Введите число:'))):
#    print(el)
#    if el > 20:
#        break

my_list = [4, 5, 6, 7]
n = 0
for x in cycle(my_list):
    print(x)
    n += 1
    if n > 15:
        break


