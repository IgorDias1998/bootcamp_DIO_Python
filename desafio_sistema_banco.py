opcoes = "[d]epósito | [s]aque | [e]xtrato | [q]sair"

valor = 0
extrato = ""
saque = 0
limite_saque = 3

while True:
    operacao = input(f"Escolha a operação {opcoes}: ")
    
    if operacao == "d":
        deposito = float(input("Digite o valor do depósito:"))
        if (deposito < 0) or (deposito > 500):
            print("Valor inválido. Digite novamente.")
        else:
            valor += deposito
            extrato += f"Depósito: R${str(deposito)} "
    
    elif operacao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        if saque >= limite_saque:
            print("Limite de saque diário excedido.")
            pass
        elif valor < valor_saque:
            print("Saldo insuficiente.")
        elif valor > 500:
            print("Saque superior a R$500,00 inválido.")
        else:
            valor -= valor_saque
            extrato += f"Saque: R${str(valor_saque)} "
            saque += 1
            
    elif operacao == "q":
        break

print(f"{extrato}")    
print(f"Saldo em conta: R${valor}")
