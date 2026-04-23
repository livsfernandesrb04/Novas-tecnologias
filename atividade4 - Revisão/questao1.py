nivelSeveridade = {
    'INFO' : 0,
    'ERROR' : 0,
    'WARNING' : 0
}

def analisar_logs(lista_logs):
    for log in lista_logs:
        severidade =  log.split()[2]
        if severidade == 'INFO':
            nivelSeveridade['INFO'] += 1
        elif severidade == 'ERROR':
            nivelSeveridade['ERROR'] += 1
        elif severidade == 'WARNING':
            nivelSeveridade['WARNING'] += 1
    print(nivelSeveridade)

lista_logs = [
    "2023-10-01 10:00:00 INFO User 105 logged in",
    "2023-10-01 10:05:23 ERROR Database connection failed",
    "2023-10-01 10:07:00 INFO User 105 requested /home",
    "2023-10-01 10:15:00 WARNING Memory usage above 80%",
    "2023-10-01 10:20:00 ERROR Timeout on API gateway",
    "2023-10-01 10:22:00 INFO User 202 logged in"
]
analisar_logs(lista_logs)
