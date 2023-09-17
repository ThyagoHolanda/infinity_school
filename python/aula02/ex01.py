lista = list()

for i in range(0,12):
    lista.append(int(input(f"Digite o {i+1}º numero: ")))

print(lista)

escolha1 = int(input("Escolha a 1ª posição: "))
escolha2 = int(input("Escolha o 2ª posição: "))

soma = lista[escolha1] + lista[escolha2]

print(f"{lista[escolha1]} + {lista[escolha2]} = {soma}")