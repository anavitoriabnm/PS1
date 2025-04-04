numero = int(input("Informe o número não negativo para o cálculo do fatorial: "))

if numero < 0:
    print("Erro: O número deve ser não negativo.")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i

    print(f"Resultado:")
    print(f"{numero}! = {fatorial}")