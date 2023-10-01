def vericacao(palavra):
    for i in palavra.lower():
        if i not in "abcdefghijklmnopqrstuvwxyz":
            return False
    
    return True

nome = input("Digite o seu nome: ")

'''
if vericacao(nome) == False:
    print("Seu nome contém numeros ou caracteres especiais.")
else:
    print("Nome cadastrado pode continuar.")
'''

while vericacao(nome) == False:
    nome = input("Digite o seu nome novamente apenas com letras: ")

print("Nome cadastrado pode continuar.")
