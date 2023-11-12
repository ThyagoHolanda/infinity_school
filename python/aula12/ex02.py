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
    def __init__(self, codigo, nome, saldo):
        self.codigo = codigo
        self.nome = nome
        self.saldo = saldo

    def verificar_informacoes():
        pass

    def deposito(valor):
        pass


class CC(Contas):
    def __init__(self, codigo, nome, saldo):
        super().__init__(codigo, nome, saldo)


    def sacar(valor):
        self.saldo -= valor

class CP(Contas):
    def __init__(self, codigo, nome, saldo):
        super().__init__(codigo, nome, saldo)

    def juros(valor):
        self.saldo += valor


        