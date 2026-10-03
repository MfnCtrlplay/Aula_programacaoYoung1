import random

# Requisitos Funcionais

#mostrar o numero de tentativas restantes
#mostrar as letras acertadas
#permitir vencer
#permitir perde
#apenas aceitar uma letra por tentativa
#impedir que a mesma letra seja digitada novamente

# requisitos funcionais opcionais


palavra_secreta = random.choice(["davi","pietro","paul"])
letras_certas = []
letras_erradas = []
tentativas = 6

while tentativas > 0: 

    palavra_formada = ""

    for letra in palavra_secreta: 

        if letra in letras_certas:
            palavra_formada += letra

        else:
            palavra_formada += "-"

    # Acompanhamento do progresso
    print("\nPalavra:", palavra_formada)

    if len(letras_erradas) > 0:
        print("\nPalavra:", letras_erradas)

    else:
        print("Letras erradas: nenhuma")

    print("Tentativas restantes:", tentativas)

    #Verificar Vitoria

    if palavra_formada == palavra_secreta:
        print("Parabéns! Você venceu!")
        break

    chute = input("Digite uma Letra: ")

    chute = chute.lower()

    # Impede mais de uma letra
    if len(chute) != 1:
        print("Digite apenas UMA letra valida:")
        continue

    if chute in letras_certas or chute in letras_erradas:
        print("Você já digitou essa letra:")
        continue


    if chute in palavra_secreta: 

        letras_certas.append(chute)
        
        print("Você já digitou essa letra:") 
        continue

    else:

        letras_erradas.append(chute)

        tentativas -= 1

        print("Você errou!") 

    if tentativas == 0:
        print("\n Você perdeu! A palavra era: ", palavra_secreta)



        




            


