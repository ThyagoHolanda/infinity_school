votos_brancos = int(input("Informe o numero de votos brancos! "))
votos_nulos = int(input("Informe o numero de votos nulos! "))
votos_validos = int(input("Informe o numero de votos validos! "))
Total_de_votos = votos_brancos + votos_nulos + votos_validos

porcen_brancos = (votos_brancos/Total_de_votos)*100
porcen_nulos = (votos_nulos/Total_de_votos)*100
porcen_validos = (votos_validos/Total_de_votos)*100

print(f"Este candidato teve {porcen_brancos}% de votos brancos e {porcen_nulos}% de votos nulos e {porcen_validos}% de votos válidos!")
