
# Função anonima/lambda
print((lambda a, b, c : a + b + c)(1, 2, 3))

print("="*30)
# ==============================

soma = lambda a, b, c : a + b + c

print(soma(1, 2, 3))

print("="*30)
# ==============================

numero_par = lambda x: "par" if x % 2 == 0 else "impar"

print((numero_par(5)))

print("="*30)

