pessoas = [
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

nomes = list(map(lambda x: x["Nome"], pessoas))

print(nomes)

