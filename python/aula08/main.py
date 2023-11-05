import datetime

imc = (lambda peso, altura: peso/altura**2)
quebra = lambda: print("\n" * 50)

paciente = dict()
id = 1

while True:
    print("\n1 - Cadastrar novo paciente\n"
        "2 - Ver todos os pacientes cadastrados\n"
        "3 - Apagar cadastro\n"
        "0 - Sair")
    escolha = int(input("Escolha uma das opções acima: \n"))

    match escolha:
        case 1:
            nome = input("\nQual o nome do paciente: ")
            data_nascimento = input("Qual a data de nascimento (dd/mm/aaa): ")
            peso = float(input("Qual o peso em kg: "))
            altura = float(input("Qual a altura em m: "))
            mt_internamento = input("Qual o motivo do internamento?\n")

            idade  = datetime.datetime.now().year - int(data_nascimento[6:])
            imc_paciente = imc(peso, altura)

            paciente[id] = {
                'nome': nome,
                'idade': idade,
                'imc': float(f"{imc_paciente:1f}"),
                'motivo_internamento': mt_internamento
            }
            
            id += 1

            input("Paciente cadastrado com sucesso! Pressione ENTER para continuar...")
            quebra()
        case 2:
            if len(paciente) == 0:
                print("Não há pacientes cadastrados!")
            else:
               for i in paciente.keys():
                   print(paciente[i])
            
            input("Pressione ENTER para continuar...")
            quebra()
        case 3:
            id_apagar = int(input("Digite o ID do paciente que deseja apagar: "))

            if len(paciente) == 0:
                print("Não há pacientes cadastrados!")
            elif id_apagar in paciente.keys():
                del paciente[id_apagar]
                print("Paciente apagado com sucesso!")
            else:
                print("ID inválido!")
            
            input("Pressione ENTER para continuar...")
            quebra()

        case 0:
            print("Saindo...")
            break
        case _:
            print("Opção inválida")