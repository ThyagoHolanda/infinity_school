from functools import reduce

palavras = ["Python", "desafio", "lista", "map", "filter", "reduce", "lambda"]

a = list(map(lambda x: len(x), palavras))
b = list(filter(lambda x: x[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ", palavras ))
c = reduce(lambda x, y: x + y, [len(word) for word in palavras] )

print(a)
print("*"*30)
print(b)
print("*"*30)
print(c)