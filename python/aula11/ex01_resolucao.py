class Fatura:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        

        self.adicionarItem()

    def adicionarItem(self):
        global numero
        global itens

        itens[numero] = {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }

        numero += 1

    @staticmethod
    def gerarFatura(itens):
        total = 0
        for i, j in itens.items():
            print(f"{i} -> {j['nome']} - R${j['preco']} - {j['quantidade']}")
            total += j['preco'] * j['quantidade']
        
        print(f"Valor total = R${total}")
        
        input("Precione enter para continuar:")
        print("\n" * 30)

itens = dict()
numero = 1

while True:
    escolha = int(input("Escolha uma das opções:\n"
                        "1 - Adicionar novo item;\n"
                        "2 - Ver fatura total;\n"
                        "0 - Sair."))
    
    match escolha:
        case 1:
            nome = input("Digite o nome do item: ")
            preco = float(input("Digite o valor do item: "))
            quantidade = int(input("Digite a quantidade de itens: "))

            item = Fatura(nome, preco, quantidade)

            print("Item adicionado a sacola")
            input("Precione enter para continuar:")
            print("\n" * 30)

        case 2:
            Fatura.gerarFatura(itens)

        case 0:
            break

        case _:
            print("Opção invalida")
            input("Precione enter para continuar:")
            print("\n" * 30)