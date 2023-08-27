palavra = input("Digite uma palavra qualquer: ")

while palavra != "pare":
    print(f"A palavra digitada foi: {palavra}")

    palavra = input("Digite uma nova palavra: ")

'''contador = 0

while True:
    print(f"Cotagem atual: {contador}")

    escolha = int(input("Digite 1 para continuar e 0 parta parar: "))

    match escolha:
        case 1:
            contador += 1
            continue
        case 0:
            break'''