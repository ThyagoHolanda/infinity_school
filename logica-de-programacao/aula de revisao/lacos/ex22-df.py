# Exercicio 22 - https://www.computersciencemaster.com.br/exercicios-lacos-de-repeticao/

pCarro = float(input("Qual o valor do carro: "))

while True:
    numParcelas = int(input("Deseja pagar em 1, 6, 12, 18, 24, 30, 36, 42, 48, 54 ou 60 vezes: "))
    if numParcelas == 1:
        desconto = pCarro * 0.2
        pFinal = pCarro - desconto

        print(f"Cliente optou por pagar à vista valor final é de: R$ {pFinal}")
        break

    elif numParcelas%6 != 0 or numParcelas < 6 or numParcelas > 60:
        print(f"Numero de parcelas não permitido!")
    else:
        percen = (numParcelas/2)/100
        juros = pCarro * percen

        pFinal = pCarro + juros
        vParcela = pFinal / numParcelas

        print(f"Preço final: R$ {pFinal}\n"
              f"Quantidade de parcelas : {numParcelas}\n"
              f"Valor da parcela: R$ {vParcela}")
        break

