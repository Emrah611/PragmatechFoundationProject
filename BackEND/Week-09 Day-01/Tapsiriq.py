#1
class Work1:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

w1 =Work1('Dadas','Dadasov')
w2 = Work1('Murad','Muradov')

print(w1.name)
print(w2.surname)

class Work2:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        
w3 =Work2('Sefer','Seferov')
w4 = Work2('Ibrahim','Ibrahimov')

print(w4.surname)
w4.surname = 'Aliyev'
print(w3.name)
print(w4.surname)

class Work3:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        
w5 =Work3('Esger','Esgerov')
print(w5.name)
w6 = Work3('Ilyas','Ilyasov')
w5.name = 'Ali'
print(w5.name)
print(w6.surname)

#2-#3
class Work:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def workperson(self):
        print(f'Name:{self.name} Surname:{self.surname}')

w1 =Work('Dadas','Dadasov')
print(w1.surname)

class Work2(Work):
    def __init__(self, name, surname,age):
        super().__init__(name, surname)
        self.age = age 

    def workperson(self):
        print(f'Name:{self.name} Surname:{self.surname} Age:{self.age}')
w2 = Work2('Murad','Muradov',25)
print(w2.surname)
print(w2.age)

w1.workperson()
w2.workperson()

#4
class Work1:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def update_name(self, change_name):
        self.name = change_name

w1 =Work1('Dadas','Dadasov')

w1.update_name('Serxan')

print(w1.name)