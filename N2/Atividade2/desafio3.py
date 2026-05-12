#Consolidação de Dados de Estoque
import pandas as pd

#Abrir os arquivos (1) estoque_atual.csv (2) produtos.csv (3) vendas_mensal.csv 
estoqueAtual = pd.read_csv('estoque_atual.csv')
produtos = pd.read_csv('produtos.csv')
vendasMensais = pd.read_csv('vendas_mensal.csv')

#Fazer o merge dos 3 datasets em um só usando produto_id
dfEstoqProd = pd.merge(estoqueAtual, produtos, on='produto_id', how='inner')
dfEstProdVend = pd.merge(dfEstoqProd, vendasMensais, on='produto_id', how='inner')

print(dfEstProdVend)

#Criar 'custo_total_estoque' = quantidade x preco_custo
dfEstProdVend['custo_total_estoque'] = dfEstProdVend['quantidade'] * dfEstProdVend['preco_custo']

#Criar 'valor_venda_mes' = quantidade_vendida x preco_custo x 1.5(markup 50%)
dfEstProdVend['valor_venda_mes'] = dfEstProdVend['quantidade_vendida'] * dfEstProdVend['preco_custo'] * 1.5

#identificar produtos com estoque zerado/negativo
produtos_sem_estoque = dfEstProdVend[(dfEstProdVend['quantidade'] - dfEstProdVend['quantidade_vendida']) <= 0 ]
print(f'Produto com estoque zerado ou negativo:\n {produtos_sem_estoque}')

#Identificar quando quantidade_vendida > quantidade(estoque insuficiente)
estoque_insuficiente = dfEstProdVend[dfEstProdVend['quantidade_vendida'] > dfEstProdVend['quantidade']]
print(f'Produto em quantidade insuficiente para a venda:\n {estoque_insuficiente}')

#Gere resumo por categoria: total em estoque, total vendido,
# produto com estoque crítico(<10) e margem bruta estimada.
print("Resumo por categoria")
total_em_estoque = (dfEstProdVend['quantidade'] - dfEstProdVend['quantidade_vendida']).sum()
print(f'Total de produtos em estoque:{total_em_estoque}')

total_vendido = dfEstProdVend['quantidade_vendida'].sum()
print(f'Total de produtos vendidos:{total_vendido}')

produto_estoque_critico = dfEstProdVend[(dfEstProdVend['quantidade'] - dfEstProdVend['quantidade_vendida']) < 10 ]
print(f'Produtos com estoque crítico:(menos que 10 produtos)\n{produto_estoque_critico}')

receita_liquida = dfEstProdVend['valor_venda_mes'].sum()
lucro_bruto = receita_liquida - ((dfEstProdVend['quantidade_vendida']* dfEstProdVend['preco_custo']).sum()) 
margem_bruta = (lucro_bruto/receita_liquida) * 100
print(f'Margem bruta de lucro: {margem_bruta:.2f}')
