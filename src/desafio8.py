# Faça um merge entre os dois arquivos pela coluna "cnpj"
# e salve um arquivo CSV com todas as empresas que são de "CURITIBA";

import pandas as pd

df_company = pd.read_csv('data/DadosEmpresa.csv')
df_address = pd.read_csv('data/DadosEndereco.csv')

df_Merge_Files = pd.merge(df_company, df_address, how='inner', on='cnpj')

Companies_Curitiba = df_Merge_Files.query('municipio == "CURITIBA"')

Companies_Curitiba.to_csv('companies_curitiba', index=False)
