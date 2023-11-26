"""
Pense em sistema bancário, nesse sistema há 2 contas: conta-corrente e conta
poupança.

Ambas possuem um identificado numérico, nome do titular e saldo. Possuem
também dois métodos: verificar informações, que retorna todas as informações
daquela conta e, depósito, que adiciona determinado valor ao saldo daquela
conta.

Apenas a conta-corrente possui também o método sacar que subtrai
determinado valor da conta.

Apenas a conta poupança possui também um atributo chamado juros.

Quem utilizará esse sistema é um gerente, portanto, o sistema deve permitir que
ele crie uma conta-correte ou conta poupança nova e, que consiga utilizar
todas as funções.
"""
from random import randint

class Conta:
    def __init__(self, indetificador, nome, saldo):
        self.indetificador = indetificador
        self.nome = nome
        self.__saldo = saldo # O __ protege o saldo para que não seja modifica do e nem visto fora da classe
    
    @property # Permite que o saldo seja visto fora da classe
    def saldo(self):
        return self.__saldo

    @saldo.setter # permite que o saldo seja modificado fora da classe
    def saldo(self, valor):
        self.__saldo = valor


    def verificar_infor(self):
        print(f"\nindetificador -> {self.indetificador}\n"
              f"nome da conta -> {self.nome}\n"
              f"saldo -> {self.__saldo}")
    
    def deposito(self, valor):
        self.__saldo += valor

        print("O Deposito foi realizado com sucesso")

class Conta_corrente(Conta):
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Valor insuficiente.")
        else:
            self.__saldo -= valor

            print("Saque efetuado com sucesso")

class Conta_poupança(Conta):
    def __init__(self, indetificador, nome, saldo, juros):
        super().__init__(indetificador, nome, saldo)
        self.juros = juros

    def verificar_infor(self):
        '''print(f"indetificador -> {self.indetificador}\n"
              f"nome da conta -> {self.nome}\n"
              f"saldo -> {self.saldo}\n"
              f"Juros -> {self.juros}")'''
        super().verificar_infor()
        print(f"Juros -> {self.juros}\n")

while True:
    escolha = int(input("Digite uma das escolhas abaixo:\n"
                        "1 - Conta Corrente\n"
                        "2 - Conta Poupança\n"
                        "0 - Finalizar Sistema\n"))
    
    match escolha:
        case 1:
            # indetificador = int(input("Digite o indetificador da conta: "))
            indetificador = randint(0, 10000)
            nome = input("Digite o nome da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))

            conta = Conta_corrente(indetificador, nome, saldo)

            print(conta.saldo)

            conta.saldo = 50

            print(conta.saldo)

            while True:
                escolha = int(input("Digite uma das opções:\n"
                                    "1 - Verificar informações\n"
                                    "2 - Depositar\n"
                                    "3 - Sacar\n"
                                    "0 - sair da conta\n"))
                
                match escolha:
                    case 1:
                        conta.verificar_infor()
                    
                    case 2:
                        valor = float(input("Digite o valor a ser depositado: "))

                        conta.deposito(valor)
                    
                    case 3:
                        valor = float(input("Digite o valor a ser sacado: "))

                        conta.sacar(valor)
                    
                    case 0:
                        break

                    case _:
                        print("Escolha inexistente")

        case 2:
            indetificador = randint(0, 10000)
            nome = input("Digite o nome da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))
            juros = float(input("Digite o valor de juros da conta: "))

            conta = Conta_poupança(indetificador, nome, saldo, juros)

            while True:
                escolha = int(input("Digite uma das opções:\n"
                                    "1 - Verificar informações\n"
                                    "2 - Depositar\n"
                                    "0 - sair da conta\n"))
                
                match escolha:
                    case 1:
                        conta.verificar_infor()
                    
                    case 2:
                        valor = float(input("Digite o valor a ser depositado: "))

                        conta.deposito(valor)
                    
                    case 0:
                        break

                    case _:
                        print("Escolha inexistente")

        case 0:
            break

        case _:
            print("Opções inexistente.")