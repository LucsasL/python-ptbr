posmai = posmen = números = list()

for cont in range(0,5):
    números.append(int(input(f'>>> Digite o valor da posição {cont}: ')))

    if cont == 0:
        maior = menor = números[cont]

    if números[cont] > maior:
        maior = números[cont]
        posmai = cont
    
    if números[cont] < menor:
        menor = números[cont]
        posmen = cont

print('-' * 50)

print(f'Você digitou os valores {números}')

print(f'... O maior número foi o {maior} na posição {posmai[0]}... {posmai[1]}')

print(f'... O menor número foi o {menor} na posição {posmen[0]}... {posmen[1]}')