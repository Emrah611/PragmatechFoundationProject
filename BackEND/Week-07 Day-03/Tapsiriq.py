#1
my_list = [1,5,9,4,5,0,3,6,8,2,7]
toplam = 0

for x in my_list:
    toplam = x + toplam

print(toplam)

#2
my_list = [17,39,54,26,70]
mak = 0

for x in my_list:
    if x > mak:
        mak = x
    
print(mak)

#3
my_list = [17,39,54,5,26,13,70]
minum = my_list[1]

for x in my_list:
    if x < minum:
        minum = x
print(minum)

#4
my_list = ['aba', 'hahe', 'f', 'fegf', 'githg','a', 'yt','28652']

for i in my_list:
    if len(i) >= 2 and i[0] == i[-1]:
        print(i)

#5
x = []
print(bool(x))

x = []
if bool(x):
    print('Siyahi bos deyil')
else:
    print('Bu siyahi bosdur')

#6
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

#7
ad = input('ad: ')

istifadeciler = ['Elnur', 'Tale', 'Mamed', 'Turan', 'admin', 'Ayxan', 'Emrah']


if ad in istifadeciler:
    if ad == 'admin':
        print("Salam admin,Xos geldin")
    else:
        print(f"Salam {ad}") 

else:
    print('Etibarsiz ad')

