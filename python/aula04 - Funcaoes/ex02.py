def conversao_idade(anos, meses, dias):
    total_dias = int((anos*365.25)+(meses*30.4167)+dias)

    return total_dias


dias = conversao_idade(26,3,5)
print(dias)