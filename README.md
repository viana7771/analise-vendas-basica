📊 Análise de Vendas – Projeto Básico em Python
📌 Descrição do Projeto

Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) a partir de uma base de vendas fictícia, utilizando Python e bibliotecas de análise de dados, com foco na extração de insights relevantes para tomada de decisão.

O projeto foi desenvolvido como parte do meu aprendizado em Análise de Dados, seguindo boas práticas de organização, versionamento e documentação.

🎯 Objetivos

Analisar o faturamento total do período

Identificar os produtos mais vendidos

Avaliar quais categorias geram mais receita

Calcular o ticket médio

Analisar o comportamento das vendas ao longo do tempo

🗂️ Estrutura do Projeto
analise-vendas-basica/
│
│
├── images/
│   ├── faturamento_categoria.png
│   ├── faturamento_produto.png
│   └── vendas_diaria.png
│
├── data/
│   └── vendas.csv
│
├── notebooks/
│   └── analise_vendas.ipynb
│
├── src/
│   └── analise.py
│
├── requirements.txt
└── README.md

🧪 Dataset

A base de dados contém informações fictícias de vendas realizadas durante o mês de janeiro de 2024, com as seguintes colunas:

data → data da venda

produto → nome do produto

categoria → categoria do produto

quantidade → quantidade vendida

preco → preço unitário

🛠️ Tecnologias Utilizadas

Python

Pandas

Matplotlib

Jupyter Notebook

⚙️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/viana7771/analise-vendas-basica.git

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\Activate

3️⃣ Instalar as dependências
pip install -r requirements.txt

4️⃣ Executar a análise

Abra o arquivo analise_vendas.ipynb no Jupyter Notebook
ou

Execute o script analise.py

📊 Principais Análises Realizadas

Cálculo do faturamento total

Criação da métrica de faturamento por venda

Análise de vendas por produto

Análise de faturamento por categoria

Cálculo do ticket médio

Análise temporal das vendas

🔎 Principais Insights

O faturamento total no período analisado foi de R$ 48745.00

Produtos de alto ticket, como Notebooks, representam uma parcela significativa da receita

A categoria Periféricos possui o maior volume de vendas, porém com um menor impacto no faturamento total por conta do seu baixo custo por venda 

O ticket médio por venda foi de aproximadamente R$ 826.19

As vendas apresentaram oscilações ao longo do mês, com picos em dias específicos

📈 Visualizações

Foram gerados gráficos para facilitar a interpretação dos dados, incluindo:

Gráfico de barras de faturamento por produto
![Faturamento por Produto](imagens\faturamento_produto.png)
Os produtos notebooks apresentão ou alto faturamento mesmo tendo poucas vendas, isso se ta justamente pelo seu alto valor 


Gráfico de barras de faturamento por categoria
![Faturamento por Cateoria](imagens\faturamento_categoria.png)
As categorias de computadores e monitores são as que mais faturam, mesmo com menor volume de venda, é viável também os periféricos pois tem um custo menor mas compensa pelas altas quantidades de produtos vendidos 

Gráfico de linha mostrando a evolução das vendas ao longo do tempo
![Vendas Diárias](imagens\vendas_diaria.png)
Há um pico significativo de vendas em um determinaso período, possivelmente associado a promoções ou sazonalidade.

🚀 Próximos Passos

Integrar análise com SQL

Criar dashboard no Power BI

Expandir o dataset com informações de clientes e formas de pagamento

👤 Autor

Kairê Henrique Viana dos Santos
📌 Estudante de Análise e Desenvolvimento de Sistemas
📊 Foco em Análise e Ciência de Dados
🔗 GitHub: https://github.com/viana7771