numero = int(input("Digite um número inteiro entre 1 e 10: "))

if numero >= 1 and numero <= 10:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido")