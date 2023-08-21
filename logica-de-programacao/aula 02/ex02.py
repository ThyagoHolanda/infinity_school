temperatura = float(input("Informe a temperatura! "))

if temperatura <= 37:
    cancela = True
else:
    cancela = False

match cancela:
    case True:
        print("Liberar")
    case False:
        print("Bloquear")