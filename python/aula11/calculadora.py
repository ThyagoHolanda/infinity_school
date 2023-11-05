"""
class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def soma(self):
        return self.numero1 + self.numero2
    
    def subtracao(self):
        return self.numero1 - self.numero2
    
    def multiplicacao(self):
        return self.numero1 * self.numero2
    
    def divisao(self):
        return self.numero1 / self.numero2

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

calculadora = Calculadora(numero1, numero2)

print("1 - Somar\n"
      "2 - Subtrair\n"
      "3 - Multiplicar\n"
      "4 - Dividir\n")
escolha = int(input("Digite a opcao desejada: "))

if escolha == 1:
    print(f"{numero1} + {numero2} = {calculadora.soma()}")
if escolha == 2:
    print(f"{numero1} - {numero2} = {calculadora.subtracao()}")
if escolha == 3:
    print(f"{numero1} * {numero2} = {calculadora.multiplicacao()}")
if escolha == 4:
    print(f"{numero1} / {numero2} = {calculadora.divisao()}")
else:
    print("Escolha uma das opções informadas!")

"""


class Calculadora:
    def __init__(self):
        while True:
            self.num1 = float(input("Digite o primeiro valor: "))
            self.num2 = float(input("Digite o segundo valor: "))

            self.operacao = int(input("Digite a operação: "))

            match self.operacao:
                case 1:
                    self.soma()
                case 2:
                    self.subtracao()
                case 3:
                    self.multiplicacao()
                case 4:
                    self.divisao()
                case 5:
                    break
                case _:
                    print("Operação inválida")
    def soma(self):
        print(self.num1 + self.num2)

    def subtracao(self):
        print(self.num1 - self.num2)

    def multiplicacao(self):
        print(self.num1 * self.num2)
    
    def divisao(self):
        print(self.num1 / self.num2)

calc = Calculadora()