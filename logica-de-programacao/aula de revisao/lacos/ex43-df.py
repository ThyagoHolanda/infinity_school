# Exercicio 43 - https://www.computersciencemaster.com.br/exercicios-lacos-de-repeticao/

print("1. Novo salário\n"
      "2. Férias\n"
      "3. Décimo terceiro\n"
      "4. Sair\n")
escolha = int(input("Digite a opção desejada: "))

if escolha == 1:
    
    salario = float(input("informe seu salário: "))
    if salario <= 350:
        novo_salario = round(salario * 1.15, 2)
        print(f"Seu novo salário é R$ {novo_salario}")
    
    elif salario <= 600:
        novo_salario = round(salario * 1.10, 2)
        print(f"Seu novo salário é R$ {novo_salario}")

    elif salario > 600:
        novo_salario = round(salario * 1.05, 2)
        print(f"Seu novo salário é R$ { novo_salario}")

elif escolha == 2:
    
    salario = float(input("informe seu salário: "))
    ferias = round(salario * (1/3), 2)
    print(f"Você receberá R$ {ferias + salario}, onde R$ {ferias} é o acrescimo de 1/3 das férias!")

elif escolha == 3:
    
    salario = float(input("informe seu salário: "))
    while True:
        meses = int(input("Quantos meses foram trabalhados: "))
        if meses >= 0 and meses <= 12:
            break
        else:
            print("Quantidade de meses invalída!")

    decimo = (salario * meses) / 12
    print(f"Você receberá R$ {decimo} referente ao seu decimo terceiro!")

elif escolha == 4:
    print("Você saiu do programa!")