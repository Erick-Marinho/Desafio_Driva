import pandas as pd

df_company = pd.read_csv('data/DadosEmpresa.csv')

Sum_Social_Capital = "R$ {:_.2f}".format(
    df_company['capital_social']
    .sum()).replace('_', '.')

print(Sum_Social_Capital)
