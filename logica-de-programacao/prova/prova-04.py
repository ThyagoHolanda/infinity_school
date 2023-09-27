cont = 0
soma = 0
while True:
    numero = int(input('Digite um número (0 para sair): '))

    if numero <= 0:
        break
    
    cont += 1
    soma += numero

print(f'Você digitou {cont} números e a soma deles foi {soma} e a média é {soma/cont}')