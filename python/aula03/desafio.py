pacientes = dict()
id = 1

while True:
    print("1 - Cadastra paciente;\n"
          "2 - Ver todos os pacientes;\n"
          "3 - Apagar pacientes;\n"
          "0 - Finalizar sistema;\n")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        peso = float(input("Digite o peso do paciente em kg: "))
        altura = float(input("Digite a altura do paciente em cm: "))

        pacientes[id] = [nome, idade, peso, altura]
        id += 1

    elif opcao == 2:
        print("Pacientes cadastrados")
        print("-"*30)
        for i, p in pacientes.items():
            print(f"Cod {i}: O paciente {p[0]} tem {p[1]} anos com {p[2]} kg e {p[3]} cm de altura")
        print("-"*30)

    elif opcao == 3:
        id_apagar = int(input("Digite o id do paciente que deseja apagar: "))
        del pacientes[id_apagar]

    elif opcao == 0:
        print("Sistema finalizado!")
        break
