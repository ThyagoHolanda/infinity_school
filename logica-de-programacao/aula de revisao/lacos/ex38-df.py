# Exercicio 38 - https://www.computersciencemaster.com.br/exercicios-lacos-de-repeticao/

while True:

    primeira_escolha = int(input("1.Média aritimetica\n"
                                 "2.Média ponderada\n"
                                 "3.Sair\n"))
    
    if primeira_escolha >= 1 and primeira_escolha <= 2:
        print("\n")
        break
    
    elif primeira_escolha == 3:
        print("Você saiu do programa!")
        break
    
    else:
        print("\n")
        print("Opção invalida, escolha novamente!")

while primeira_escolha !=3:
    segunda_escolha = int(input("1.receber duas notas, calcular e mostrar a média aritmética.\n"
                                "2.receber três notas e seus respectivos pesos, calcular e mostrar a média ponderada.\n"
                                "3.sair do programa\n"))
    if segunda_escolha >= 1 and segunda_escolha <= 2:
        print("\n")
        break
    
    elif segunda_escolha == 3:
        print("Você saiu do programa!")
        break
    
    else:
        print("\n")
        print("Opção invalida, escolha novamente!")



if (primeira_escolha == 1 and segunda_escolha == 1) or (primeira_escolha == 2 and segunda_escolha == 1):
    n1 = float(input("Informe a 1ª nota: "))
    n2 = float(input("Informe a 2ª nota: "))
    soma = n1+n2
    media = soma/2
    print(f"A média aritimetica das notas é {media}")

elif (primeira_escolha == 1 and segunda_escolha == 2) or (primeira_escolha == 2 and segunda_escolha == 2):
    n1 = float(input("Informe a 1ª nota: "))
    p1 = float(input("Qual o peso desta nota: ")) 

    n2 = float(input("Informe a 2ª nota: "))
    p2 = float(input("Qual o peso desta nota: ")) 

    n3 = float(input("Informe a 3ª nota: "))
    p3 = float(input("Qual o peso desta nota: "))

    mediap = ((n1*p1) + (n2*p2) + (n3*p3)) / (p1+p2+p3)
    print(f"A média ponderada é {mediap}")