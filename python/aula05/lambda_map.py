# Metodo MAP
numeros = [1,2,3,4,5]

quadrados = list(map(lambda x: x % 2 == 0, numeros))

print(numeros)
print(quadrados)

print("="*30)
# ==============================

palavras = ["curso", "Thyago", "Edenia"]

palavras = list(map(lambda x: x.upper()[0], palavras))
print(palavras)

print("="*30)