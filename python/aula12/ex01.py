from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor
    
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def beber(self):
        pass


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f"O {self._nome} está comendo")

    def beber(self):
        print(f"O {self._nome} está beber")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f"O {self._nome} está comendo")
    
    def beber(self):
        print(f"O {self._nome} está beber")



gato = Gato("Bichano", "Branco")
cachorro = Cachorro("Totó", "Preto")

gato.comer()
cachorro.comer()