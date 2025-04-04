def IMC(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros (Ex: 1.72)): "))

    imc = IMC(peso, altura)

    print(f"\nResultado:")
    print(f"Seu IMC é: {imc:.2f}")

    if imc > 30:
        print("Uepa! Manera no garfo!")
    elif imc < 16.4:
        print("Tá magrin hein, se passar um vento leva")
    else: 
        print("Tudo da paz irmão!")

if __name__ == "__main__":
    main()