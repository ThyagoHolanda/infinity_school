# Tupla vazia
tupla = ()
tupla = tuple()

tupla = (1,2,3,4,5,6)
print(tupla[2])

for i in tupla:
    print(i)

# Adicionar valor a tupla
tupla += (7,8,9,10,9,8,7,6,8,5,4,3,1)
print(tupla)

# Função de tupla
    # Exemplo de count

print(tupla.count(1)) #Conta quantas vezes o numero 1 aparece

    # Exemplo de index

print(tupla.index(1)) # Retorna a posição do valor

# Tupla + lista
tupla = ([1,2,3,4,5,6],[1,2,3,4,5,6])