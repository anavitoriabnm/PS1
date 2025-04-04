def main():
    v1 = int(input("Digite um número inteiro: "))
    v2 = int(input("Digite outro número inteiro: "))

    soma = v1 + v2
    subtracao = v1 - v2
    multiplicacao = v1 * v2
    divisao_float = v1 / v2
    divisao_int = v1 // v2
    resto_divisao = v1 % v2
    potenciacao = v1 ** v2

    print("\nResultado:")
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão (com resultado como float): {divisao_float}")
    print(f"Divisão inteira: {divisao_int}")
    print(f"Resto da divisão: {resto_divisao}")
    print(f"Potenciação: {potenciacao}")

if __name__ == "__main__":
    main()