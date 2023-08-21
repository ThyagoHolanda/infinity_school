produto1 = float(input("Informe o preço do 1º produto! "))
produto2 = float(input("Informe o preço do 2º produto! "))
produto3 = float(input("Informe o preço do 3º produto! "))

if produto1 < produto2 and produto1 < produto3:
    print("O 1º produto é o mais barato!")
elif produto2 < produto3:
    print("O 2º produto é o mais barato!")
else:
    print("O 3º produto é o mais barato!")