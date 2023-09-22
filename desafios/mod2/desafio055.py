maior = 0

menor = 1000000000

for c in range(0, 6):
    peso = float(input('Digite o peso [Kg]: '))

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('... MAIS PESADO: {:.2f}Kg'.format(maior))
print('... MENOS PESADO: {:.2f}Kg'.format(menor))