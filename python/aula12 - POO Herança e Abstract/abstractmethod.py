from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
       self.name = name

    @abstractmethod
    def comer(self):
        pass 
    @abstractmethod
    def beber(self):
        pass 

class Mamifero(Animal):
    def comer(self):
        print(f"{self.name} está comendo") 
    
    def beber(self):
        print(f"{self.name} está bebendo") 


macaco = Mamifero("macaco")
macaco.comer()