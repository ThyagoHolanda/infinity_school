def fatorial(n):
    if n == 1:
        return 1
    elif n <= 0:
        return "Erro!"
    else:
        return n * fatorial(n-1)

print(fatorial(6))

print(f"="*30)


'''
def fatorial(n):
    acc = 1
    for i in range(n-1):
        acc *= n
        n -=1        
    return acc

fator = fatorial(5)
print(fator)

print(f"="*30)

def fatorial(n):
   acc = 1
   while n > 1:
       acc *= n
       n -= 1
   return acc

fator = fatorial(5)
print(fator)
'''