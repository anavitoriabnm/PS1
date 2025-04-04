nota = float(input("Digite sua nota (entre 0 e 100): "))

if nota >= 90:
    conceito = 'A'
elif nota >= 75:
    conceito = 'B'
elif nota >= 60:
    conceito = 'C'
elif nota >= 40:
    conceito = 'D'
else:
    conceito = 'F'

print(f"Resultado:")
print(f"A nota {nota} traduz-se para o conceito '{conceito}'")