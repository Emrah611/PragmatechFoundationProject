#1
def toplama(my_list):
    cem = 0
    for i in my_list:
        cem += i
    return cem
print(toplama([5,9,7,5,1,0,9,35,62]))

#1.2
def toplama(my_list):
    cem = 0
    for i in my_list:
        cem += i
    return cem
x = list(map(int, input().split()))
print(x)
print(toplama(x))

#2
def vurma(my_list):
    x = 1
    for i in my_list:
        x *= i
    return x
print(vurma([4,-2,2,5,1,3,-3]))

#3
def ReturnDay(x):
    if x >= 1 and x <= 7:
        if x == 1:
            print('1:Bazar Ertəsi')
        elif x == 2:
            print('2:Çərşənbə Axşamı')
        elif x == 3:
            print('3:Çərşənbə')
        elif x == 4:
            print('4:Cümə Axşamı')
        elif x == 5:
            print('5:Cümə')
        elif x == 6:
            print('6:Şənbə')
        elif x == 7:
            print('7:Bazar')
    else:
        print('x 1-7 araliqi reqem ala biler')

y = int(input())
ReturnDay(y)

#4
def LastElement(my_list):

    if my_list:
        return my_list [-1]
    return

my_list1 = [7,9,3,8]
my_list2 = []
print(LastElement(my_list1))
print(LastElement(my_list2))

#5.1
my_list = [3,6,23,54,47,89,40,22,13,100]
for i in my_list:
    if i % 2 == 0:
        print(i)

#5.2
def my_list(cut):
    for x in cut:
        if x % 2 == 0:
            print(x)

my_list([3,6,23,54,47,89,40,22,13,100])

#6
def my_list(ad,maas = 9000):
    print(ad,maas)
my_list('Fazil',777)


#7
def toplama(*args):
    cem = 0
    for i in args:
        cem += i
    return cem
print(toplama(5,1,9,7,43,57,21,79))