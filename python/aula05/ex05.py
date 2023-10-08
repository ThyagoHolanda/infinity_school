nomes = ["Thyago", "Holanda", "Mont", "Lima"]

nomes_grandes = list(filter(lambda x: len(x) > 5, nomes))

print(nomes)
print(nomes_grandes)