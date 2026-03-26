nivelSeveridade = {
    'INFO' = 0,
    'ERROR' = 0,
    'WARNING' = 0
}

#Crie uma função analisar_logs(lista_logs) que percorra a lista recebida.
function analisar_logs(lista_logs) {
    #Utilize operações de fatiamento de strings (slicing/split) e laços de repetição para isolar o nível
    # de severidade (INFO, ERROR, WARNING) do restante da mensagem.
    for log in lista_logs:
        severidade =  

    if severidade == 'INFO':
        nivelSeveridade['INFO'] +=
    elif severidade == 'ERROR':
        nivelSeveridade
    elif severidade == 'WARNING':
        nivelSeveridade
}

#Retorne um dicionário contendo a contagem total de cada tipo de log de forma automatizada (Exemplo de
#  retorno esperado: {'INFO': 3, 'ERROR': 2, 'WARNING': 1}).