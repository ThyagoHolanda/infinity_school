agenda = dict()

while True:
    print("1 - Adicionar novo numero.\n"
          "2 - Ver todos os contatos.\n"
          "0 - Encerrar.")
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            nome = input("Digite o nome do cliente: ")
            numero = int(input("Digite o numero do Cliente: "))
            agenda[nome] = numero

        case 2:
            print("Contatos:")
            print("-"*30)
            for nome, numero in agenda.items():
                print(f"{nome} - {numero}")
            print("-"*30)
        case 0:
            break
print("="*30)
print(agenda)

# outra forma de fazer

while True:
    print("1 - Adicionar novo numero.\n"
          "2 - Ver todos os contatos.\n"
          "0 - Encerrar")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = input("Digite o nome do cliente: ")
        numero = int(input("Digite o numero do Cliente: "))
        agenda[nome] = numero

    elif escolha == 2:
        print("Contatos:")
        print("-"*30)
        for nome, numero in agenda.items():
            print(f"{nome} - {numero}")
        print("-"*30)
    elif escolha == 0:
        break
print("="*30)
print(agenda)
