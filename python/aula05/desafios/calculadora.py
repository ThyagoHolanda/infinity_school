import datetime

def ano_bissextos(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


def dias_mes(mes, bissextos=False):
    quant_dias_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
    }
    if bissextos == True and mes == 2:
        quant_dias_mes[2] = 29

    return quant_dias_mes[mes]


def verificar_data(dia, mes, ano):

    if ano <= 0 or mes <= 0 or mes > 12 or dia <= 0 or dia > dias_mes(mes, ano_bissextos(ano)):
        return False

    return True

def quantidade_ano_bissextos(ano_atual, ano):
    acumulador = 0
    for i in range(ano_atual-ano):
        acumulador += 1 if ano_bissextos(ano) == True else 0
        ano += 1
    
    return acumulador


def conversao(dia, mes, ano):
    data_atual = datetime.date.today()
    ano_atual = data_atual.year
    mes_atual = data_atual.month
    dia_atual = data_atual.day

    if verificar_data(dia, mes, ano) == True:
        d_ano = ((ano_atual - ano) * 365) + quantidade_ano_bissextos(ano_atual, ano)
        d_mes = (mes_atual - mes) * 30
        d_dia = (dia_atual - dia) + 1
        return d_dia + d_mes + d_ano
    else:
        return False


dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

print(conversao(dia, mes, ano))
