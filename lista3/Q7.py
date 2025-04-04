lista = []

for i in range(15):
    notas = float(input(f"Digite a nota do(a) {i+1}º aluno(a): "))
    lista.append(notas) 

soma = sum(lista) 
media = soma / 15

print(f"Esta é a média da turma: {media}")