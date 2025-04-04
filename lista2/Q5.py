input("\nObrigada por comprar conosco! Por favor, insira a descrição do produto (número de 3 dígitos): ")

quantidade = int(input("A quantidade adquirida: "))

preco = float(input("E o preço unitário: "))

total = quantidade * preco

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade > 5 and quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

pagamento =  total - desconto

print(f"O valor bruto é de {total:.2f}. Com o desconto fica {pagamento:.2f}")