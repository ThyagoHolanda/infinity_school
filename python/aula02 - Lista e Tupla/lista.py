# Lista vazia
'''lista_vazia = list()

print(lista_vazia)'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista[2:8:3]) # Mostra da posição 2 ao 7 de 3 em 3
print(lista[::-1]) # Mostra a lista invertida
print(lista[1:7:1]) # Mostra a lista de 1 a 7 de 1 em 1
print(lista[::-2]) # Mostra a lista invertida de 2 em 2
print(lista[:4]) # Mostra a lista até a posição 4
print(lista[4:]) # Mostra a lista a partir da posição 4

print("\n=================================")

lista[3] = "Jas"
print(lista) # Mostra a lista atualizada

print("\n=================================")

for i in lista:
    print(i) # Mostra os itens da lista

print("\n=================================")





