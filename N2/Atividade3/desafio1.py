import pandas as pd
import matplotlib.pyplot as pit


bugsDataFrame = pd.read_csv('Atividade3/Bugs.csv')
print(bugsDataFrame)
#Se o tempo de resolução em horas for negativo ou nulo, 
# substituir pela média geral da coluna
media_tempo_resolucao = bugsDataFrame['Tempo_Resolucao_Horas'].mean()
bugsDataFrame.loc[bugsDataFrame['Tempo_Resolucao_Horas'].isnull(), 'Tempo_Resolucao_Horas'] = media_tempo_resolucao
bugsDataFrame.loc[bugsDataFrame['Tempo_Resolucao_Horas'] <= 0, 'Tempo_Resolucao_Horas'] = media_tempo_resolucao


#Calcular o tempo médio de resolução por Módulo
Tempo_Medio_Modulo = bugsDataFrame.groupby('Módulo')['Tempo_Resolucao_Horas'].mean().sort_values(ascending=False).reset_index()

#Criar um gráfico de barras com os módulos 
# ordenados do maior para o menor tempo médio de resolução
data=Tempo_Medio_Modulo, x='Módulo', y='Tempo_Resolucao_Horas', x_label='Módulo', y_label='Tempo médio de resolução'
