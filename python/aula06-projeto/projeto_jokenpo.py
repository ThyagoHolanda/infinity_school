import random

# Função para compara escolha do jogador com computador


def jogo(computador, jogador):
    # empate = f"Empate!" if jogador == computador else False

    if jogador == computador:
        return f"Empate!"

    elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
        return f"Jogador venceu!"

    else:
        return f"Computador venceu!"


# Função parar determinar a escolha do computador
def escolha_pc(escolha_jogador):

    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)

    if escolha_jogador == opcoes[0] or escolha_jogador == opcoes[1] or escolha_jogador == opcoes[2]:

        print(
            f"Você escolheu {escolha_jogador} e o computador escolheu {escolha_computador}")
        return jogo(escolha_computador, escolha_jogador)

    else:

        return "Escolha uma das opções!"


# Começo do jogo
escolha_jogador = input("Pedra, papel ou tesoura: ").lower()

resultado = escolha_pc(escolha_jogador)
print(resultado)


while True:
    novamente = input("Deseja jogar novamente S/N: ").upper()
    if novamente == "N":
        break

    escolha_jogador = input("Pedra, papel ou tesoura: ").lower()

    resultado = escolha_pc(escolha_jogador)
    print(resultado)
