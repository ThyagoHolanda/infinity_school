import random
lista = []

for i in range(20):
    lista.append(random.randint(-50, 50))

print(lista)

for i in range(len(lista)):
    if lista[i] <= 0:
        lista[i] = 0

print(lista)