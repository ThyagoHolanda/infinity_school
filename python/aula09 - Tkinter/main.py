import tkinter as tk
from tkinter.ttk import Combobox

janela = tk.Tk()
janela2 = tk.Tk()

janela.geometry("500x500")

janela.maxsize(height=600, width=600)

def hello():
    print("Olá mundo!")

def exibir_texto():
   texto = caixa_texto.get()
   print("Texto inserido:", texto)

def deleta_texto():
   caixa_texto.delete(0, "end")

label = tk.Label(text=("Digite algum texto"))
label.pack()

caixa_texto= tk.Entry(bg="lightgray")
caixa_texto.pack()

butao = tk.Button(text="Submit", foreground="green", bg="lightblue", width=10, height=2, font=("System", 8), command=exibir_texto)
butao.pack()

delete_butao = tk.Button(master=janela2, text="Limpar", foreground="green", bg="lightblue", width=10, height=2, font=("System", 8), command=deleta_texto)
delete_butao.pack()

# Janela 2

combo = Combobox(values=["C++", "Python", "JS"], state="readonly")
combo.pack()

combo_butao = tk.Button()

janela.mainloop()