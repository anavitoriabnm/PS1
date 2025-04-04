print("Bem-vindo(a) ao Jogo do Número Secreto")
nome = input("Digite seu nome: ")

import random
numero = random.randint(1, 100)
tentativas = 0

print(":: O Número Secreto está entre 1 e 100 ::")

while True:
    chute = int(input("Digite seu chute: "))
    tentativas += 1 

    if chute == numero:
        print(f"Parabéns, {nome}! Acertou o número {numero} em {tentativas} tentativas!")
        break 

    elif chute < numero:
        print("É maior")
    else:
        print("É menor")