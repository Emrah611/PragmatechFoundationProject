#1
x = int(input('Diametri daxil edin: '))
z = 2
y = 2 * 3.14 * (x ** z)
print(y)

#2
x = """ Sweep through the days Like children that can't stay awake """
z = int(input('z-i daxil edin: '))
y = x[:z]
if z < 0:
    print('False')
elif len(y) < len(x):
    print(y)
    print('İslem Basarılı')
else:
    print('Error')

#3
ad = input('Ad: ')
soyad = input('Soyad: ')
z = f'{ad}{soyad}11@gmail.com' 
print(z)

#4
x = int(input('Eded daxil edin: '))
y = int(input('Ikinci ededi daxil edin: '))
c = input('Riyazi emel daxil edin: ')
if c == '+':
    print(x + y)
elif c == '-':
    print(x - y)
elif c == '*':
    print(x * y)
elif c == '/':
    print(x / y) 

#5
x = int(input('x-i daxil edin: '))

if x % 2 == 0:
    print('EVEN')
else:
    print('ODD') 

#6
n = int(input('n-i daxil edin: '))
x = int(input('a-ni daxil edin: '))
y = int(input('b-ni daxil edin: '))

if (n%x and n%y ):
    print('YES')
else:
    print('NO')

#7
n = int(input('n-i daxil edin: '))

if n > 0:
    print('Positive')
elif n == 0:
    print('Zero')
elif n < 0:
    print('Negative')

#8.1
x = int(input('x-i daxil edin: '))
y = int(input('y-i daxil edin: '))
z = int(input('z-i daxil edin: '))

if (x + y) > z and (x+z) > y and (y + z) > x:
    print('YES')
else:
    print('NO')

#8.2
x = int(input('x-i daxil edin: '))
if x >= 0 and x <=3:
    print('Initial')
elif x > 3 and x <=6:
    print('Average')
elif x >6 and x <=9:
    print('Sufficient')
elif x >9 and x <=12:
    print('High')
else:
    print('x-in ala bileceyi max deyer 12-dir')

#9
x = int(input('x-i daxil edin: '))
print(x - 1)

#10

x = int(input('x: '))
y = int(input('y: '))

a = x // y
b = x % y

print(f'Tam hissesi:{a} Qalıq hissesi:{b}')

#11
x = int(input('x-i daxil edin: '))
print(-x)

# 12
num = input(':') 
toplam = 0
for i in num:
    toplam = toplam + int(i)

print(toplam**2)

#13

Ad = input('Ad: ')

if len(Ad) < 3 or len(Ad) > 11:
     print('Adiniz 3 simvoldan kicik ve ya 11 simvoldan boyuk ola bilmez')
else:
    Soyad = input('Soyad: ')
    if len(Soyad) < 5 or len(Soyad) > 15:
        print('Soyadiniz 5 simvoldan kicik ve ya 15 simvoldan boyuk ola bilmez')
    else:
        Year = input('Year: ')
        if len(Year) != 4:
             print('Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır')
        else:
             x = input('Mailin adin daxin edin(@gmail.com): ')
             y = '@gmail.com'
             Email = f'{x}{y}'
             print(Email)
             if (len(Email) < 10 or len(Email) > 22 and '@gmail.com'):
                 print('Emailiniz 10 simvoldan kicik,22 simvoldan boyuk ve @gmail.com olmadan istifade oluna bilmez')
             else:
                 Parol = input('Parol: ')
                 if len(Parol) < 6 or len(Parol) > 13:
                     print("Parol 6-13 arasi uzunluqda olmalidir.")
                 else:
                     Parol2 = input("Parol2: ")
                     if Parol != Parol2:
                         print("Tesdiqleme parolu eyni deyil")
                     else:
                         print("Qeydiyyat tamamlandi!")
                         x = input('Qeydiyyatın detallarına baxmaq istəyirsizmi: ')
                         if x == 'he' or x == 'He':
                             print(f'Ad:{Ad} Soyad:{Soyad} Yas:{Year} Email:{Email} Parol:{Parol}')
                         elif x == 'yox' or x == 'Yox':
                             print(f'{Ad} {Soyad},Ugurlar!')
                         else:
                             print('Qeydiyyat Tamamlandı')
