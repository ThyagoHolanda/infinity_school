import tkinter as tk

janela = tk.Tk()

def somar():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
    except:
        print("Não foi possível converter!")

label_numero_1 = tk.Label(text="Digite o primeiro numero")
entrada1 = tk.Entry(bg="lightgray")
label_numero_2 = tk.Label(text="Digite o segundo numero")
entrada2 = tk.Entry(bg="lightgray")
butao_somar = tk.Button(text="Somar", command=somar)

label_numero_1.pack()
entrada1.pack()
label_numero_2.pack()
entrada2.pack()
butao_somar.pack()

janela.mainloop()