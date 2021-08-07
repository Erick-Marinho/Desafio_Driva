# Print no terminal as primeiras linhas desse arquivo

import pandas as pd

df_company = pd.read_csv('data/DadosEmpresa.csv')

First_Lines_DF = df_company.head(3)

print(First_Lines_DF)
