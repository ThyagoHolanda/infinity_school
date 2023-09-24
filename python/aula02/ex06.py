# Crie uma lista onde cada posição é uma letra que forma uma frase, incluindo os espaços.

lista = ["O","l","á"," ","M","u","n","d","o"]

for i in lista:
    print(i, end="")

print("\n=================================")

for i in range(len(lista)-1):
    if lista[i] == " ":
        print(lista[i])
        lista.pop(i)
    
print(lista)



