import pandas as pd

def menu():
    """Exibe o menu inicial com as funções do sistema"""

    while True: # True garante que o loop SEMPRE execute

        print("[1] Registrar vendas\n[2] Relatórios\n[0] Sair\n")
        opt = input(">")

        match opt: 
            case '1': sale()
            case '2': product_ranking()
            case '0': 
                print("Saindo...")
                break
            case _: print("Opção inválida") # tratamento de erro

def sale():
    id = 0 # numero aleatorio
    date = input("Informe a data da venda (dd/mm/aaaa): ")
    # incluir uma função para validação de data
    product = input("Informe o nome do produto: ")
    price = float(input("Informe o preço do produto: "))
    quantity = float(input("Informe a quantidade vendida: "))
    value = price*quantity
    print(f"produto: {product} | data: {date} | id: {id}\npreço: R${price}\nquantidade: {quantity}\nTotal: R${value}")

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
    updated_sales.to_excel("sales/sales.xlsx", sheet_name="sales", index=False)


# poderia ser feito usando método de pd mas o enunciado exige laço de repetição comum
def product_ranking():
    ranking = {} # tipo dicionário (chave:valor), ententdam como objeto do JS
    current_sales = pd.read_excel("sales/sales.xlsx")

    for index, row in current_sales.iterrows():
        if row["Produto"] in ranking:
            ranking[row["Produto"]] += row["Valor"]
        else: 
            ranking[row["Produto"]] = row["Valor"]

    # passar o dicionário para dataframe e usar as chaves do diconário como colunas
    ranking_df = pd.DataFrame(ranking.items(), columns=["Produto", "Valor"])
    ranking_df = ranking_df.sort_values("Valor", ascending=False) # ordena pela coluna false
    print(ranking_df)

        





