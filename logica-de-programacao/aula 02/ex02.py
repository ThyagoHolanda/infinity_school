temperatura = float(input("Informe a temperatura! "))

if temperatura <= 37:
    cancela = True
else:
    cancela = False

print(f"True para liberado\n"
      f"False para não liberado\n"
      f"{cancela}")