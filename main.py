
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("Qual Valor você quer depositar? => "))
        if valor > 0:
            saldo += valor
            extrato += f"deposito no valor de R$ {valor:.2f}\n"
            
    elif opcao.lower() == "s":
        if(numero_saques == LIMITE_SAQUE):
            print("Você excedeu o limite de saques diarios")
            continue
        valor = float(input("Qual valor você quer sacar? =>"))
        if(valor > limite):
            extrato += f"Tentativa de saque de R$ {valor:.2f} não teve sucesso por exceção do limite.\n"
            valor = float(input("O valor informado excedeu o limite de R$ 500,00, tente novamente. => "))
        if(valor > saldo):
            print("O valor desejado para saque é maior que o saldo.")
            extrato += f"Tentativa de saque de R$ {valor:.2f} não teve sucesso por falta de saldo.\n"
            continue
        saldo -= valor
        extrato += f"Saque no valor de R$ {valor:.2f}\n"
        numero_saques += 1
    elif opcao.lower() == "e":
        print("==================EXTRATO BANCÁRIO=====================\n")
        print(extrato)
    else:
        print("Opção invalida, tente novamente!")