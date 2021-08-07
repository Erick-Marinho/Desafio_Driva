import pandas as pd

df_company = pd.read_csv('data/DadosEmpresa.csv')

Total_Single_Opting_Companies = df_company.filter(
    like='opcao_pelo_simples').query(
    'opcao_pelo_simples == "SIM"'
).count()

print(Total_Single_Opting_Companies)
