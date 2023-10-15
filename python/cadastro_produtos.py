def remove_produto():
    a = 1


def ver_estoque(estoque):
    print(f"{'Nome':<15} {'Quantidade':<15} {'Preço':<15} {'Categoria':<15}")
    for produto in estoque:
        print(f"{produto['nome']:<15} {produto['quantidade']:<15} {produto['preco']:<15} {produto['categoria']:<15}")



def pesquisar_produto():
    a = 1


def estatisticas_produto():
    a = 1


def add_produto(estoque, produto):
    for i in range(len(estoque)):
        if estoque[i]["nome"] == produto["nome"]:
            print(f"Produto em estoque.\n{estoque[i]}\n Atualzando informações...")
            estoque[i]["quantidade"] += produto["quantidade"]
            estoque[i]["preco"] = produto["preco"]
            estoque[i]["categoria"] = produto["categoria"]
            print(estoque[i])
            print("Produto atualizado!")
            return estoque
        else:
            estoque.append(produto)
            print("Adicionando produto na lista...")
            print("Produto adiconado!\n")
            
            ver_estoque(estoque)

            return estoque
            
            


estoque = [
    {"nome": "arroz",
     "quantidade": 5,
     "preco": 5.59,
     "categoria": "mercearia",
     },
    {"nome": "feijão",
        "quantidade": 10,
        "preco": 3.99,
        "categoria": "mercearia",
     },
    {"nome": "macarrão",
        "quantidade": 2,
        "preco": 4.99,
        "categoria": "mercearia",
     },
    {"nome": "ovos",
        "quantidade": 12,
        "preco": 5.99,
        "categoria": "pescaria",
     },
    {"nome": "frango",
        "quantidade": 6,
        "preco": 7.99,
        "categoria": "carne",
     },
    {"nome": "filetes",
        "quantidade": 8,
        "preco": 9.99,
        "categoria": "carne",
     },
    {"nome": "mortadela",
        "quantidade": 4,
        "preco": 6.99,
        "categoria": "lanche",
     },
    {"nome": "pastel",
        "quantidade": 6,
        "preco": 3.99,
        "categoria": "doce",
     },
    {"nome": "chocolate",
        "quantidade": 10,
        "preco": 4.99,
        "categoria": "doce",
     },
    {"nome": "banana",
        "quantidade": 10,
        "preco": 2.99,
        "categoria": "fruta",
     },
    {"nome": "uva",
        "quantidade": 5,
        "preco": 3.99,
        "categoria": "fruta",
     },
    {"nome": "pera",
        "quantidade": 8,
        "preco": 4.99,
        "categoria": "fruta",
     },
    {"nome": "mango",
        "quantidade": 6,
        "preco": 5.99,
        "categoria": "fruta",
     }
]


print("1 - Adicionar produto\n"
      "2 - Remover produto\n"
      "3 - Pesquisar produto\n"
      "4 - Ver estoque\n"
      "5 - Estatisticas")
escolha = int(input("Escolha uma das opções acima: "))

while escolha < 1 or escolha > 5:
    print("1 - Adicionar produto\n"
          "2 - Remover produto\n"
          "3 - Pesquisar produto\n"
          "4 - Ver estoque\n"
          "5 - Estatisticas")
    escolha = int(input("Escolha uma das opções acima (Ente 1 e 5): "))

if escolha == 1:
    produto = dict()
    produto["nome"] = "arroz"  # input("Informe o nome do produto: ")
    produto["quantidade"] = 1 # int(input("Informe a quantidade que deseja adicionar: "))
    produto["preco"] = 6.09  # float(input("Informe o preço do produto: "))
    produto["categoria"] = "mercearia" # input("Qual a categoria desse produto: ")
    estoque = add_produto(estoque, produto)
