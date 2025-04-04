def main():
    x = int(input("Informe a tabuada de qual número deseja saber a tabuada: "))

    print("\nResultado:")
    for i in range(11): 
        resultado = i * x
        print(f"{i}×{x} = {resultado}")

if __name__ == "__main__":
    main()