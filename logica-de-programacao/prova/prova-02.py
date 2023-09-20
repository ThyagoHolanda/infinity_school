velocidade = float(input("Qual a velocidade do carro? "))

if velocidade > 80:
    print("Você foi multado!")
    #valor da multa é R$ 20 por cada km acima dos 80
    multa = (velocidade - 80) * 20
    print(f"Você deve pagar uma multa de R$ {multa}")
else:
    print("Você está dentro do limite de velocidade")