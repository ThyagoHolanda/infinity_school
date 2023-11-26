# Crie um dict dentro de um dict dentro de um dict

dicionario = {
    'pessoa': {
        'thyago': {
            'idade': 26,
            'altura': 140,
        },
        'Hely': {
            'idade': 25,
            'altura': 175,
        },
    },
}


for chave, valor in dicionario.items():
    print(f'Chave: {chave}')
    for chave_interna, valor_interno in valor.items():
        print(f'Chave interna: {chave_interna}')
        for chave_interna_interna, valor_interno_interno in valor_interno.items():
            print(f'Chave interna interna: {chave_interna_interna}')
            print(f'Valor interno interno: {valor_interno_interno}')
            