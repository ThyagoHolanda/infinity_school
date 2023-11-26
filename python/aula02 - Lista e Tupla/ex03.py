# Crie uma lista de 10 posições
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

x = int(input("Digite um número: "))

# if lista.index(x) == x:
#     print(f"O número {x} está na posição {lista.index(x)} da lista")
# else:
#     print("O número não está na lista")

# print(lista.index(x))

cont = 0
for i in lista:
    
    if i == x:
        print(f"O número {x} está na posição {cont} da lista")
        break
    cont += 1

if cont >= len(lista):
    print("O número não está na lista")