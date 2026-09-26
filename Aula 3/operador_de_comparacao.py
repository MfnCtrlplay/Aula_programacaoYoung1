email_salvo = "professor@ctrlplay.com"
senha_salva = "1234"

print("===Entre com Sua conta===")
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

if email == email_salvo and senha == senha_salva:
    print("Login realizado com sucesso!")

elif email == email_salvo and senha != senha_salva:
    print("Senha incorreta!")

elif email != email_salvo and senha == senha_salva:
    print("Email incorreto!")

else:
    print("Email e senha incorretos!")