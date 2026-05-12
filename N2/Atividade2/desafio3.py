#Consolidação de Dados de Estoque
import pandas as pd

#Abrir os arquivos (1) estoque_atual.csv (2) produtos.csv (3) vendas_mensal.csv 
estoqueAtual = pd.read_csv('estoque_atual.csv')
produtos = pd.read_csv('produtos.csv')
vendasMensais = pd.read_csv('vendas_mensal.csv')

#Fazer o merge dos 3 datasets em um só usando produto_id
dfEstoqProd = pd.merge(estoqueAtual, produtos, on='produto_id', how='inner')

print(dfEstoqProd)

dfEstProdVend = pd.merge(dfEstoqProd, vendasMensais, on='produto_id', how='inner')

print(dfEstProdVend)
#Criar 'custo_total_estoque' = quantidade x preco_custo
dfEstProdVend['custo_total_estoque'] = dfEstProdVend['quantidade'] * dfEstProdVend['preco_custo']
print(dfEstProdVend)

#Criar 'valor_venda_mes' = quantidade_vendida x preco_custo x 1.5(markup 50%)
dfEstProdVend['valor_venda_mes'] = dfEstProdVend['quantidade-vendida'] * dfEstProdVend['preco_custo'] * 1.5
print(dfEstProdVend)

#identificar produtos com estoque zerado/negativo
df_filtrado = quantidade - quantidade vendida <= 0 

#Identificar quando quantidade_vendida > quantidade(estoque insuficiente)
quantidade_vendida > quantidade

#Gere resumo por categoria: total em estoque, total vendido,
# produto com estoque crítico(<10) e margem bruta estimada.
total_em_estoque = dfEstProdVend['quantidade'].sum()
total_vendido = dfEstProdVend['']
Produto_estoque_critico = 
margem_bruta = 
