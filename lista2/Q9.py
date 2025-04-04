def maximo(a, b, c):
    
    if a > b and c: return a
    elif a < b > c: return b
    else: return c

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

print(maximo(a, b, c))