from datetime import datetime
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Valida se a string informada está no formato dd/mm/aaaa e se representa uma data real.
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
    
# Exibe o menu principal e gerencia a navegação do sistema.
def menu():
    while True:
        print("[1] Registrar vendas\n[2] Ranking de produtos\n[3] Faturamento mensal\n[0] Sair\n")
        opt = input(">")
        match opt:
            case '1': record_sale()
            case '2': plot_product_ranking(product_ranking())
            case '3': plot_monthly_revenue(monthly_revenue())
            case '0':
                print("Saindo...")
                break
            case _: print("Opção inválida! Por favor, escolha uma das opções abaixo.") 

# Coleta os dados de uma nova venda, valida a data e persiste no arquivo Excel.
def record_sale():
    current_sales = pd.read_excel("sales/sales.xlsx")
    id = len(current_sales) + 1

    date = input("Informe a data da venda (dd/mm/aaaa): ")
    while not validar_data(date):
        print("Data inválida! Por favor, insira no formato dd/mm/aaaa com uma data válida.")
        date = input("Informe a data da venda (dd/mm/aaaa): ")

    product = input("Informe o nome do produto: ")
    price = float(input("Informe o preço do produto: "))
    quantity = float(input("Informe a quantidade vendida: "))
    value = price * quantity
    
    print(f"produto: {product} | data: {date} | id: {id}\npreço: R${price}\nquantidade: {quantity}\nTotal: R${value}")

    new_sale = pd.DataFrame({
        "Produto": [product],
        "Preço": [price],
        "Quantidade": [quantity],
        "Valor": [value],
        "Data": [date],
        "id": [id]
    })

    update_sales_history(new_sale)

def update_sales_history(new_sale):
    current_sales = pd.read_excel("sales/sales.xlsx")
    updated_sales = pd.concat([current_sales, new_sale])
    updated_sales.to_excel("sales/sales.xlsx", sheet_name="sales", index=False)

# Processa as vendas e retorna um DataFrame com o ranking de produtos por receita gerada.
def product_ranking():
    ranking = {}
    current_sales = pd.read_excel("sales/sales.xlsx")

    for index, row in current_sales.iterrows():
        if row["Produto"] in ranking:
            ranking[row["Produto"]] += row["Valor"]
        else: 
            ranking[row["Produto"]] = row["Valor"]

    ranking_df = pd.DataFrame(ranking.items(), columns=["Produto", "Valor"])
    ranking_df = ranking_df.sort_values("Valor", ascending=False)
    return ranking_df

# Processa as vendas e retorna um DataFrame com o faturamento acumulado por mês.
def monthly_revenue():
    revenue = {}
    current_sales = pd.read_excel("sales/sales.xlsx")

    for index, row in current_sales.iterrows():
        data = row["Data"]
        
        # Compatibilidade caso o pandas leia como texto ou como Timestamp do Excel
        if isinstance(data, str):
            month_year = data.split("/")[2] + "/" + data.split("/")[1]
        else:
            month_year = data.strftime("%Y/%m")
            
        if month_year in revenue:
            revenue[month_year] += row["Valor"]
        else:
            revenue[month_year] = row["Valor"]

    revenue_df = pd.DataFrame(revenue.items(), columns=["Mês", "Valor"])
    revenue_df = revenue_df.sort_values("Mês", ascending=True)
    return revenue_df

# Gera, exibe e salva o gráfico de barras do faturamento mensal.
def plot_monthly_revenue(revenue):
    os.makedirs("dashboards", exist_ok=True)  # Cria a pasta se não existir
    plt.clf()
    sns.barplot(data=revenue, x="Mês", y="Valor")

    plt.title("Faturamento mensal")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento (R$)")

    plt.savefig("dashboards/faturamento_mensal.png")
    plt.show()

# Gera, exibe e salva o gráfico de barras do ranking de produtos.
def plot_product_ranking(ranking):
    os.makedirs("dashboards", exist_ok=True)  # Cria a pasta se não existir
    plt.clf()
    sns.barplot(data=ranking, x="Produto", y="Valor")

    plt.title("Ranking de produtos por receita gerada")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento (R$)")

    plt.savefig("dashboards/ranking_produtos.png")
    plt.show()