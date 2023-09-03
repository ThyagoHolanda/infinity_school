# acc = 0
# contar = 0
# nota = 1

# while nota > 0:
#     nota = float(input("Digite uma nota: "))

#     if nota > 0: 
#         acc += nota
#         contar += 1

# media = acc / contar

# print(f"A media total das notas foi: {media}")

# acc = 0
# contar = 0
# while True:
#     nota = float(input("Digite uma nota; "))

#     if nota < 0:
#         break
#     else:
#         acc += nota
#         contar += 1

# media = acc / contar

# print(f"A media total das notas foi: {media}")

acc = 0
contar = 0
while True:
    nota = input("Digite uma nota; ")

    if nota not in "012345678910":
        print("Caracter invalido ou numero diferente de 0 a 10.")
    else:
        nota = float(nota)

        if nota >= 0 and nota <= 10:
            acc += nota
            contar += 1

            escolha = input("Quer adionar mais uma nota?(s/n) ")

            if escolha.lower() == 'n' or escolha.lower() == 'não':
                break
        else:
            print("Notas apenas entre 0 e 10")

media = acc / contar

print(f"A media total das notas foi: {media}")