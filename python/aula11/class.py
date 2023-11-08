class Carro:

    def __init__(self, cor, portas, motor, arcondicionado, ano_fabricacao, fume):
        self.cor = cor
        self.portas = portas
        self.motor = motor
        self.arcondicionado = arcondicionado
        self.ano_facricacao = ano_fabricacao
        self.fume = fume

    def acelerar(self):
        print("Acelerando")
    
    def frear(self):
        print("Freando")

    def seta_direita(self):
        print("Direita")

    def seta_esquerda(self):
        print("Esquerda")


gol = Carro("Preto", 4, "1.0", True, 2019, True)
onix = Carro("Branco", 2, "2.0", True, 2023, False)

gol.frear()

print(f"Cor do Gol: {gol.cor}")
gol.cor = "Azul"
print(f"Cor do Gol: {gol.cor}")

print(f"Cor do Onix: {onix.cor}")