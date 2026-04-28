#Análise de notas de uma turma por aluno
import numpy as np

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])

#Calcule a média de cada aluno. Usar axis
media_por_aluno = np.mean(notas, axis=1)
print(media_por_aluno)

#Qual aluno teve a maior média?
print(f"O aluno com a maior média é: {np.max(media_por_aluno)}")

#Normalizar as notas (média da coluna/desvio-padrão)
# usar broadcast


#Exibir as notas originais apenas dos alunos cuja média for >=6 
# usar indexação booleana

