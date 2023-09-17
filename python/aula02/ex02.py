lista = list()

while True:
    numero = int(input('Digite um número: '))

    if numero%2 != 0:
        lista.append(numero)

    if len(lista) == 10:
        print(lista)
        break

