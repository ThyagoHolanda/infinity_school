continuar = 1
quebra = "\n"*2
while continuar == 1:
    numero_bin = input(
        "Informe 8 digitos entre 1 e 0 para ser convertido em Decimal: ")

    if len(numero_bin) > 8:
        print("Deve ser informado no máximo 8 digitos!")

    else:
        for i in numero_bin:
            if int(i) < 0 or int(i) > 1:
                print("Os digitos dever ser 0 ou 1!")
            else:

                numero_dec = 0
                acumulador = len(numero_bin)-1
                for i in numero_bin:
                    # print(f"{i}*2**{acumulador} = {int(i)*2**acumulador}")
                    # print(f"Acumulador = {acumulador}")
                    numero_dec += int(i)*2**acumulador
                    acumulador -= 1
                    # print(f"bin = {numero_bin}")
                    # print("="*30)
                break
    print(quebra)

    print(f"O numero {numero_bin} em decimal é {numero_dec}")

    print(quebra)

    print("1 - Sim\n"
          "0 - Não\n")
    continuar = int(input("Deseja continuar?\n"))
