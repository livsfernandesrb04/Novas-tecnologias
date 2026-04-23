# Criar gerar_boletins(dados) que processe a lista
def gerar_boletins(lista): 
    notas_finais = {
        "boletins": {},
        "ranking": []
    }

    #Agrupar por aluno e por matéria
    for notas in lista:
        aluno = notas["aluno"]
        materia = notas["materia"]
        nota = notas["nota"]
        somaNotas = []

        #verificar se aluno já existe em boletins
        if aluno not in notas_finais["boletins"]:
            #se aluno não existe adicionar
            notas_finais["boletins"][aluno] = {"medias_disciplinas": {}}
        #verificar se a materia já existe em boletins
        if materia not in notas_finais["boletins"][aluno]["medias_disciplinas"]:
            #se materia não existe adicionar
            notas_finais["boletins"][aluno]["medias_disciplinas"] = {materia : nota }
            somaNotas.append(nota)
        
        #Se a materia já existir e apresentar mais de 2 notas descartar a menor
        if materia in notas_finais["boletins"][aluno]["medias_disciplinas"]:
            if len(somaNotas) > 3 :
                #Descartar as piores notas
                somaNotas.remove(min(somaNotas))
            elif len(somaNotas) = 3:
                somaNotas.sort()
                somaNotas.pop(0)

                
            #Calcular a media por matéria
            #A media deve ser arrendondada para 2 casas decimais.
            mediaMateria = round(sum(somaNotas)/ len(somaNotas), 2)

        ##Calcular media geral (média simples de todas as materias)
        #A media deve ser arrendondada para 2 casas decimais.
        media_geral = round( , 2)

        ##Definir o status de acordo com a média
        if notas_finais["boletins"][aluno]["media_geral"] >= 7.00:
            notas_finais["boletins"][aluno]["status"] : "Aprovado"
        elif (notas_finais["boletins"][aluno]["media_geral"] <= 6.99) and (notas_finais["boletins"][aluno]["media_geral"] >= 5.00) :
            notas_finais["boletins"][aluno]["status"] : "Recuperacao"
        elif notas_finais["boletins"][aluno]["media_geral"] < 5.00:
            notas_finais["boletins"][aluno]["status"] : "Reprovado"
    

    ##Gerar lista com apenas os nomes dos alunos da maior para menor media
    #dois alunos com mesma nota desempate ordem alfabética
    notas_finais["ranking"] = sorted( notas_finais["boletins"].keys(), key=lambda x: (-notas_finais["boletins"][x]["media_geral"], x))

    #Imprimir os boletins
    print(notas_finais)

