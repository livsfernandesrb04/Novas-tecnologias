
transacoes = [
    (1, "Infraestrutura", 1500.50),
    (2, "Licenças", 450.00),
    (3, "Infraestrutura", 3200.00),
    (4, "Marketing", 800.00),
    (5, "Licenças", 150.00)
]

categorias = set()
for transacao in transacoes: 
    categorias.add(transacao[1])

print(f"Categorias: {categorias}")

valorTotal = {}

for transacao in transacoes:
    categoria = transacao[1]
    valor = transacao[2]

    if categoria in valorTotal:
        valorTotal[categoria] += valor
    else:
        valorTotal[categoria] = valor

print(f"Valor por categoria: {valorTotal}")