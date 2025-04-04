v = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    v.append(num)

v2 = []
for num in v:
    v2.append(num ** 2)

print("\nVetor original:")
print(v)

print("\nVetor com quadrados:")
print(v2)