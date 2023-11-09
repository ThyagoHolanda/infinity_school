import random

print("Pense em um numero entre 0 e 100. Tentarei adivinhar.")
input("Aperte enter para começar!")

inicio_intervalo = 0
fim_intervalo = 100
contador = 0

while True:
    contador += 1


    guess = (fim_intervalo + inicio_intervalo)/2
    print(f"O numero que pensou é o {guess}?")
    escolha = int(input("1 - Sim\n"
                        "2 - Maior\n"
                        "3 - Menor"))
    if escolha == 1:
        print("Acertei!!!")
        break
    elif escolha == 2:
        inicio_intervalo = guess + 1
    elif escolha == 3:
        fim_intervalo = guess - 1
    else:
        print("Escolha uma das opções!")