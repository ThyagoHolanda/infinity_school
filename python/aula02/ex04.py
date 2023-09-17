# Crie uma lista de 20 numeros aleatorios

import random
lista = []

for i in range(20):
    lista.append(random.randint(1, 100))

print(lista)

par = 0
for i in lista:
    if i % 2 == 0:
        print(f'{i} é par')
        par += 1

print(f'A lista tem {len(lista)} numeros e {par} são pares')