from operacoes import *

escolha = int(input("1 - Somar\n"
                    "2 - Subtrair\n"
                    "3 - Multiplicar\n"
                    "4 - Dividir\n"
                    "Escolha uma das opções acima: "))

numeros = list()

n = int(input(f"Informe o 1º numero: "))
numeros.append(n)

n = int(input(f"Informe o 2º numero: "))
numeros.append(n)

contador = 3
while True:
    parar = input("Deseja para S/N: ").upper()
    if parar == "N":
        break
    
    n = int(input(f"Informe o {contador}º numero: "))
    numeros.append(n)
    
    contador += 1

match escolha:
    case 1:
        resultado = soma(numeros)
        print(resultado)

    case 2:
        resultado = subtracao(numeros)
        print(resultado)
    
    case 3:
        resultado = multi(numeros)
        print(resultado)
    
    case 4:
        resultado = divisao(numeros)
        print(resultado)

# print(somar)
# print(sub)
# print(multiplicar)
# print(div)