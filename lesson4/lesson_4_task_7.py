from itertools import count
from math import factorial
def my_gen():
    for el in count(1):
        yield factorial(el)

gen = my_gen()
n = 0
for i in gen:
    if n < 5:
        print(i)
        n += 1
    else:
        break
