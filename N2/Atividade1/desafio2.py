#manipulação de imagem em escala de cinza
import numpy as np

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

#Calcular o brilho médio geral
brilho_medio = round(np.mean(imagem), 2)
print(f"Brilho medio geral: {brilho_medio}")

#Calcular o brilho médio por linha
brilho_medio_por_linha = np.mean(imagem, axis=1)
print(f"Brilho medio por linha: {brilho_medio_por_linha}")

#Calcular o brilho médio por coluna
brilho_medio_por_coluna = np.mean(imagem, axis=0)
print(f"Brilho medio por coluna: {brilho_medio_por_coluna}")

#Procurar a linha mais escura
linha_escura = np.min(imagem, axis=0 )
indice = np.where(np.all(imagem == linha_escura, axis=1))[0]

#Qual linha é mais escura (menor média)?
print(f"Linha mais escura: {indice + 1}ª linha = {linha_escura}")

#Usar indexação booleana para criar uma versão binária da imagem
#ALteração condicional
imagem[imagem > 127] = 255
imagem[imagem < 126] = 0
print(imagem)



