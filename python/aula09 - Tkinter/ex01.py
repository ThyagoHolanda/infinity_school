import tkinter as tk

janela = tk.Tk()

janela.geometry("500x500")

def ola():
    print("Olá, Seja bem vindo!")

butao = tk.Button(text="Inicializar", command=ola, bg="lightgray", font=("Arial", 12))

butao.pack()

janela.mainloop()