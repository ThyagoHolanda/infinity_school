# https://www.computersciencemaster.com.br/

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, nome_do_veiculo, quantidade_de_motores, tem_rodas):
        self.nome = nome_do_veiculo
        self.quantidade_de_motores = quantidade_de_motores
        self.rodas = tem_rodas

    @abstractmethod
    def buzinar(self):
        print("Erro!")

class Carro(Veiculo):
    
    def buzinar(self):
        print("Biiiii")


class Barco(Veiculo):

    def buzinar(self):
        print("Foooom")

class Aviao(Veiculo):

    def buzinar(self):
        print("Tem buzina?")


gol = Carro("Gol", 1, True)
navio = Barco("Navio", 2, False)
boeing = Aviao("Boeing", 4, True)


print(gol.nome, gol.quantidade_de_motores, gol.rodas)
gol.buzinar()
print("\n")

print(navio.nome, navio.quantidade_de_motores, navio.rodas)
navio.buzinar()
print("\n")

print(boeing.nome, boeing.quantidade_de_motores, boeing.rodas)
boeing.buzinar()