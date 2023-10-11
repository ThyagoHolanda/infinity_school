def calculadora(*args, **kwargs):
    '''
    Exemplo de uso da calculadora:
    resultado = calculadora("+", 5, 10, 15)
    print(resultado)  # Saída: 30
    '''
    soma = 0
    for numero in args:
        soma += numero
    if kwargs:
        for chave, valor in kwargs.items():
            if chave == "soma":
                soma += valor
            elif chave == "subtracao":
                soma -= valor
            elif chave == "multiplicacao":
                soma *= valor
            elif chave == "divisao":
                soma /= valor
    return soma
