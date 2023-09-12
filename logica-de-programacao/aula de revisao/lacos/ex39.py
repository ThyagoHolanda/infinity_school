cod = 1
valor_acc = 0
mes = 0
while cod != 0:
    cod = int(input("Qual o código do cliente: "))
    
    while True:
        print("1.Poupança\n2.Poupança plus\n3.Fundos de renda")
        conta = int(input("Digite a opção desejada: "))

        if conta >= 1 and conta <= 3:
            break
        else:
            print("\nopção inválida. Escolha novamente!")

    mes += 1
    valor_investimento = float(input(f"Quanto irá investir no {mes}º mês: "))

    if conta == 1:
        valor_acc = round((valor_investimento + valor_acc) * 1.015, 2)
        print(f"Aporte = R$ {valor_investimento}\n"
              f"Valor acumulado = R$ {valor_acc}")
        
    elif conta == 2:
        valor_acc = round((valor_investimento + valor_acc) * 1.02, 2)
        print(f"Aporte = R$ {valor_investimento}\n"
              f"Valor acumulado = R$ {valor_acc}")
    
    elif conta == 3:
        valor_acc = round((valor_investimento + valor_acc) * 1.04, 2)
        print(f"Aporte = R$ {valor_investimento}\n"
              f"Valor acumulado = R$ {valor_acc}")
