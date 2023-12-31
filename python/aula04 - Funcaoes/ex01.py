'''
def conversao(seg):
    hora = round((seg/60)/60)
    minuto = round((seg/60)%60)
    segundo = round((seg%60)%60)

    return f"{hora}h {minuto}m {segundo}s"


seg = int(input("Tempo em segundos: "))
tempo = conversao(seg)
print(tempo)

print("="*30)

'''


def conversao(seg):
    hora = seg//3600
    minuto = (seg//60)%60
    segundo = (seg%60)%60

    return hora, minuto, segundo


seg = int(input("Tempo em segundos: "))

hora, min, seg = conversao(seg)

print("="*30)
print(f"{hora}:{min}:{seg}")


'''
def funcionamento(seg): #3601
    # 1h -> 3600seg
    # 1min -> 60seg
    # 1s -> 1s
    horas = seg // 3600 # horas = 1

    seg -= horas * 3600 # seg -= 1 * 3600 = 1

    min = seg // 60

    seg -= min * 60

    return f"{horas}:{min}:{seg}"

seg = int(input("Digite a quantidade de tempo de funcionamento em segundos: "))

tempo = funcionamento(seg)

print(tempo)
'''