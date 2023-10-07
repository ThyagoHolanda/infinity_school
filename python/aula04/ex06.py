def soma (n):
    if n <= 0:
        return "O numero deve ser menor ou igual a zero"
    else:
        soma = f"S = 1"
        acc = 1

        if n == 1:
            return soma
        else:
            for i in range(2, n+1):
                acc += 1/i
                soma += f" + 1/{i}"

        soma += f" = {acc}"
        return soma


print(soma(2))