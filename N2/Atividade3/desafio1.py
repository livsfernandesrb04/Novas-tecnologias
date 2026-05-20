import pandas as pd
import streamlit

bugsDataFrame = pd.read_csv(Bugs.csv)
print(bugsDataFrame)
#Se o tempo de resolução em horas for negativo ou nulo, 
# substituir pela média geral da coluna
bugsDataFrame['Tempo_Resolucao_Horas'] <= 0

bugsDataFrame['Tempo_Resolucao_Horas'].mean()

#Calcular o tempo médio de resolução por Módulo

#Criar um gráfico de barras com os módulos 

st.bar_chart
# ordenados do maior para o menor tempo médio de resolução