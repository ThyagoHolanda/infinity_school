# Dicionario com nome de idades de pessoas
idade = {"Thyago": 18, "Maria": 20, "Pedro": 21, "Joao": 18, "Hely": 19, "Joaquim": 17}

nome = input("Digite seu nome: ")

if nome in idade:
    print(f"{nome} tem {idade[nome]} anos.")
else:
    print(f"{nome} não tem idade cadastrada.")


print("=================================")
# Outra forma de fazer
print(f"{nome} tem {idade.get(nome, 0)} anos.")

print("=================================")
# Outra forma de fazer
mensagem = idade.get(nome, 0)

if mensagem == 0:
    print(f"{nome} não tem idade cadastrada.")
else:
    print(f"{nome} tem {mensagem} anos.")