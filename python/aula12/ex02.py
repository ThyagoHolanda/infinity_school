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

    # Return the values of nome, saldo, and tipo
    def verificar_informacoes(self):
        return self.nome, self.saldo, self.tipo

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
    def __init__(self, codigo, nome, saldo, tipo, juros):
        super().__init__(codigo, nome, saldo, tipo)
        self.juros = juros

    # Increase the saldo of the account
    def juros(self, valor):
        self.saldo += valor

# Ask the user to press enter to start the program
input("Precione enter para começar\n")
# Create an empty dictionary to store the accounts
contas = {}
# Create a variable to store the codigo
codigo = 1
# Create an infinite loop to run the program
while True:
    # Print the options for the user
    print("1 - Criar Conta-Corrente\n"
          "2 - Criar Conta-Poupança\n"
          "3 - Sacar\n"
          "4 - Depositar\n"
          "5 - Verificar informações\n"
          "0 - Sair")
    # Ask the user to input the option
    escolha = int(input("Escolha uma das opções acima: \n"))

    # Check the user's input and run the corresponding code
    match escolha:
        case 1:
            # Ask the user to input the name of the account holder
            nome = input("Informe o nome do titular da conta: ")
            # Set the initial balance to 0.00
            saldo = 0.00
            # Add the account to the dictionary
            contas[codigo] = CC(codigo, nome, saldo, "CC")
            # Increment the codigo
            codigo += 1

        case 2:
            # Ask the user to input the name of the account holder
            nome = input("Informe o nome do titular da conta: ")
            # Set the initial balance to 0.00
            saldo = 0.00
            juros = float(input("Digite o valor de juros da conta: "))
            # Add the account to the dictionary
            contas[codigo] = CP(codigo, nome, saldo, "CP", juros)
            # Increment the codigo
            codigo += 1

        case 3:
            # Ask the user to input the number of the account
            numero_conta = int(
                input("Qual o numero da conta que deseja sacar: "))
            # Check if the account exists in the dictionary
            if numero_conta in contas:
                # Get the type of the account
                tipo = contas[numero_conta].verificar_informacoes()[2]
                # Check if the account is a CC
                if tipo == "CC":
                    # Ask the user to input the amount to be withdrawn
                    valor = float(input("Qual o valor do saque: "))
                    # Withdraw the amount
                    saque = contas[numero_conta].sacar(valor)
                    # Print the result
                    print(saque)
                else:
                    # Print an error message
                    print("Saque somente permitido para Contas Correntes!")
                    input("Precione enter para continuar!")
                    # Ask the user to press enter
                    input("Precipe enter para continuar!")
                    # Print a blank line
                    print("\n"*30)
            else:
                # Print an error message
                print("Conta não existe!")
                input("Precione enter para continuar!")
                # Ask the user to press enter
                input("Precipe enter para continuar!")
                # Print a blank line
                input("Precipe enter para continuar!")
                # Print a blank line
                print("\n"*30)

        case 4:
            # Ask the user to input the number of the account
            numero_conta = int(
                input("Qual o numero da conta que deseja depositar: "))
            # Check if the account exists in the dictionary
            if numero_conta in contas:
                # Ask the user to input the amount to be deposited
                valor = float(input("Qual o valor do deposito: "))
                # Deposit the amount
                deposito = contas[numero_conta].deposito(valor)
                # Print the result
                print(deposito)
            else:
                # Print an error message
                print("Conta não existe!")
                input("Precione enter para continuar!")
                # Ask the user to press enter
                input("Precipe enter para continuar!")
                # Print a blank line
                input("Precipe enter para continuar!")
                # Print a blank line
                print("\n"*30)

        case 5:
            # Ask the user to input the number of the account or 0 to show all accounts
            numero_conta = int(input("Qual o numero da conta que deseja verificar (0 para mostrar todas as contas): "))
            # Check if the user input is 0
            if numero_conta <= 0:
                # Iterate through the dictionary and print the information of each account
                for i in contas:
                    verificar = contas[i].verificar_informacoes()
                    print(f"\nNumero: {i}\n"
                          f"Titular: {verificar[0]}\n"
                          f"Saldo: {verificar[1]}\n"
                          f"Tipo: {verificar[2]}\n")
            else:
                # Get the information of the account
                verificar = contas[numero_conta].verificar_informacoes()
                # Print the information
                print(f"\nTitular: {verificar[0]}\n"
                      f"Saldo: {verificar[1]}\n"
                      f"Tipo: {verificar[2]}\n")

        case 0:
            # Print a message to indicate the program is closing
            print("Programa fechado!")
            # Break out of the loop
            break
