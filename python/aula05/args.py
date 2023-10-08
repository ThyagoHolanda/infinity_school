def media(*args):
    soma = 0
    cont = 0

    for i in args:
        soma += i
        cont += 1

    media = soma / cont

    print(media)

print("1 - Media 3 notas\n"
      "2 - Media 4 notas\n"
      "3 - Media 5 notas\n")
escolha = int(input("Escolha uma das opções acima: "))

n1 = float(input("Digite o valor: "))
n2 = float(input("Digite o valor: "))
n3 = float(input("Digite o valor: "))

match escolha:
    case 1:
        media(n1,n2,n3)

    case 2:
        n4 = float(input("Digite o valor: "))
        media(n1,n2,n3,n4)

    case 3:
        n4 = float(input("Digite o valor: "))
        n5 = float(input("Digite o valor: "))
        media(n1,n2,n3,n4,n5)