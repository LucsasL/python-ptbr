from random import randint

cont = maior = 0

listanum = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for num in listanum:
    print(f'... {num}', end=' ' if cont < 4 else '\n')

    if cont == 0:
        maior = menor = num

    if maior < num:
        maior = num

    if menor > num:
        menor = num
    
    cont += 1

print(f'\n... Números sorteados: {listanum}')

print(f'... O maior número gerado foi {maior}')

print(f'... O menor número gerado foi {menor}')