# -*- coding: utf-8 -*-

""" Desafio 1"""
nome = input("Nome: ")
peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = round(peso/(altura**2), 2)



if imc < 18.5:
    classificacao = "Abaixo do peso"
elif (imc >= 18.5) and (imc <= 24.9):
    classificacao = "Peso normal"
elif (imc >= 25.0) and (imc <= 29.9):
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Olá!, {nome}")
print(f"Seu IMC é: {imc}")
print(f"Classificação: {classificacao}")

""" Desafio 2"""
NUMERO_SECRETO = 42
MAX_TENTATIVAS = 5

tentativaAtual = 1

while tentativaAtual <= MAX_TENTATIVAS:
    numero = int(input(f"Tentativa {tentativaAtual}/5: "))
    
    if numero == NUMERO_SECRETO:
        print("Correto!")
        print("Você ganhou!")
        break
    elif numero < NUMERO_SECRETO:
        print("Muito baixo! Tente maior.")
        tentativaAtual += 1
    elif numero > NUMERO_SECRETO:
        print("Muito alto! Tente menor.")
        tentativaAtual += 1
    
    if tentativaAtual > MAX_TENTATIVAS:
        print("Você Perdeu!")
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    