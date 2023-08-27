maior_numero = 0
for i in range(3):
    numero = float(input(f"Informe o {i}º numero: "))

    if maior_numero < numero:
        maior_numero = numero 

print(maior_numero)

print("=========================")

i = 1
maior_numero = 0
while i < 4:
    numero = float(input(f"Informe o {i}º numero: "))

    if maior_numero < numero:
        maior_numero = numero 
    i += 1

print(maior_numero)