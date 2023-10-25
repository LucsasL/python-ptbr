posmai = posmen = números = list()

for cont in range(0,5):
    números.append(int(input(f'>>> Digite o valor da posição {cont}: ')))

    if cont == 0:
        maior = menor = números[cont]

    if números[cont] > maior:
        maior = números[cont]
        posmai.append(números[cont])
        
    
    if números[cont] < menor:
        menor = números[cont]
        posmen.append(números[cont])

print('-' * 50)

print(f'Você digitou os valores {números}')

if len(posmai) == 1:
    print(f'... O maior número foi o {maior} na posição {posmai[0]}')

else:
    print(f'... O maior número foi o {maior} na posição ', end='')

    for pos in posmai:
        print(f'{posmai[pos]}... ', end='' if posmai[:pos - 1] else '\n')

if len(posmen) == 1:
    print(f'... O menor número foi o {menor} na posição {posmen[0]}')

else:
    print(f'... O menor número foi o {menor} na posição ', end='')

    for pos in posmen:
        print(f'{posmen[pos]}... ', end='' if posmen[:pos - 1] else '\n')