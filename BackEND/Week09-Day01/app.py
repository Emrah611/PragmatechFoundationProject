class Main:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def index(self):
        print('index metodu')
    ## SELF - CLASSDAN YARANAN OBYEKTI GOSTERIR
    ## INIT - CALSSDAN BIR OBYEKT YARANANDA INIT-I ISE SALIR
    @property ##decorator
    def fullname(self):
        return self.name + ' ' + self.surname
    @fullname.setter
    def fullname(self,new_fullname):
        ad,soyad = new_fullname.split()
        self.name = ad
        self.surname = soyad

    def set_age(self,new_age):
        self.age = new_age
    

    
main1 = Main('Emrah','Seferli',20)
print(main1.name)
main1.fullname = 'Ehmed Hesenov'
print(main1.fullname)
print(main1.surname)