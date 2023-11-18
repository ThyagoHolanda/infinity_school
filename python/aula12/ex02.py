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


class Contas:
    def __init__(self, codigo, nome, saldo, tipo):
        self.codigo = codigo
        self.nome = nome
        self.saldo = saldo
        self.tipo = tipo

    def verificar_informacoes(self):
        return self.nome, self.saldo, self.tipo

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de {valor} realizado. Novo saldo: {self.saldo}"


class CC(Contas):
    def __init__(self, codigo, nome, saldo, tipo):
        super().__init__(codigo, nome, saldo, tipo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de {valor} realizado. Novo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente para saque."

class CP(Contas):
    def __init__(self, codigo, nome, saldo, tipo):
        super().__init__(codigo, nome, saldo, tipo)

    def juros(self, valor):
        self.saldo += valor


input("Precione enter para começar\n")
contas = {}
codigo = 1
while True:
    print("1 - Criar Conta-Corrente\n"
          "2 - Criar Conta-Poupança\n"
          "3 - Sacar\n"
          "4 - Depositar\n"
          "5 - Verificar informações\n"
          "0 - Sair")
    escolha = int(input("Escolha uma das opções acima: \n"))

    match escolha:
        case 1:
            nome = input("Informe o nome do titular da conta: ")
            saldo = 0.00
            contas[codigo] = CC(codigo, nome, saldo, "CC")
            codigo += 1

        case 2:
            nome = input("Informe o nome do titular da conta: ")
            saldo = 0.00
            contas[codigo] = CP(codigo, nome, saldo, "CP")
            codigo += 1

        case 3:
            numero_conta = int(
                input("Qual o numero da conta que deseja sacar: "))
            if numero_conta in contas:
                tipo = contas[numero_conta].verificar_informacoes()[2]
                if tipo == "CC":
                    valor = float(input("Qual o valor do saque: "))
                    saque = contas[numero_conta].sacar(valor)
                    print(saque)
                else:
                    print("Saque somente permitido para Contas Correntes!")
                    input("Precione enter para continuar!")
                    print("\n"*30)
            else:
                print("Conta não existe!")
                input("Precione enter para continuar!")
                print("\n"*30)

        case 4:
            numero_conta = int(
                input("Qual o numero da conta que deseja depositar: "))
            if numero_conta in contas:
                valor = float(input("Qual o valor do deposito: "))
                deposito = contas[numero_conta].deposito(valor)
                print(deposito)
            else:
                print("Conta não existe!")
                input("Precione enter para continuar!")
                print("\n"*30)

        case 5:
            numero_conta = int(input("Qual o numero da conta que deseja verificar (0 para mostrar todas as contas): "))
            if numero_conta <= 0:
                for i in contas:
                    verificar = contas[i].verificar_informacoes()
                    print(f"\nNumero: {i}\n"
                          f"Titular: {verificar[0]}\n"
                          f"Saldo: {verificar[1]}\n"
                          f"Tipo: {verificar[2]}\n")
            else:
                verificar = contas[numero_conta].verificar_informacoes()
                print(f"\nTitular: {verificar[0]}\n"
                    f"Saldo: {verificar[1]}\n"
                    f"Tipo: {verificar[2]}\n")

        case 0:
            print("Programa fechado!")
            break
