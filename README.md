
# operações de depósito, saque e extrato 
# limite de saques diários = 4 
# limite de valor por  saque = 400

```python
menu = """\n
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 400
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Seu saldo é insuficiente.")
        elif excedeu_limite:
            print("Operação inválida! O valor do saque excede o limite de valor.")
        elif excedeu_saques:
            print("Operação inválida! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação inválida! O valor informado é inválido.")

    elif opcao == "3":
        print("\n**************** EXTRATO ****************")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************************")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")
```
