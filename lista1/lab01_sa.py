print("Bem-vindo(a) ao Jogo do Número Secreto")
nome = input("Digite seu nome: ")

random = hash(nome) % 100
tentativas = 0

print(":: O Número Secreto está entre 1 e 99 ::")

while True:
    chute = int(input("Digite seu chute: "))
    tentativas += 1 

    if chute == random:
        print(f"Parabéns, {nome}! Acertou o número {random} em {tentativas} tentativas!")
        break 

    elif chute < random:
        print("É maior")
    else:
        print("É menor")