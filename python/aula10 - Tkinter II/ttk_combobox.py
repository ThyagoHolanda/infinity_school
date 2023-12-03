from tkinter import *
from tkinter import ttk

#Criar janela

janela = Tk()
janela.title("Exemplo de combobox")

label = Label(janela, text="Escolha um dia da semana")
label.pack(padx=75, pady=20)

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
combobox = ttk.Combobox(janela, values=dias_semana, state="readonly")
combobox.pack(padx=75, pady=20)
combobox.current(0)

janela.mainloop()