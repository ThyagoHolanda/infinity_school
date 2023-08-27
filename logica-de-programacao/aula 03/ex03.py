soma = 0
media = 0
for i in range(1, 6, 1):
    numero = float(input(f"Informe o {i}º numero: "))
    soma += numero

media = soma / i
print(f"A soma dos numeros digitados é: {soma}\n"
      f"A média dos mesmos numeros é: {media}")

print("================")

i = 1
while i < 6:
    numero = float(input(f"Informe o {i}º numero: "))
    soma += numero
    i += 1

media = soma / (i-1)
print(f"A soma dos numeros digitados é: {soma}\n"
      f"A média dos mesmos numeros é: {media}")
