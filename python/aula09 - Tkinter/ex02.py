"""
import tkinter as tk

janela = tk.Tk()

def boas_vindas():
    nome = caixa_texto.get()
    print(f"Bem vindo {nome}!")

def deletar_texto():
    caixa_texto.delete(0, "end")


janela.geometry("500x500")

caixa_texto = tk.Entry(bg="lightgray")
caixa_texto.pack()

butao_enviar = tk.Button(text="Enviar", command=boas_vindas)
butao_enviar.pack()

butao_deletar = tk.Button(text="Limpar",command=deletar_texto)
butao_deletar.pack()

janela.mainloop()

"""


import tkinter as tk

janela = tk.Tk()

def verificar_iadade():
    try:
        idade = int(caixa_idade.get())
        print(f"Sua idade é: {idade}")
        if idade < 18:
            print(f"Você é menor de idade")
        elif idade >= 18 and idade <= 60:
            print(f"Você é Adulto")
        elif idade > 60:
            print(f"Você é Idoso")
    except:
        print("Impossível converter!")

def deleta_texto():
   caixa_idade.delete(0, "end")

janela.geometry("500x500")

caixa_idade = tk.Entry(bg="lightgray")
caixa_idade.pack()

butao_enviar = tk.Button(text="Enviar", command=verificar_iadade)
butao_enviar.pack()

delete_butao = tk.Button(text="Limpar", command=deleta_texto)
delete_butao.pack()

janela.mainloop()
