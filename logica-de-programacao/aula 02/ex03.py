indice = float(input("Informe o índice de poluição atual! "))

if indice < 0.3:
    print("Nenhuma industria é intimada!")
elif indice >= 0.3 and indice < 0.4:
    print("Enviar intimação para as industrias do 1º grupo e suspendam suas atividades!")
elif indice >= 0.4 and indice < 0.5:
    print("Enviar intimação para as industrias do 1º e 2º grupo e suspendam suas atividades!!")
else:
    print("Urgênte: Enviar intimação para todas as industrias e suspendam suas atividades!!!")


if indice >= 0.5 :
    print("Urgênte: Enviar intimação para todas as industrias e suspendam suas atividades!!!")
elif indice >= 0.4:
    print("Enviar intimação para as industrias do 1º e 2º grupo e suspendam suas atividades!!")
elif indice >= 0.3:
    print("Enviar intimação para as industrias do 1º grupo e suspendam suas atividades!")
else:
    print("Nenhuma industria é intimada!")