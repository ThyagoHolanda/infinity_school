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
    # Initialize the class with the parameters of codigo, nome, saldo, and tipo
    def __init__(self, codigo, nome, saldo, tipo):
        self.codigo = codigo
        self.nome = nome
        self.saldo = saldo
        self.tipo = tipo

        self.adicionar()

    def adicionar(self):
        global contas
        global codigo
        contas[codigo] = {
            "nome": self.nome,
            "saldo": self.saldo,
            "tipo": self.tipo
        }
        codigo += 1

    # Return the values of nome, saldo, and tipo
    def verificar_informacoes(self):
        for i in contas:
            print(contas[i])
        return f"Código: {self.codigo}\nNome: {self.nome}"

    # Increase the saldo of the account
    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de {valor} realizado. Novo saldo: {self.saldo}"


# Create a subclass of Contas called CC
class CC(Contas):
    # Initialize the class with the parameters of codigo, nome, saldo, and tipo
    def __init__(self, codigo, nome, saldo, tipo):
        super().__init__(codigo, nome, saldo, tipo)

    # Decrease the saldo of the account
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de {valor} realizado. Novo saldo: {self.saldo}"
        else:
            return "Saldo insuficiente para saque."

# Create a subclass of Contas called CP


class CP(Contas):
    # Initialize the class with the parameters of codigo, nome, saldo, and tipo
    def __init__(self, codigo, nome, saldo, tipo):
        super().__init__(codigo, nome, saldo, tipo)

    # Increase the saldo of the account
    def juros(self, valor):
        self.saldo += valor


contas = dict()
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
            print("Criar Conta-Corrente")
            nome = input("Digite o nome do titular: ")
            saldo = 0.00
            nova_cc = Contas(codigo, nome, saldo, "CC")
            print(f"Conta-Corrente criada com sucesso!\n")

        case 2:
            print("Criar Conta-Poupança")
            nome = input("Digite o nome do titular: ")
            saldo = 0.00
            nova_cp = Contas(codigo, nome, saldo, "CP")
            print(f"Conta-Poupança criada com sucesso!\n")

        case 3:
            print("Sacar")
            codigo = int(input("Digite o código da conta: "))
            valor = float(input("Digite o valor do saque: "))
            if contas[codigo]["tipo"] == "CC":
                nova_cc.sacar(valor)
            elif contas[codigo]["tipo"] == "CP":
                nova_cp.sacar(valor)
            else:
                print("Conta não encontrada!")
        
        case 4:
            print("Depositar")
            codigo = int(input("Digite o código da conta: "))
            valor = float(input("Digite o valor do depósito: "))
            if contas[codigo]["tipo"] == "CC":
                nova_cc.deposito(valor)
            elif contas[codigo]["tipo"] == "CP":
                nova_cp.deposito(valor)
            else:
                print("Conta não encontrada!")
        
        case 5:
            print("Verificar informações")
            codigo = int(input("Digite o código da conta: "))
            if contas[codigo]["tipo"] == "CC":
                nova_cc.verificar_informacoes()
            elif contas[codigo]["tipo"] == "CP":
                nova_cp.verificar_informacoes()
            else:
                print("Conta não encontrada!")
        
        case 0:
            print("Sair")
            break