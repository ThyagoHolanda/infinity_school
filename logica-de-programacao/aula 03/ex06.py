for i in range(1, 11, 1):
    for c in range(1, 11, 1):
        numero = i * c
        print(f"{i} x {c} = {numero}")
    print("----------------------------------------")

print("===============================================================")

i = 1
c = 1
while i <= 10:
    while c <= 10:
        numero = i * c
        print(f"{i} x {c} = {numero}")
        c += 1
    i += 1
    c = 1
    print("----------------------------------------")