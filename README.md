# 🛒 Sistema de Gestão de Vendas Online (Tema 2)

## 1. Informações do Projeto

Este projeto foi desenvolvido no âmbito da disciplina de **Análise de Dados e Big Data**. O sistema simula o ambiente de uma **loja virtual**, permitindo o registro e processamento de produtos vendidos com seus respectivos valores, quantidades e datas.

- **Problema que resolve:** Automatiza o registro de vendas diárias e o cálculo de indicadores comerciais que seriam feitos de forma manual ou custosa.
- **Objetivo do sistema:** Fornecer uma ferramenta interativa via linha de comando (CLI) capaz de persistir dados de vendas e gerar visualizações gráficas (dashboards) para apoio à tomada de decisão.
- **Relação com o Minimundo e Caso de Uso:** Atende diretamente ao minimundo de uma loja virtual, focando no caso de uso em que o administrador precisa acompanhar o desempenho comercial e o ranking dos produtos mais rentáveis.

---

## 2. Informações da Disciplina

- **Universidade:** Universidade Veiga de Almeida (UVA)
- **Curso:** Ciência da Computação
- **Disciplina:** Análise de Dados e Big Data
- **Ano/Semestre:** 2026.2

---

## 3. Integrantes do Grupo 5

- Isabella Lessa — Matrícula: `1250117682`
- João Pedro Hammes Pacheco — Matrícula: `1250114386`
- Renan Luis — Matrícula: `1250110903`
- Sarah Beatriz — Matrícula: `1250123606`
- Vinicius Seraine — Matrícula: `1250123608`

---

## 4. Funcionalidades do Sistema

O sistema entrega todas as funcionalidades principais exigidas pelo projeto:

- **Registro de Vendas (`record_sale` e `update_sales_history`):** Captura informações de produtos, preços, quantidades e datas com validação rigorosa do formato `dd/mm/aaaa`.
- **Cálculo de Ranking (`product_ranking`):** Utiliza laços de repetição tradicionais para totalizar a receita por produto, atendendo à exigência acadêmica de evitar funções automáticas de soma do Pandas.
- **Acompanhamento de Faturamento (`monthly_revenue` e `plot_monthly_revenue`):** Processa, consolida e agrupa os dados por ano/mês (`YYYY/MM`) de forma cronológica para que o administrador acompanhe o faturamento mensal com gráficos em barras.
- **Geração de Dashboards:** Cria gráficos visuais (como o ranking de produtos por receita).

---

## 5. Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Manipulação de Dados:** Pandas
- **Visualização de Dados:** Matplotlib & Seaborn
- **Persistência de Dados:** Planilhas Excel (`.xlsx` com suporte do motor `openpyxl`)
- **Controle de Versão:** Git e GitHub (com gestão via GitHub Projects)

---

## 6. Instalação e Configuração

Siga os passos abaixo para configurar o ambiente em sua máquina local:

```bash
# 1. Clone o repositório
git clone <link-do-repositorio>
cd <nome-do-projeto>

# 2. Crie e ative um ambiente virtual Python
python -m venv venv

# No Windows:
venv\Scripts\activate

# No macOS/Linux:
# source venv/bin/activate

# 3. Instale as dependências necessárias
pip install -r requirements.txt

```

---

## 7. Como Executar

Para iniciar o sistema via linha de comando, execute:

```bash
python main.py

```

### O Menu Principal oferece as seguintes opções:

- **`[1] Registrar vendas`**: Abre o assistente interativo para cadastrar o nome do produto, preço, quantidade e data (com validação automática e ID incremental).
- **`[2] Ranking de produtos`**: Processa a base de dados utilizando laços de repetição, ordena o faturamento por produto e gera o gráfico correspondente.
- **`[3] Faturamento mensal`**: Agrega as vendas cronologicamente por mês (`YYYY/MM`) e exibe o dashboard de faturamento.
- **`[0] Sair`**: Encerra a execução do programa.

### Estrutura de arquivos gerados:

- **Planilhas de Dados:** Salvas em `sales/sales.xlsx`
- **Gráficos e Dashboards:** Salvos em `dashboards/`

---

## 8. Estrutura do Projeto

```text
projeto/
├── main.py
├── requirements.txt
├── src/
│   └── functions.py
├── sales/
│   └── sales.xlsx
└── dashboards/
    ├── ranking_produtos.png
    └── faturamento_mensal.png
```
- **`src/`**: Contém os módulos com a lógica de negócio, rotinas de validação, manipulação do Excel e geração de gráficos
- **`main.py`**: Arquivo central que concentra a lógica do menu, validações, regras de negócio e geração de gráficos.
- **`sales/`**: Armazena os dados brutos em formato tabular (Excel).
- **`dashboards/`**: Armazena as imagens de relatórios gráficos geradas para a apresentação.

---

## 9. Relação com os Requisitos do Enunciado

| Requisito do Enunciado                                        | Onde foi implementado                            |
| ------------------------------------------------------------- | ------------------------------------------------ |
| **Minimundo** (Loja virtual com valores e datas)              | Estrutura de dados em `sales.xlsx`               |
| **Fluxograma** (Entrada → Processamento → Relatório)          | Fluxo do algoritmo feito em `mermaid`            |
| **Caso de Uso** (Administrador acompanha faturamento/ranking) | Função `product_ranking()` e gráficos            |
| **Python** (Estruturas de repetição para somar vendas)        | Laço `for` em `product_ranking()`                |
| **Apresentação** (Dashboards com ranking)                     | Biblioteca `seaborn` em `plot_product_ranking()` |

---

## 10. Link com conteúdos do projeto 

Armazenamos via Google Drive documentações extensas sobre o projeto:

[Drive Projeto](https://drive.google.com/drive/folders/1DhJNUYIKenwkRffSFHYpyG-SYs5rAUyM?usp=sharing)
