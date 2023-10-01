cadastro = dict()
matricula = 0

'''
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
'''

# Outra forma
'''
while True:
    print("1 - Adicionar novo aluno: \n"
          "2 - Ver todos os alunos: \n"
          "0 - Finaliar sistema: \n")
    escolha = int(input("Digite a opção desejada: "))

    if escolha == 1:
        matricula += 1
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        sexo = input("Digite o sexo do aluno [M/F]: ").upper()[0]

        # cadastro[matricula] = [nome, idade, sexo]

        cadastro[matricula] = {
            'nome': nome, 
            'idade': idade, 
            'sexo': sexo
            }
    
    elif escolha == 2:
        print("-="*30)
        for k, v in cadastro.items():
            print(f"Cod: {k} - {v['nome']} tem {v['idade']} anos e é do sexo {v['sexo']}")
        print("-="*30)
    
    elif escolha == 0:
        print("Finalizando...")
        break

    else:
        print("Opção inválida!")

print("-="*30)
print("Volte sempre!")
'''

while True:
    print("1 - Adicionar novo aluno: \n"
          "2 - Ver todos os alunos: \n"
          "0 - Finaliar sistema: \n")
    escolha = int(input("Digite a opção desejada: "))

    if escolha == 1:
        matricula += 1
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        sexo = input("Digite o sexo do aluno [M/F]: ").upper()[0]

        while sexo not in ['M', 'F']:
            sexo = input("Digite o sexo do aluno [M/F]: ").upper()[0]

        # cadastro[matricula] = [nome, idade, sexo]

        cadastro[matricula] = {
            'nome': nome, 
            'idade': idade, 
            'sexo': sexo
            }
    
    elif escolha == 2:
        print("-="*30)
        for k, v in cadastro.items():
            print(f"Cod: {k} - {v['nome']} tem {v['idade']} anos e é do sexo {v['sexo']}")
        print("-="*30)
    
    elif escolha == 0:
        print("Finalizando...")
        break

    else:
        print("Opção inválida!")

print("-="*30)
print("Volte sempre!")