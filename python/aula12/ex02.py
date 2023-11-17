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

        self.addconta()

    def addconta(self):
        global contas
        global codigo

        contas[codigo] = {
            "titular": self.nome,
            "saldo": self.saldo,
            "tipo": self.tipo
        }
        codigo += 1

    @staticmethod
    def verificar_informacoes(numero):
        print(f"Titular: {contas[numero]['titular']}\n"
              f"Saldo: {contas[numero]['saldo']}\n"
              f"Tipo: {contas[numero]['tipo']}")

    def deposito(self, valor):
        self.saldo += valor


class CC(Contas):
    def __init__(self, codigo, nome, saldo, tipo):
        super().__init__(codigo, nome, saldo, tipo)

    def sacar(self, valor):
        self.saldo -= valor


class CP(Contas):
    def __init__(self, codigo, nome, saldo, tipo):
        super().__init__(codigo, nome, saldo, tipo)

    def juros(self, valor):
        self.saldo += valor


print("Precione enter para começar")
contas = {}
codigo = 1
while True:
    print("1 - Criar Conta-Corrente\n"
          "2 - Criar Conta-Poupança\n"
          "3 - Sacar\n"
          "4 - Depositar\n"
          "5 - Verificar informações\n"
          "0 - Sair")
    escolha = int(input("Escolha uma das opções acima: "))

    match escolha:
        case 1:
            nome = input("Informe o nome do titular da conta: ")
            saldo = 0.00
            nova_CC = CC(codigo, nome, saldo, "CC")
            print(contas)
            
        case 2:
            nome = input("Informe o nome do titular da conta: ")
            saldo = 0.00
            nova_CP = CP(codigo, nome, saldo, "CP")
            print(contas)
        
        case 3:
            pass
        
        case 4:
            pass
        
        case 5:
            numero_conta = int(input("Qual o numero da conta que deseja verificar: "))
            Contas.verificar_informacoes(numero_conta)
            pass
        
        case 0:
            print("Programa fechado!")
            break