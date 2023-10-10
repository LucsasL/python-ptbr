números = list()

for cont in range(0,5):
    números.append(int(input('>>> Digite um número: ')))

    if cont == 0:
        maior = menor = números

    if números > maior:
        maior = números
    
    if números < menor:
        menor = números

print(números)

print(f'... O maior número foi o {maior}')

print(f'... O menor número foi o {menor}')