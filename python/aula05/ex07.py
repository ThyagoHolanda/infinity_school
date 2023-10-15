def listar_nomes(pessoas):
    nomes = list()

    for i in pessoas:
        for x in i:
            nomes.append(x["Nome"])
        
    return nomes
    

pessoas = [  
   [ 
        {
            "Nome": "Thyago",
            "Idade": 26
        },
        {
            "Nome": "Hely",
            "Idade": 26
        },
        {
            "Nome": "Rafael",
            "Idade": 26
        },
        {
            "Nome": "Lucas",
            "Idade": 26
        },
        {
            "Nome": "Joana",
            "Idade": 30
        },
    ],
    [
        {
            "Nome": "Mariana",
            "Idade": 22
        },
        {
            "Nome": "Pedro",
            "Idade": 28
        },
        {
            "Nome": "Carla",
            "Idade": 24
        },
        {
            "Nome": "Marcos",
            "Idade": 32
        },
        {
            "Nome": "Alice",
            "Idade": 27
        },
    ]
]

print(listar_nomes(pessoas))

# Percorrendo a lista utilizando map e lambda
nomes2 = list(map(lambda x: x["Nome"], pessoas[0], pessoas[1]))

print(nomes2)


