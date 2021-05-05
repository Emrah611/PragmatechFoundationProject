# deyıshken1 = 10
# deyıshken2 = 20
# netice = deyıshken1 + deyıshken2
# print(netice)

# deyıshken3 = 'string tip deyishken'
# deyıshken4 = "string tip deyishken"
# deyıshken5 = '''string tip deyishken'''
# deyıshken6 = """string tip deyishken"""
# print(deyıshken3)

# print('Ali Aliyev 1948-ci ilde "Heyvanistan"eserini yazmisdir')

# deyıshken = 'String tip deyishken'
# print(deyıshken.upper()) #Herflerin hamisin boyudur
# print(deyıshken.lower()) #Herflerin hamisin balaca edir
# print(deyıshken.index('t')) #t herfinin necenci indexde olduqun gosterir
# print(deyıshken.index('s'.upper())) #upper verdiyimize gore boyuk S-i qebul edir
# x = 30
# y = 50
# print(x+y)

# x = 'hfkjdshfjdshjkfhsd jjhsdkjhfksdhfjS JHDKJSDHFJDHFLJAS AJKSHWKJDHJKH ffjhjkhjdhkjghggggggggggggggggggggggggggggggggggggggggggghhhhhhhhhhhhhhh'
# print(len(x)) #x-in daxilindeki simvollarin sayi

# name = 'Faiq'
# surname = 'Seferli'
# year = 2020
# uni = 'ADU'

# shablon_text = '{} {} {}-ci ilde {} universitetine qebul olmusdur'.format(name, surname, year, uni)
# print(shablon_text)

# name = input("Telebenin adi: ")
# surname = input("Telebenin soyadi: ")
# year = input("Qebul olduqu il: ")
# uni = input("Qebul olduqu universitet: ")

# shablon_text2 = f'{name} {surname} {year}-ci ilde {uni} universitetine qebul olmusdur'
# print(shablon_text2)

# num1 = input('Birinci reqem: ') #string
# print(type(num1))
# num2 = input('Ikinci reqem: ') #string
# print(type(num2))
# cavab = num1 + num2
# print(f'Netice:{cavab}')


# num1 = int(input('Birinci reqem: '))

# num2 = int(input('Ikinci reqem: ')) #burdaki int (stringi integere cevirir)

# cavab = num1 + num2
# print(f'Netice:{cavab}')

# print(ord('A'))
# print(chr(230))

# x = 'string daxildir' 
# print(x[0:4]) #NETICE = stri

# x = 'string daxildir' 
# print(x[-1]) #NETICE = r

# x = 5
# print(x >= 5)
# print(x == 5)
# print(x != 5)

# city = 'Baku'
# print('u' in city)  #in = uzvluk operatoru

# city = 'Baku'
# print('u' not in city)

# x = 0 # False
# x = 1.5 # True
# city = 'Baku' # True
# city = '' # False
# a = [] # False
# print(bool(x)) 
# print(bool(city)) 

# print('='*30)

# print('login form ', end='') #Netice = login form form (yeni yan yana dusur)
# print('form')

ad = input('Adi: ')
parol = input('Parol: ')
user_password = '12345'
admin_password1 = 'admin'
admin_password2 = 'admin2'

if parol == user_password:
    print('Logged in')

elif parol == admin_password1:
    print('Admin Logged in')
elif parol == 'admin2':
    print('Admin2 Logged in')

else:
    print('Password is wrong !! ')
