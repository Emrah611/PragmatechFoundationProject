result = lambda x: x + 5
print(result(2))

m = [2,3,4,5,6,7]

def func(n):

    return n ** 2

netice = map(func, m)
# print(netice)
print(list(netice))

x = lambda n: n ** 2
netice1 = map(x,m)
netice2 = map(lambda n: n ** 2,m)
netice3 = list(map(lambda n: n ** 2,m))
print(list(netice1))
print(list(netice2))
print(netice3)

filtered_data = filter(lambda x: x < 6,m)
print(list(filtered_data))

# import sys
# print(sys.argv[0])
# import os
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())