# Exercicio 25 - https://www.computersciencemaster.com.br/exercicios-lacos-de-repeticao/

inicio = int(input("Qual o inicio do intervalo: "))
fim = int(input("Qual o final do intervalo: "))

# inicio = 1
# fim = 7
cont = 0

print("Os numero: ", end="")

if inicio > 0 and fim > 0 and fim > inicio:
    for inicio in range(inicio, fim+1):
        cont = 0

        for d in range(1, inicio+1):
            if inicio % d == 0:
                cont += 1 

        if cont <= 2:
            if inicio == fim:
                print(f"{inicio} ", end="")
            else:
                print(f"{inicio}, ", end="")
        

print("são primos!")

