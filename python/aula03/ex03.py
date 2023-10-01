cadastro = dict()
matricula = 0

while True:
    matricula += 1
    nome = input('Nome do aluno: ')
    idade = input('Idade do aluno: ')
    sexo = input('Sexo do aluno [M/F]: ').upper()[0]
    cadastro[matricula] = {'nome': nome, 'idade': idade, 'sexo': sexo}
    resposta = input('Deseja continuar? [S/N] ').upper()[0]
    if resposta == 'N':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"IDADE":>10}{"SEXO":>10}')
print('-'*30)
for k, v in cadastro.items():
    print(f'{k:<4}{v["nome"]:<10}{v["idade"]:>10}{v["sexo"]:>10}')

print('-='*30)

while True:
    print("1 - Adicionar novo aluno: \n"
          "2 - Ver todos os alunos: \n"
          "3 - Finaliar sistema: \n")
    escolha = int(input("Digite a opção desejada: "))
    if escolha == 1:
        matricula += 1
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        sexo = input("Digite o sexo do aluno [M/F]: ").upper()[0]

        cadastro[matricula] = [nome, idade, sexo]
    
    elif escolha == 2:
        print("-="*30)
        for k, v in cadastro.items():
            print(f"{k} - {v[0]} tem {v[1]} anos e é do sexo {v[2]}")
        print("-="*30)
    
    elif escolha == 3:
        print("Finalizando...")
        break

    else:
        print("Opção inválida!")

print("-="*30)
print("Volte sempre!")