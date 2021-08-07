import pandas as pd

df_company = pd.read_csv('data/DadosEmpresa.csv')

Capital_Social_Between_10000_And_20000 = df_company.loc[
    df_company['capital_social']
    .between(10000, 20000, inclusive=True),
    ['razao_social', 'capital_social']
]

print(Capital_Social_Between_10000_And_20000)
