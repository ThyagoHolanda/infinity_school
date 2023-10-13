def eh_primo(n):
    if n == 1:
        return False
    
    d = 0
    for i in range(2, n+1):
        # print(f"{n} % {i} = {n % i}")
        if n % i == 0:
            d += 1

    if d == 1:
        return True
    else:
        return False             

def encontrar_primos(fim=0, inicio=1):
    if fim < 0:
        return "O final do internvalo não pode ser negativo!"
    elif fim == 0:
        return "O final do intervaldo não pode ser zero!"
    
    primo = []
    for i in range(inicio, fim+1):
        if eh_primo(i) == True:
            primo.append(i)
    
    return primo