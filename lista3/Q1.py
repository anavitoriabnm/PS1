entrada = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if len(entrada) == 0:
        entrada.append(numero)
    else:
        inserido = False
        for j in range(len(entrada)):
            if numero < entrada[j]:
                entrada.insert(j, numero)
                inserido = True
                break
        if not inserido:
            entrada.append(numero)

print(f"Números em ordem crescente: {entrada}")
