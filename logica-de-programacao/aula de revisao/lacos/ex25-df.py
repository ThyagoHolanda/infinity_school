# Exercicio 25 - https://www.computersciencemaster.com.br/exercicios-lacos-de-repeticao/

n = int(input("Digite um numero: "))
res = 1

if n == 0:
    print(f"0! = 1")

else:
    for i in range(1, n+1):
        res *= i
            
    print(f"{n}! = {res}")