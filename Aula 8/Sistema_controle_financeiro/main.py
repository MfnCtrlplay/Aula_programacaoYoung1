import json
from datetime import datetime

bd = "transacoes.json"

def menu():
    print("===== Controle Financeiro =====")
    print("1. Adicionar Reiceita")
    print("2. Adicionar Despesa")
    print("3. Ver todas as Transações")
    print("4. Ver Saldo")
    print("0. Sair")
    return input("Escolha uma opção:")

def salvar_dados():
    with open(bd,"w", encoding = "utf-8")as arquivo:
        json.dump(transacoes,arquivo,indent=4,ensure_ascii=False)

def carregar_dados():
    with open(bd,"r",encoding= "utf-8")as arquivo:
        return json.load(arquivo)

def adicionar_transacao(transacoes,descricao,valor,tipo):
    transacao = {

        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    transacoes.append(transacao)
    salvar_dados(transacoes)
    print(f"{tipo} registrada: {descricao} - R$ {valor}")

transacoes = carregar_dados()

while True:

    opcao = menu()
    if opcao == "1":
        adicionar_transacao()

    elif opcao == "2":
        adicionar_transacao()

