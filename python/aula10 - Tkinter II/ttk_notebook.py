from tkinter import *
from tkinter import ttk

#Criar janela

janela = Tk()
janela.title("Exemplo de Notebook")

#Sizegrip
janela.resizable(True, True)

#Criando um widget Sizegrip
sizegrip = ttk.Sizegrip(janela)

#Criando notbook
notebook = ttk.Notebook(janela)

#Primeira guia
guia_semana = ttk.Frame(notebook)
notebook.add(guia_semana, text="Dias da semana")

label1 = ttk.Label(guia_semana, text="Escolha um dia da semana")
label1.pack(padx=50, pady=10)

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
combobox = ttk.Combobox(guia_semana, values=dias_semana, state="readonly")
combobox.pack(padx=50, pady=20)
combobox.current(0)

#Segunda guia
guia_mes = ttk.Frame(notebook)
notebook.add(guia_mes, text="Meses")

label2 = ttk.Label(guia_mes, text="Escolha um mês")
label2.pack(padx=50, pady=10)

#Criando separador
separador = ttk.Separator(guia_mes, orient=HORIZONTAL)
separador.pack(padx=50, ipadx=50)

dias_semana = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
combobox = ttk.Combobox(guia_mes, values=dias_semana, state="readonly")
combobox.pack(padx=50, pady=20)
combobox.current(0)

#Terceira guia
guia3 = ttk.Frame(notebook)
notebook.add(guia3, text="Guia 3")

label3 = ttk.Label(guia3, text="Conteúdo da guia 3")
label3.pack(padx=50, pady=50)

#Terceira guia
guia4 = ttk.Frame(notebook)
notebook.add(guia4, text="Guia 4")

label4 = ttk.Label(guia4, text="Conteúdo da guia 4")
label4.pack(padx=50, pady=50)

notebook.pack(padx=50, pady=50)

sizegrip.pack(anchor="ne", padx=3, pady=3, expand=True)

janela.mainloop()