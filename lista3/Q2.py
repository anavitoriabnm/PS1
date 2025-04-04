def MinMax(lista):
    lista.sort()
    return lista[0], lista[-1]

numeros = [24, 26, 2, 5, 9]
menor, maior = MinMax(numeros)
print(f"Menor valor: {menor}, Maior valor: {maior}")


