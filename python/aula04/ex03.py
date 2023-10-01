def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def verificar_p_n(numero):
    if numero >=0:
        if par_impar(numero) == True:
            return f"Numero {numero} é positivo e par"
        else:
            return f"Numero {numero} é positivo e impar"
    else:
        return f"Numero {numero} é negativo"
    
print(verificar_p_n(6))
print(verificar_p_n(7))
print(verificar_p_n(55))
print(verificar_p_n(-5))