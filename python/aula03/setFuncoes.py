# Funções de set

nomes_unicos = {"Joaquim", "Maria", "Thyago", "Pedro", "Joao", "Hely"}
print(nomes_unicos)

'''# Exemplo de remove

nomes_unicos.remove("Pedro")
print(nomes_unicos)

print("===============================")

# Exemplo de discard

nomes_unicos.discard("Maria")
print(nomes_unicos)

print("===============================")'''

# Exemplo de pop

for i in range(len(nomes_unicos)-1):
    nomes_unicos.pop()
    print(nomes_unicos)

print("===============================")
