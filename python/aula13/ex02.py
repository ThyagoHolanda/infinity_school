"""
Faça um sistema para venda de ingressos de shows. Existem
três tipos de ingressos, ingressos pista, ingressos camarote e
ingressos VIPs, todos possuem um identificador único, o
preço e o título do show, eles possuem também um método
que retorna essas informações e, possuem um método que
retorna

"Este ingresso é: pista ou camarote ou vip
".

O sistema deve permitir que o usuário crie ingressos de cada
tipo.

Lembre-se de utilizar todos os conceitos que vimos até
agora! Utilize herança, polimorfismo e encapsulamento
"""
from abc import ABC, abstractmethod
from random import randint


class Ingresso(ABC):
    def __init__(self, identificador, preco, titulo_do_show):
        self.identificador = identificador
        self.__preco = preco
        self.titulo_do_show = titulo_do_show

    @property
    def preco(self):
        return self.__preco

    def info(self):
        print(f"Identificador: {self.identificador}\n"
              f"Preço: {self.__preco}\n"
              f"Titulo do Show: {self.titulo_do_show}")
        

    @abstractmethod
    def tipo(self):
        pass


class Pista(Ingresso):

    def tipo(self):
        super().info()
        print("Este ingresso é: pista\n")


class Camarote(Ingresso):
    def tipo(self):
        super().info()
        print("Este ingresso é: camarote\n")


class VIPs(Ingresso):
    def tipo(self):
        super().info()
        print("Este ingresso é: vip\n")


input("Precione enter para começar!")
ingressos = dict()
identificador = 1
while True:
    print("1 - Ingresso para pista")
    print("2 - Ingresso para camarote")
    print("3 - Ingresso para Vip")
    print("4 - Ver informações")
    print("0 - Sair")
    opcao = int(input("Escolha uma das opções acima: "))

    match opcao:
        case 1:
            preco = randint(100,500) #float(input("Qual o preço do ingresso: "))
            titulo_do_show = "Teste" #input("Qual o titulo do Show: ")
            ingressos[identificador] = Pista(identificador, preco, titulo_do_show)
            identificador += 1

        case 2:
            preco = randint(501,1000) #float(input("Qual o preço do ingresso: "))
            titulo_do_show = "Teste" #input("Qual o titulo do Show: ")
            ingressos[identificador] = Camarote(identificador, preco, titulo_do_show)
            identificador += 1

        case 3:
            preco = randint(1001,2000) #float(input("Qual o preço do ingresso: "))
            titulo_do_show = "Teste" #input("Qual o titulo do Show: ")
            ingressos[identificador] = VIPs(identificador, preco, titulo_do_show)
            identificador += 1
        
        case 4:
            for i in ingressos:
                ingressos[i].tipo()

        case 0:
            break
