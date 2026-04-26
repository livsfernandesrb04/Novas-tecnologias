#Criar um programa que receba uma frase do usuário e produza um relatório estístico sobre ela
def analisar_frase(frase):
    #Separar a frase em palavras(.split())
    lista_palavras = frase.split()

    #Usar dicionário para contar quantas vezes cada palavra aparece
    contagem_palavras = {}
    for palavra in lista_palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
        
    palavras_repetidas = []
    for palavra, contagem in contagem_palavras.items:
        #Identificar o número de palavras únicas na frase
        if contagem == 1:
            total_palavras_únicas += 1
        else:
            #Adicionar as palavras que se repetem a uma lista
            palavras_repetidas.append(palavra)
        
    # exibir quais se repetem mais de uma vez
    lista_reorganizada = list(sorted(contagem_palavras.items(), key=lambda, item: item[1], reverse=True))
    palavra_mais_frequente = lista_reorganizada[0]


    #relatório final deve exibir:
    # total de palavras
    print(f"Total de palavras:{len(contagem_palavras)}")
    # total de palavras únicas
    print(f"Total de palavras únicas: {total_palavras_únicas}")
    # A palavra mais frequente
    print(f"A palavra mais frequente é: {palavra_mais_frequente}")