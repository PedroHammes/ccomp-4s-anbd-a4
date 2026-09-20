import pandas as pd

def menu():
    """Exibe o menu inicial com as funções do sistema"""

    while True: # True garante que o loop SEMPRE execute

        print("[1] Registrar vendas\n[2] Relatórios\n[0] Sair\n")
        opt = input(">")

        match opt: 
            case '1': sale()
            case '2': print("Relatórios") # relatorios()
            case '0': 
                print("Saindo...")
                break
            case _: print("Opção inválida") # tratamento de erro

def sale():
    id = 0 # numero aleatorio
    date = input("Informe a data da venda (dd/mm/aaaa): ")
    # incluir uma função para validação de data
    name = input("Informe o nome do produto: ")
    price = float(input("Informe o preço do produto: "))
    quantity = float(input("Informe a quantidade vendida: "))
    value = price*quantity
    print(f"produto: {name} | data: {date} | id: {id}\npreço: R${price}\nquantidade: {quantity}\nTotal: R${value}")


