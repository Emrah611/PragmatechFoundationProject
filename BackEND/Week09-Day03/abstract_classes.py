#   ABSTRACT CLASSES

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


# vehicle = Vehicle() # abstract classdan obyekt yaratmaq olmaz!
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()

from app import x,y
print(y, x)

from app import *  #hamisin cagirmaq ucun *-dan istifade olunur
print(y, x)

from app import y, xfhfxffgdhdfgdgf as top  #as- uzun adi deyisdirib qisa elemek ucun lazimdir
print(y, top)



FRAMEWORK, MOLDULS, __name__ and __main__

if __name__ == '__main__':
    print(__name__)

import app
print(__name__)