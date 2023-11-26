''# Dicionario com nome de idades de pessoas
idade = {"thyago": 18, 
         "maria": 20, 
         "pedro": 21, 
         "joao": 18, 
         "hely": 19, 
         "joaquim": 17}

# Recebe o nome da pessoa a ser consultada
nome = input("Digite seu nome: ").lower()

# Verifica se o nome está no dicionário de idades
if nome in idade:
    # Imprime a idade da pessoa
    print(f"{nome} tem {idade[nome]} anos.")
else:
    # Imprime uma mensagem de erro caso o nome não exista no dicionário
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