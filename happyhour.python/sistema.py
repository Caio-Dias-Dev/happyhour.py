participantes = {}
gastos = []

def cadastrar_participante():
    nome = input("Nome do participante: ")
    if nome in participantes:
        print("Participante já cadastrado!")
    else:
        participantes[nome] = 0.0
        print(f"{nome} cadastrado com sucesso!")

def registrar_gasto():
    nome = input("Quem pagou? ")
    if nome not in participantes:
        print("Participante não encontrado.")
        return
    
    valor = float(input("Valor do gasto: R$ "))
    participantes[nome] += valor
    gastos.append(valor)
    print("Gasto registrado com sucesso!")

def mostrar_resumo():
    if not participantes:
        print("Nenhum participante cadastrado.")
        return

    total_gasto = sum(gastos)
    qtd = len(participantes)
    valor_por_pessoa = total_gasto / qtd

    print("\n--- RESUMO DO HAPPY HOUR ---")
    print(f"Total gasto: R$ {total_gasto:.2f}")
    print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}\n")

    for nome, pago in participantes.items():
        saldo = pago - valor_por_pessoa
        if saldo > 0:
            print(f"{nome} deve receber R$ {saldo:.2f}")
        elif saldo < 0:
            print(f"{nome} deve pagar R$ {abs(saldo):.2f}")
        else:
            print(f"{nome} está quite")

def menu():
    while True:
        print("\n=== GERENCIADOR DE HAPPY HOUR ===")
        print("1 - Cadastrar participante")
        print("2 - Registrar gasto")
        print("3 - Mostrar resumo")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_participante()
        elif opcao == "2":
            registrar_gasto()
        elif opcao == "3":
            mostrar_resumo()
        elif opcao == "4":
            print("Encerrando o programa 🍻")
            break
        else:
            print("Opção inválida!")

menu()
