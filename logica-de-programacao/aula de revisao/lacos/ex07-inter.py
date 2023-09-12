# import math

# valordacompra = float(input("Qual o valor da sua comprar: "))

# desconto = math.floor(((valordacompra-500)/100)+1)
# if desconto > 25:
#     desconto = 25

# desconto_descimal = 1-(desconto/100)

# valor_final = valordacompra * desconto_descimal

# print(f"Valor da compra: R$ {valordacompra}\n"
#       f"Desconto: {desconto}%\n"
#       f"Valor final: R$ {valor_final}\n")

# print("===========================================")


# if valordacompra >= 500:
#     acm = 500

#     for i in range(1, 26):
#         if acm > valordacompra-100:
#             break

#         acm += 100
        
#     valor_final = valordacompra * (1-(i/100))
    
#     print(f"Valor da compra: R$ {valordacompra}\n"
#             f"Desconto: {i}%\n"
#             f"Valor final: R$ {valor_final}\n")


valordacompra = 500

for i in range(1,26):
    print("valor da compra: ", valordacompra, "porcentagem de desconto:", i, "valor final", valordacompra *(1-(i/100)))
    valordacompra = valordacompra +100