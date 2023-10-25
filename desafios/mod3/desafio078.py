números = []

for cont in range(0,5):
    números.append(int(input(f'>>> Digite o valor da posição {cont}: ')))

    if cont == 0:
        maior = menor = números[cont]

    else:
        if números[cont] > maior:
            maior = números[cont]
        
        if números[cont] < menor:
            menor = números[cont]

print('-' * 50)

print(f'Você digitou os valores {números}')

print(f'... O maior número foi o {maior} nas posições ', end='')

for c, v in enumerate(números):
    if v == maior:
        print(f'{c}... ', end='')

print('\n')

print(f'... O menor número foi o {menor} nas posições ', end='')

for c, v in enumerate(números):
    if v == menor:
        print(f'{c}... ', end='')