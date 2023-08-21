time1_nome = input("Informe o nome do primeiro time! ")
time1_gol = float(input("Quantos gols esse time fez? "))
time2_nome = input("Informe o nome do segundo time! ")
time2_gol = float(input("Quantos gols esse time fez? "))

if time1_gol > time2_gol:
    print(f"{time1_nome} ganhou!")
elif time2_gol > time1_gol:
    print(f"{time2_nome} ganhou!")
else:
    print("O jogo terminou em empate!")