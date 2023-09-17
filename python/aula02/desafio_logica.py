import random

# cleintes = list()

# while True:
#     print("1- Adicionar novo cliente.\n"
#           "0 - Encerrar")
#     escolha = int(input("Escolha uma opção: "))

#     match escolha:
#         case 1:
#             nome = input("Digite o nome do cliente: ")
#             numero = int(input("Digite o numero do cliente: "))
#             cleintes.append([nome, numero])

#         case 0:
#             break

# sorteio = random.randint(0, len(cleintes) - 1)

cleintes = [
    ["João", 123456789],
    ["Maria", 987654321],
    ["Pedro", 111111111],
    ["Ana", 222222222],
    ["Bia", 333333333],
]

sorteio = random.randint(0, len(cleintes) - 1)
print(len(cleintes))
print(sorteio)


# print(f"Nome do cliente: {cleintes[sorteio][0]}")
# print(f"Numero do cliente: {cleintes[sorteio][1]}")
