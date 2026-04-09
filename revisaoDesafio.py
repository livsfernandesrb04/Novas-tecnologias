# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:08:03 2026

@author: Livia.bezerra
"""

#criar uma função chamada gerar_boletins(dados)

def gerar_boletins(dados):
    
#dicionario de boletins
boletins = {}

#lista para o ranking
ranking = []

#1      
#organizar os dados para saber exatamente quais notas cada aluno tirou em cada matéria específica
for notas_por_prova in dados:
    
#notas por aluno    

#2
#calcular a média de uma matéria, você deve somar as notas e dividir pela quantidade de provas daquela matéria
mediaMateria = 
#se um aluno fez 3 ou mais provas em uma mesma matéria, o sistema deve descartar as notas mais baixas, até que sobrem 2 notas, antes de calcular a média
contador = 
# A média final de cada matéria deve ser arredondada para 2 casas decimais
round(mediaMateria,2)
#3
# média geral do aluno é a média aritmética simples das médias finais de suas matérias (também arredondada para 2 casas decimais)
mediaGeral = round( ,2)

#Baseado na média geral, defina o status do aluno

    if mediaGeral >= 7.00:
        status = "Aprovado"
    elif mediaGeral > 5.00 && mediaGeral <= 6.99:
        status = "Recuperação"
    elif mediaGeral < 5.00:
        status = "Reprovado"

#4
#gerar uma lista apenas com os nomes dos alunos, ordenada da maior média geral para a menor

#Regra de Desempate: Se dois alunos tiverem exatamente a mesma média geral, a ordem entre eles deve ser alfabética
ranking = sorted() 