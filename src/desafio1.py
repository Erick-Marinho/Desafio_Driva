import pandas as pd

df_company = pd.read_csv('data/DadosEmpresa.csv')

Column_File = df_company.columns.tolist()

print(Column_File)
