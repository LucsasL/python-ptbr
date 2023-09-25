maior = 0

menor = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa [Kg]: '.format(c)))

    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('... MAIS PESADO: {:.2f}Kg'.format(maior))
print('... MENOS PESADO: {:.2f}Kg'.format(menor))