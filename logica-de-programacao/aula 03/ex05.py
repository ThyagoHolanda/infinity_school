contar = 0
# for i in range(10):
#     numero = float(input(f"Digite o {i+1}º numero entre 0 e 100: "))

#     if numero >= 25 and numero <= 75:
#         contar += 1

# print(f"{contar} dos numeros digitados estão entre 25 e 75")


i = 1
while i <= 10:
    numero = float(input(f"Digite o {i}º numero entre 0 e 100: "))

    if numero >= 25 and numero <= 75:
        contar += 1
    
    i += 1

print(f"{contar} dos numeros digitados estão entre 25 e 75")