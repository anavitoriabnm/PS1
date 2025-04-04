def CforF(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def FforC(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    escolha = input("Deseja converter de Celsius ou Fahrenheit [C/F]? ").strip().upper()

    if escolha == "C":
        celsius = float(input("Digite a temperatura em °C: "))
        
        fahrenheit = CforF(celsius)

        print(f"\nResultado:")
        print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}")
    
    elif escolha == "F":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = FforC(fahrenheit)
 
        print(f"\nResultado:")
        print(f"Temperatura em °C: {celsius:.2f}")
    
    else:
        print("Erro: Escolha inválida. Digite 'C' para Celsius ou 'F' para Fahrenheit.")

if __name__ == "__main__":
    main()