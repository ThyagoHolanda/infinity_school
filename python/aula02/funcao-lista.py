# Funções para listas

lista = [4, 3, 2, 1, 5, 6, 8, 9, 10]
print(f"Lista inicial: {lista}")

    # Exemplos de append, insert
print("\n=================================")
lista.append(51) # Adiciona o item "51" na lista
lista.insert(0, 50) # Insere o item "50" na posição 1
print(lista) # Mostra a lista atualizada

    # Exemplos de pop, del e remove
print("\n=================================")

lista.pop(2) # Remove o item na posição 2
del(lista[1:3]) # Remove os itens na posição 1 e 2
lista.remove(1) # Remove o item na posição 0
print(lista) # Mostra a lista atualizada

    # Exemplo de sort
print("\n=================================")

lista.sort() # Ordena a lista
print(lista) # Mostra a lista atualizada

    # Exemplo de reverse
print("\n=================================")

lista.reverse() # Inverte a lista
print(lista) # Mostra a lista atualizada

    # Exemplo de len
print("\n=================================")

print(len(lista)) # Mostra a quantidade de itens na lista

    # Exemplo de clear
print("\n=================================")

lista.clear() # Limpa a lista
print(lista) # Mostra a lista atualizada