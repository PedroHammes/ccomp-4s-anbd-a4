from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def validar_data(data_str: str) -> bool:
    partes = data_str.split('/')
    if len(partes) != 3:
        return False
    dia_str, mes_str, ano_str = partes
    if not (dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit()):
        return False
    dia, mes, ano = int(dia_str), int(mes_str), int(ano_str)
    if mes < 1 or mes > 12:
        return False
    if ano < 1900 or ano > 2100:
        return False
    try:
        datetime(ano, mes, dia)
        return True
    except ValueError:
        return False
    
def menu():
    while True:
        print("[1] Registrar vendas\n[2] Ranking de produtos\n[0] Sair\n")
        opt = input(">")
        match opt:
            case '1': sale()
            case '2': plot_product_ranking(product_ranking())
            case '0':
                print("Saindo...")
                break
            case _: print("Opção inválida") 

def sale():
    id = 0 
    date = input("Informe a data da venda (dd/mm/aaaa): ")
    while not validar_data(date):
        print("Data inválida! Por favor, insira no formato dd/mm/aaaa com uma data válida.")
        date = input("Informe a data da venda (dd/mm/aaaa): ")
    product = input("Informe o nome do produto: ")
    price = float(input("Informe o preço do produto: "))
    quantity = float(input("Informe a quantidade vendida: "))
    value = price*quantity
    print(f"produto: {product} | data: {date} | id: {id}\npreço: R${price}\nquantidade: {quantity}\nTotal: R${value}")
    new_sale = pd.DataFrame({
        "Produto": [product],
        "Preço": [price],
        "Quantidade": [quantity],
    })