# cod = float(input("Informe o código do empregado! "))
ano_nas = int(input("Informe o ano de nascimento do empregado! "))
ano_contrato = int(input("Informe o ano que o empregado foi contratado! "))

idade = 2023-ano_nas
tempo_trabalho = 2023-ano_contrato

print(f"Idade: {idade}")
print(f"Tempo trabalhado: {tempo_trabalho}")

if idade >= 65 or tempo_trabalho >= 30:
    print("Requerer aposentadoria")
    print(1)
elif idade >= 60 and tempo_trabalho >= 25:
    print("Requerer aposentadoria")
    print(2)
else:
    print("Não requerer")