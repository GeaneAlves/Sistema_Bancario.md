
import datetime

# Listas para armazenar usuários e contas
usuarios = []
contas = []

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, num - bairro - cidade/UF): ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print("Usuário não encontrado! Cadastre primeiro.")
        return

    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    })
    print("Conta criada com sucesso!")

def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação inválida! Valor negativo.")
    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente!")
    elif excedeu_limite:
        print("Saque excede limite!")
    elif excedeu_saques:
        print("Número máximo de saques excedido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado!")
    else:
        print("Valor inválido!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n**************** EXTRATO ****************")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("******************************************")

AGENCIA = "0001"
numero_conta = 1
saldo = 0
limite = 400
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[0] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "1":
        saldo, extrato = deposito(saldo, extrato)
    elif opcao == "2":
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "4":
        criar_usuario(usuarios)
    elif opcao == "5":
        criar_conta(AGENCIA, numero_conta, usuarios)
        numero_conta += 1
    elif opcao == "6":
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Usuário: {conta['usuario']['nome']}")
    elif opcao == "0":
        break
    else:
        print("Operação inválida, selecione uma opção válida.")

