# Exercicio 4 - https://www.computersciencemaster.com.br/exercicios-lacos-de-repeticao/

# n = int(input("Digite um numero inteiro e positivo: "))

# s = 0

# texto = ""

# if n > 0:
#     for i in range(1, n+1):
#         div = 1 / i

#         s += div

#         if i == 1:
#             texto += "1"
#         else:
#             texto += f" + 1/{i}"

    
#     print(f"Valor final é de: S = {texto} = {s}")

# else:
#     print("Numero indicado é menor ou igual a zero, tente novamente.")

n = int(input("Digite um numero inteiro e positivo: "))
s = 0

print("S =", end="")
if n > 0:
    for i in range(1, n+1):
        div = 1 / i

        s += div

        if i == 1:
            print(" 1", end="")
        else:
            print(f" + 1/{i}", end="")

    
    print(f" = {s}")

else:
    print("Numero indicado é menor ou igual a zero, tente novamente.")