#Consolidação de Dados de Estoque
import pandas as pd

#Abrir os arquivos (1) estoque_atual.csv (2) produtos.csv (3) vendas_mensal.csv 
df1 = pd.read_csv('estoque_atual.csv')
df2 = pd.read_csv('produto.csv')
df3 = pd.read_csv('vendas_mensais.csv')

#Fazer o merge dos 3 datasets em um só usando produto_id
#Criar 'custo_total_estoque' = quantidade x preco_custo
#Criar 'valor_venda_mes' = quantidade_vendida x preco_custo x 1.5(markup 50%)
#identificar produtos com estoque zerado/negativo
#Identificar quando quantidade_vendida > quantidade(estoque insuficiente)
#Gere resumo por categoria: total em estoque, total vendido,
# produto com estoque crítico(<10) e margem bruta estimada.