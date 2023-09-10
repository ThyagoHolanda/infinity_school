# Exercicio 11 - https://www.computersciencemaster.com.br/exercicios-if-e-else/

salario = float(input("Qual o salário do empregado: "))

print("==============================================")

if salario <= 280:
    valor_acrescimo = salario * 0.20
    salario_atualizado = salario + valor_acrescimo

    print(f"Salário antes do reajuste: {salario}.\n"
          f"Ese funcionario teve um aumento de 20%, ou seja foi acrescentado R$ {valor_acrescimo} em seu salário.\n"
          f"Assim o novo salário é: R$ {salario_atualizado}.")
    
elif salario < 700:
    valor_acrescimo = salario * 0.15
    salario_atualizado = salario + valor_acrescimo

    print(f"Salário antes do reajuste: {salario}.\n"
          f"Ese funcionario teve um aumento de 15%, ou seja foi acrescentado R$ {valor_acrescimo} em seu salário.\n"
          f"Assim o novo salário é: R$ {salario_atualizado}.")
    
elif salario < 1500:
    valor_acrescimo = salario * 0.10
    salario_atualizado = salario + valor_acrescimo

    print(f"Salário antes do reajuste: {salario}.\n"
          f"Ese funcionario teve um aumento de 10%, ou seja foi acrescentado R$ {valor_acrescimo} em seu salário.\n"
          f"Assim o novo salário é: R$ {salario_atualizado}.")
    
elif salario >= 1500:
    valor_acrescimo = salario * 0.05
    salario_atualizado = salario + valor_acrescimo
    
    print(f"Salário antes do reajuste: {salario}.\n"
          f"Ese funcionario teve um aumento de 5%, ou seja foi acrescentado R$ {valor_acrescimo} em seu salário.\n"
          f"Assim o novo salário é: R$ {salario_atualizado}.")