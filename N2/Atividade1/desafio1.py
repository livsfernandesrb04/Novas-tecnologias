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
print(f"Media por aluno: {media_por_aluno}")

#Procurar o indice do aluno com a maior media
indice = np.argmax(media_por_aluno)
maior_media = media_por_aluno[indice]

#Qual aluno teve a maior média?
print(f"O aluno com a maior media esta na linha {indice + 1} com a media {maior_media}")

#Normalizar as notas (média da coluna/desvio-padrão)
# usar broadcast
media_por_aluno_coluna = media_por_aluno.reshape(-1,1)
desvio_padrao = np.std(notas)
notas_normalizadas = (notas - media_por_aluno_coluna)/desvio_padrao
print(f"Notas normalizadas: {notas_normalizadas}")

#Exibir as notas originais apenas dos alunos cuja média for >=6 
# usar indexação booleana
# filtragem
print(f"Notas dos aluno com media >= 6: {notas[media_por_aluno >= 6]}")

