a = float(input("Informe o lado A do triângulo: "))
b = float(input("Informe o lado B do triângulo: "))
c = float(input("Informe o lado C do triângulo: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Resultado:")
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Resultado:")
        print("É um triângulo isósceles.")
    else:
        print("Resultado:")
        print("É um triângulo escaleno.")
else:
    print("Resultado:")
    print("Os lados fornecidos violam a condição de existência de um triângulo.")