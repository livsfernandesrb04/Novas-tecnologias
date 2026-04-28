#manipulacao de imagem em escala de cinza
import numpy as np

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

#Calcular o brilho medio geral
brilho_medio = round(np.mean(imagem), 2)
print(f"Brilho medio geral: {brilho_medio}")

#Calcular o brilho medio por linha
brilho_medio_por_linha = np.mean(imagem, axis=1)
np.round(brilho_medio_por_linha)
print(f"Brilho medio por linha: {brilho_medio_por_linha}")

#Calcular o brilho medio por coluna
brilho_medio_por_coluna = np.mean(imagem, axis=0)
print(f"Brilho medio por coluna: {brilho_medio_por_coluna}")

#Procurar a linha mais escura
linha_escura = np.min(imagem, axis=0 )
indice = np.where(np.all(imagem == linha_escura, axis=1))[0]

#Qual linha � mais escura (menor m�dia)?
print(f"Linha mais escura: linha {indice + 1} = {linha_escura}")

#Usar indexa��o booleana para criar uma vers�o bin�ria da imagem
#Altera��o condicional
imagem[imagem > 127] = 255
imagem[imagem < 126] = 0
print(imagem)



