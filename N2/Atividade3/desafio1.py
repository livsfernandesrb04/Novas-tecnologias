import pandas as pd
import matplotlib.pyplot as plt


bugsDataFrame = pd.read_csv('Atividade3/Bugs.csv')

#Se o tempo de resolução em horas for negativo ou nulo, 
# substituir pela média geral da coluna
media_tempo_resolucao = bugsDataFrame['Tempo_Resolucao_Horas'].mean()
bugsDataFrame.loc[bugsDataFrame['Tempo_Resolucao_Horas'].isnull(), 'Tempo_Resolucao_Horas'] = media_tempo_resolucao
bugsDataFrame.loc[bugsDataFrame['Tempo_Resolucao_Horas'] <= 0, 'Tempo_Resolucao_Horas'] = media_tempo_resolucao


#Calcular o tempo médio de resolução por Módulo
Tempo_Medio_Modulo = bugsDataFrame.groupby('Módulo')['Tempo_Resolucao_Horas'].mean().sort_values(ascending=False)


#Criar um gráfico de barras com os módulos 
# ordenados do maior para o menor tempo médio de resolução
plt.figure(figsize=(10,6))
Tempo_Medio_Modulo.plot(kind='bar', color='skyblue', edgecolor='black')

#Labels
plt.title('Tempo médio de resolução por módulo', fontweight='bold')
plt.xlabel('Módulo')
plt.ylabel('Tempo médio de resolução')

plt.xticks(rotation=0)
plt.show()

