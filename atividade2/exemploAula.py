#Como criar uma lista em python
frutas = ["maçã","banana","laranja","uva"]

#acessando a lista por indice
print(frutas[0])
print(frutas[-1])

#Fatiamento(slicing)
print(frutas[1:3])

#métodos para adicionar elementos a lista
frutas.append("morango") #adiciona o elemento ao final

frutas.insert(2, "abacaxi") #insere na posição 2 o elemento abacaxi

#métodos para remover elementos da lista
frutas.remove("uva")#remove o elemento pelo valor

frutas.pop(1) #remove elemento pelo indice

#métodos para consultar a lista
len(frutas) #consulta o tamanho da lista

"laranja" in frutas #verifica a existencia do elemento na lista
"pera" in frutas

#métodos para ordenar a lista
frutas.sort() #ordena in place

sorted(frutas) #retorna nova lista

#laço for com listas
notas = [8.5, 7.0, 9.2, 6.8, 10.0]

#iterando diretamente
for nota in notas:
    print(f"Nota:{nota}")

#com indice enumerated()
for i, nota in enumerated(notas);
    print(f"Aluno {i+1}: {nota}")

#Soma e média
total = sum(notas)
media = total/len(notas)
print(f"Média da turma: {media:.2f}")

#List comprehension
numeros = [1,2,3,4,5,6,7,8,9,10]

#Forma tradicional
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)

#List comprehension equivalent
pares = [n for n in numeros if n % 2 == 0]

#Criando e manipulando dicionário

#criar dicionário 
aluno = {
    "nome":"Luisa Lima",
    "curso": "Engenharia de Software",
    "nota": 9.5
}

#acessando valores
print(aluno["nome"])
print(aluno.get("idade", 0))

#adicionando e atualizando o dicionário
aluno["semestre"] = 4
aluno["nota"] = 10.0

#Removendo elementos do dicionário
del aluno["semestre"]

#Iterando sobre chave e valor
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

#métodos uteis em python
inventario = {
    "maçã" : 50,
    "banana" : 30,
    "laranja" : 20
}

#Retorna todas as chaves do dicionário
print(inventario.keys())

#Retorna todos os valores do dicionário
print(inventario.values())

#Retorna os pares do dicionario
print(inventario.items())

#Realiza a busca segura sem KeyError
print(inventario.get("laranja", 0))

#Verificar a existencia de um item no dicionário
if "banana" in inventario:
    print("Banana está em estoque!")

#Dicionário de dicionários
estoque = {
    "fruta" : inventario,
    "total" : sum(inventario.values())
}

#iteração com for em dicionarios
turma = {
    "ana": [8.0, 9.5, 7.5],
    "Bruno": [6.0, 7.0, 8.5],
    "Carla": [10.0, 9.0, 9.5]
}

#Calcular média de cada aluno
for nome, notas in turma.items():
    media = sum(notas)/len(notas)
    status = "Aprovado" if media >= 7 else "Reprovado"
    print(f"{nome}: {media:.1f} -> {status}")


#Tuplas e Conjuntos
