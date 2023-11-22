class Calculadora:
    def __init__(self, operacao):
        self.operacao = operacao
        self.expressao_separada = self.separar_numeros()

    def separar_numeros(self):
        expressao_separada = dict()
        contador = 1
        for i in self.operacao:
            if i not in "+-*/":
                expressao_separada[f"{contador}º numero"] = int(i)
                contador += 1
            else:
                expressao_separada["Operador"] = i

        return expressao_separada

    def somar(self):
        return self.expressao_separada["1º numero"] + self.expressao_separada["2º numero"]

    def subtrair(self):
        return self.expressao_separada["1º numero"] - self.expressao_separada["2º numero"]

    def multiplicacao(self):
        return self.expressao_separada["1º numero"] * self.expressao_separada["2º numero"]

    def divisao(self):
        return self.expressao_separada["1º numero"] / self.expressao_separada["2º numero"]


while True:
    expressao = input("Informe uma soma, subtração, multiplicação ou divisão entre 2 numeros: ")

    calcular = Calculadora(expressao)
    expressao_separada = calcular.separar_numeros()

    if expressao_separada["Operador"] == "+":

        resultado = calcular.somar()
        print(
            f"{expressao_separada['1º numero']} + {expressao_separada['2º numero']} = {resultado}\n")

    elif expressao_separada["Operador"] == "-":

        resultado = calcular.subtrair()
        print(
            f"{expressao_separada['1º numero']} - {expressao_separada['2º numero']} = {resultado}\n")

    elif expressao_separada["Operador"] == "*":

        resultado = calcular.multiplicacao()
        print(
            f"{expressao_separada['1º numero']} * {expressao_separada['2º numero']} = {resultado}\n")

    elif expressao_separada["Operador"] == "/":

        resultado = calcular.divisao()
        print(
            f"{expressao_separada['1º numero']} / {expressao_separada['2º numero']} = {resultado}\n")

    print("1 - Sim")
    print("2 - Não")
    escolha = int(input("Deseja continuar: "))
    print("\n"*3)
    if escolha == 2:
        print("Programa encerrado!")
        break
    elif escolha < 1 or escolha > 2:
        print("Escolha uma das opções acima!\n")