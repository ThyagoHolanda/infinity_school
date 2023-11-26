"""
Crie uma classe chamada Fatura que possa ser utilizada por uma loja de
suprimentos de informática para representar uma fatura de um item
vendido na loja. Uma fatura deve incluir as seguintes informações como
atributos:

o nome do item;
o preço unitário do item;
quantidade de item a ser faturado;
valor total da fatura;

Sua classe deve ter um construtor que inicialize todos os atributos menos o
valor total da fatura. Além disso, forneça um método chamado
gerar_fatura que calcula o valor da fatura (isto é, multiplicar a quantidade
pelo preço por item).
"""

class Fatura:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = self.gerar_fatura()

    def gerar_fatura(self):
        return self.preco_unitario * self.quantidade
    
caixa = dict()
cod = 0
while True:

    caixa[cod] = {
        "nome": input("Informe o nome do produto: "),
        "valor": float(input("Informe o valor unitário do produto: ")),
        "quantidade": int(input("Informe a quantidade: "))
        }
 
    cod += 1

    escolha = int(input("0 - Não\n"
                        "1 - Sim\n"
                        "Deseja informar outro produto: "))
    if escolha == 0:
        break



# produto = Fatura(nome, valor_unitario, quantidade)

# print(f"Valor total deste produto = {produto.valor_total}")
