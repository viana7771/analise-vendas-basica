import pandas as pd

df = pd.read_csv(r'C:\Users\kaire\OneDrive\Área de Trabalho\Estudos de Dados\Nova pasta\data\vendas.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())