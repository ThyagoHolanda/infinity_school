print("Nota 1º semestre")
nota1 = float(input())

print("Nota 2º semestre")
nota2 = float(input())

print("Nota 3º semestre")
nota3 = float(input())

print("Nota 4º semestre")
nota4 = float(input())

media = (nota1 + nota2 + nota3 + nota4) / 4

# if media >= 7:
#     print(f"Parabéns sua média é {media}")
#     if media == 10:
#         print("Aprovado com Excelencia")
#     else:
#         print("Aprovado")
# else:
#     print(f"Sua média é {media}")
#     if media >= 5:
#         print("Recuperação")
#     else:
#         print("Reprovado")


# Esturura ternaria. Código na mesma linha.
print("Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado")