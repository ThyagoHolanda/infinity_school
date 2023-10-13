def soma(num):
    for i in range(len(num)):
        if num[i] == "+":
            num[i+1] = int(num[i-1]) + int(num[i+1])
            
    return num[-1]
            
def sub(num):
    for i in range(len(num)):
        if num[i] == "-":
            num[i+1] = int(num[i-1]) - int(num[i+1])
            
    return num[-1]

def mult(*num):
    return int(num[0])*int(num[1])

def div(*num):
    return int(num[0])/int(num[1])

def expresao(e):
    while len(e) > 1:
        e
    
    
    


s = "2/2/5/4"
equ = []
for i in s:            
    equ.append(i)

print(equ.index("*"))



equacao = "5+6-1*2+5+6-5+7-2/2*5/4"
res = 5+6-1*2+5+6-5+7-2/2*5/4

