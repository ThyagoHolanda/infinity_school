class Animal:
    def __init__(self, name):
       self.name = name

    def comer(self):
        print(f"{self.name} está comendo") 
    
    def beber(self):
        print(f"{self.name} está bebendo") 

class Mamifero(Animal):
    def amamentar(self):
        print(f"{self.nome} está amamentando")


animal = Animal("Bilu")
manifero = Mamifero("Macaco")

animal.comer()
manifero.comer()

animal.beber()
manifero.beber()
