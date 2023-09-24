agenda = dict()

while True:
    print("1- Adicionar novo numero.\n"
          "0 - Encerrar")
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            nome = input("Digite o nome do cliente: ")
            numero = int(input("Digite o numero do Cliente: "))
            agenda[nome] = numero
        case 0:
            break

print(agenda)

# outra forma de fazer

while True:
    print("1- Adicionar novo numero.\n"
          "0 - Encerrar")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = input("Digite o nome do cliente: ")
        numero = int(input("Digite o numero do Cliente: "))
        agenda[nome] = numero
    elif escolha == 0:
        break

print(agenda)