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
    """exibe o menu inicial com as funcoes do sistema"""

    while True:  # mantem o menu em execucao ate a opcao de saida
        print("[1] Registrar vendas\n[2] Ranking de produtos\n[0] Sair\n")
        opt = input(">")

        match opt:
            case '1':
                sale()
            case '2':
                plot_product_ranking(product_ranking())
            case '0':
                print("Saindo...")
                break
            case _:
                print("Opção inválida")


def sale():
    id = 0  # substituir por um id random

    date = input("Informe a data da venda (dd/mm/aaaa): ")

    while not validar_data(date):
        print("Data inválida! Por favor, insira no formato dd/mm/aaaa com uma data válida.")
        date = input("Informe a data da venda (dd/mm/aaaa): ")

    product = input("Informe o nome do produto: ")
    price = float(input("Informe o preço do produto: "))
    quantity = float(input("Informe a quantidade vendida: "))
    value = price * quantity

    # exibe os dados da venda durante o desenvolvimento
    print(
        f"produto: {product} | data: {date} | id: {id}\n"
        f"preço: R${price}\n"
        f"quantidade: {quantity}\n"
        f"Total: R${value}"
    )

    new_sale = pd.DataFrame({
        "Produto": [product],
        "Preço": [price],
        "Quantidade": [quantity],
        "Valor": [value],
        "Data": [date],
        "id": [id]
    })

    current_sales = pd.read_excel("sales/sales.xlsx")
    updated_sales = pd.concat([current_sales, new_sale])
    updated_sales.to_excel(
        "sales/sales.xlsx",
        sheet_name="sales",
        index=False
    )


# usa um laco de repeticao comum conforme solicitado no enunciado
def product_ranking():
    ranking = {}  # dicionario com o produto como chave e o valor como dado
    current_sales = pd.read_excel("sales/sales.xlsx")

    for index, row in current_sales.iterrows():
        if row["Produto"] in ranking:
            ranking[row["Produto"]] += row["Valor"]
        else:
            ranking[row["Produto"]] = row["Valor"]

    # dicionario -> dataframe
    ranking_df = pd.DataFrame(
        ranking.items(),
        columns=["Produto", "Valor"]
    )

    # ordena os produtos do maior valor pro menor
    ranking_df = ranking_df.sort_values(
        "Valor",
        ascending=False
    )

    return ranking_df


def plot_product_ranking(ranking):
    plt.clf()

    # fluxo de criacao do grafico:
    # 1- preparar os dados em product_ranking
    # 2- criar o grafico
    # 3- adicionar os rotulos
    # 4- salvar e exibir o resultado

    sns.barplot(
        data=ranking,
        x="Produto",
        y="Valor"
    )  # grafico

    # add o titulo e os nomes dos eixos
    plt.title("Ranking de produtos por receita gerada")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento (R$)")

    # salva o grafico p/ uso na apresentacao
    plt.savefig("dashboards/ranking_produtos.png")

    # exibe o grafico
    plt.show()
