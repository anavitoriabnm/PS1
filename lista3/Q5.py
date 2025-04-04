def start(nome):
    v = []
    print("Digite 5 números (sem repetição):")
    while len(v) < 5:
        num = int(input(f"Elemento {len(v) + 1}: "))
        if num not in v:
            v.append(num)
        else:
            print("Número repetido! Digite um diferente.")
    return v

def produto_vetores(x, y):
    return [x[i] * y[i] for i in range(len(x))]

def intersecao_vetores(x, y):
    return [num for num in x if num in y]

def unindo(x, y):
    uniao = x[:]
    for num in y:
        if num not in uniao:
            uniao.append(num)
    return uniao


x = start("x")
y = start("y")

produto = produto_vetores(x, y)
intersecao = intersecao_vetores(x, y)
uniao = unindo(x, y)

print("Vetor x:", x)
print("Vetor y:", y)
print("Produto entre x e y:", produto)
print("Interseção entre x e y:", intersecao)
print("União entre x e y:", uniao)