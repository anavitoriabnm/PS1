def verificando(numero):
    for digito in str(numero):
        digitoint = int(digito)
    
        if digitoint % 2 == 0:
            print(f"{digitoint} é par.")
        else:
            print(f"{digitoint} é ímpar.")

def main():
    numero = input("Digite um número: ")
    
    if not numero.isdigit():
        print("Por favor, insira apenas números.")
        return
    
    print("Resultado:")
    verificando(numero)

if __name__ == "__main__":
    main()