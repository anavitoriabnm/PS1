

from num2words import num2words

numero = input("Por favor, insira um número de dois dígitos: ")  

if numero >= 10 or numero <= 99:
  
    nome = num2words(numero, lang='pt')
    print(f"Você inseriu o número {nome}.")

else:
    print("Número inválido.")

   
   

    