a = 10
b = 20
c, d = 30, 40
print(f"Antes da mudança\n a = {a}\n b = {b}\n c = {c}\n d = {d}")

# 1ª Forma
a2 = a
a = b
b = a2
print(f"Primeira forma, depois da mudança\n a = {a}\n b = {b}")

# 2ª Forma
d, c = c, d
print(f"Segunda forma, depois da mudança\n c = {c}\n d = {d}")