numero = int(input("Informe qual numero deseja ver a tabuada: "))

for i in range(11):
    soma = numero + i
    print(f"{numero} + {i} = {soma}")

print("====================")

i = 0
while i < 11:
    soma = numero + i
    print(f"{numero} + {i} = {soma}")
    i += 1