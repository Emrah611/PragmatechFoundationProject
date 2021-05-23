class car:
    def __init__(self,model,year):
        self.marka = model
        self.il = year
car1 = car('Toyota',2018)
print(car1.marka,car1.il)

class car:
    def __init__(self,model,year):
        self.model = model
        self.year = year
car1 = car('Toyota',2018)
car1.year = 2021
print(car1.marka,car1.il)

class car:
    def __init__(self,model,year=2005):
        self.model = model
        self.year = year
car1 = car('Toyota',2018)
car1.year = 2021
car2 = car('Bmw')
print(car1.model,car1.year)
print(car2.year)

class car:
    year = 2005
    def __init__(self,model,year):
        self.model = model
        self.year = year
car1 = car('Toyota',2018)
car1.year = 2021
car2 = car()
print(car1.marka,car1.il)
print(car2.year)

class car:
    def __init__(self,model,year):
        self.model = model
        self.year = year
        self.speed = 200

    def displyay_info(self):
        print(f"Model:{self.model}\nYear:{self.year}\nSpeed:{self.speed}")
    
    def change_marka(self,new_model):
        self.model = new_model

car1 = car('Toyota',2018)
car1.displyay_info()
car1.change_marka('Mercedes')
car1.year = 2021
print(car1.model,car1.year)




