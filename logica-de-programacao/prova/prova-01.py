nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura em cm: '))
maior = idade > 18

print(f"Olá {nome}. Então você tem {altura} de altura com {idade} anos e {'é maior de idade' if maior else 'é menor de idade'}.")