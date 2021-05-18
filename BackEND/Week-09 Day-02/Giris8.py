# Encapsulation
# Private Variables
# Public Variables
# Protected Variable
# Public methods
# Private methods
# Class variable or attributes
# Class methods

# Abstact classes
# map, reduce, filter, lambda, os, sys

class Person:
    
    def __init__(self,name,age,gender):
        self.name = name
        self._age = age
        self.__gender = gender
    
    def public_method(self):
        print(self.__private_method())
    
    def __private_method(self):
        return self.__gender

p1 = Person('Mike', 20, 'male')
print(p1._age)

p1.public_method()

class BankHesab:
    def __init__(self,name = 'Bill',balance = 50):
        self.__name = name
        self.__balance = balance
    
    def show_balance(self):
        print(self.__balance)
    
    def take_money(self,amount):
        if amount <= self.__balance:
            print(f'{amount} AZN is ready to be taken')
            self.__balance -= amount
        else:
            print('Not enough money in your balance')

p1 = BankHesab()
p1.show_balance()
p1.take_money(40)
p1.show_balance()
p1.take_money(20)
p1.show_balance()

class Workers:

    company = 'Apple'

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display_info(self):
        print(f'Name: {self.name}\nAge: {self.age}\nCompany: {Workers.company}\n============================')
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # def change_company_obj(self, new_obj_company):
    #     Workers.company = new_obj_company
    
w1 = Workers('Tale',20)
w2 = Workers('Teymur',30)

w1.display_info()
w1.change_company('Samsung')
w1.display_info()
w2.change_company('Apple')
w2.display_info()
print()

# w3 = Workers('Arif', 25)
# w4 = Workers('Serxan', 35)

# print('Before')
# w3.display_info()
# print(Workers.company)
# w3.change_company('Samsung')
# print('After')
# w4.display_info()
# print(Workers.company)