import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    texto_resposta['text'] = f"Dólar: {cotacao_dolar}"

janela = Tk()
janela.title("Cotação autal dolar")

texto = Label(janela, text = "Clique no botão para ver a cotação")
texto.grid(column = 0, row = 0, padx = 50, pady = 50)

botao = Button(janela, text="Buscar cotação", command=pegar_cotacoes)
botao.grid(column = 0, row= 1, padx = 50, pady = 50)

#Testo resposta
texto_resposta = Label(janela, text="")
texto_resposta.grid(column = 0, row = 2, padx = 50, pady = 50)

janela.mainloop()