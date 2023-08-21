cafe = input("Você gosta de café? ")

match cafe.lower():
    case "sim":
        print("Então você gosta de café!")
    case "não":
        print("Que pena, você não gosta de café")
    case _:
        print("Opção inválida")