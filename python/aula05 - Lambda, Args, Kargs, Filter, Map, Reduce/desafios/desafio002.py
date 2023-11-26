from functools import reduce

def calculadora(operador, *args, **kwargs):
    if operador == "+":
        resultado = reduce(lambda x, y: x + y, args)
    elif operador == "-":
        resultado = args[0] - reduce(lambda x, y: x + y, args[1:])
    elif operador == "*":
        resultado = 1
        for num in args:
            resultado *= num
    elif operador == "/":
        resultado = kwargs.get("divisor", 1)
        for num in args:
            resultado /= num
    else:
        return "Operador inválido"
    
    return resultado

# Testes
resultado_soma = calculadora("+", 5, 10, 15)
print("Soma:", resultado_soma)

resultado_subtracao = calculadora("-", 100, 30, 10)
print("Subtração:", resultado_subtracao)

resultado_multiplicacao = calculadora("*", 2, 3, 4, 5)
print("Multiplicação:", resultado_multiplicacao)

resultado_divisao = calculadora("/", 100, divisor=10)
print("Divisão:", resultado_divisao)

