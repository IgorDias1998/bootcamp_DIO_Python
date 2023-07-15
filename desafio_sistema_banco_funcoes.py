def menu():
    menu = '''
    "--*--*--MENU--*--*--"
    [d] -> Depositar
    [s] -> Sacar
    [e] -> Extrato
    [nu] -> Novo usuário
    [nc] -> Nova conta
    [q] -> Sair do programa
    Escolha sua opção:
    '''
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\n Valor depositado com sucesso.")
    else:
        print("\n Operação inválida. Valor inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, limite_valor, extrato, limite_saque, numero_saque):
    excedeu_saldo = saldo < valor
    excedeu_limite_valor = valor > limite_valor
    excedeu_n_saques = numero_saque > limite_saque

    if excedeu_saldo:
        print("Saldo insuficiente para essa operação.")
    elif excedeu_limite_valor:
        print("Valor de saque acima do permitido.")
    elif excedeu_n_saques:
        print("Número de saques diários excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t R${valor:.2f}\n"
        numero_saque += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação inválida. Valor inválido")
    
    return saldo, extrato
    
def exibir_extrato(saldo,/ ,* ,extrato):
    print("--*--*--Extrato--*--*--")
    print("Até o momento não houve movimentação." if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Digite o seu cpf(SOMENTE NÚMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario is not None:
        print("Já existe um usuário com esse cpf")
        return

    nome = input("Digite o seu nome: ")
    data_nascimento = input("Informe a sua data de nascimento: formato(dia/mes/ano): ")
    endereco = input("Digite o seu endereço: formato(rua - numero - cidade/estado): ")
        
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf":cpf})

    print("-Usuário criado com sucesso!-")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if "cpf" in usuario and usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n -Conta criada com sucesso- ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n -Usuário não encontrado-")

def programa():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite_valor = 600
    numero_saques = 0
    extrato = ""
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor, 
                limite_valor=limite_valor, 
                extrato=extrato, 
                limite_saque=LIMITE_SAQUE, 
                numero_saque=numero_saques,
                )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif opcao == "q":
            break

programa()
