my_tuple = (5)
my_tuple = tuple(my_tuple)
print(type(my_tuple))

import math
my_float = 5.98
print(math.floor(my_float))
print(math.floor(1.4))
print(math.ceil(22.6))

ad = input('ad: ')
yas = int(input('yas: '))
if len(ad) < 3 or yas <15:
    print('error')

my_tuple = (4, 9, 'hi')
my_tuple = list(my_tuple)
my_tuple.append(55) 
my_tuple[2] = 43
my_tuple = tuple(my_tuple)
print(type(my_tuple))