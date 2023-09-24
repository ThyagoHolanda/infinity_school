# Crie 3 listas com 9 numeros aleatorios cada.

from random import randint

lista1 = list()
lista2 = list()
lista3 = list()

for i in range(0, 9):
    lista1.append(randint(0, 100))
    lista2.append(randint(0, 100))
    lista3.append(randint(0, 100))

# print(lista1)
# print(lista2)
# print(lista3)

lista_join = list()

lista_join += lista1[:3] + lista2[3:-3] + lista3[6:]
print(lista_join)

# Agora utilizando um laço

lista_join2 = list()
for i in range(0, 9):
    if i / 3 < 1:
        lista_join2.append(lista1[i])
    elif i / 3 < 2:
        lista_join2.append(lista2[i])
    elif i / 3 < 3:
        lista_join2.append(lista3[i])

print(lista_join2)

