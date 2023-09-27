email = "thyago142536@gmail.com"
senha = "123456"

# Utilizando condição dentro do while
while True:
    email_user = input("Digite seu email: ")
    senha_user = input("Digite sua senha: ")

    if email_user == email and senha_user == senha:
        print("Login realizado com sucesso!")
        break
    else:
        print("Email ou senha incorretos!")


# Utilizando somente while
email_user = input("Digite seu email: ")
senha_user = input("Digite sua senha: ")

while senha_user != senha or email_user != email:
   print("Email ou senha incorretos. Tente novamente.")
   email_user = input("Digite a senha: ")
   senha_user = input("Digite o email: ")

print("Login realizado com sucesso!")