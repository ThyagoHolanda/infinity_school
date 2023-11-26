import tkinter as tk
from tkinter.ttk import Combobox

janela = tk.Tk()
janela2 = tk.Tk()

janela.geometry("500x500")
janela2.geometry("500x500")

def exibir1():
        escolha1 = combo1.get()
        print(escolha1)

def exibir2():
        escolha2 = combo2.get()
        print(escolha2)

combo1 = Combobox(master=janela, values=["Disney", "Dreamworks", "Pixel"], state="readonly")
combo2 = Combobox(master=janela2, values=["Python", "Java", "C++"], state="readonly")

butao1 = tk.Button(master=janela, text="Escolher", command=exibir1)
butao2 = tk.Button(master=janela2, text="Escolher", command=exibir2)

combo1.current(0)
combo1.pack()
butao1.pack()

combo2.current(1)
combo2.pack()
butao2.pack()


janela.mainloop()