def verificar_1_0(bin):
    for i in bin:
        if int(i) < 0 or int(i) > 1:
            return False
    
    return True

def verificar(bin):
    if len(bin) == 0:
        mensagem = "Nenhum digito informado!"
        return False, mensagem
    elif len(bin) > 8:
        mensagem = "Digite no máximo 8 digitos!"
        return False, mensagem
    elif verificar_1_0(bin) == False:
        mensagem = "Os digitos dever ser 0 ou 1!"
        return False, mensagem
    else:
        return True
        
        

continuar = 1
quebra = "\n"*2
while continuar == 1:
    numero_bin = input(
        "Informe 8 digitos entre 1 e 0 para ser convertido em Decimal: ")

    if verificar(numero_bin) == True:
        numero_dec = 0
        acumulador = len(numero_bin)-1
        for i in numero_bin:
            # print(f"{i}*2**{acumulador} = {int(i)*2**acumulador}")
            # print(f"Acumulador = {acumulador}")
            numero_dec += int(i)*2**acumulador
            acumulador -= 1
            # print(f"bin = {numero_bin}")
            # print("="*30)
        
        print(quebra)

        print(f"O numero {numero_bin} em decimal é {numero_dec}")

        print(quebra)


    elif verificar(numero_bin)[0] == False:
        print(verificar(numero_bin)[1])



    print("1 - Sim\n"
        "0 - Não\n")
    continuar = int(input("Deseja continuar?\n"))
