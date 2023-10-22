def soma(numeros):
    return sum(numeros)

def subtracao(numeros):
    return numeros[0] - sum(numeros[1:])

def multi(numeros):
    acumulador = 1
    for i in numeros:
        acumulador *= i
    return acumulador

def divisao(numeros):
    acumulador = 0
    for i in range(0,len(numeros)):
        if i == 0:
            acumulador = numeros[i]
        else:
            acumulador /= numeros[i]

    return acumulador

