from random import randint

cont = maior = 0

num1 = randint(0, 10)

num2 = randint(0, 10)

num3 = randint(0, 10)

num4 = randint(0, 10)

num5 = randint(0, 10)

listanum = (num1, num2, num3, num4, num5)

for cont in listanum:
    print(cont)
    if cont == 0:
        maior = menor = listanum

    if maior < listanum:
        maior = listanum

    if menor > listanum:
        menor = listanum

    cont += 1

print(f'... Números sorteados: {listanum}')

print(f'... O maior número gerado foi {maior}')

print(f'... O menor número gerado foi {menor}')