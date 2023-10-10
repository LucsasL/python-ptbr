números = list()

posmai = posmen = 0

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

print(f'... O maior número foi o {maior} na posição {posmai}')

print(f'... O menor número foi o {menor} na posição {posmen}')