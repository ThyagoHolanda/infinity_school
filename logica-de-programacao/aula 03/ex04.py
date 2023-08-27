acc = 0
contar = 0
nota = 1

while nota > 0:
    nota = float(input("Digite uma nota: "))

    if nota > 0: 
        acc += nota
        contar += 1

media = acc / contar

print(f"A media total das notas foi: {media}")