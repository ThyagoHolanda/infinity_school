#  Exercicio 12 - https://www.computersciencemaster.com.br/exercicios-if-e-else/

salario = float(input("Qual o valor da hora do funcionario: "))
horas = float(input("Quantas horas esse funacionario trabalhou neste mês: "))
salario_bruto = salario * horas

inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11

if salario_bruto <= 900:

    ir = salario_bruto * 0
    total_desconto = ir+inss
    salario_liquido = salario_bruto - total_desconto

    print(f"Salário Bruto: {salario_bruto}\n"
          f"( - ) IR (0%): R$ {ir}\n"
          f"( - ) INSS (10%): R$ {inss}\n"
          f"( - ) FGTS (11%): R$ {fgts}\n"
          f"Total de descontos: R$ {total_desconto}\n"
          f"Salário Líquido: {salario_liquido}")
    
elif salario_bruto <= 1500:

    ir = salario_bruto * 0.05
    total_desconto = ir+inss
    salario_liquido = salario_bruto - total_desconto

    print(f"Salário Bruto: {salario_bruto}\n"
          f"( - ) IR (5%): R$ {ir}\n"
          f"( - ) INSS (10%): R$ {inss}\n"
          f"( - ) FGTS (11%): R$ {fgts}\n"
          f"Total de descontos: R$ {total_desconto}\n"
          f"Salário Líquido: {salario_liquido}")
    
elif salario_bruto <= 2500:

    ir = salario_bruto * 0.10
    total_desconto = ir+inss
    salario_liquido = salario_bruto - total_desconto

    print(f"Salário Bruto: {salario_bruto}\n"
          f"( - ) IR (10%): R$ {ir}\n"
          f"( - ) INSS (10%): R$ {inss}\n"
          f"( - ) FGTS (11%): R$ {fgts}\n"
          f"Total de descontos: R$ {total_desconto}\n"
          f"Salário Líquido: {salario_liquido}")

elif salario_bruto > 2500:

    ir = salario_bruto * 0.20
    total_desconto = ir+inss
    salario_liquido = salario_bruto - total_desconto

    print(f"Salário Bruto: {salario_bruto}\n"
          f"( - ) IR (20%): R$ {ir}\n"
          f"( - ) INSS (10%): R$ {inss}\n"
          f"( - ) FGTS (11%): R$ {fgts}\n"
          f"Total de descontos: R$ {total_desconto}\n"
          f"Salário Líquido: {salario_liquido}")