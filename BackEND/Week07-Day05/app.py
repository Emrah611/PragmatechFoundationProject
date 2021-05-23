x = 5
print(x)

ad = 'sefer '
soyad = 'seferov'
tam_ad = ad + soyad
print('Salam ', end='')
print(tam_ad.title())

x = 7
y = 2
z = x**y
print(z)

y ='4.92'
x = int(float(y))
print(x)

x = int(input('Havanin temperaturu nece derecedi?'))
if x < 10:
    print('soyuq')
elif x == 20:
    print('normal')
elif x > 30:
    print('isti')
else:
    print(None)

y = 'proqramlasdirma'
print('x' in y)

x = ('alma', 'armud')
y = ('banan', 'portagal')
z = x + y
print(z)

x = int(input('diametr:'))
y = 2 * 3.14 * ((x/2)**2)
print(y)

x = """ Sweep through the days Like children that can't stay awake """ 
z = int(input('uzunluqu daxil edin: '))
y = x[:z]
if z < 0:
    print('False')
elif len(y) < len(x):
    print(y)
    print('İslem Basarılı')
else:
    print('Error')

ad = input('adi daxil edin: ')
soyad = input('soyadi daxil edin: ')
print(f'{ad}{soyad}11@gmail.com')

x = int(input('x -i daxil edin:'))
y = int(input('y -i daxil edin:'))
z = input('bir riyazi emel daxil edin:')
if z == '+':
    print(x + y)
elif z == '-':
    print(x - y)
elif z == '*':
    print(x * y)
elif z == '/':
    print(x / y)

n = (68)

if n % 2 == 0:
    print('EVEN')
else:
    print('ODD')

n = 28
a = int(input('a -ni daxil edin:'))
b = int(input('b -ni daxil edin:'))
if n % a == 0 and n % b == 0:
    print('YES')
else:
    print('NO')


n = int(input('n-i daxil edin: '))

if n > 0:
    print('Positive')
elif n == 0:
    print('Zero')
elif n < 0:
    print('Negative')

x = int(input('x-i daxil edin: '))
y = int(input('y-i daxil edin: '))
z = int(input('z-i daxil edin: '))

if (x + y) > z and (x+z) > y and (y + z) > x:
    print('YES')
else:
    print('NO')

x = 10
print(x -1)

x = 10
print(-x)

x = input('x -i daxil edin:')
toplam = 0
for i in x:
    toplam += int(i)
print(toplam**2)

my_list = [1,2,3,4,5,6,7,8,9,10]
toplam = 0
for i in my_list:
    toplam += i
print(toplam)

my_list = [1,2,3,4,57,6,75,8,9,10,54]
x = 0
for i in my_list:
    if i > x:
        x = i
print(x)

my_list = [1,2,3,4,57,6,75,8,-70,9,10,54]
x = len(my_list)
for i in my_list:
    if i < x:
        x = i
print(x)

my_list = ['alma','armud','banana','343']
for i in my_list:
    if i[0] == i[-1]:
        print(i)


x = []
print(bool(x))

Eat = ['sup', 'aş', 'qatiq', 'lobya', 'kabab']
x = Eat.copy()
x[3] = 'dolma'
if Eat [1] == 'aş':
     for i in Eat:
        print('Menu: ' + i)
        
print('< Yeni Menu >')
Eat [1] = 'dolma'
Eat [4] = 'lahmacun'
for x in Eat:
    print('Yeni Menu: ' + x)

my_list = [1,2,3,4,5,78,6,9,54]
toplama = 0
for i in my_list:
    toplama += i
    toplama = y
print(y)

def my_list(toplam):
    cem = 1
    for i in toplam:
        cem *= i
    return cem
print(my_list([1,5,8,9,5,3,67,21]))

def vurma(my_list):
    x = 0
    for i in my_list:
        x += i
    return x
print(vurma([5,9,7,5,1,0,9,35,62]))

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
ReturnDay(5)

def my_list(ad,maas = 9000):
    print(ad,maas)
my_list('Fazil',777)