print("Digite qualquer numero:")
numero = float(input())

if numero < 0:
    print(f"O numero {numero} é negativo!")
    print(f"O numero {numero} ao quadrado é {numero**2}")
elif numero > 0:
    # print(f"O numero {numero} é positivo!")
    if numero % 2 == 0:
        print(f"O numero {numero} é positivo e par!")
    else:
        print(f"O numero {numero} é positivo e impar!")
else:
    print(f"O numero é igual a 0.0!")