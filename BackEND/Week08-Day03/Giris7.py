class car:
    def __init__(self,model,year):
        self.model = model
        self.year = year
        self.speed = 200

    def displyay_info(self):
        print(f"Model:{self.model}\nYear:{self.year}\nSpeed:{self.speed}")
    
    def change_marka(self,new_model):
        self.model = new_model
    
    def show_energy(self):
        print('Masinda 20 litr benzin qalib')

car1 = car('Toyota',2018)
car1.displyay_info()
car1.change_marka('Mercedes')
car1.year = 2021
print(car1.model,car1.year)

class Electric_car(car):
    def __init__(self,model,year,battery):
        super().__init__(model,year)
        self.battery = battery

    def show_energy(self):
        print('Masinda 100 km-lik enerji qalib')

electric_car1 = Electric_car('Toyota', 2019,300)
print(electric_car1.model,electric_car1.year,electric_car1.battery)
print(electric_car1.displyay_info())

##Polimorfizm
car1.show_energy()
electric_car1.show_energy()

class registr:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    @property
    def fullad(self):
        return self.ad + ' ' + self.soyad

    @fullad.setter
    def set_fullad(self,new_fullad):
        ad,soyad = new_fullad.split(' ')
        self.ad = ad
        self.soyad = soyad
    @fullad.deleter
    def fullad(self):
        self.ad = ''
        self.soyad = ''
        print('Deleted')

    
r1 = registr('Teymur','Memmedov')
print(r1.ad)
r1.ad = 'Elsen'
r1.soyad = 'Celilov'
print(r1.ad)
r1.set_fullad = 'Orxan Hesenli'
print(r1.fullad)
print(r1.ad)
del r1.fullad
print(r1.fullad)