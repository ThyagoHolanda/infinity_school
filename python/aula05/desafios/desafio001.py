from functools import reduce

vendas = [
    {"produto": "A", "quantidade": 5, "preco": 10.0},
    {"produto": "B", "quantidade": 3, "preco": 15.0},
    {"produto": "A", "quantidade": 2, "preco": 10.0},
    {"produto": "C", "quantidade": 7, "preco": 8.0},
    {"produto": "B", "quantidade": 4, "preco": 15.0},
]

total_por_produto = list(map(lambda p: [p["produto"], p["quantidade"] * p["preco"]], vendas))
print("Preços totais por produto:", total_por_produto)

print("-=-"*30)

venda_protudo_a = list(filter(lambda p: p["produto"] == "A", vendas))
print("Vendas do produto 'A':", venda_protudo_a)

print("-=-"*30)

total_de_vendas = reduce(lambda acumulador, venda: acumulador + (venda["quantidade"] * venda["preco"]), vendas, 0)

print("Total de vendas:", total_de_vendas)







