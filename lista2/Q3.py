while True:
  
    numero = input("Por favor, insira um número inteiro (ou digite 'tchau' caso queira sair): ")
    
    if numero == "tchau":
        break
    
    digitos = len(numero)
    numero_int = int(numero)

    if (digitos > 4) or (numero_int < 0): 
        print("Valor inválido")

    else:
        print(f"O número {numero} possui {digitos} dígitos.")  



