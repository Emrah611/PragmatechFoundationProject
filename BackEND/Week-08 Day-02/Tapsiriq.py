#1
class Restoran:
    def __init__(self,restoran_adi,metbex_novu):
        self.restoran_adi = restoran_adi
        self.metbex_novu = metbex_novu
       
    def tesvir_restaurant(self):
        print(f'Restoran:{self.restoran_adi}\nMetbex:{self.metbex_novu}')
    def open_restaurant(self):
        print('Restoran saat 9:00 da acilir')
Restoran1 = Restoran('Havana','Azerbaycan Metbexi')
print(Restoran1.restoran_adi,Restoran1.metbex_novu)
Restoran1.tesvir_restaurant()
Restoran1.open_restaurant()

#2
class Restoran:
    def __init__(self,Ad,Metbex,Unvan):
        self.Ad=Ad
        self.Metbex=Metbex
        self.Unvan=Unvan
    def description_restaurant(self):
        print(f'Restoran:{self.Ad}\nMetbex:{self.Metbex}\nUnvan:{self.Unvan}')
restoran1 = Restoran('Havana','Azerbaycan Metbexi','Xetai')
print(restoran1.Ad,restoran1.Metbex,restoran1.Unvan)
restoran2 = Restoran('Diamond','Turk Metbexi','28 May')
print(restoran2.Ad,restoran2.Metbex,restoran2.Unvan)
restoran3 = Restoran('La Terrace','Italyan Metbexi','Genclik')
print(restoran3.Ad,restoran3.Metbex,restoran3.Unvan)

#3
class Istifadeci:
    def __init__(self,first_name,last_name ):
        self.first_name=first_name
        self.last_name=last_name
        self.age= 22
        self.height= 1.90
    def tesvir_user(self):
        print(f'Ad:{self.first_name}\nSoyad:{self.last_name}\nAge:{self.age}\nHeight:{self.height}')
    def salam(self):
        print(f'Salam {self.first_name} {self.last_name} bugun senin {self.age} yasin tamam olur ve senin boyun {self.height}-dır')

Istifadeci1 = Istifadeci('Anar','Celilov')
print(Istifadeci1.first_name,Istifadeci1.last_name,Istifadeci1.age,Istifadeci1.height)
Istifadeci1.tesvir_user()
Istifadeci1.salam()

Istifadeci2 = Istifadeci('Tale','Hesenli')
Istifadeci2.age = 30
Istifadeci2.height = 1.78
print(Istifadeci2.first_name,Istifadeci2.last_name,Istifadeci2.age,Istifadeci2.height)
Istifadeci2.tesvir_user()
Istifadeci2.salam()

Istifadeci2 = Istifadeci('Faiq','Memmedov')
Istifadeci2.age = 20
Istifadeci2.height = 1.72
print(Istifadeci2.first_name,Istifadeci2.last_name,Istifadeci2.age,Istifadeci2.height)
Istifadeci2.tesvir_user()
Istifadeci2.salam()