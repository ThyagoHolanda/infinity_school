p1 = input("Digite uma palavra qualquer: ")
p2 = input("Digite uma palavra qualquer: ")

juncao = lambda a, b: a + b if len(a) > 5 and len(b) > 5 else "Erro"

print(juncao(p1, p2))