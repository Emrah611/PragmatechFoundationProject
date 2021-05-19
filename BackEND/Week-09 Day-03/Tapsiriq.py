from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def Hybrid(self):
        pass
    @abstractmethod
    def Electric(self):
        pass

class Cars(Car):
    def Hybrid(self):
        print('0-100km daha az Benzin serfiyyati var')
    def Electric(self):
        print('Benzin serfiyyati 0')

car1 = Cars()
car1.Hybrid()
car1.Electric()

from app import x,y
print(y,x)