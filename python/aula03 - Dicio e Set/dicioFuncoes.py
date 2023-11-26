#  Funções para manipular dicionários

# Exemplo de keys e values

dicio = {
    0: "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
}

print(dicio)

'''print(dicio.keys())
print(dicio.values())'''

print("\n=================================")

# Exemplos de items e del

'''print(dicio.items())
del dicio[2]
print(dicio.items())'''

print("\n=================================")

# Exemplo de copy e clear

'''nDicio = dicio.copy()
dicio.clear()

print(nDicio)
print(dicio)'''

print("\n=================================")

# Exemplo de get e pop

print(dicio.get(5, "Erro"))
print(dicio.pop(1, "Erro"))

print(dicio)

print("\n=================================")
