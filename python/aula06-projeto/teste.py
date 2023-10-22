import random

jogadas = ['Pedra', 'Papel', 'Tesoura']

def jogador():
    escolha = int(input("Escolha uma das opções:\n"
                        "1 - Pedra\n"
                        "2 - Papel\n"
                        "3 - Tesoura\n")) - 1
    
    return jogadas[escolha]

def computador():
    escolha = random.choice(jogadas)

    return escolha

def jogo(jogador, computador):
    if jogador == computador:
        print("Empate")
    elif (
        (jogador == "Pedra" and computador == "Tesoura") or
        (jogador == "Tesoura" and computador == "Papel") or
        (jogador == "Papel" and computador == "Pedra")
    ):
        print("O jogador Venceu\n"
              f"j:{jogador} x c:{computador}")
    else:
        print("O jogador Perdeu\n"
              f"j:{jogador} x c:{computador}")
        
j = jogador()
c = computador()

jogo(j,c)