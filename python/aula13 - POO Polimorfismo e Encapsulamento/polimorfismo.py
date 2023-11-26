class Eevee:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
        self.tipo = "Normal"

    def ataque_basico(self):
        print(f"{self.nome} usou Investida!")


class Vaporeon(Eevee):
    def __init__(self, nome, nivel):
        super().__init__(nome, nivel)
        self.tipo = "Água"

    def ataque_basico(self):
        print(f"{self.nome} usou Jato d'água!")

eevee = Eevee("Eevee", 12)
vap = Vaporeon("Vaporeon", 25)

eevee.ataque_basico()
vap.ataque_basico()