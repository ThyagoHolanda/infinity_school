from functools import reduce

numero = [1,2,3,4,5]

soma = reduce(lambda x, y: x + y, numero)

print(soma)