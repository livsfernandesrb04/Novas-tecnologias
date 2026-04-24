#Criar um programa que receba uma frase do usuário e produza um relatório estístico sobre ela
def analisar_frase(frase):
    #Separar a frase em palavras(.split())
    lista_palavras = frase.split()
    #usar dicionário para contar quantas vezes cada palavra aparece
    contagem_palavras = {}
    
    for palavra in lista_palavras:
        if palavra is in contagem_palavras:
            contagem_palavras[palavra] = contagem_palavras[palavra] + 1
        elif palavra is not contagem_palavras:
            contagem_palavras.update(palavra: 1)

        #Identificar o número de palavras únicas na frase 
        if contagem_palavras[palavra] == 1:
            total_palavras_únicas =+ 1
        
        
        if contagem_palavras[palavra] < 

    # exibir quais se repetem mais de uma vez

    print(len(contagem_palavras))
    print(total_palavras_únicas)

#relatório final deve exibir:
# total de palavras
# total de palavras únicas
# palavra mais frequente