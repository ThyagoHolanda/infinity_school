valor_fabrica = float(input("Digite o valor de fabrica do carro"))

valor_dis = valor_fabrica * 0.28

valor_imposto = valor_fabrica * 0.45

valor_total = valor_fabrica + valor_dis + valor_imposto

print(f"O valor final do carro é de: R$ {valor_total}!")