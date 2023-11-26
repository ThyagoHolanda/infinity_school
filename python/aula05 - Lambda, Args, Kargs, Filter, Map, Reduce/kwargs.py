def info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

info(nome="Thyago", idade= 26)