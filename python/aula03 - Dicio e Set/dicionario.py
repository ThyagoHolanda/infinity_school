'''# Criando um dicionário
dicio = {
    "v1": 1,
    "v2": 2,
    "v3": 3,
    "v4": 4,
    "v5": 5
    }

print(f"Dicionario original: \n{dicio}\n")

# Criando um dicionário com lista de nomes
dicio["Nome"] = ["João", "Maria", "Pedro"]
print(f"Dicionario atualizado com lista de nomes: \n{dicio}\n")

# Alterando lista de nomes dentro do dicionário
dicio["Nome"][2] = "Bia"
print(f"Alterando lista de nomes dentro do dicionario: \n{dicio}\n")'''


print("=================================")


dicio2 = {
    0: "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
}
print(f"Dicionario original: \n{dicio2}\n")


print("=================================")
# Imprimindo chaves
for i in dicio2:
    print(f"Chave: {i}")


print("=================================")
# Imprimindo valores utilizando .values()
for j in dicio2.values():
    print(f"Valor: {j}")


print("=================================")
# Imprimindo valores e chaves utilizando f""
for i in range(5):
    print(f"O nome {dicio2[i]} foi adicionado na posicão {i}")

print("=================================")

