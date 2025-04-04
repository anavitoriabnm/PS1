v = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    v.append(numero)

v1 = []
v2 = []

for numero in v:
    if numero % 2 == 1:
        v1.append(numero)
    else:  
        v2.append(numero)
    
print(f"Lista completa: {v}")
print(f"Estes são os ímpares: {v1}")
print(f"Estes são os pares: {v2}")
