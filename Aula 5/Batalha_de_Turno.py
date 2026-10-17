import random
import math


player = {"nome": "Player", "vida": 100, "defesa": 100}
inimigo = {"nome": "NPC das sombras", "vida": 100, "defesa": 100}
historico = {"rounds": [], "vida_player": [], "vida_npc": []}
rounds = 1


def calcular_dano():
    dano = random.randint(15, 35)
    return dano


def atacar(alvo, dano):
    if alvo["defesa"] > 0:
        alvo["defesa"] = alvo["defesa"] - dano
    else:
        alvo["vida"] = alvo['vida'] - dano


def escolher_acao_player():
    escolha = input("1 - Atacar | 2 - Defender: ")
    if escolha == "1":
        return "atacar"
    elif escolha == "2":
        return "defender"
    else:
        return "invalido"


while player['vida'] > 0 and inimigo['vida'] > 0: 
    print(f"--- ROUND {rounds} ---") 
    print(f"Player -> Vida: {player['vida']} | Defesa: {player['defesa']}") 
    print(f"NPC -> Vida: {inimigo['vida']} | Defesa: {inimigo['defesa']}")
    acao_player = escolher_acao_player()
    if acao_player == "invalido":
        print("Ação inválida. Tente novamente.")
        continue
    acao_npc = random.choice(["atacar", "defender"])
    print(f"Player: {acao_player.upper()} | NPC: {acao_npc.upper()}")


    if acao_player == "atacar" and acao_npc == "atacar":
        player["vida"] -= calcular_dano()
        inimigo["vida"] -= calcular_dano()
        print("Os dois atacaram!")


    elif acao_player == "atacar" and acao_npc == "defender":
        atacar(inimigo, calcular_dano())
        print("Player atacou!")


    elif acao_player == "defender" and acao_npc == "atacar":
        atacar(player, calcular_dano())
        print("NPC atacou!")


    else:
        print("Os dois defenderam!")
    
    historico["rounds"].append(rounds)
    historico["vida_player"].append(player["vida"])
    historico["vida_npc"].append(inimigo["vida"])
    rounds = rounds + 1


if player["vida"] <= 0 and inimigo["vida"] <= 0:
    print("Empate!")
elif player["vida"] <= 0:
    print("NPC venceu!")
else:
    print("Player venceu!")


print("Histórico da batalha:")
print(historico)
