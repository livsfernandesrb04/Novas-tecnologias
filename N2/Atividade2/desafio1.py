#Análise de vendas
import pandas as pd

#Carregar o CSV 
vendasDF = pd.read_csv('vendas.csv')

#exibir as 10 primeiras linhas 
print(vendasDF.head(10))

#exibir o info()
vendasDF.info()

#Criar uma coluna'total_venda'=quantidade x preco_unitario
vendasDF['total_vendas'] = vendasDF['quantidade'] * vendasDF['preco_unitario']
print(vendasDF)

#Filtrar apenas vendas da categoria 'Eletrônicos' com
# total_vendas> 1000
print(vendasDF.query("categoria == 'Eletrônicos' & total_vendas > 1000"))

#Calcular a média de total_vendas por cidade, ordenando
# do maior para o menor
vendas_por_cidade = vendasDF.groupby('cidade', as_index=False)['total_vendas'].mean()
vendas_por_cidade.sort_values(by='total_vendas', ascending=False)
