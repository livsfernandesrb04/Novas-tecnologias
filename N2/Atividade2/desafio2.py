#Limpeza de Dados de RH
import pandas as pd

funcDF = pd.read_csv('funcionarios.csv')

#Identificar quantos valores nulos existem em cada coluna
# (usar isnull().sum())
nulos = funcDF.isnull().sum()
print(nulos)

#Remover linhas onde 'salario' é nulo
funcDF.dropna(axis=0, how='any', subset=["salario"], inplace=True)
print(funcDF)

#Prencheer 'idade' nula com a média do departamento
media_idade = funcDF['idade'].mean()
funcDF.loc[funcDF['idade'].isnull() , 'idade'] = media_idade
print(funcDF)

#Converter 'data_admissao' para datetime e criar 'anos_empresa' com o tempo de serviço até hoje
funcDF['anos_empresa'] = pd.Timestamp.now() - pd.to_datetime(funcDF['data_admissao'])

#Filtar funcionários com mais de 5 anos de empresa 
# e salário abaixo da média do departamento
tempo_empresa = (funcDF['anos_empresa'].dt.days / 365.25) > 5
salario = funcDF['salario'] < funcDF['salario'].mean()

print('Funcionário há mais de 5 anos com salário abaixo da média:')
print(funcDF[tempo_empresa & salario])
