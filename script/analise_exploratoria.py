import pandas as pd

df = pd.read_csv(r'C:\Users\kaire\OneDrive\Área de Trabalho\Estudos de Dados\Nova pasta\data\vendas.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Função para transformar a coluna data em índice do DataFrame
def data_index(df, column):
    df[column] = pd.to_datetime(df[column])
    df.set_index(column, inplace=True)
data_index(df, 'data')
print(df.head())