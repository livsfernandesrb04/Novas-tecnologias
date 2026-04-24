#Criar um programa que simula o estoque de uma loja de eletrônicos.
#Represente o estoque como uma lista de dicionários
##cada item deve possuir nome, preco e quantidade

estoque = []

def adicionar_item(nome, preco, quantidade):

    produto = {"nomeProduto": nome, "preço": preco, "quant": quantidade}
    estoque.append(produto)


def calcular_total_estoque(estoque):

    #Usar um laço for para calcular o valor total em estoque(preço x quantidade)
    for item in estoque:
        valorTotal = item["preço"] * item["quant"]
        print(f"Valor Total em estoque de {item["nomeProduto"]} : R${valorTotal}")
        ##imprimir os itens com valor acima de R$500
        if item["preço"] > 500.00:
            print(f"Nome do produto: {item["nomeProduto"]} preço: R${item["preço"]}")
        
        
#Gerar uma lista com os nomes dos produtos em falta(quantidade == 0)
produtos_em_falta = [item["nomeProduto"] for item in estoque if item["quant"] == 0]
        

adicionar_item("tablet", 2765.20, 5)
adicionar_item("mouse", 120.0, 10)
adicionar_item("fone de ouvido", 57.90, 8)
adicionar_item("monitor", 570.47, 0)
calcular_total_estoque(estoque)
print(f"{produtos_em_falta}")