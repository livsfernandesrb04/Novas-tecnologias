#Consolidação de Dados de Estoque
import pandas as pd

#Abrir os arquivos (1) estoque_atual.csv (2) produtos.csv (3) vendas_mensal.csv 
estoqueAtual = pd.read_csv('estoque_atual.csv')
produtos = pd.read_csv('produto.csv')
vendasMensais = pd.read_csv('vendas_mensais.csv')

#Fazer o merge dos 3 datasets em um só usando produto_id
dfEstoqProd = pd.merge(estoqueAtual, produtos, on='produto_id', how='inner')

print(dfEstoqProd)

dfEstProdVend = pd.merge(dfEstoqProd, vendasMensais, on='produto_id', how='inner')
#Criar 'custo_total_estoque' = quantidade x preco_custo

#Criar 'valor_venda_mes' = quantidade_vendida x preco_custo x 1.5(markup 50%)

#identificar produtos com estoque zerado/negativo

#Identificar quando quantidade_vendida > quantidade(estoque insuficiente)

#Gere resumo por categoria: total em estoque, total vendido,
# produto com estoque crítico(<10) e margem bruta estimada.