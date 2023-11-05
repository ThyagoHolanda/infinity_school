class Calculadora:

    def __init__(self, numeros):
        self.numeros = numeros
    
    def soma(self):
        return sum(self.numeros)
    
    def subtracao(self):
        return self.numeros[0] - sum(self.numeros[1:])
    
    def multiplicacao(self):
        resultado = 1
        for i in self.numeros:
            resultado *= i
        return resultado
    
    def divisao(self):
        resultado = 0
        for i in range(0,len(self.numeros)):
            if i == 0:
                resultado = self.numeros[i]
            else:
                resultado /= self.numeros[i]
        return resultado
    
numeros = list()
contador = 0
numeros.append(float(input(f"Informe o {contador+1}º numero: ")))

continuar = 1
while True:
    contador += 1
    numeros.append(float(input(f"Informe o {contador+1}º numero: ")))

    continuar = int(input("Deseja informar mais numeros?\n"
                          "1 - Sim\n"
                          "0 - Não\n"))

    if continuar == 0:
        break



calculadora = Calculadora(numeros)

print("1 - Somar\n"
      "2 - Subtrair\n"
      "3 - Multiplicar\n"
      "4 - Dividir\n")
escolha = int(input("Digite a opcao desejada: "))

if escolha == 1:
    print(f"{calculadora.soma()}")
elif escolha == 2:
    print(f"{calculadora.subtracao()}")
elif escolha == 3:
    print(f"{calculadora.multiplicacao()}")
elif escolha == 4:
    print(f"{calculadora.divisao()}")
else:
    print("Escolha uma das opções informadas!")