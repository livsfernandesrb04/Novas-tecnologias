#Análise de passageiros do titanic

#Tarefa 1: Carga e Inspeção Inicial
#Importe a biblioteca Pandas e carregue os dados da URL fornecida usando read_csv().
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#Exiba as 5 primeiras linhas para ter uma primeira impressão dos dados usando o método head().
print(df.head())

#Faça um diagnóstico inicial chamando info() para verificar os tipos de dados e valores nulos.
df.info()

#Descubra a dimensão do dataset (quantidade de linhas e colunas) utilizando o atributo shape.
linhas = df.shape[0]
colunas = df.shape[1]
print(f'linhas: {linhas}, colunas: {colunas}')

#Tarefa 2: Estatísticas Descritivas
#Gere as estatísticas descritivas básicas para as colunas numéricas usando describe().
print(df.describe())

#Verifique quantas classes de embarque diferentes existem na coluna Pclass usando o método nunique().


#Exiba a frequência de passageiros por sexo (coluna Sex) utilizando value_counts().

#Tarefa 3: Seleção de Dados com loc e iloc
#Utilizando loc, selecione e exiba apenas as colunas Name e Age para as linhas de índice 0 a 10. Lembre-se do comportamento do limite superior no loc.

#Utilizando iloc, recupere os dados exclusivos da 15ª linha do DataFrame.

#Tarefa 4: Filtros e Máscaras Booleanas
#Crie um filtro simples para exibir apenas os passageiros com idade (Age) maior que 60 anos.

#Combinando condições com o operador & (AND), filtre as mulheres (Sex == 'female') que viajaram na 1ª classe (Pclass == 1). Não esqueça dos parênteses em cada condição!

#Encontre os passageiros que pagaram uma tarifa (Fare) entre 50 e 100 libras utilizando o método between().

#Escreva uma condição usando a sintaxe limpa do query() para filtrar os passageiros que embarcaram no porto 'C' (Embarked == 'C') e que sobreviveram (Survived == 1).